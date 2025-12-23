from django.shortcuts import render , redirect
from .models import Aadhar, Student

# Create your views here.
def index(req):
    return render(req,'index.html')

def add_aadhar(req):
    return render(req,'add_aadhar.html')

def save_aadhar(req):
    if req.method=='POST':
        aadharNo=req.POST.get('aadharNo')
        createdDate=req.POST.get('createdDate')
        createdBy=req.POST.get('createdBy')

        Aadhar.objects.create(
           Aadhar_no=aadharNo, 
           Created_date=createdDate, 
           Created_by=createdBy,
           )
        return redirect('show_aadhar')
    return redirect('add_aadhar')
    
def show_aadhar(req):
    aadharData=Aadhar.objects.all().order_by()
    return render(req,'show_aadhar.html',{'aadharData':aadharData})
      
def add_student(req):
    return render(req,'add_student.html')

def save_student(req):
    if req.method=='POST':
        name=req.POST.get('name')
        email=req.POST.get('email')
        cnumber=req.POST.get('cnumber')
        stu_aadharNo=req.POST.get('stu_aadharNo')
        Student.objects.create(
            Stu_name=name, 
            Stu_email=email, 
            Stu_contact=cnumber,
            Stu_aadhar=stu_aadharNo
           )
        return redirect('show_student')
    return redirect(add_student)

def show_student(req):
    studentData=Student.objects.all().order_by()
    return render(req, 'show_Student.html',{'studentData':studentData})

def relation_table(req):
    return