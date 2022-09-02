from modulefinder import Module
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Document(models.Model):
    documentName = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.documentName

class User(models.Model):
    Tipe_document = models.ForeignKey(Document, on_delete=models.CASCADE)
    document = models.BigIntegerField()
    names = models.CharField(max_length=60) 
    surnames = models.CharField(max_length=60)
    hobbie = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombres
