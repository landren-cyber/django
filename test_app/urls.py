from django.urls import path, include
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.product_list, name='catalog'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
    views.product_detail,
    name='product_detail'),
    url(r'^(?P<category_slug>[-\w]+)/$',
    views.product_list,
    name='product_list_by_category'),
]
