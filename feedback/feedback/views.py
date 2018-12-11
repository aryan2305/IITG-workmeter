from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'feedback/index.html', None)
