from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class anusuchit_swechha(models.Model):
    name = models.CharField(max_length=80,default=None,null=True,blank=True)
    father_palak = models.CharField(max_length=80,default=None,null=True,blank=True)
    nate = models.CharField(max_length=30,default=None,null=True,blank=True)
    father_edu = models.CharField(max_length=60,default=None,null=True,blank=True)
    mother_name = models.CharField(max_length=80,default=None,null=True,blank=True)
    mom_edu = models.CharField(max_length=50,default=None,null=True,blank=True)
    jat = models.CharField(max_length=40,default=None,null=True,blank=True)
    potjat = models.CharField(max_length=40,default=None,null=True,blank=True)
    dharma = models.CharField(max_length=40,default=None,null=True,blank=True)
    gender = models.CharField(max_length=7,default=None,null=True,blank=True)
    nationality = models.CharField(max_length=25,default=None,null=True,blank=True)
    birthdate = models.DateField(default=None,null=True,blank=True)
    birth_letter = models.CharField(max_length=50,default=None,null=True,blank=True)
    mukam = models.CharField(max_length=40,default=None,null=True,blank=True)
    post = models.CharField(max_length=30,default=None,null=True,blank=True)
    taluka = models.CharField(max_length=30,default=None,null=True,blank=True)
    jilha = models.CharField(max_length=25,default=None,null=True,blank=True)
    mobile = PhoneNumberField(unique=True, blank=True)
    mukam2 = models.CharField(max_length=40,default=None,null=True,blank=True)
    post2 = models.CharField(max_length=30,default=None,null=True,blank=True)
    taluka2 = models.CharField(max_length=30,default=None,null=True,blank=True)
    jilha2 = models.CharField(max_length=25,default=None,null=True,blank=True)
    mobile2 = PhoneNumberField(unique=True, blank=True)
    language = models.CharField(max_length=30,default=None,null=True,blank=True)
    std = models.CharField(max_length=30,default=None,null=True,blank=True)
    reason = models.CharField(max_length=80,default=None,null=True,blank=True)
    passed = models.CharField(max_length=30,default=None,null=True,blank=True)
    year = models.CharField(max_length=20,default=None,null=True,blank=True)
    percent = models.CharField(max_length=30,default=None,null=True,blank=True)
    grade = models.CharField(max_length=20,default=None,null=True,blank=True)
    income = models.CharField(max_length=15,default=None,null=True,blank=True)
    business = models.CharField(max_length=50,default=None,null=True,blank=True)
    kutumb = models.IntegerField(default=None,null=True,blank=True)
    student = models.IntegerField(default=None,null=True,blank=True)
    date = models.DateField(default=None,null=True,blank=True)
    place = models.CharField(max_length=50,default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    palak = models.CharField(max_length=60,default=None,null=True,blank=True)
    mukam3 = models.CharField(max_length=40,default=None,null=True,blank=True)
    post3 = models.CharField(max_length=30,default=None,null=True,blank=True)
    taluka3 = models.CharField(max_length=30,default=None,null=True,blank=True)
    jilha3 = models.CharField(max_length=25,default=None,null=True,blank=True)
    janmjat = models.CharField(max_length=30,default=None,null=True,blank=True)
    palya = models.CharField(max_length=60,default=None,null=True,blank=True)
    std3 = models.CharField(max_length=3,default=None,null=True,blank=True)
    saksh1 = models.CharField(max_length=60,default=None,null=True,blank=True)
    saksh2 = models.CharField(max_length=60,default=None,null=True,blank=True)
    palak_nav = models.CharField(max_length=50,default=None,null=True,blank=True)
    palak_sahi = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    dinank = models.DateField(default=None,null=True,blank=True)
    thikan = models.CharField(max_length=50,default=None,null=True,blank=True)
    vidyarthi_swaksh = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    palak_swaksh = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "anusuchit_swechha"
    def __str__(self) -> str:
        return str(self.name)