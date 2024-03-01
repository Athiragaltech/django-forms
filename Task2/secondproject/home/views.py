from django.shortcuts import render,redirect
from . models import student

# Create your views here.
def index(request):
    data ={
        'stu' :student.objects.all()

    }
    print(data)
    return render(request,'index.html',data)
def add(request):
    return render(request,'about.html')
def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        place=request.POST.get('place')
        print(name)
        query=student(name=name,place=place)
        query.save()
    return  redirect("/")
def delete(request,id):
    dlt=student.objects.get(id=id)
    dlt.delete()
    return redirect("/")
def edit(request,id):
    data={"data":student.objects.get(id=id)}
    return render(request,'edit.html',data)
def update(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        place=request.POST.get('place')
        edit=student.objects.get(id=id)
        edit.name=name
        edit.place=place
        edit.save()
        return redirect("/")

