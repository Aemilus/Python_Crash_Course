from django.db import models

# Create your models here.


class Pizza(models.Model):
    """Model for a pizza."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Topping(models.Model):
    """Model for a flavor."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        if len(self.name) > 50:
            return f"{self.name[:50]}..."
        else:
            return self.name
