from django.shortcuts import render, render_to_response
from django.template import RequestContext

from cars.models import Car
from cars.forms import CarForm

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cars.serializers import CarSerializer

def carHome(request):
    if request.POST:
        form = CarForm(request.POST)
        if form.clean:
            instance = form.save(commit = False)
            instance.save() 
    form = CarForm()
    return render_to_response('car_home.html', locals(), context_instance=RequestContext(request))

@api_view(['GET', 'POST'])
def listCars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many = True)
    return Response(serializer.data)



