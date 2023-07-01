from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class kendra_prashikshan(models.Model):
    date = models.DateField(default=None,null=True,blank=True)
    yojna = models.CharField(max_length=120,default=None,null=True,blank=True)
    name = models.CharField(max_length=80,default=None,null=True,blank=True)
    fahus_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    mother_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    birthdate = models.DateField(default=None,null=True,blank=True)
    jamat = models.CharField(max_length=40,default=None,null=True,blank=True)
    potjat = models.CharField(max_length=40,default=None,null=True,blank=True)
    daridrya_no = models.CharField(max_length=30,default=None,null=True,blank=True)
    adhar_no = models.BigIntegerField(default=None,null=True,blank=True)
    pan = models.CharField(max_length=20,default=None,null=True,blank=True)
    edu = models.CharField(max_length=80,default=None,null=True,blank=True)
    tech_edu = models.CharField(max_length=200,default=None,blank=True,null=True)
    income_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    adhikari = models.CharField(max_length=110,default=None,blank=True,null=True)
    acc_type = models.CharField(max_length=15,default=None,blank=True,null=True)
    acc_no = models.BigIntegerField(null=True, blank=True, default=None)
    ifsc = models.CharField(max_length=20,null=True, blank=True, default=None)
    bank_name = models.CharField(max_length=50,null=True, blank=True, default=None)
    branch = models.CharField(max_length=80,null=True, blank=True, default=None)
    mobile1 = PhoneNumberField(unique=True, blank=True)
    mobile2 = PhoneNumberField(unique=True, blank=True)
    email_id = models.EmailField(null=False, blank=False, default=None)
    gav = models.CharField(max_length=40,default=None,null=True,blank=True)
    taluka = models.CharField(max_length=30,default=None,null=True,blank=True)
    dist = models.CharField(max_length=30,default=None,null=True,blank=True)
    shetjamin = models.CharField(max_length=12,default=None,null=True,blank=True)
    suvey = models.CharField(max_length=40,default=None,null=True,blank=True)
    jamin = models.CharField(max_length=6,default=None,null=True,blank=True)
    water_src = models.CharField(max_length=40,default=None,null=True,blank=True)
    shetra = models.CharField(max_length=40,default=None,null=True,blank=True)
    home = models.CharField(max_length=8,default=None,null=True,blank=True)
    milkat_no = models.CharField(max_length=30,default=None,null=True,blank=True)
    shetra_chaumi = models.CharField(max_length=40,default=None,null=True,blank=True)
    mauje1 = models.CharField(max_length=30,default=None,null=True,blank=True)
    pada1 = models.CharField(max_length=30,default=None,null=True,blank=True)
    post1 = models.CharField(max_length=25,default=None,null=True,blank=True)
    taluka1 = models.CharField(max_length=25,default=None,null=True,blank=True)
    jilha1 = models.CharField(max_length=20,default=None,null=True,blank=True)
    pincode1 = models.IntegerField(default=None,null=True,blank=True)
    mauje2 = models.CharField(max_length=30,default=None,null=True,blank=True)
    pada2 = models.CharField(max_length=30,default=None,null=True,blank=True)
    post2 = models.CharField(max_length=25,default=None,null=True,blank=True)
    taluka2 = models.CharField(max_length=25,default=None,null=True,blank=True)
    jilha2 = models.CharField(max_length=20,default=None,null=True,blank=True)
    pincode2 = models.IntegerField(default=None,null=True,blank=True)
    yojna1 = models.CharField(max_length=120,default=None,null=True,blank=True)
    year1 = models.CharField(max_length=4,default=None,null=True,blank=True)
    yojna2 = models.CharField(max_length=120,default=None,null=True,blank=True)
    year2 = models.CharField(max_length=4,default=None,null=True,blank=True)
    yojna3 = models.CharField(max_length=120,default=None,null=True,blank=True)
    year3 = models.CharField(max_length=4,default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
 
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "kendra_prashikshan"
    def __str__(self) -> str:
        return str(self.name)