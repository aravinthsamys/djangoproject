from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


from .models import movie

def result(request):
    data = movie.objects.all()
    x={
        'data':data,
    }
    if request.method == 'POST':
        name= request.POST['name']
        desc= request.POST['desc']
        img = request.FILES['img']
        movie.objects.create(name=name,desc=desc,img=img)
        return redirect('result')
    return render(request, 'result.html',x)

def delete_id(request,id):
    del_item = movie.objects.get(id=id)
    print(del_item.id)
    del_item.delete()
    return redirect('result')


def update_id(request,id):
    update_item = movie.objects.get(id=id)
    y={
        'data':update_item
    }
    if request.method == 'POST':
        name= request.POST['name']
        desc= request.POST['desc']
        img = request.FILES.get('img')
        if name:
            update_item.name=name
        if desc:
            update_item.desc = desc
        if img:
            update_item.img = img
        update_item.save()
        return redirect('result')
        
    return render(request, 'update.html',y)


from .forms import registerform,loginform

def register_page(request):
    form = registerform()
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html',{'form':form})

from django.contrib.auth import login,logout

def login_page(request):
    form = loginform()
    if request.method == "POST":
        form = loginform(request,data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('index')
    return render(request,'login.html',{'form':form})

def logout_page(request):
    logout(request)
    return redirect('login')