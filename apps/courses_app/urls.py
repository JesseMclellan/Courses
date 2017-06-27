from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^are_you_sure/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^are_you_sure/(?P<id>\d+)$', views.are_you_sure),
    url(r'^course_entry$', views.course_entry),
    url(r'^$', views.index),
]
