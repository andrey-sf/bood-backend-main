from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, name=""):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, name=""):
        """
        Creates and saves a Superuser with the given email and password.
        """
        user = self.create_user(email=email, password=password, name=name)
        user.is_admin = True
        user.save(using=self._db)
        return user


# Custom User Model.
class Person(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="Эл. почта",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255, blank=True, verbose_name="Имя")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_admin = models.BooleanField(default=False, verbose_name="Админ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Зарегистрирован")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    is_verified = models.BooleanField(("Подтвержден"), default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
