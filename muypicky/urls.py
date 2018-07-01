from django.conf.urls import url
from django.contrib import admin
# from restaurants.views import home, about, contact, ContactView, ContactTemplateView
from restaurants import views
from django.views.generic import TemplateView

# urlpatterns =[
#     # url(r'^$', home),
#     # url(r'^contact/', contact),
#     # url(r'^about/', about),
#     # url(r'^contact/(?P<id>\d+)', ContactView.as_view()),
#     # url(r'^$', HomeView.as_view()),
#     # url(r'^about/', AboutView.as_view()),
#     # url(r'^contact/(?P<id>\d+)', ContactView.as_view()),
# ]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    url(r'^restaurantlist/create/$', views.restaurant_createview),
    url(r'^restaurantlist/(?P<slug>[\w-]+)/$', views.RestaurantDetailView.as_view()),
    url(r'^restaurantlist/$', views.RestuarantListview.as_view()),
    # url(r'^restaurantlist/(?P<rest_id>\w+)/$', views.RestuarantListview.as_view()),   
]
