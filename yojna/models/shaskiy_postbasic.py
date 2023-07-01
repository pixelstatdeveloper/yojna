from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class shaskiy_postbasic(models.Model):
    name = models.CharField(max_length=100,default=None,null=True,blank=True)
    patta = models.CharField(max_length=180,default=None,null=True,blank=True)
    jat = models.CharField(max_length=15,default=None,null=True,blank=True)
    birthdate = models.DateField(default=None,null=True,blank=True)
    age = models.CharField(max_length=40,default=None,null=True,blank=True)
    education = models.CharField(default=None,null=True,blank=True,max_length=70)
    income = models.CharField(max_length=13,default=None,null=True,blank=True)
    labh_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    nokri_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    nondni_no = models.CharField(max_length=20,default=None,null=True,blank=True)
    abhyaskram = models.CharField(max_length=60,default=None,null=True,blank=True)
    thikan = models.CharField(max_length=30,default=None,null=True,blank=True)
    dinank = models.DateField(default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "shaskiy_postbasic"
    def __str__(self) -> str:
        return str(self.name)