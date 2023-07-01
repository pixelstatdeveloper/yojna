from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class vaiyaktik_sabhasad(models.Model):
    shri =  models.CharField(max_length=1000, null=True, blank=True)
    form_date = models.DateField(default=None,null=True,blank=True)
    name3= models.CharField(max_length=1000,null=True, blank=True, default=None)
    form_date1 = models.DateField(default=None,null=True,blank=True)
    singh = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_image',default=None,null=True,blank=True)
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    birth_date = models.DateField(default=None,null=True,blank=True)
    patta =  models.CharField(max_length=1000, null=True, blank=True)
    mobile_number = PhoneNumberField( blank=True)
    email_id = models.EmailField(null=False, blank=False, default=None)
    patta1 =  models.CharField(max_length=1000, null=True, blank=True)
    business = models.CharField(max_length=1000, null=True, blank=True)
    name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    patta2 =  models.CharField(max_length=1000, null=True, blank=True)
    mobile_number1 = PhoneNumberField( blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "vaiyaktik_sabhasad"
        

