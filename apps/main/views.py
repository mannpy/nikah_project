# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
# from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.shortcuts import redirect
from django.contrib import messages
#  django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
# django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pure_pagination.mixins import PaginationMixin
from .models import Category, Item, FeedBack
from .forms import OrderForm, FeedbackForm


class HomeList(PaginationMixin, ListView):
    queryset = Item.objects.order_by('-pub_date')
    template_name = "main/index.html"
    context_object_name = 'items'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['slider'] = Item.objects.order_by('-views')[:6]
        return context


class ProductList(PaginationMixin, ListView):
    queryset = Item.objects.order_by('-pub_date')
    template_name = "main/products.html"
    context_object_name = 'items'
    paginate_by = 6


class CategoryList(PaginationMixin, ListView):
    template_name = 'main/products.html'
    context_object_name = 'items'
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(
            Category, slug=self.kwargs['category_name_slug'])
        return Item.objects.filter(
            category=self.category).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


def product_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.views += 1
    item.save()
    return render(request, 'main/product_detail.html', {'item': item})


def feedback(request):
    from pure_pagination import Paginator, PageNotAnInteger
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            fb = form.save(commit=False)
            fb.published = True
            fb.save()
            messages.success(request, 'Thank you for your feedback')
            return redirect('main:feedback')
    else:
        form = FeedbackForm()
    feedback = FeedBack.objects.filter(published=True).order_by('-time')
    p = Paginator(feedback, 10, request=request)
    pages = p.page(page)
    return render(request, 'main/feedback.html', {
        'form': form, 'feedback': feedback, 'pages': pages})


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


""""
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        items_list = Item.objects.filter(category=category)
        page = request.GET.get('page', 1)
        paginator = Paginator(items_list, 10)
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context_dict['items'] = items
        context_dict['category'] = category
    except Category.DoesNotExist:
            context_dict['category'] = None
            context_dict['items'] = None
    return render(request, 'main/products.html', context_dict)
    """
