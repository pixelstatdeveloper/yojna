from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class andh_vyaktinsathi(models.Model):
    name = models.CharField(max_length=1000,default=None,null=True,blank=True)
    age = models.IntegerField(default=None,null=True,blank=True)
    gender = models.CharField(default=None,null=True,blank=True,max_length=100)
    caste = models.CharField(default=None,null=True,blank=True,max_length=200)
    education = models.CharField(default=None,null=True,blank=True,max_length=400)
    married = models.CharField(default=None,null=True,blank=True,max_length=200)
    income = models.BigIntegerField(default=None,null=True,blank=True)
    handicap_type = models.CharField(default=None,null=True,blank=True,max_length=400)
    percent = models.FloatField(default=None,null=True,blank=True)
    handicap_certificate_no = models.CharField(default=None,null=True,blank=True,max_length=200)
    form_date = models.DateField(default=None,null=True,blank=True)
    business = models.CharField(default=None,null=True,blank=True,max_length=500)
    adhar_card_no = models.BigIntegerField(default=None,null=True,blank=True)
    address = models.TextField(default=None,null=True,blank=True)
    mobile_no = PhoneNumberField(unique=True, blank=True)
    avashak_seva = models.TextField(default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    previous_benefit = models.CharField(default=None,null=True,blank=True,max_length=40)
    # signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "Andha_Vyaktisathi"
    def __str__(self) -> str:
        return str(self.name)