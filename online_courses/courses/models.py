from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator

# Foydalanuvchi roli
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Kurslar modeli
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(5)
    ])
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

# Darslar modeli
class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_url = models.URLField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Izohlar modeli
class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"