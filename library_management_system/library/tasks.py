from celery import shared_task
from .models import Author, Book, BorrowRecord
import json
import os
from datetime import datetime

@shared_task
def generate_report():
    data = {
        "total_authors": Author.objects.count(),
        "total_books": Book.objects.count(),
        "total_books_borrowed": BorrowRecord.objects.filter(return_date__isnull=True).count(),
    }
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(report_path, "w") as file:
        json.dump(data, file)
    latest_report_path = os.path.join(report_dir, "latest_report.json")
    with open(latest_report_path, "w") as file:
        json.dump(data, file)
