from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import FileField


class CustomUser(AbstractUser):
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
    phoneno = models.IntegerField(default=False)
    fname = models.CharField("First Name",blank=True, max_length=10)
    lname = models.CharField(blank=True, max_length=10)
    profpic = models.FileField(default='', upload_to="documents%Y%m%d")
    address = models.TextField(default='')
    def __str__(self):
        return self.email

class Documents(models.Model):
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    resume = models.FileField(default='documents20180702/Event_list_UXMJVy4.pdf', upload_to="documents%Y%m%d")
    birth_certificate = models.FileField(default='documents20180702/Event_list_UXMJVy4.pdf', upload_to="documents%Y%m%d")
    marksheet = models.FileField(default='documents20180702/Event_list_UXMJVy4.pdf', upload_to="documents%Y%m%d")
    def __str__(self):
        return self.customuser.email