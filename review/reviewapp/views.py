from django.shortcuts import render,redirect
from.models import reviews
from .forms import laptopform
from django.contrib import messages

# Create your views here.
def index(request):
    obj=reviews.objects.all()

    return render(request,'index.html',{'rev':obj})

def vreview(request,nu):
    obj=reviews.objects.get(id=nu)
    return render(request,'reviews.html',{'rev':obj})

def new(request):
    if request.method=='POST':
        name=request.POST['name']
        specs=request.POST['specs']
        uploaded_file = request.FILES['picss']
        obj1=reviews(name=name,specs=specs,image=uploaded_file)
        obj1.save()
        return redirect('/')
    return render(request,'new.html')
def update(request,id):
    obj=reviews.objects.get(id=id)
    forms=laptopform(request.POST or None,request.FILES,instance=obj )
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'edit.html',{'form':forms,'laptop':obj})
def delete(request,id):
    if request.method=='POST':
        obj=reviews.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
