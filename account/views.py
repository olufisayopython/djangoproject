from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == Password2:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save();
            print('user saved')
        else:
            print('password does not match ')
        return redirect('successful')

    else:
        return render(request,'register.html')