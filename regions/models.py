from django.db import models

from movies.models import Status


# Create your models here.


class Region(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="Активность")
    name = models.CharField(verbose_name="Название", max_length=500)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = "Регионы"
        verbose_name_plural = "Регион"


class Location(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="Активность")
    name = models.CharField(verbose_name="Название", max_length=500)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name} - {self.region}"

    class Meta:
        verbose_name = "Населённый пункт"
        verbose_name_plural = "Населённый пункт"


class Speciality(models.Model):

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    name = models.CharField(max_length=1000, verbose_name="Название")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальность"


class City(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="Активность")
    name = models.CharField(max_length=1000, verbose_name="Название")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Населенный пункт"
        verbose_name_plural = "Населенный пункт"


class Specialist(models.Model):

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    photo = models.FileField(verbose_name="Фотография", upload_to='specialists/')
    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True, null=True)
    surname = models.CharField(verbose_name="Отчество", max_length=100, blank=True, null=True)
    speciality = models.ManyToManyField(Speciality, related_name="specialities")
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name="Регион")
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name="Населенный пункт")
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    email = models.EmailField(max_length=225, verbose_name="Электронный адрес")
    portfolio_link = models.URLField(verbose_name="Ссылка на портфолио")
    social_link = models.URLField(verbose_name="Ссылка на социальные сети")
    descriptions = models.TextField(verbose_name="Дополнительно")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}"

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалист"
