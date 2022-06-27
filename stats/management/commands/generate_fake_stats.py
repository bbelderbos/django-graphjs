from django.core.management.base import BaseCommand

from stats.models import BiteStat

from stats.factories import BiteStatFactory


class Command(BaseCommand):
    help = "Generate fake PyBites stats"

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--num",
            type=int,
            required=True,
            help="Specify the number of fake records to create.",
        )
        parser.add_argument(
            "-d",
            "--del",
            action="store_true",
            required=False,
            help="Flag for deleting existing data",
        )

    def handle(self, *args, **options):
        number_of_records = options["num"]
        delete_flag = options["del"]
        if delete_flag:
            self.stdout.write("Deleting existing data from BiteStat model...")
            BiteStat.objects.all().delete()

        self.stdout.write(f"Creating {number_of_records} new fake records...")
        for record in range(number_of_records):
            BiteStatFactory()

        self.stdout.write(f"Successfully created {number_of_records} new fake records.")
