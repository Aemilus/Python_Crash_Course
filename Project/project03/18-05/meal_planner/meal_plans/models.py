from django.db import models

# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Meal(models.Model):
    plan = models.ForeignKey(Plan, models.CASCADE)
    name = models.CharField(max_length=50)
    calories = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return f"{self.name} - {self.calories} calories."
