from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from .models import City
from .forms import CityForm
#from django.http import HttpResponse

def home(request):
    cities= City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fec603eb73ea64597f9c9e14ba30d1dc'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            #'icon' : city_weather['weather'][0]['icon']

        }
        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'index.html' , context)





    






# Create your views here.
