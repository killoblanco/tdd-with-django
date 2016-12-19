from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'/solos/(?P<pk>\d+)/$', views.SoloDetailView.as_view(), name="detail"),
]
