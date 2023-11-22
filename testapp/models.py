from django.db import models


    
class Users(models.Model):
    password = models.CharField(primary_key=True, max_length=50)
    sub_sr = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'