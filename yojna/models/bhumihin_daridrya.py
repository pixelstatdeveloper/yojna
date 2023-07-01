from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class bhumihin_daridrya(models.Model):
    jilha = models.CharField(max_length=15,default=None,null=True,blank=True)
    name = models.CharField(max_length=100,default=None,null=True,blank=True)
    huswife_name = models.CharField(max_length=100,default=None,null=True,blank=True)
    address = models.CharField(max_length=180,default=None,null=True,blank=True)
    anu_jamat = models.CharField(max_length=100,default=None,null=True,blank=True)
    adim_jamat = models.CharField(max_length=50,default=None,null=True,blank=True)
    striya = models.CharField(max_length=60,default=None,null=True,blank=True)
    vidhwa = models.CharField(max_length=60,default=None,null=True,blank=True)
    bhumihin_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    daridrya_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    daridrya_no = models.CharField(max_length=20,default=None,null=True,blank=True)
    talathi_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    age = models.CharField(max_length=2,default=None,null=True,blank=True)
    labhdharak_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    tapshil = models.CharField(max_length=100,default=None,null=True,blank=True)
    jamin_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    atikraman_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    pratidnyapatra = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    hamipatra = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    mashagat = models.CharField(max_length=100,default=None,null=True,blank=True)
    income_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    water_src = models.CharField(max_length=11,default=None,null=True,blank=True)
    yojnalabh_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    yojna1 = models.CharField(max_length=120,default=None,null=True,blank=True)
    year1 = models.CharField(max_length=4,default=None,null=True,blank=True)
    yojna2 = models.CharField(max_length=120,default=None,null=True,blank=True)
    year2 = models.CharField(max_length=4,default=None,null=True,blank=True)
    dinank = models.DateField(default=None,null=True,blank=True)
    place = models.CharField(max_length=20,default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "bhumihin_daridrya"
    def __str__(self) -> str:
        return str(self.name)