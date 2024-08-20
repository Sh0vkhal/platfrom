from django.shortcuts import render, redirect
from django.urls import *
from django.views import View
from .models import *
from django.contrib.messages import warning, success
from .utils import send_verification_email
from django.contrib.auth import authenticate, login
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.

class HomePageView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'
    paginate_by = 3
    

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        phone = request.POST.get('phone')
        
        if password != password_confirm:
            warning(request, 'Password confirmation is incorrect')
            return redirect(reverse('main:register'))
        if User.objects.filter(username=username).exists():
            warning(request, 'User already registered')
            return redirect(reverse('main:register'))
        user = User.objects.create_user(username=username, 
                                        email=email,
                                        password=password,
                                        phone=phone, is_active=False)
        send_verification_email(user)
        login(request, user)
        success(request, 'User  registered')
        return redirect(reverse("main:kirish"))


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            warning(request, 'User does not exist')
            return redirect(reverse('main:kirish'))
        user = User.objects.get(username=username)
        if not user.check_password(password):
            warning(request, 'Password is incorrect')
            return redirect(reverse('main:kirish'))
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('main:home'))
        warning(request, 'Error')
        return redirect(reverse('main:kirish'))
        

        
class ContactView(View):
    def get(self, request):
        return render(request, 'contact_us.html')


    def post(request):
     if request.method == 'post':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect('main:contact')  
     else:
          return render(request, 'contact_us.html')
    

def contact_us_success(request):
    return render(request, 'contact_us_success.html')


#4-lesson.homework(views.py_code)
class TagView(CreateView):
    model = Category
    fields =['title'] 
    template_name = 'tag_create.html'
    success_url="/"


class TagUpdate(UpdateView):
    model = Tag
    fields = [ 'title']  
    template_name = 'tag_update.html'  
    success_url = '/'  