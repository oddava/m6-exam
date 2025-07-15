from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Expenses(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    expense_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=[
        ("food", "Oziq-ovqat"), ("transport", "Transport"), ("bills", "To'lovlar"), ("other", "boshqa")
    ], default="other")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Email', max_length=50, unique=True)

    def __str__(self):
        return "{}".format(self.user)