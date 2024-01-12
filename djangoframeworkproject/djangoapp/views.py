from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.urls import reverse
import random

"""
Django ORM (OBJECT RELATIONAL MAPPING): 

get() : fetch data from model and return an object but only single records if there are mutiple records found with given condition it will thorws an exception
"""
# Create your views here.
def home(request):
    if "email" in request.session :
        frameworkid = Framework.objects.get(email = request.session['email'])
        djangoid = Django.objects.get(userid = frameworkid)
        context = {
            'frameworkid' : frameworkid,
            'djangoid' : djangoid,
        }
        return render(request, "djangoapp/index.html", context)

    return render(request,"djangoapp/login.html")

def login(request):

    if "email" in request.session :
        frameworkid = Framework.objects.get(email = request.session['email'])
        djangoid = Django.objects.get(userid = frameworkid)
        context = {
            'frameworkid' : frameworkid,
            'djangoid' : djangoid,
        }
        return render(request, "djangoapp/index.html", context)
    else :
        if request.POST :
            try :

                Email = request.POST["email"]
                Password = request.POST["password"]
                print("========>> Email", Email)
                # print("========>> Password", Password)
                frameworkid = Framework.objects.get(email=Email,password=Password)
                print("=========================>>>> Object " ,frameworkid)
                print("=====>>> ",frameworkid.email)
                print("=====>>> ",frameworkid.role)
                djangoid = Django.objects.get(userid = frameworkid)
                
                print("===========>>> fname", djangoid.fname)
                request.session['email'] = frameworkid.email
                return HttpResponseRedirect(reverse('home'))
                # return render(request,"djangoapp/login.html")
                # context = {
                #     'frameworkid' : frameworkid,
                #     'djangoid' : djangoid,
                # }
                # return render(request, "djangoapp/index.html", context)
            
            except Exception as e:

                print("================> Exception", e)
                message = "Invalid email and password"
                return render(request,"djangoapp/login.html",{'e_message' : message})
            
        else:
            print("----------->> page loaded")
            return render(request,"djangoapp/login.html")
        
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('login'))
    
def profile(request):
    if "email" in request.session:
        frameworkid = Framework.objects.get(email = request.session['email'])
        djangoid = Django.objects.get(userid = frameworkid)
        context = {
            'frameworkid' : frameworkid,
            'djangoid' : djangoid,
        }

        return render(request, "djangoapp\profile.html", context)
    else:
        return HttpResponseRedirect(reverse('login'))
    
def change_password(request):
    if "email" in request.session:
        frameworkid = Framework.objects.get(email = request.session['email'])
        djangoid = Django.objects.get(userid = frameworkid)
        
        currentpassword = request.POST['currentpassword']
        newpassword = request.POST['newpassword']
        
        if frameworkid.password == currentpassword :
            frameworkid.password = newpassword
            frameworkid.save() #update

            del request.session['email']
            s_message = "Changed Password Successfully"
            return render(request, "djangoapp\profile.html", {'s_messege': s_message} )
   
        else:
            e_message = "Invalid current password"
            del request.session['email']
            return render(request, "djangoapp\login.html", {'e_messege': e_message})

def change_profile(request):
    if "email" in request.session:
        frameworkid = Framework.objects.get(email = request.session['email'])
        djangoid = Django.objects.get(userid = frameworkid)

        if request.POST :

            djangoid.fname = request.POST['Firstname']
            djangoid.lname = request.POST['Lastname']
            djangoid.contact = request.POST['Contact']
            djangoid.houseno = request.POST['Houseno']
            djangoid.blockno = request.POST['Blockno']

            if "pic" in request.FILES :

                djangoid.pic = request.FILES['pic']
                djangoid.save() #update

            djangoid.save() #update

        context = {
            'frameworkid' : frameworkid,
            'djangoid' : djangoid,
        }

        return render(request, "djangoapp\profile.html", context)
    
def add_member(request):
    if "email" in request.session:
        frameworkid = Framework.objects.get(email = request.session['email'])
        djangoid = Django.objects.get(userid = frameworkid)

        if request.POST:
            print("====> Add Operation :")

            email = request.POST['email']
            contact = request.POST['contact']
            l1 = ["hgfhgg", "101010" ,"234234","13061997","05091975","30102004","12121974"]

            password = random.choice(l1) + email[3:6] + contact[4:7]
            memberuserid = Framework.objects.create(email = request.POST['email'], password = password, role ="member")
            
            if memberuserid :
                memberid = member.objects.create(
                    frameworkid = memberuserid,
                    fname = request.POST['firstname'],
                    lname = request.POST['lastname'],
                    contact = request.POST['contact'],
                    houseno = request.POST['houseno'],
                    blockno = request.POST['blockno'],
                    occupation = request.POST['occupation'],
                    job_address =request.POST['job_address'],
                    bloodgroup = request.POST['bloodgroup'],
                    vehicle_details = request.POST['vehicle_details'],
                )

            context = {
                'frameworkid' : frameworkid,
                'djangoid' : djangoid,
                "s_message" : "Member Added Successfully",
            }

            return render(request, "djangoapp/addMember.html", context)
    

        context = {
            'frameworkid' : frameworkid,
            'djangoid' : djangoid,
        }

        return render(request, "djangoapp/addMember.html", context)
