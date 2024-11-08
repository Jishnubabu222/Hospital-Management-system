from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

from django.http import HttpResponse


# Create your views here.
def display(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def home(request):
    return render(request, "home.html")


def hospitalsignup(request):
    if request.method == 'POST':
        n = request.POST['name']
        em = request.POST['email']
        mob = request.POST['phone']
        uname = request.POST['username']
        pw = request.POST['password']
        gn = request.POST['Gender']
        data1 = signup_db.objects.filter(email=em)
        if data1:
            messages.info(request, 'email is already exists')
            return redirect(signup)
        data = signup_db.objects.create(name=n, email=em, phone=mob, username=uname, password=pw, gender=gn)
        data.save()
        return redirect(login)


def bookingapp(request):
    if request.method == 'POST':
        n = request.POST['name']
        em = request.POST['email']
        dt = request.POST['setTodayDate']
        gn = request.POST['Sex']
        dept = request.POST['department']
        phn = request.POST['phone']
        msg = request.POST['message']
        pymnt = request.POST['payment']
        data = booking_db.objects.create(name=n, email=em, date=dt, gender=gn, department=dept, phone=phn, message=msg,
                                         payment=pymnt)
        data.save()
        messages.info(request, 'Data stored Sucessfully')
        return redirect(home)


def login_func(request):
    if request.method == 'POST':
        mail = request.POST['email']
        pswd = request.POST['Password']
        data = signup_db.objects.filter(email=mail)
        if data:
            data1 = signup_db.objects.get(email=mail)
            if data1.password == pswd:
                request.session['id'] = mail
                return redirect(home)
            else:
                messages.info(request, 'invalid E-mail or password')
                return redirect(login)
        else:
            messages.info(request, 'invalid E-mail or password')
            return redirect(login)


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(display)


def adminlogin(request):
    return render(request, "adminlogin.html")


def adminhome(request):
    d = signup_db.objects.all()
    return render(request, "adminhome.html", {'data': d})


def adminappoinment(request):
    d = booking_db.objects.filter(status='pending')
    return render(request, "appoinments.html", {'data': d})


def adminlogout(request):
    if 'admin_id' in request.session:
        request.session.flush()
        return redirect(display)


def adminlog(request):
    if request.method == 'POST':
        name = request.POST['uname']
        pswrd = request.POST['Password']
        data = admin_log.objects.filter(admin_name=name)
        if data:
            data1 = admin_log.objects.get(admin_name=name)
            if data1.admin_pass == pswrd:
                request.session['admin_id'] = name
                return redirect(adminhome)
            else:
                messages.info(request, "invalid username or password")
                return redirect(adminlogin)
        else:
            messages.info(request, "invalid username or password")
            return redirect(adminlogin)


def acceptapp(request, id):
    booking_db.objects.filter(pk=id).update(status='approve')
    messages.info(request, "Appoinmnet Approved")
    return redirect(adminappoinment)


def rejectapp(request, id):
    booking_db.objects.filter(pk=id).delete()
    messages.info(request, "Appoinment rejected")
    return redirect(adminappoinment)


def booking_dtl(request):
    pending_booking = []
    history = []
    d = booking_db.objects.filter(status='pending')
    for i in d:
        if i.email == request.session['id']:
            pending_booking.append(i)
    d1 = booking_db.objects.filter(status='approve')
    for j in d1:
        if j.email == request.session['id']:
            history.append(j)
    return render(request, 'booking_details.html', {'data': pending_booking, 'data1': history})


def docsform(request):
    return render(request, 'docs.html')


def docs_add(request):
    if request.method == 'POST':
        dname = request.POST['name']
        dId = request.POST['docid']
        dPic = request.FILES['docpic']
        dDep = request.POST['department']
        data = docs_db.objects.create(doc_name=dname, doc_id=dId, doc_file=dPic, doc_department=dDep)
        data.save()
        messages.info(request, 'Data stored Sucessfully')
        return redirect(docsform)

def docDisplay(request):
    d=docs_db.objects.all()
    return render(request,"DocsTable.html",{'data':d})

def docDele(request,id):
    docs_db.objects.filter(pk=id).delete()
    messages.info(request,"Doctor Deleted")
    return redirect(docDisplay)
