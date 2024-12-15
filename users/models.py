from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UsersModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Уникальный email
    phone_number = models.CharField(max_length=15)
    data_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Хэшируем пароль при создании нового пользователя
        if not self.pk:  # Только для новых пользователей
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Проверяет, соответствует ли введённый пароль хэшированному"""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.first_name
