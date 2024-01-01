from django.db import models


# Create your models here.

class MenuItem(models.Model):
    category_index = models.IntegerField()
    category = models.CharField(max_length=20)
    main_num = models.IntegerField()
    main_name = models.CharField(max_length=20)
    sub_num = models.IntegerField()
    sub_name = models.CharField(max_length=20)
