from django.db import models

# Create your models here.
class Job(models.Model):
    # Images (you will need pillow - pip3 install pillow)
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary