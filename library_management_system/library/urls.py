from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BorrowRecordViewSet, ReportViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('borrow', BorrowRecordViewSet, basename='borrow')
router.register('reports', ReportViewSet, basename='reports')

urlpatterns = router.urls


