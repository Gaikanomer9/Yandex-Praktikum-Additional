from django.db import models
import datetime


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    issued = models.DateField(default=datetime.date(1970, 1, 1))
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    marginal_price = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class StoreChain(models.Model):
    name = models.CharField(max_length=300)
    stores = models.ManyToManyField(Store, related_name='chains')
    best_store = models.ForeignKey(Store,
                                   related_name='championed_by',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name
