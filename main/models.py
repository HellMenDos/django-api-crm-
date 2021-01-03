from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Pass = models.CharField(max_length=30)
    Activate = models.IntegerField()
    Role = models.IntegerField()

    def __str__(self):
        return f"{self.Name}"


class Message(models.Model):
    Сontractor = models.ForeignKey(User,related_name='contrMessage', on_delete = models.PROTECT)
    Customer = models.ForeignKey(User,related_name='custmMessage', on_delete = models.PROTECT)
    Message = models.TextField()
    Seen = models.IntegerField()


class Deal(models.Model):
    Title = models.CharField(max_length=30)
    Customer = models.ForeignKey(User,related_name='dealCustomer', on_delete = models.PROTECT)
    Message = models.TextField()
    Price = models.IntegerField()
    Status = models.IntegerField()

    def __str__(self):
        return f"{self.Title}"

class Start(models.Model):
    Сontractor = models.ForeignKey(User, related_name='contrStart', on_delete = models.PROTECT)
    Customer = models.ForeignKey(User, related_name='custmStart', on_delete = models.PROTECT)