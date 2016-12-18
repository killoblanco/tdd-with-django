from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Solo


# Create your views here.
def index(request):
    context = {'solos': []}

    if request.GET.keys():
        solos_queryset = Solo.objects.all()

        if request.GET.get('instrument', None):
            solos_queryset = solos_queryset.filter(
                instrument=request.GET.get('instrument', None)
            )
        if request.GET.get('artist', None):
            solos_queryset = solos_queryset.filter(
                artist=request.GET.get('artist', None)
            )
        context['solos'] = solos_queryset

    return render_to_response('solos/index.html', context)


def SoloDetailView(DetailView):
    pass
