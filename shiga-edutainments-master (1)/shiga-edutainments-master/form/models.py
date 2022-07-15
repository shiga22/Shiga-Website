from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    details = models.TextField()
    happy = models.BooleanField()
    good =models.BooleanField()
    average =models.BooleanField()
    bad =models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
