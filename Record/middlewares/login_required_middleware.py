from django.shortcuts import render , redirect



def login_required(get_response):
    #index function pass here

    def middleware(request):
        user =  request.session.get('user')
        print(user,"user")
        if user:
            print("already login")
            return redirect(f'/?return_url={url}')
        else:
            print("Please Login ")
            url = request.path
            print(url)
            return redirect(f'/login?return_url={url}')

    
    return middleware