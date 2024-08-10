from django.shortcuts import render,HttpResponse,get_object_or_404
from . models import Image
from django.db.models import Q,query
from django.http import HttpResponseBadRequest
# Create your views here.
def index(request):
    obj=Image.objects.all()
    return render(request,'index.html',{'image':obj})


def detail_view(request, id=None, slug=None):
    # Try to get object by ID first, if ID is provided
    if id is not None:
        try:
            obj = get_object_or_404(Image, id=id)
        except ValueError:
            return HttpResponseBadRequest("Invalid ID format.")
    # If no ID, fall back to slug
    elif slug is not None:
        obj = get_object_or_404(Image, slug=slug)
    else:
        return HttpResponseBadRequest("No ID or Slug provided.")
    
    return render(request, 'details.html', {'image': obj})


def search(request):
    query=None
    result=[]
    if request.method == 'GET':
        query=request.GET.get('search')
        result=Image.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query))
    return render(request,'search.html',{'query':query,'result':result})