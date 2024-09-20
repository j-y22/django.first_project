from django.shortcuts import render
from .models import Author, Profile
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

def my_view(request):
    car_list = [
        {"title": "BMW"},
        {"title": "Mazda"}
    ]
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)

def car_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")

class CarListView(TemplateView):
    template_name= "my_first_app/car_list.html"

    def get_context_data(self):
        car_list = [
            {"title": "BMW"},
            {"title": "Mazda"},
        ]
        return {
            "car_list": car_list
        }

def author_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    author = Author.objects.get(id=kwargs['id'])
    profile = Profile.objects.get(author_id=kwargs['id'])
    return HttpResponse(f"Author: {author.name} - Website: {profile.website} - Biografia: {profile.biography} ")