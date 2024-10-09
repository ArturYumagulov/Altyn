import secrets

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from regions.models import Region, Location
from users.managers import CustomUserManager
# from users.services import generate_hex_token


# Create your models here.

class SocialNets(models.Model):
    name = models.CharField(verbose_name="Название", max_length=300)
    icon = models.ImageField(upload_to="social_network/", verbose_name="Иконка")
    is_active = models.BooleanField(verbose_name="Активность", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Социальные сети"
        verbose_name_plural = "Социальные сети"


class Roles(models.Model):
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    name = models.CharField(verbose_name="Название", max_length=300)
    created_date = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    edit_date = models.DateField(verbose_name="Дата изменения", auto_now=True)
    default = models.BooleanField(verbose_name="По умолчанию", default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class CustomUser(AbstractBaseUser, PermissionsMixin):

    MALES = [
        ("M", "Мужской"),
        ("F", "Женский"),
    ]

    username = models.CharField('Логин', max_length=255, unique=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=30, null=True, blank=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True)
    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True, null=True)
    surname = models.CharField(verbose_name="Отчество", max_length=100, blank=True, null=True)
    site = models.CharField(verbose_name="Сайт", max_length=1000, blank=True, null=True, default=None)
    # social_networks = models.ManyToManyField('SocialNetsData', related_name='socials', verbose_name="Социальные сети",
    #                                          blank=True, default=None)
    social_networks = models.CharField(max_length=2000, verbose_name="Социальные сети",
                                       blank=True, null=True, default=None)
    male = models.CharField(choices=MALES, max_length=1, default=None, blank=True, null=True, verbose_name="Пол")
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name="Роль", null=True, default=None, blank=True)
    birthday = models.DateField(verbose_name="Дата рождения", blank=True, null=True, default=None)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион", blank=True, null=True,
                               default=None)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="Локация", blank=True, null=True,
                                 default=None)
    company_name = models.CharField(max_length=1000, verbose_name="Наименование компании", blank=True,
                                    null=True, default=None)
    platform_name = models.CharField(max_length=1000, verbose_name="Наименование площадки", blank=True,
                                     null=True, default=None)
    date_joined = models.DateTimeField(auto_now_add=True)
    verify_token = models.CharField(max_length=40, blank=True, null=True, default=secrets.token_hex(20))

    is_staff = models.BooleanField(default=False, verbose_name="Сотрудник")
    is_active = models.BooleanField(default=False, verbose_name="Активирован")
    is_superuser = models.BooleanField(default=False, verbose_name="Суперпользователь")
    is_looking = models.BooleanField(default=False, verbose_name="Смотрит")
    is_shooting = models.BooleanField(default=False, verbose_name="Снимает")
    is_show = models.BooleanField(default=False, verbose_name="Показывает")
    is_organize = models.BooleanField(default=False, verbose_name="Продвигает")
    is_verified = models.BooleanField(_('verified'), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        unique_together = ('username', 'email', 'phone')

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
