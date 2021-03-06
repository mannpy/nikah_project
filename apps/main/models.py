# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unidecode import unidecode
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(_('name'), max_length=128, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Category, self).save(*args, **kwargs)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Item(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_('category'))
    name = models.CharField(_('name'), max_length=128)
    description = models.TextField(_('description'))
    price = models.FloatField(_('price'))
    photo = models.ImageField(_('image'), upload_to='main')
    views = models.PositiveIntegerField(_('views'), default=0)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('a good')
        verbose_name_plural = _('goods')


class CommentManager(models.Manager):
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(published=True, **kwargs)


class CommentAbstract(models.Model):
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(null=True)
    message = models.TextField(verbose_name=_('Message'))
    time = models.DateTimeField(auto_now_add=True, verbose_name=_('Time'))
    published = models.BooleanField(default=False, verbose_name=_('published'))

    objects = CommentManager()

    @python_2_unicode_compatible
    def __str__(self):
        return "%s: %s" % (self.email, self.name)

    class Meta:
        abstract = True


class FeedBack(CommentAbstract):

    class Meta:
        ordering = ['-time']
        verbose_name = _('a feedback')
        verbose_name_plural = _('feedback')


class Comment(CommentAbstract):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ['time']
        verbose_name = _('a comment')
        verbose_name_plural = _('comments')
