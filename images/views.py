import logging

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from images.forms import UploadForm
from images.models import Image
from images.tables import ImageTable


logger = logging.getLogger(__name__)

def index_view(request):
    
    from django.http import JsonResponse
    return JsonResponse({'foo':'bar'})

