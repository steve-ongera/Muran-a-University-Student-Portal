from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20)
    nationality = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    disability = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    medical = models.CharField(max_length=100)
    co_curricular = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.registration_number} - {self.name}"
    
class Studentdata(models.Model):
    registration_number = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, null=True)
    nationality = models.CharField(max_length=100, null=True)
    religion = models.CharField(max_length=50, null=True)
    DOB= models.DateField(max_length=100, null=True)
    disability = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    hostel= models.CharField(max_length=100, null=True)
    romm_no = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.registration_number}"
    
class Units(models.Model):
    unit_code=models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    lec=models.CharField(max_length=100)
    # Other fields as needed
    def __str__(self):
        return f"{self.unit_code} - {self.name} - {self.lec}"

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.registration_number}  - {self.marks}"
    
class UnitCode(models.Model):
    code = models.CharField(max_length=100)
    def __str__(self):
        return self.code



class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    unitCode = models.ForeignKey(UnitCode, on_delete=models.CASCADE , null=True)
    
    def __str__(self):
        return f"{self.student.registration_number} - {self.student} "
    
#f"{self.student.registration_number} - {self.student} - {self.date_paid}"