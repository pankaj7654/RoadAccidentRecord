from django.views import View
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password , make_password
from Record.models import User



class LoginView(View):
    def get(self , request):
        return_url = None
        print("From Class Based View")
        LoginView.return_url = request.GET.get('return_url')
        return render(request, 'login.html')


    def post(self , request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        print(phone, password)
        try:
            user = User.objects.get(phone = phone)
            flag = check_password(password = password , encoded = user.password)
            print(flag)
            if flag:
                #collect Products
                temp = {}
                temp['phone'] = user.phone
                temp['id'] = user.id
                request.session['user'] = temp
                print("Login success")
                if LoginView.return_url:
                    return redirect(LoginView.return_url)
                return redirect('index') #redirect index from url name
            else:
                return render(request, 'login.html' , {'error' : 'Please Enter Valide Email or Password'})        
            
        except:
            return render(request, 'login.html' , {'error' : 'Please Enter Valide Email or Password'})
            
        


