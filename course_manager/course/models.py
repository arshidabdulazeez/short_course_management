from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # details = models.TextField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    image = models.ImageField(upload_to='course_images/')

    def __str__(self):
        return self.title