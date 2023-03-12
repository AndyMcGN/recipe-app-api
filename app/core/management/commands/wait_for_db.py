"""
    django command to wait for db to become available
"""
from django.core.management.base import BaseCommand
import time
from django.db import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django command to wait for db"""

    def handle(self, *args, **options):
        """entrypoint for command"""
        self.stdout.write("waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("DB unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
