from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

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
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^restaurants/', include('restaurants.urls', namespace="restaurants")),
    url(r'^menus/', include('menus.urls', namespace="menus")),
]
