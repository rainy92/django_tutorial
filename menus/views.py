from django.shortcuts import render
from django.views import generic
from .models import Item
from .forms import ItemForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemListView(generic.ListView):

    context_object_name = 'menus_list'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(generic.DetailView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ItemForm
    template_name = 'form.html'

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Menu'
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    
    def get_form_kwargs(self, *args, **kwargs):
        super(ItemCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user']=self.request.user
        return kwargs




class ItemUpdateView(LoginRequiredMixin, generic.UpdateView):

    form_class = ItemForm
    model = Item
    template_name = 'form.html'
    
    # def get_queryset(self):
    #     return Item.objects.filter(user=self.request.user)


    # def get_context_data(self, *args, **kwargs):
    #     context = super(ItemUpdateView, self).get_context_data(*args, **kwargs)
    #     context['title'] = 'Update Menu'
    #     return context

    # def get_form_kwargs(self, *args, **kwargs):
    #     super(ItemUpdateView, self).get_form_kwargs(*args, **kwargs)
    #     kwargs['user']=self.request.user
    #     return kwargs