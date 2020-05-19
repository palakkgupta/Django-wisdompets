from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from .models import Pet
def home(request):
    #return HttpResponse('<p>home view</p>')
    pets=Pet.objects.all()
    return render(request,'home.html',{'pets':pets})


def pet_detail(request,id):
    #return HttpResponse('<p>pet_detail view with the id {}</p>'.format(id))
    try:
        pet=Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request,'pet_detail.html',{'pet':pet})