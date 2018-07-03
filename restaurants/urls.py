from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.RestaurantCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.RestaurantDetailView.as_view(), name="detail"),
    url(r'^update/(?P<pk>\d+)/$', views.RestaurantUpdateView.as_view(), name="update"),
    url(r'^$', views.RestuarantListview.as_view(), name="list"),
]