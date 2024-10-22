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
    photo = models.ImageField(verbose_name="Фотография", upload_to='regions/specialists/')
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
        return f"{self.last_name} {self.first_name} {self.birthday}"

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
        return f"{self.last_name} {self.first_name} - {self.birthday}"

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


class ArtisticalDirector(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Художник постановщик"
        verbose_name_plural = "Художник постановщик"


class CostumerDesigner(models.Model):

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    slug = models.SlugField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Художник по костюмам"
        verbose_name_plural = "Художник по костюмам"


class ScreeningPoint(models.Model):
    """Точки кинопоказов"""

    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(verbose_name="Название", max_length=500)
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=30, null=True, blank=True)
    social_net = models.CharField(verbose_name="Ссылка на соцсеть", max_length=2000, null=True, blank=True)
    site = models.CharField(verbose_name="Сайт", max_length=2000, null=True, blank=True)
    address = models.CharField(verbose_name="Адрес", max_length=2000, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    image = models.ImageField(upload_to='regions/screening_points/')
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['pk']
        verbose_name = "Точка кинопоказа"
        verbose_name_plural = "Точки кинопоказа"


class RegionalInternetResources(models.Model):
    """Региональные интернет ресурсы """

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    name = models.CharField(verbose_name="Название", max_length=2000)
    link = models.URLField(verbose_name="Ссылка на ресурс")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Региональный интернет ресурс"
        verbose_name_plural = "Региональные интернет ресурсы "


class Production(models.Model):
    """Производство"""

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    name = models.CharField(verbose_name="Название", max_length=2000)
    logo = models.ImageField(upload_to="regions/productions/")
    services_type = models.TextField(verbose_name="Тип услуг")
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=30, null=True, blank=True)
    social_net = models.CharField(verbose_name="Ссылка на соцсеть", max_length=2000, null=True, blank=True)
    site = models.CharField(verbose_name="Сайт", max_length=2000, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Производство"
        verbose_name_plural = "Производства"


class RegionalProfile(models.Model):
    """Портрет региона"""

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    name = models.CharField(verbose_name="Название", max_length=2000)
    photo = models.ImageField(verbose_name="Фотография", upload_to='regions/regional_profile/', blank=True)
    descriptions = models.TextField(verbose_name="Краткая информация", blank=True)
    link_to_video = models.URLField(verbose_name="Ссылка на видео", blank=True)
    link_to_presentation = models.URLField(verbose_name="Ссылка на презентацию", blank=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Портрет региона"
        verbose_name_plural = "Портреты региона"


class FilmmakersChat(models.Model):
    """Чаты кинематографистов """

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    name = models.CharField(verbose_name="Название", max_length=2000)
    link_to_chat = models.URLField(verbose_name="Ссылка на чат", blank=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Чат кинематографистов"
        verbose_name_plural = "Чаты кинематографистов"


class LocationPhoto(models.Model):
    """Фотографии локаций"""

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    photo = models.ImageField(verbose_name="Фотография", upload_to='regions/locations/', blank=True)
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.photo.path}"

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Фотография локации"
        verbose_name_plural = "Фотографии локаций"


class RegionLocation(models.Model):
    """Локации"""

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    name = models.CharField(verbose_name="Название", max_length=2000)
    photo = models.ManyToManyField(LocationPhoto, verbose_name="Фотография", blank=True, related_name="photos")
    descriptions = models.TextField(verbose_name="Краткая информация", blank=True)
    address = models.CharField(verbose_name="Адрес", max_length=5000, blank=True)
    coordinates = models.CharField(max_length=500, verbose_name="Координаты", blank=True)
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=30, null=True, blank=True)
    social_net = models.CharField(verbose_name="Ссылка на соцсеть", max_length=2000, null=True, blank=True)
    site = models.CharField(verbose_name="Сайт", max_length=2000, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class Events(models.Model):
    """Мероприятия"""

    is_active = models.BooleanField(default=False, verbose_name="Активность")
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    name = models.CharField(verbose_name="Название", max_length=2000)
    photo = models.ImageField(verbose_name="Фотография", blank=True, upload_to='regions/events/')
    descriptions = models.TextField(verbose_name="Краткая информация", blank=True)
    site = models.CharField(verbose_name="Сайт", max_length=2000, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
