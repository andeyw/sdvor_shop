import string

from django.utils.crypto import random

from shop.models import Category, Product


def randstring(n):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])

def categories_generate():

    Category.objects.all().delete()
    for i in range(1,6):
            c = Category(code=i,name='Категория ' + str(i))
            c.save()

def products_generate():

        for i in range(1,6):
            c = Category.objects.get(code=i)
            Product.objects.all().filter(category=c).delete()

            for r in range(1,31):
                price = random.randint(10, 100)
                desc = randstring(300)
                p = Product(code= i + r,name='Товар ' + str(r)+str(i),
                            category=c,price=price,description=desc)
                p.save()
