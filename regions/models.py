from django.db import models

# Create your models here.


class Region(models.Model):
    name = models.CharField(verbose_name="Название", max_length=500)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регионы"
        verbose_name_plural = "Регион"


class Location(models.Model):
    name = models.CharField(verbose_name="Название", max_length=500)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name} - {self.region}"

    class Meta:
        verbose_name = "Локации"
        verbose_name_plural = "Локация"
