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

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=50, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    assignment = models.CharField(max_length=20, default='unassigned')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    feedback = models.TextField(max_length=200, blank=True)
    deletion = models.BooleanField(default=False)

    def generate_title(self):
        return f'Job for {self.equipment} in {self.category}'

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.generate_title()
        super(Job, self).save(*args, **kwargs)

    class Meta:
        permissions = [
            ('is_manager', 'Is manager'),
            ('is_employee', 'Is employee'),
            ('is_client', 'Is client')]

    def __str__(self):
        return self.title
