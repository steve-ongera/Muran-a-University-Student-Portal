from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.http import JsonResponse
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Student,Units, Registration, UnitCode,Studentdata



@login_required
def register_units(request):
    
    units = Units.objects.all()
    if request.method == 'POST':
        selected_units = request.POST.getlist('units')
        student = request.user.student
        for unit_id in selected_units:
            unit = Units.objects.get(id=unit_id)
            
            Registration.objects.create(student=student, unit=unit)
        return redirect('dashboard')
    context = {
        'units': units,
       
    }
    return render(request, 'register_units.html', context)



def tour_json_view(request):
    # Your JSON data generation logic goes here
    data = {
        'tour': {
            'name': 'Example Tour',
            'description': 'This is an example tour.',
            # Add more data as needed
        }
    }
    return JsonResponse(data)
@login_required
def dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return render(request , '404.html')
    #student = request.user.student
    
    registrations = Registration.objects.filter(student=student)
    context = {
        'registrations': registrations
    }
    return render(request,'dashboard.html', context)

@login_required
def unit(request):
	return render(request,'unit.html')

@login_required
def profile(request):
    student = request.user.student
    context = {
        'student': student
    }
    return render(request,'profile.html', context)

def mutsignup(request):
    return render(request,'signup.html ')

def mutlogin(request):
    return render(request,'signin.html ')

@login_required
def mut(request):
    return render(request,'mut.html ')


def register(request):
    if request.method == "POST":
        
        username = request.POST['username']
        
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username = username).first():
            messages.error(request,"Username already taken")
            return redirect('register')
        

        if password != password2:
            messages.error(request,"Passwords do not match")
            return redirect('register')

        myuser = User.objects.create_user(username=username,password=password)
        
        myuser.save()
        messages.success(request,"Your account has been successfully created!")
        return redirect('signin')


    else:
        print("error")
        return render(request,'signup.html')
    

def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request,"Successfully logged in!")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('signin')

    else:
        print("error")
        return render(request,'signin.html')

def signout(request):
        logout(request)
        # messages.success(request,"Successfully logged out!")
        return redirect('signout')

def homepage(request):
     return render(request, 'index.html')