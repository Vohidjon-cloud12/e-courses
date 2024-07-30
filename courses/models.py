from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from blogs.models import Author, Blog
from courses.managers import UserManager
from teachers.models import Teacher


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    number_of_students = models.IntegerField(default=0)
    price = models.FloatField()
    duration = models.IntegerField()
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='courses/images', null=True, blank=True)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def hours(self):
        if self.duration >= 60:
            hours = self.duration // 60
            return hours
    @property
    def minuts(self):
        if self.duration >= 60:
            minutes = self.duration % 60
            return minutes


    def __str__(self):
        return self.title

class CourseVideo(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='courses/videos', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class RatingChoices(models.TextChoices):
        Zero = '0'
        One = '1'
        Two = '2'
        Three = '3'
        Four = '4'
        Five = '5'

    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    is_published = models.BooleanField(default=False)
    rating = models.CharField(max_length=100, choices=RatingChoices.choices, default=RatingChoices.Zero.value)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    birth_of_date = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)