import datetime

import factory
from factory.django import DjangoModelFactory

from .models import BiteStat

class BiteStatFactory(DjangoModelFactory):
    class Meta:
        model = BiteStat

    exercise = factory.Faker(
        'random_int',
        min=0,
        max=370,
    )
    completed = factory.Faker(
        'date_between_dates',
        date_start=datetime.date(2017, 11, 1),
        date_end=datetime.date(2022, 5, 31),
    )
    level = factory.Faker(
        'random_int',
        min=1,
        max=10,
    )