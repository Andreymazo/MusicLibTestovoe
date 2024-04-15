from django.db import models

from musiclib.managers import CustomUserManager

NULLABLE = {'blank': True, 'null': True}

from django.contrib.auth.base_user import AbstractBaseUser

class CustomUser(AbstractBaseUser):  # , PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=30, **NULLABLE)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.id}: {self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
    
class MusicFiles(models.Model):
    title = models.CharField(max_length=150, verbose_name='название произведения')
    file = models.FileField(upload_to='media/')
    customuser = models.ForeignKey('musiclib.Customuser', related_name='musicfiles', on_delete=models.CASCADE, **NULLABLE)
