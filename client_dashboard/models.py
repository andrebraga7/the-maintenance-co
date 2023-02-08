from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    assignment = models.CharField(max_length=20, default='unassigned')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    feedback = models.TextField(
        max_length=200, blank=True, default='No feedback given so far.')
    deletion = models.BooleanField(default=False)

    def __str__(self):
        return self.title
