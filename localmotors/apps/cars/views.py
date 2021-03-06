from django.shortcuts import render_to_response
from django.template import RequestContext

from cars.models import Car
from cars.forms import CarForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from cars.serializers import CarSerializer

def car_home(request):
    """ Car home. """
    if request.POST:
        form = CarForm(request.POST)
        if form.clean:
            instance = form.save(commit=False)
            instance.save() 
    form = CarForm()
    return render_to_response('car_home.html', locals(), context_instance=RequestContext(request))

@api_view(['GET', 'POST'])
def list_cars():
    """ DRF method to get list of cars. """
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

def hack():
     r = raw_input("Enter the range:")
     for i in xrange(1, int(r)+1):
        if i%3==0 and i%5==0:
             print "FizzBuzz" + "\n"
        elif i%3==0:
            print "Fizz" + "\n"
        elif i%5==0:
            print "Buzz" + "\n"
        else:
            print "%s \n" %i



