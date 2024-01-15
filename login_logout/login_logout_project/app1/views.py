from django.contrib.auth.models import User
from django.shortcuts import render , redirect

# Create your views here.




def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname = request.POST.get('first_name')
        email= request.POST.get('email_id')
        #password = request.POST.get('password')
        print(username,firstname)

        x=User.objects.create_user(username,firstname,email)
        #x= User.objects.create_user(username=username,first_name=first_name,email=email,password=password)
        x.save()
        print("user created")
        #return HttpResponse('usercreated')
        return redirect('/')
    else:

        return render(request,'signup.html')