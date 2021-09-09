from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password , check_password
from Record.models.user import User



class SignupView(View):
    def get(self , request):
        return render(request, 'signup.html')


    def post(self , request):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')           #Hashing password
            hashedPassword = make_password(password = password)
            user = User(name = name , email = email , phone = phone, password = hashedPassword)
            result = user.save()
            print("submit sucessfull")
            return render(request , 'login.html')
        except:
            return render(request, 'signup.html' , {'error' : "User Already Registered..."})

            