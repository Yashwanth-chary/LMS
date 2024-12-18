from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Author, Book, BorrowRecord
from .serializers import AuthorSerializer, BookSerializer, BorrowRecordSerializer
from .tasks import generate_report
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowRecordViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = BorrowRecordSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.validated_data['book']
            if book.available_copies > 0:
                book.available_copies -= 1
                book.save()
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"error": "No copies available."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def return_book(self, request, pk=None, url_path='return_book'):
        try:
            borrow = BorrowRecord.objects.get(pk=pk)
            if not borrow.return_date:
                borrow.return_date = request.data.get('return_date')
                borrow.book.available_copies += 1
                borrow.book.save()
                borrow.save()
                return Response({"message": "Book returned successfully."})
            return Response({"error": "Book already returned."}, status=status.HTTP_400_BAD_REQUEST)
        except BorrowRecord.DoesNotExist:
            return Response({"error": "Borrow record not found."}, status=status.HTTP_404_NOT_FOUND)

class ReportViewSet(viewsets.ViewSet):
    def create(self, request):
        generate_report.delay()
        return Response({"message": "Report generation started."}, status=status.HTTP_202_ACCEPTED)

    def list(self, request):
        try:
            with open("reports/latest_report.json", "r") as file:
                return Response({"report": file.read()})
        except FileNotFoundError:
            return Response({"error": "No reports found."}, status=status.HTTP_404_NOT_FOUND)
