from django.db import models


CATEGORIES = (
    (0, 'Kitchen'),
    (1, 'Front Counter'),
    (2, 'Dinning Area'),
    (3, 'Back Area'),
    (4, 'Building Facilities'),
    (5, 'Eletrical'),
    (6, 'Other'))


class Job(models.Model):
    category = models.CharField(choices=CATEGORIES,max_length=50, default=0)
    # equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    # client = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    assignment = models.CharField(max_length=20, default='unassigned')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)
    feedback = models.TextField(max_length=200)
    deletion = models.BooleanField(default=False)


# class Equipment(models.Model):
