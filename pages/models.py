from django.db import models
from django import forms
from common import BaseModel

class ContactForm(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    subject = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.name
