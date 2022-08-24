from django.db import models

# Create your models here.
class Advert(models.Model):
    advert_name = models.CharField(max_length=100)
    advert_company = models.CharField(max_length=100)
    advert_city = models.CharField(max_length=20)
    advert_date = models.CharField(max_length=100)
    advert_desc = models.CharField(max_length=500)
    advert_experience = models.CharField(max_length=50)
    education_level = models.CharField(max_length=30)
    
class Meta:
    db_table = 'job_advert'