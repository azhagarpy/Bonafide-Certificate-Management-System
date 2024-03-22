from django.shortcuts import render, redirect,HttpResponse
from .forms import *
from django.contrib.auth import login,logout,authenticate
from .Bonafide import *
from .sendMail import sendMail

def home(request):
    if request.user.is_authenticated :
        if request.user.is_student:
            student =Student.objects.get(user=request.user)
            if Applications.objects.filter(student=student).exists():
                application = Applications.objects.get(student=student)
                print("application exists")
                return render(request,"applyBonafide.html",{'student':student,'showForm':False,'application':application})
            else:
                return render(request,"applyBonafide.html",{'student':student,'showForm':True})
        else:
            staff=Staff.objects.get(user=request.user)
            staffDepartment = staff.dep
            staffDepartmentStudents= Student.objects.filter(dep=staffDepartment)
            applications = Applications.objects.filter(student__in=staffDepartmentStudents)
            applications = list(applications)
            return render(request,"bonafideRequests.html",{'staff':staff,'applications':applications})
    return render(request,"index.html")




def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            login(request,user)
            return  redirect('home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'stdRegister.html', {'form': form})


def login_student(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)

            if user is not None and user.is_student:
                login(request, user)
                try:
                    return  redirect('home')
                except Student.DoesNotExist:
                    # Handle case where the user is not associated with a student
                    return HttpResponse("You are not a registered student.")  
            else:
                form.add_error(None,"invalid username or password")
        else:
            form.add_error(None,"username or password is incorrect")
    else:
        form = StudentLoginForm()
    return render(request, 'stdLogin.html', {'form': form})


def staff_login(request):
    if request.method=="POST":
        form =  StaffLoginForm(request.POST)
        if form.is_valid():
            staff = authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if staff is not None and staff.is_student==False:
                login(request,staff)
                try:
                    return redirect('home')
                except Staff.DoesNotExist:
                    return HttpResponse("you are not registerd as staff")
            else:
                form.add_error(None,"invalid username or password")
                     
    else:
        form = StaffLoginForm()
    return render(request,"staffLogin.html",{'form':form})      



def staff_register(request):
    if request.method=="POST":
        form = StaffRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request,user)
            return redirect('home')
        
    else:
        form = StaffRegisterForm()
    return render(request,"staffRegister.html",{'form':form})


def logoutUser(request):
    logout(request)
    return redirect('home')


def applyBonaifde(request):
    if request.method=="POST":
        student =request.user.student
        reason = request.POST['reason']
        application = Applications.objects.create(student=student,reason=reason)
        return redirect("home")


def acceptBonafideRequest(request, requestId):
    application = Applications.objects.get(id=requestId)
    application.status = True
    student = application.student
    certificate_url = generateBonafideCertificate(student)
    application.certificateFile.name = certificate_url
    application.save()
    sendMail(student,student.user.email,certificate_url)
    
    return redirect("home")

def rejectBonafideRequest(request,requestId):
    resonForReject = request.POST['rreson']
    application = Applications.objects.get(id=requestId)
    application.rejectReson=resonForReject
    application.rejected=True
    application.save()
    return  redirect("home")



