from django.shortcuts import render
from .models import Description

# Create your views here.
def index(request):
    dests = Description.objects.all()

    return render(request,"index.html",{'dests':dests})
def home(request):
    query=request.GET.get("title")
    allCourses=None
    if query:
        allCourses=Course.objects.filter(name__icontains=query)
    else:
        allCourses=Course.objects.all()
    context={
        'courses':allCourses,
    }