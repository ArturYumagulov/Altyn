from django.contrib.auth.base_user import BaseUserManager

from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username=None, email=None, phone=None, password=None, **extra_fields):

        if not username:
            username = email

        user = self.model(username=username, email=email, phone=phone, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username=username, phone=phone, email=email, password=password, **extra_fields)

    def create_superuser(self, username, email, phone, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(username=username, password=password, email=email, phone=phone, **extra_fields)
