from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# class User(AbstractUser):
#     phone = models.CharField(max_length=13, blank=True, null=True, unique=True, db_index=True)
#     auth_code = models.CharField(max_length=6, blank=True)

#     def __str__(self) -> str:
#         return f"{self.username}"


# class AuthUser(models.Model):
#     # ...
#     groups = models.ManyToManyField(User, related_name='auth_user_groups')
#     user_permissions = models.ManyToManyField(User, related_name='auth_user_permissions')


# class MainUser(models.Model):
#     # ...
#     groups = models.ManyToManyField(User, related_name='main_user_groups')
#     user_permissions = models.ManyToManyField(User, related_name='main_user_permissions')


class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.title    


class Tag(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.title    



class Course(models.Model):
    LANGUAGES = (
        ("uz", "O'zbekcha"),
        ("ru", "Ruscha"),
        ("en", "Inglizcha"),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255,unique=True,blank=True)
    description = models.TextField()
    duration = models.DurationField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(verbose_name="Boshlanish vaqti")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Yangilanish vati")
    language = models.CharField(max_length=100,blank=True,choices=LANGUAGES)
    rating = models.PositiveBigIntegerField(verbose_name="Rating", default=0)
    image = models.ImageField(upload_to="images",blank=True)
    tags = models.ManyToManyField(Tag, verbose_name="tags")




class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    