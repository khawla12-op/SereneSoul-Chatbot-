from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=250, blank=True, null=True)
    Occupation = models.CharField(max_length=50, blank=True, null=True)
    institution = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.TextField()
    image = models.ImageField(upload_to='./static/users', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='./static/users', blank=True, null=True)
    friends= models.ManyToManyField('self', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
