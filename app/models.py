from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
    routes = models.ManyToManyField('Route', related_name="stations", verbose_name='Маршруты')

    class Meta:
        verbose_name = 'Остановка'
        verbose_name_plural = 'Остановки'

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=50, verbose_name='Маршрут')

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return self.name