from django.db.models import Q
from django.views import generic
from .models import RestaurantLocation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


# def restaurant_listview(request):
#     template_name = 'restaurants/restaurant_list.html' 
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         'restaurant_list': queryset
#     }
#     return render(request, template_name, context)


# @login_required(login_url='/login/')
# def restaurant_createview(request):
#     form = RestaurantLocationCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         print("form is valid")
#         if request.user.is_authenticated:
#             print("authentication:", request.user.is_authenticated)
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             print("owner:", instance.owner)
#             instance.save()
#             # obj = RestaurantLocation.objects.create(
#             #     name = form.cleaned_data.get('name'),
#             #     location=form.cleaned_data.get('location'),
#             #     category=form.cleaned_data.get('category')
#             # )
#             return HttpResponseRedirect('/restaurants/')
#         else:
#             return HttpResponseRedirect('/login/')
#     if form.errors:
#         print(form.errors)
#         errors = form.errors
#     template_name = 'restaurants/form.html'
#     context ={'form': form, 'errors': errors}
#     return render(request, template_name, context)


class RestuarantListview(LoginRequiredMixin, generic.ListView):
    # template_name = 'restaurants/restaurant_list.html'   # it takes bydefault name 'modelname_list.html' 
    # queryset = RestaurantLocation.objects.all()
    context_object_name = 'restaurant_list'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    # def get_queryset(self):
    #     slug = self.kwargs.get("slug")
    #     if slug:
    #         queryset = RestaurantLocation.objects.filter( Q(category__iexact=slug) | Q(category__icontains=slug))
    #     else:
    #         queryset = RestaurantLocation.objects.all()
    #     return queryset
    

class RestaurantDetailView(generic.DetailView):
    template_name='restaurants/detail-update.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


        

class RestaurantCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    success_url = '/restaurants/'
    login_url = '/login/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user

        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title']= "Add Restaurant"
        return context


class RestaurantUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'form.html'
    model = RestaurantLocation

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title']= "Update Restaurant"
        return context