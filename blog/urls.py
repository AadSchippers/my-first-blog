from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/comment/(?P<pk>\d+)/$', views.comment_new, name='comment_new'),
    url(r'^logout/$', views.bloglogout, name ='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'blog/login.html'}, name='login'),
]
