from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)
    GEN_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GEN_CHOICE)

    SEC_CHOICE = (
        ('1', 'Best friends name'),
        ('2', 'Favourite food'),
        ('3', 'Pet\'s name'),
    )
    sq = models.TextField("Security Question", max_length=20, choices=SEC_CHOICE,default=False)
    sa = models.CharField("Security Answer", max_length=10)
    bd = models.DateField("Birth Date", auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.email