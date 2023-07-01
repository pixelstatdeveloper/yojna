from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class silk_samagra(models.Model):
    city = models.CharField(max_length=35,default=None,null=True,blank=True)
    dinank = models.DateField(default=None,null=True,blank=True)
    karyalay = models.CharField(max_length=35,default=None,null=True,blank=True)
    yojna = models.CharField(max_length=15,default=None,null=True,blank=True)
    name = models.CharField(max_length=60,default=None,null=True,blank=True)
    gender = models.CharField(default=None,null=True,blank=True,max_length=8)
    birthyear = models.CharField(max_length=4 ,default=None,null=True,blank=True)
    jat = models.CharField(default=None,null=True,blank=True,max_length=14)
    mukam = models.CharField(max_length=35 ,default=None,null=True,blank=True)
    taluka = models.CharField(max_length=25, default=None,null=True,blank=True)
    jilha = models.CharField(max_length=20, default=None,null=True,blank=True)
    mobile = PhoneNumberField(unique=True, blank=True)
    adharno = models.BigIntegerField(default=None,null=True,blank=True)
    education = models.CharField(default=None,null=True,blank=True,max_length=80)
    bank = models.CharField(max_length=50, default=None,null=True,blank=True)
    acc_no = models.BigIntegerField(default=None,null=True,blank=True)
    branch = models.CharField(default=None,null=True,blank=True,max_length=30)
    ifsc = models.CharField(default=None,null=True,blank=True,max_length=18)
    land = models.CharField(default=None,null=True,blank=True,max_length=5)
    utara_no = models.CharField(max_length=30, default=None,null=True,blank=True)
    shetra = models.CharField(default=None,null=True,blank=True,max_length=30)
    pik1 = models.CharField(default=None,null=True,blank=True,max_length=40)
    pik2 = models.CharField(default=None,null=True,blank=True,max_length=40)
    pik3 = models.CharField(default=None,null=True,blank=True,max_length=40)
    pik4 = models.CharField(default=None,null=True,blank=True,max_length=40)
    tuti = models.CharField(default=None,null=True,blank=True,max_length=25)
    sinchan = models.CharField(default=None,null=True,blank=True,max_length=9)
    kalavadhi = models.CharField(default=None,null=True,blank=True,max_length=8)
    vij = models.CharField(default=None,null=True,blank=True,max_length=4)
    kitak = models.CharField(default=None,null=True,blank=True,max_length=4)
    majur = models.CharField(default=None,null=True,blank=True,max_length=4)
    shetkari = models.CharField(default=None,null=True,blank=True,max_length=5)
    daridrya = models.CharField(default=None,null=True,blank=True,max_length=4)
    daridrya_no = models.CharField(default=None,null=True,blank=True,max_length=25)
    ropvatika = models.CharField(default=None,null=True,blank=True,max_length=4)
    shree = models.CharField(default=None,null=True,blank=True,max_length=60)
    padnam = models.CharField(default=None,null=True,blank=True,max_length=50)
    yanni = models.CharField(default=None,null=True,blank=True,max_length=60)
    shetkari_name = models.CharField(default=None,null=True,blank=True,max_length=50)
    shetkari_sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "silk_samagra"
    def __str__(self) -> str:
        return str(self.name)