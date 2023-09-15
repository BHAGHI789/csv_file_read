from django.db import models

# Create your models here.
class CSVRequest(models.Model):
    num_records = models.IntegerField()
    new_file_name = models.CharField(max_length=255)