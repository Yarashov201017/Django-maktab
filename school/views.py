from django.shortcuts import render

from school.models import  sinf_royhati

# Create your views here.
def schols(request):
    chsb = sinf_royhati.objects.all()
    return render(request, 'maktab.html', {'chsb': chsb})

