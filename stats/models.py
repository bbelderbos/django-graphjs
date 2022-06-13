from django.db import models


class BiteStat(models.Model):
    exercise = models.PositiveSmallIntegerField()  # 0 to 32767
    completed = models.DateField()  # don't care about time
    level = models.PositiveSmallIntegerField(null=True, blank=True)  # not every Bite has user feedback

    def __str__(self):
        return f"{self.exercise} - {self.completed} - {self.level}"
