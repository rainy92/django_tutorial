from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views import View
import random

# def home_old(request):
#     _html_var = 'deatils'  #f string is not working here
#     number = random.randint(0, 10000)
#     _html = f"""
#         <!DOCTYPE html>
#         <html lang=en>
#             <head> <title> Restaurant </title> </head>
#             <body>
#                 <h1> Welcome to our Restaurant's Home Page </h1>
#                 <p> Here will be the details of Restaurant </p>
#                 <p> Random number is : { number } </p>
#             </body>
#         </html>"""

#     return HttpResponse(_html)
# #     return render(request, 'home.html')


def home(request):
    number = random.randint(0, 10000)
    menu_list = [number, random.randint(0, 1000), random.randint(0, 1000000)]
    context = {
        'home_var': 'Home Page',
        'random_num': number, 
        'bool_item': False,
        'menu_list': menu_list,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


# class ContactView(View):
#     def get(self, request, *args, **kwargs):
#         print(kwargs)
#         context={}
#         return render(request, 'contact.html', context)

#     # def post(self, request, *args, **kwargs):
#     #     print(kwargs)
#     #     context={}
#     #     return render(request, 'contact.html', context)

#     # def put(self, request, *args, **kwargs):
#     #     print(kwargs)
#     #     context={}
#     #     return render(request, 'contact.html', context)


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        number = random.randint(0, 10000)
        menu_list = [number, random.randint(0, 1000), random.randint(0, 1000000)]
        context = {
            'home_var': 'Home Page',
            'random_num': number,
            'bool_item': False,
            'menu_list': menu_list,
        }
        return context  



class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'

