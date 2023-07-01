from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class anusuchit_shabri(models.Model):
    jilha = models.CharField(max_length=30,default=None,null=True,blank=True)
    name = models.CharField(max_length=100,default=None,null=True,blank=True)
    address = models.CharField(max_length=180,default=None,null=True,blank=True)
    jat = models.CharField(max_length=70,default=None,null=True,blank=True)
    birthdate = models.DateField(default=None,null=True,blank=True)
    age = models.CharField(max_length=10 ,default=None,null=True,blank=True)
    gender = models.CharField(default=None,null=True,blank=True,max_length=15)
    married = models.CharField(default=None,null=True,blank=True,max_length=20)
    son = models.CharField(max_length=3 ,default=None,null=True,blank=True)
    daughter = models.CharField(max_length=3, default=None,null=True,blank=True)
    total_child = models.CharField(max_length=3, default=None,null=True,blank=True)
    ladies = models.CharField(max_length=3, default=None,null=True,blank=True)
    gents = models.CharField(max_length=3, default=None,null=True,blank=True)
    total = models.CharField(max_length=3, default=None,null=True,blank=True)
    education = models.CharField(default=None,null=True,blank=True,max_length=80)
    yojna = models.CharField(default=None,null=True,blank=True,max_length=150)
    samu_vayaktik = models.CharField(default=None,null=True,blank=True,max_length=150)
    daridrya_cardno = models.CharField(default=None,null=True,blank=True,max_length=40)
    income = models.CharField(max_length=10, default=None,null=True,blank=True)
    income_src = models.CharField(default=None,null=True,blank=True,max_length=50)
    jaga = models.CharField(default=None,null=True,blank=True,max_length=8)

    alpa_bhudharak = models.CharField(default=None,null=True,blank=True,max_length=8)
    alpa_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    bhumihin = models.CharField(default=None,null=True,blank=True,max_length=8)
    bhumihin_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    vidhva = models.CharField(default=None,null=True,blank=True,max_length=8)
    vidhva_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    vidhur = models.CharField(default=None,null=True,blank=True,max_length=8)
    vidhur_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    ghatsphotit = models.CharField(default=None,null=True,blank=True,max_length=8)
    ghatsphotit_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    bhukampgrast = models.CharField(default=None,null=True,blank=True,max_length=8)
    bhukamp_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    apang = models.CharField(default=None,null=True,blank=True,max_length=8)
    apang_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    dharangrast = models.CharField(default=None,null=True,blank=True,max_length=8)
    dharangrast_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    majhi_sainik = models.CharField(default=None,null=True,blank=True,max_length=8)
    sainik_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    
    labh = models.CharField(default=None,null=True,blank=True,max_length=8)
    yojna1 = models.CharField(default=None,null=True,blank=True,max_length=150)
    year1 = models.CharField(max_length=8, default=None,null=True,blank=True)
    yojna2 = models.CharField(default=None,null=True,blank=True,max_length=150)
    year2 = models.CharField(max_length=8, default=None,null=True,blank=True)

    dinank = models.DateField(default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    place = models.CharField(default=None,null=True,blank=True,max_length=40)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "anusuchit_shabri"
    def __str__(self) -> str:
        return str(self.name)