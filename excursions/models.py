from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

# Creates a Excursion model containing data about each individual Excursion
class Excursions(models.Model):
    CHOICES = (
       ('Active', ('Active')),
       ('Inactive', ('Inactive')),
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=201, null=True)
    Price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, default=0)
    main_image = models.ImageField(upload_to='excursions/uploads/', null=True)
    image_name = models.CharField(max_length=201, null=True, blank=True)
    description = RichTextUploadingField(null=False, blank=False, default='')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=CHOICES, default='Inactive', max_length=20)

    def __str__(self):
        return self.title
    

# Creates all the Excursion fotos
class Photos(models.Model):
    excursion = models.ForeignKey(Excursions, null=True, blank=True, on_delete=models.CASCADE, related_name='photos')
    images = models.ImageField(upload_to='excursions/uploads/', null=True)
    image_name = models.CharField(max_length=201, null=True, blank=True)
    
    def __str__(self):
        return self.image_name


# Creates excursion review model 
class Review(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True,)
    content = models.TextField(null=True, blank=True,)
    rating = models.IntegerField(null=True, blank=True, default=0)
    excursion = models.ForeignKey(Excursions, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title