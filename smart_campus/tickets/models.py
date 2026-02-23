from django.db import models

class Ticket(models.Model):

    

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    category = models.CharField(max_length=50)
    priority = models.CharField(max_length=20)
    

    def __str__(self):
        return self.title