import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nikah.settings')

import django 
django.setup()

from apps.main.models import Category, Item


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_item(cat, name, description, price=1000, photo=None, views=0):
    i = Item.objects.get_or_create(category=cat, name=name, price=price)[0]
    i.description = description
    i.price = price
    i.photo = photo
    i.views = views
    i.save()
    return i


def populate():
    nikah_cat = add_cat('Одежда для никаха')

    add_item(cat=nikah_cat,
        name="Синее платье",
        description="Это платье отлично подойдет для вас",
        price=1234.56,
        views=12)

    add_item(cat=nikah_cat,
        name="Платье № 1",
        description="Это первое платье",
        price=1366.20,
        views=10)

    add_item(cat=nikah_cat,
        name="Платье № 2",
        description="Это второе платье",
        price=1450.98,
        views=15)

    platki_cat = add_cat('Платки')

    add_item(cat=platki_cat,
        name="Платок 1",
        description="Это платок",
        price=346,
        views=12)

    add_item(cat=platki_cat,
        name="Платок 2",
        description="Это платок 2",
        price=476,
        views=10)

    add_item(cat=platki_cat,
        name="Платок 3",
        description="Это третий платок",
        price=134.2,
        views=15)

    jubki_cat = add_cat('Длинные юбки')

    add_item(cat=jubki_cat,
        name="Юбка 1",
        description="Это юбка",
        price=198.90,
        views=1)

    add_item(cat=jubki_cat,
        name="Юбка 2",
        description="Это юбка 2",
        price=202.30,
        views=15)

    add_cat('Платья')

    for c in Category.objects.all():
        for p in Item.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


if __name__ == '__main__':
    populate()
