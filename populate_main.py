import os
import urllib
import random

# Предварительная настройка
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nikah.settings')

import django 
django.setup()

from django.core.files import File
from apps.main.models import Category, Item, Comment, FeedBack


# Фото одежд с сайта вконтакте

photo_urls = (
    'https://pp.userapi.com/c636116/v636116486/3ca29/Rf1W2sgK3E4.jpg',
    'https://pp.userapi.com/c636116/v636116486/3ca1f/JkMDNqreyRY.jpg',
    'https://pp.userapi.com/c636116/v636116486/3ca15/rcAgI6rTVOU.jpg',
    'https://pp.userapi.com/c636116/v636116486/3ca0c/Z_D6YkdEtek.jpg',
    'https://pp.userapi.com/c636116/v636116486/3ca02/Zne4T8sRkeo.jpg',
    'https://pp.userapi.com/c636116/v636116486/3c9f9/O0XzsGje48s.jpg',
    'https://pp.userapi.com/c636116/v636116486/3c9f0/2XrLq9ra2Q0.jpg',
    'https://pp.userapi.com/c636116/v636116486/3c9dc/oK_vXHmzcqk.jpg',
    'https://pp.userapi.com/c636116/v636116486/3c9d2/ykqbOzQi7_M.jpg',
    'https://pp.userapi.com/c636116/v636116486/3c9bf/5w78YK0B0js.jpg')


# Функции для заполнения базы данных некоторыми данными

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_item(cat, name, description, price=1000, photo=None, views=0):
    i = Item.objects.get_or_create(category=cat, name=name, price=price)[0]
    i.description = description
    i.price = price
    photo = random.choice(photo_urls)
    result = urllib.request.urlretrieve(photo)
    i.photo.save(
        os.path.basename(photo),
        File(open(result[0], 'rb')))
    i.views = views
    i.save()
    return i


def add_comment(item, name, email, message, published=True):
    c = Comment.objects.get_or_create(
        item=item,
        name=name,
        email=email,
        message=message,
        published=published)[0]
    c.save()
    return c


def add_feedback(name, email, message, published=True):
    f = FeedBack(
        name=name,
        email=email,
        message=message,
        published=published)
    f.save()
    return f


# Функция заполняет базу данных

def populate():

    # Одежда для никаха

    nikah_cat = add_cat('Одежда для никаха')

    # mikah_cat items

    # Синее платье

    blue_dress = add_item(
        cat=nikah_cat,
        name="Синее платье",
        description="Это платье отлично подойдет для вас",
        price=1234.56,
        views=12)

    # blue_dress comments

    add_comment(
        blue_dress,
        'Azat',
        'test@test.com',
        'Отличный продукт')

    add_comment(
        blue_dress,
        'Richard',
        'test@test.ru',
        'Великолепно')

    # Платье № 1

    dress1 = add_item(
        cat=nikah_cat,
        name="Платье № 1",
        description="Это первое платье",
        price=1366.20,
        views=10)

    # dress1 comments

    add_comment(
        dress1,
        'Azat',
        'test@test.com',
        'Отличный продукт')

    add_comment(
        dress1,
        'Black man',
        'test@test.ru',
        'Красивое платье')

    add_comment(
        dress1,
        'Richard',
        'test@test.ru',
        'Превосходно!')

    add_comment(
        dress1,
        'Mercuriy',
        'test@test.ru',
        'Мне нравится')

    # Платье № 2

    add_item(
        cat=nikah_cat,
        name="Платье № 2",
        description="Это второе платье",
        price=1450.98,
        views=15)

    # Категория: платки

    platki_cat = add_cat('Платки')

    add_item(
        cat=platki_cat,
        name="Платок 1",
        description="Это платок",
        price=346,
        views=12)

    add_item(
        cat=platki_cat,
        name="Платок 2",
        description="Это платок 2",
        price=476,
        views=10)

    add_item(
        cat=platki_cat,
        name="Платок 3",
        description="Это третий платок",
        price=134.2,
        views=15)

    # Категория: длинные юбки

    jubki_cat = add_cat('Длинные юбки')

    add_item(
        cat=jubki_cat,
        name="Юбка 1",
        description="Это юбка",
        price=198.90,
        views=1)

    add_item(
        cat=jubki_cat,
        name="Юбка 2",
        description="Это юбка 2",
        price=202.30,
        views=15)

    # Категория: платья

    add_cat('Платья')

    # отзывы

    add_feedback(
        name='Azat',
        email='test@test.com',
        message='Отличный сайт')

    add_feedback(
        name='Conor',
        email='test@test.com',
        message='Мне нравится')

    add_feedback(
        name='Azat',
        email='test@test.com',
        message='Все прекрасно работает')

    # Вывод на консоль:
    for c in Category.objects.all():
        for p in Item.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))
            for com in Comment.objects.filter(item=p):
                print("-- {}".format(str(com)))
    print("Отзывы:")
    for f in FeedBack.objects.all():
        print("- {}".format(str(f)))


if __name__ == '__main__':
    populate()
