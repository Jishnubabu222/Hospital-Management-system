from django.db import models


# Create your models here.
class signup_db(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    status_choice = [('male', 'Male'), ('female', 'Female'), ('notspecified', 'Notspecified')]
    gender = models.CharField(max_length=25, choices=status_choice, default='Notspecified')

    def __str__(self):
        return self.name


class booking_db(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    status_choice = [('male', 'Male'), ('female', 'Female'), ('notspecified', 'Notspecified')]
    gender = models.CharField(max_length=25, choices=status_choice, default='Notspecified')
    department = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, default=0)
    message = models.CharField(max_length=200)
    payment = models.CharField(max_length=200, default=0)
    status_choice = [
        ('approve', 'approve'),
        ('reject', 'reject'),
        ('pending', 'pending')
    ]
    status = models.CharField(max_length=10, choices=status_choice, default='pending')

    def __str__(self):
        return self.name


class admin_log(models.Model):
    admin_name = models.CharField(max_length=25)
    admin_pass = models.CharField(max_length=25)

    def __str__(self):
        return self.admin_name


class docs_db(models.Model):
    doc_name = models.CharField(max_length=25)
    doc_id = models.CharField(max_length=25)
    doc_file = models.FileField(max_length=25)
    doc_department = models.CharField(max_length=25)

    def __str__(self):
        return self.doc_name
