from django.shortcuts import render
from .models import Oquvchi
from school.models import sinf_royhati

# Create your views here.
def oquvchi(request):
    oquvchilar = Oquvchi.objects.all()
    chsb = sinf_royhati.objects.all()
    return render(request, 'maktab.html', {'oquvchilar': oquvchilar, 'chsb': chsb})