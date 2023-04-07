from django.shortcuts import render
from .models import Customers,Orders,Order_items,Products
from django.db.models import Avg, Sum, Min, Max, Count,StdDev,Variance

def customer_orders(request):
    customers = Customers.objects.prefetch_related('customer__item__product')

    for customer in customers:
      print("Customer Name:", customer.first_name, customer.last_name)
      print("Email Address:", customer.email_address)
      print("Phone Number:", customer.phone_number)
      for order in customer.customer.all():
            print("Order Date:", order.order_date)
            print("Total Amount:", order.total_Amount)
            for item in order.item.all():
                  print("Product Name:", item.product.product_name)
                  print("Category:", item.product.category)
                  print("Description:", item.product.description)
                  print("Price:", item.price)
                  print("Quantity:", item.quantity)
      print("\n")

      # # annotate():---------------------------------------------------------------------------------------
      # pro=Customers.objects.annotate(Avg('customer__id'),Sum('customer__id'))
      # for i in pro:
      #      print(
      #           i.customer__id__avg
      #       #     i.customer__id__sum,

      #      )
      # print(pro,"ooooooooooooooooooooooooooooo")

      # customers = Customers.objects.prefetch_related('orders_set__item__product').get(id=1)
      # for order in customers.orders_set.all():
      #       print("bshdbdkjsbdkj",order)
      #       for pro in order.item.all():
      #             print(pro.product.category)
      #             print(pro.product)
      #             print(pro.dis)
      #             print(pro.quantity)
      # print(customers.query,"queryyyyyyyyyyyyyyyyyyyyyyy")
      # orders = Orders.objects.filter(customer_ID=customer.customer_ID).select_related('order_items').prefetch_related('order_items_set__products')
      # print(orders)
      
      # order=Orders.objects.filter(customer_ID=customer.customer_ID)
      # print(order)

      # order_items=Order_items.objects.filter(order_ID__in=order.values_list('order_ID',flat=True))
      # print(order_items)
      # product = Products.objects.filter(product_name__in=order_items.values_list('product_name', flat=True))    
      # print(product)
     
     
      context={
            'customers':customers,
            # 'order':orders,


            # 'order_items':order_items,
            # 'product':product
      }
      return render(request,'home.html',context)
          
