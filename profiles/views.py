from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views import generic
from menus.models import Item
from restaurants.models import RestaurantLocation
from .models import Profile


User = get_user_model()


class ProfileFollowToggle(LoginRequiredMixin, generic.View):
    
    def post(self, request, *args, **kwargs):
        user_to_toggle = request.POST.get("username")
        profile_ = Profile.objects.get(username__iexact=user_to_toggle)
        user = request.user
        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)

        return redirect('/profiles/rainy/')     


class ProfileDetailView(generic.DetailView):
    template_name = 'profiles/user.html'
    # context_object_name = 'user'

    def get_object(self):
        username = self.kwargs.get('username')
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        user = context['user']
        query = self.request.GET.get('q')
        item_exist = Item.objects.filter(user=user)
        rest_qs = RestaurantLocation.objects.filter(owner=user).search(query)
        # if query:
        #     rest_qs = rest_qs.search(query)

        if item_exist.exists() and rest_qs.exists():
            context['locations'] = rest_qs
        return context
        



