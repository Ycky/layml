from django.shortcuts import render, redirect
from rest_framework import generics
from django.views.generic import DetailView,DeleteView,UpdateView
from django.contrib import messages, auth
from django.contrib.auth.models import User
from main.forms import *
from main.models import *
from main.serializer import *

class SjopAPIList(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
class JuiceAPIList(generics.ListCreateAPIView):
    queryset = Juice.objects.all()
    serializer_class = JuiceSerializer

class JuiceAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Juice.objects.all()
    serializer_class = JuiceSerializer

class JuiceAPIDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juice.objects.all()
    serializer_class = JuiceSerializer



class JuiceAPIListDetail(DetailView):
    model = Juice
    template_name = 'main/detail_view.html'
    context_object_name = 'article'

class JuiceAPIUpdates(UpdateView):
    model = Juice
    template_name = 'main/create.html'

    form_class = JuiceForm

class JuiceAPIDelete(DeleteView):
    model = Juice
    template_name = 'main/juice-delete.html'
    success_url = '/api/juice-delete/'

def body(request):
    juice = Juice.objects.order_by('-id')
    news = News.objects.order_by('-id')
    return render(request, 'main/body.html',{'juice':juice,'news':news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = JuiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('body')
        else:
            error = 'wrong'

    form = JuiceForm()

    data = {
            'form':form,
            'error': error
        }
    return render(request,'main/create.html',data)



class NewsAPIList(generics.ListCreateAPIView):
    queryset =  News.objects.all()
    serializer_class = NewsSerializer

class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset =  News.objects.all()
    serializer_class = NewsSerializer

class NewsAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset =  News.objects.all()
    serializer_class = NewsSerializer


class NewsAPIDetail(DetailView):
    model = News
    template_name = 'main/details_view.html'
    context_object_name = 'articles'

class NewsAPIUpdates(UpdateView):
    model = News
    template_name = 'main/creat.html'

    form_class = NewsForm

class NewsAPIDelete(DeleteView):
    model = News
    template_name = 'main/news-delete.html'
    success_url = '/api/news/'


def creat(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('body')
        else:
            error = 'wrong'

    form = NewsForm()

    data = {
            'form':form,
            'error': error
        }
    return render(request,'main/creat.html',data)


def register(request):
    if request.method == 'POST':
      #get
      name = request.POST['name']
      email = request.POST['email']
      password = request.POST['password']
      password2  = request.POST['password2']

      #check
      if password == password2:
          if User.objects.filter(name=name).exists():
              messages.error(request, 'That user is taken')
              return redirect('register')
          else:
             if User.objects.filter(email=email).exists():
                messages.error(request, 'That email is taken')
                return redirect('register')
             else:
                  #looks good
                user = User.objects.create_user(name=name, password=password,email=email)
                # auth.login(request,user)
                # messages.success(request, 'you are log in')
                # return  redirect('index')
                user.save()
                messages.success(request,'you are log in')
                return redirect('login')

      else:
          messages.error(request, "passwords don't match")
          return redirect('register')
    else:
         return render(request,'main/register.html')

def login(request):
    if request.method == 'POST':
        return
    else:
      return render(request,'main/login.html')


def logout(request):
    return render(request,'main/index.html')


def dashboard(request):
    return render(request,'main/dashboard.html')

def shop(request):
    shop = Shop.objects.all()
    return render(request, 'main/shop.html',{'shop':shop})
