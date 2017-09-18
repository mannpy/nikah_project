# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib import messages
from django.views.generic import ListView
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.utils.translation import ugettext as _
# from django.http import HttpResponseRedirect
#  django.core.urlresolvers import reverse
# django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..pure_pagination import Paginator
from ..pure_pagination.mixins import PaginationMixin
from .models import Category, Item, FeedBack
from .forms import OrderForm, FeedbackForm, CommentForm


class ProductsMixin(object):
    template_name = "main/products.html"
    context_object_name = 'items'
    paginate_by = 6


class HomeList(ProductsMixin, PaginationMixin, ListView):
    queryset = Item.objects.order_by('-creation_date')
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeList, self).get_context_data(**kwargs)
        context['slider'] = Item.objects.order_by('-views')[:6]
        return context


class ProductList(ProductsMixin, PaginationMixin, ListView):
    queryset = Item.objects.order_by('-creation_date')


class CategoryList(ProductsMixin, PaginationMixin, ListView):

    def get_queryset(self):
        self.category = get_object_or_404(
            Category, slug=self.kwargs['category_name_slug'])
        return Item.objects.filter(
            category=self.category).order_by('-creation_date')

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


def product_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.views += 1
    item.save()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.published = True
            c.item = item
            c.save()
            messages.success(request, _('Thank you for your comment'))
            return redirect('main:product_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'main/product_detail.html', {
        'item': item, 'form': form})


def feedback(request):
    page_num = request.GET.get('page', 1)
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.published = True
            fb.save()
            messages.success(request, _('Thank you for your feedback'))
            return redirect('main:feedback')
    else:
        form = FeedbackForm()
    feedback = FeedBack.objects.published()
    p = Paginator(feedback, 10, request=request)
    pages = p.page(page_num)
    return render(request, 'main/feedback.html', {
        'form': form, 'pages': pages})


def callback(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        subject = "Заявка на обратный звонок"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'maaz1313@gmail.com']
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            template = get_template('callback.txt')
            context = {
                'name': name,
                'phone': phone,
            }
            content = template.render(context)
            send_mail(
                subject,
                content,
                from_email,
                to_email,
                fail_silently=False,
            )
            return redirect('main:home')
