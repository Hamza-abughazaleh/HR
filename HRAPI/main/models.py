# Create your models here.
from django.db import models as models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from main.validators import validate_file_extension


class Candidates(AbstractUser):
    DEPARTMENT_CHOICES = (
        ('IT', _('Information Technology')),
        ('HR', _('Human Resource')),
        ('FI', _('Finance)')),
    )
    department_id = models.CharField(max_length=2, choices=DEPARTMENT_CHOICES)
    years_of_experience = models.CharField(max_length=3)
    date_of_birth = models.DateField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True, upload_to='resume/%Y/%m/%d', validators=[validate_file_extension])

    def __str__(self):
        full_name = self.get_full_name()
        if full_name == "":
            return self.email
        return full_name

    def get_full_name(self):
        full_name = super(Candidates, self).get_full_name()
        if not full_name:
            full_name = self.email
        return full_name
