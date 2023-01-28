from django.db import models

# Create your models here.


class Datas(models.Model):
    type_data = models.IntegerField()
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()

    storage = models.ForeignKey(
        'storege.Storage',
        on_delete = models.CASCADE,
        related_name = 'datas'
    )
