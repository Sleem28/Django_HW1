from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'Client info:\nName: {self.name}\nEmail: {self.email}\nPhone number: {self.phone}\n' \
               f'Address: {self.address}\n'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=0)
    date_of_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product info:\nName: {self.name}\nDescription: {self.description}\nPrice: {self.price}\n' \
               f'Pieces: {self.quantity}\nCreate date: {self.date_of_order}\n'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_of_order = models.DateTimeField(auto_now_add=True)

    





