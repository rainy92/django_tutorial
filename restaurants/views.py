from django.views import generic
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import RestaurantLocation
from django.db.models import Q
from .forms import RestaurantCreateForm


def restaurant_listview(request):
    template_name = 'restaurants/restaurant_list.html' 
    queryset = RestaurantLocation.objects.all()
    context = {
        'restaurant_list': queryset
    }
    return render(request, template_name, context)


def restaurant_createview(request):
    form = RestaurantCreateForm(request.POST or None)
    if form.is_valid():
        obj = RestaurantLocation.objects.create(
            name = form.cleaned_data.get('name'),
            location=form.cleaned_data.get('location'),
            category=form.cleaned_data.get('category'),
        )
    return HttpResponseRedirect('/restaurantlist/')
    if form.errors:
        print(form.errors)
    template_name = 'restaurants/form.html'
    context ={'form': form}
    return render(request, template_name, context)


class RestuarantListview(generic.ListView):
    # template_name = 'restaurants/restaurant_list.html'   # it takes bydefault name 'modelname_list.html' 
    queryset = RestaurantLocation.objects.all()
    context_object_name = 'restaurant_list'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter( Q(category__iexact=slug) | Q(category__icontains=slug))
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(generic.DetailView):
    queryset = RestaurantLocation.objects.all()
    
    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     slug = self.kwargs.get("slug")
    #     obj = get_object_or_404(RestaurantLocation, id=slug)
    #     return obj  
        
