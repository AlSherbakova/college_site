from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    curator = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    clubs = models.ManyToManyField(Club, blank=True)
    photo = models.ImageField(upload_to='students_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
