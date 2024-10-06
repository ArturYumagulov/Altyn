from django.db import models


# Create your models here.


class Region(models.Model):
    is_active = models.BooleanField(default=False, verbose_name="Активность")
    name = models.CharField(verbose_name="Название", max_length=500)
    other = models.BooleanField(verbose_name="Другой", default=False)
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
    speciality = models.ManyToManyField(Speciality, related_name="specialities")
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name="Регион")
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name="Населенный пункт")
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    email = models.EmailField(max_length=225, verbose_name="Электронный адрес")
    portfolio_link = models.URLField(verbose_name="Ссылка на портфолио")
    social_link = models.URLField(verbose_name="Ссылка на социальные сети")
    descriptions = models.TextField(verbose_name="Дополнительно")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалист"


class Director(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография")
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.pk}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"


class Producer(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Продюссер"
        verbose_name_plural = "Продюссеры"


class Scenarist(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    birthday = models.DateField(
        verbose_name="Дата рождения", blank=True, null=True, default=None
    )
    biography = models.TextField(verbose_name="Биография")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Сценарист"
        verbose_name_plural = "Сценаристы"


class Compositor(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Композитор"
        verbose_name_plural = "Композиторы"


class Operator(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Оператор"
        verbose_name_plural = "Операторы"
