from django.shortcuts import render
import requests
def weather_view(request):
    API_KEY = '343ff9c9d338008ce0b6e4063958ad2b'
    weather_data={}
    city=''
    if request.method == 'POST':
        city=request.POST.get('city')
        url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'
        response = requests.get(url)
        if response.status_code == 200:
            data=response.json()
            weather_data={
                'city':data['name'],
                'temperature':data['main']['temp'],
                'humidity':data['main']['humidity'],
                'pressure':data['main']['pressure'],
                'wind':data['wind']['speed'],
                'description':data['weather'][0]['description'],
                'icon':data['weather'][0]['icon'],

            }
        else:
            weather_data={
                'error':'Город не найден',
            }
    return render(request,'weather_app/weather.html',{'weather_data':weather_data,'city':city})

# Create your views here.
