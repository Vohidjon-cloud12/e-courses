from django.db import models


class Teacher(models.Model):
    class LevelChoices(models.TextChoices):
        JUNIOR = 'JUNIOR'
        MIDDLE = 'MIDDLE'
        SENIOR = 'SENIOR'

    full_name = models.CharField(max_length=100)
    rating = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='teachers/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('courses.Category', on_delete=models.CASCADE)
    level = models.CharField(choices=LevelChoices.choices, default=LevelChoices.MIDDLE.value)

    def __str__(self):
        return self.full_name
