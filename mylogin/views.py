from django.shortcuts import render

from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password = password)
        if user is not None:
            login(request, user)
            #redirect to the dashboard page
            return HttpResponseRedirect('/dashboard')
        else:
            error_message = "invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
        
    else:
        return render(request, 'login.html')
        
        
        
    