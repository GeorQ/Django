from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.FloatField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100, unique=True)

