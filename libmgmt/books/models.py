from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    '''Class to create books'''

    title = models.CharField(max_length=256)
    isbn = models.PositiveIntegerField(blank=False, null=False)
    edition = models.PositiveSmallIntegerField(blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    pages = models.PositiveSmallIntegerField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def get_abs_url(self):
        return reverse("products:product-detail",
                       kwargs={"id": self.id})  #f"/product/{self.id}/"