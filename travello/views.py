from django.shortcuts import render
from .models import destination


def index(request):
    descs = destination.objects.all()


    return render(request, "index.html",{'descs': descs} )

