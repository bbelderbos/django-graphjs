import csv

from django.core.management.base import BaseCommand
from dateutil.parser import parse

from stats.models import BiteStat


class Command(BaseCommand):
    help = 'Import bite exercise stats'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--csv', required=True)

    def handle(self, *args, **options):
        file = options["csv"]
        with open(file) as f:
            reader = csv.DictReader(f)
            for row in reader:
                completed = row["first_completed"]
                if not completed:
                    continue

                level = row["user_level"]
                if not level:
                    level = 0

                date = parse(completed)
                stat, created = BiteStat.objects.get_or_create(
                    exercise=row["bite_id"],
                    completed=date,
                    level=level,
                )

                if created:
                    self.stdout.write(f"{stat} created")
                else:
                    self.stderr.write(f"{stat} already in db")
