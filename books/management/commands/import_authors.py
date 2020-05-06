import csv

from django.core.management.base import BaseCommand
from books.models import Author


class Command(BaseCommand):
    help = 'Imports authors information to database from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to CSV file")

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader, None)

            for row in csv_reader:
                name = str(row).strip("'[]")
                try:
                    author = Author(name=name)
                    author.save()

                    self.stdout.write(
                        self.style.SUCCESS(f"Author {name} added successfully")
                    )
                except:
                    self.stdout.write(self.style.ERROR("Something went wrong"))
