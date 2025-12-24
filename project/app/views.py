from django.shortcuts import render , redirect
from .models import Aadhar, Student

# Create your views here.
def index(req):
    return render(req,'index.html')

def add_aadhar(req):
    all_aadhar=Aadhar.objects.all()
    return render(req,'add_aadhar.html',{'data':all_aadhar})

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
    all_aadhar = Aadhar.objects.all()
    return render(req,'add_student.html',{'data':all_aadhar})

def save_student(req):
    if req.method=='POST':
        name=req.POST.get('name')
        email=req.POST.get('email')
        cnumber=req.POST.get('cnumber')
        stu_aadharNo=req.POST.get('stu_aadharNo')
        # a_inst instance of stu_adharno
        a_inst = Aadhar.objects.get(id=stu_aadharNo)
        Student.objects.create(
            Stu_name=name, 
            Stu_email=email, 
            Stu_contact=cnumber,
            Stu_aadhar=a_inst
           )
        return redirect('show_student')
    return redirect(add_student)

def show_student(req):
    studentData=Student.objects.all().order_by()
    return render(req, 'show_Student.html',{'studentData':studentData})

def relation_table(req):
    ## with out using related_name attribute---------
    
    # # through Forword access--------------------------(access Student table to Aadhar table)
    all_data = Student.objects.all()
    return render(req,'relation_table.html',{'data':all_data})
    # for i in all_data:
    #     print(i.Stu_name)
    #     print(i.Stu_email)
    #     print(i.Stu_contact)
    #     print(i.Stu_aadhar.Aadhar_no)
    #     print(i.Stu_aadhar.Created_date)
    #     print(i.Stu_aadhar.Created_by)
    
    # through reverse access---------------------------------(access Aadhar table to Student table)
    # all_data = Aadhar.objects.all()
    # return render(req,'relation_table.html',{'data':all_data})
    # for i in all_data:
    #     print(i.Aadhar_no)
    #     print(i.Created_by)
    #     print(i.Created_date)
    #     print(i.student.Stu_name)
    #     print(i.student.Stu_email)
    #     print(i.student.Stu_contact)
