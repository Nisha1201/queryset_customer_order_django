from django.contrib import admin
from .models import Customers,Order_items,Orders,Products

@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email_address','phone_number')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display=('id','customer','order_date','total_Amount')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=('id','product_name','category','description','price')



@admin.register(Order_items)
class Order_itemsAdmin(admin.ModelAdmin):
    list_display=('id','order','product','quantity','price')


