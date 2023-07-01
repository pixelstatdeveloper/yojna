from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class eklavya_school(models.Model):
    std1 = models.CharField(max_length=2,default=None,null=True,blank=True)
    std2 = models.CharField(max_length=2,default=None,null=True,blank=True)
    name = models.CharField(max_length=80,default=None,null=True,blank=True)
    birth_date = models.DateField(default=None,null=True,blank=True)
    birth_place = models.CharField(max_length=30,default=None,null=True,blank=True)
    jamat = models.CharField(max_length=60,default=None,null=True,blank=True)
    rahivasi_yn = models.CharField(max_length=4,default=None,null=True,blank=True) 
    nate = models.CharField(max_length=50,default=None,null=True,blank=True)
    father_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    father_add = models.CharField(max_length=120,default=None,null=True,blank=True)
    mobile_no = PhoneNumberField(unique=True, blank=True)
    mother_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    income = models.CharField(max_length=15,default=None,null=True,blank=True)
    vyavsay = models.CharField(max_length=35,default=None,null=True,blank=True)
    school = models.CharField(max_length=60,default=None,null=True,blank=True)
    marks = models.CharField(max_length=30,default=None,null=True,blank=True)
    std3 = models.CharField(max_length=20,default=None,null=True,blank=True)
    paas = models.CharField(max_length=5,default=None,null=True,blank=True)
    members = models.IntegerField(default=None,null=True,blank=True)
    bank_name = models.CharField(max_length=80,null=True, blank=True, default=None)
    branch = models.CharField(max_length=30,null=True, blank=True, default=None)
    acc_no = models.BigIntegerField(null=True, blank=True, default=None)
    ifsc = models.CharField(max_length=30,null=True, blank=True, default=None)
    adhar_no = models.BigIntegerField(null=True, blank=True, default=None)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
   
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "eklavya_school"
    def __str__(self) -> str:
        return str(self.name)