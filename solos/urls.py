from django.conf.urls import url
from solos.views import index, SoloDetailView

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'solos/(?P<pk>\d+)/$', SoloDetailView.as_view(), name="detail"),
]
