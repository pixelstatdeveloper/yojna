from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class pramod_mah(models.Model):
    umedwar_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    second_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    fa_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    birth_date = models.DateField(default=None,null=True,blank=True)
    paripurn_patta = models.CharField(max_length=1000, null=True, blank=True)
    mobile_number = PhoneNumberField( blank=True)
    email_id = models.EmailField(null=False, blank=False, default=None)
    gender = models.CharField(default=None,null=True,blank=True,max_length=100)
    education = models.CharField(max_length=1000, null=True, blank=True)
    adhaar_no = models.CharField(max_length=100, null=True, blank=True)
    shakha =  models.CharField(max_length=100, null=True, blank=True)
    dharma =  models.CharField(max_length=100, null=True, blank=True)
    jat =  models.CharField(max_length=100, null=True, blank=True)
    pravarg = models.CharField(default=None,null=True,blank=True,max_length=200)
    rahivasi = models.CharField(default=None,null=True,blank=True,max_length=50)
    prashikshan= models.CharField(max_length=1000,null=True, blank=True, default=None)
    prashikshan1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    prashikshan2= models.CharField(max_length=1000,null=True, blank=True, default=None)
    course_prashikshan= models.CharField(max_length=1000,null=True, blank=True, default=None)
    course_prashikshan1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    course_prashikshan2= models.CharField(max_length=1000,null=True, blank=True, default=None)
    kau_prashikshan = models.CharField(default=None,null=True,blank=True,max_length=50)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    vikas_prashikshan= models.CharField(max_length=1000,null=True, blank=True, default=None)
    # umedwar_sign = models.FileField(upload_to='signatures', null=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "pramod_mah"
        


