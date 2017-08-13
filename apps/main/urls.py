from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.HomeList.as_view(), name='home'),
    url(r'^login/$', login, {
        'template_name': 'main/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^category/all$', views.ProductList.as_view(), name='products'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.CategoryList.as_view(), name='show_category'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail,
        name="product_detail"),
    url(r'^callback/$', views.callback,
        name="callback"),
    url(r'^feedback/$', views.feedback,
        name="feedback"),
]
