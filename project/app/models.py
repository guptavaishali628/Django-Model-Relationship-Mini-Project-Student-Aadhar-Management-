from django.db import models

# Create your models here.
class Aadhar(models.Model):
    Aadhar_no = models.IntegerField()
    Created_date=models.DateField(auto_now=True) # use auto_now = true means bo current date ko pick krega
    Created_by=models.CharField(max_length=40)

    def __str__(self):
        return str(self.Aadhar_no)  # column value ko print krane k liye hum use krte hai is function ka
    
class Student(models.Model):
    Stu_name=models.CharField(max_length=40)
    Stu_email=models.EmailField()
    Stu_contact=models.IntegerField()
    Stu_aadhar=models.OneToOneField(Aadhar, on_delete=models.CASCADE) 

    # Stu_aadhar=models.IntegerField()
    
    # on_delete=models.CASCADE --> iska mtlb hai agar hum stu_adhar ko delete kr rhe hai to adahr_no bhi delete ho jayega
    # on_delete=models.PROTECTED --> opposite of CASCADE


        
    
