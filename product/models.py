from django.db import models

class Customers(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email_address=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=12)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Orders(models.Model):
    # customer=models.ForeignKey(Customers,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,related_name='customer')
    order_date=models.DateField(auto_now=False, auto_now_add=False)
    total_Amount=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Customer: {self.customer} - Total Amount: {self.total_Amount}"

class Products(models.Model):
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name

class Order_items(models.Model):
    order=models.ForeignKey(Orders,on_delete=models.CASCADE,related_name='item')
    product=models.ForeignKey(Products,on_delete=models.CASCADE,related_name='result')
    quantity=models.IntegerField(default=0)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order: {self.order} - Product: {self.product}"

