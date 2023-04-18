from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Spoiler
from django.contrib.sessions.models import Session

from django.contrib import auth
import re
def logout(request):
    if request.user.is_authenticated :
        auth.logout(request)
        return redirect('signin')
def signin(request):
    is_loggin=False
    if request.method == 'POST' and 'btn_login' in request.POST :
        user=request.POST['username']
        ps=request.POST['password']

        the_user=auth.authenticate(username=user,password=ps)

        if the_user is not None:
            auth.login(request,the_user)
            # messages.success(request,'you are login')
            is_loggin=True
            return redirect('main')

        else:
            messages.error(request,'invalid user name or pass')


 
            return render(request,'account/index.html')

    else:
        return render(request,'account/index.html')
def signup(request):
    if request.method == 'POST' and 'btn-signup' in request.POST:
               #varibales for fields
        fname=None
        lname=None
        email=None
        adress=None
        adress2=None
        state=None
        city=None
        zip=None
        password=None
        username=None
        terms=None
        is_added = False
        # Get the values from forms
        if 'fname' in request.POST : fname = request.POST['fname']
        else: messages.error(request,'Error in firstname')

        if 'lname' in request.POST : lname = request.POST['lname']
        else: messages.error(request,'Error in lastnamee')

        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request,'Error in email')

        if 'adress' in request.POST: adress = request.POST['adress']
        else: messages.error(request,'Error in adress')

        if 'adress2' in request.POST:adress2 = request.POST['adress2']
        else: messages.error(request,'Error in adress2')

        if 'state' in request.POST: state = request.POST['state']
        else: messages.error(request,'Error in state')

        if 'city' in request.POST: city = request.POST['city']
        else: messages.error(request,'Error in city')

        if 'zip' in request.POST:zip = request.POST['zip']
        else: messages.error(request,'Error in zip')

        if 'password' in request.POST:password = request.POST['password']
        else: messages.error(request,'Error in passwrod')

        if 'username' in request.POST:username = request.POST['username']
        else: messages.error(request,'Error in username')

        if 'terms' in request.POST:terms = request.POST['terms']
        #check the values 
        if fname and lname and email and adress and adress2 and city and zip and username and password and state and terms:
            if terms=='on':
                # user name chech
                if User.objects.filter(username=username).exists():
                    messages.error(request,'user already taken')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request,'the Email is already taken')
                    else:
                        # patt= "^[0-9a-zA-Z]([-\.\w]*[0-9a-zA-Z])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$"
                        # if re.match(patt,email):
                            #add user 
                            user=User.objects.create_user(first_name=fname , last_name=lname ,email=email,username=username,password=password)
                            user.save()
                            # add user_pofile
                            user_profile=Spoiler(User=user,adress=adress,adress2=adress2,city=city,zip_num=zip,state=state)
                            user_profile.save()
                            # empty the fields 
                            fname=''
                            lname=''
                            adress=''
                            adress2=''
                            state=''
                            city=''
                            zip=''
                            password=''
                            username=''
                            email=''
                            terms=None
                            messages.success(request,'Your account is created')
                            is_added=True
                            return redirect('signin')
                      
            else:
                messages.error(request,'You should accept terms')
            
        else:
            messages.error(request,': Empty fields ')

        return render(request,'account/signup.html',
        {
            'fname':fname,
            'lname':lname,
            'adress':adress,
            'adress2':adress2,
            'state':state , 'zip':zip , 'password':password , 'user':username
            ,'city':city, 'email':email,'terms':terms,
            'is_added':is_added

        }
        )
    else:
        return render(request,'account/signup.html')
