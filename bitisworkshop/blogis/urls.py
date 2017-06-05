from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^blogs/$', BlogView.as_view(), name='blog_list'),
    url(r'^blogs/post/(?P<pk>\d+)/$', SingleBlogPost.as_view(), name='single_blog'),
    url(r'^blogs/add/$', AddBlogView.as_view(), name='blog_add'),
]


