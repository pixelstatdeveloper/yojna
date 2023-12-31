from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class mahatmagandhi_reshim(models.Model):
    jilha = models.CharField(max_length=15,default=None,null=True,blank=True)
    dinank = models.DateField(default=None,null=True,blank=True)
    jilha2 = models.CharField(max_length=15,default=None,null=True,blank=True)
    yojna = models.CharField(max_length=11,default=None,null=True,blank=True)
    name = models.CharField(max_length=100,default=None,null=True,blank=True)
    gender = models.CharField(max_length=8,default=None,null=True,blank=True)
    birthyear = models.CharField(max_length=4,default=None,null=True,blank=True)
    jat = models.CharField(max_length=15,default=None,null=True,blank=True)
    mukam = models.CharField(max_length=60,default=None,null=True,blank=True)
    taluka = models.CharField(max_length=30,default=None,null=True,blank=True)
    dist = models.CharField(max_length=15,default=None,null=True,blank=True)
    mobile_no = PhoneNumberField(unique=True, blank=True)
    adhar_no = models.BigIntegerField(default=None,null=True,blank=True)
    education = models.CharField(default=None,null=True,blank=True,max_length=80)
    bank_name = models.CharField(default=None,null=True,blank=True,max_length=50)
    acc_no = models.CharField(default=None,null=True,blank=True,max_length=20)
    branch = models.CharField(default=None,null=True,blank=True,max_length=40)
    ifsc = models.CharField(default=None,null=True,blank=True,max_length=20)
    land_type = models.CharField(default=None,null=True,blank=True,max_length=10)
    gat_712 = models.CharField(default=None,null=True,blank=True,max_length=10)
    ekun_shetra = models.CharField(default=None,null=True,blank=True,max_length=50)
    pik1 = models.CharField(default=None,null=True,blank=True,max_length=40)
    pik2 = models.CharField(default=None,null=True,blank=True,max_length=40)
    pik3 = models.CharField(default=None,null=True,blank=True,max_length=40)
    pik4 = models.CharField(default=None,null=True,blank=True,max_length=40)
    acre = models.CharField(default=None,null=True,blank=True,max_length=60)
    sinchan_src = models.CharField(default=None,null=True,blank=True,max_length=20)
    sinchan_time = models.CharField(default=None,null=True,blank=True,max_length=15)
    vijjodni_yn = models.CharField(default=None,null=True,blank=True,max_length=4)
    kitak_yn = models.CharField(default=None,null=True,blank=True,max_length=4)
    majur_yn = models.CharField(default=None,null=True,blank=True,max_length=4)
    shetkari_varg = models.CharField(default=None,null=True,blank=True,max_length=5)
    daridrya_yn = models.CharField(default=None,null=True,blank=True,max_length=4)
    bpl_no = models.CharField(default=None,null=True,blank=True,max_length=25)
    ropvatika_yn = models.CharField(default=None,null=True,blank=True,max_length=4)
    nam = models.CharField(default=None,null=True,blank=True,max_length=80)
    padnam = models.CharField(default=None,null=True,blank=True,max_length=50)
    karyalay = models.CharField(default=None,null=True,blank=True,max_length=60)
    shetkari_sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    shetkari_name = models.CharField(default=None,null=True,blank=True,max_length=60)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "mahatmagandhi_reshim"
    def __str__(self) -> str:
        return str(self.name)


    #name = models.CharField(max_length=100,default=None,null=True,blank=True)
    #mukam = models.CharField(max_length=100,default=None,null=True,blank=True)
    #post = models.CharField(max_length=50,default=None,null=True,blank=True)
    #taluka = models.CharField(max_length=40,default=None,null=True,blank=True)
    #pincode = models.IntegerField(default=None,null=True,blank=True)
    #adhar_no = models.BigIntegerField(default=None,null=True,blank=True)
    #mobile_no = PhoneNumberField(unique=True, blank=True)
    #elction_no = models.CharField(max_length=40,default=None,null=True,blank=True)
    #jobcard_no = models.CharField(max_length=40,default=None,null=True,blank=True)
    #education = models.CharField(default=None,null=True,blank=True,max_length=80)
    #birthdate = models.DateField(default=None,null=True,blank=True)
    #varg_jat = models.CharField(default=None,null=True,blank=True,max_length=20)
    #shetjamin = models.CharField(default=None,null=True,blank=True,max_length=10)
    #bagayat = models.CharField(default=None,null=True,blank=True,max_length=10)
    #survey_no = models.CharField(default=None,null=True,blank=True,max_length=40)
    #pik1 = models.CharField(default=None,null=True,blank=True,max_length=40)
    #pik2 = models.CharField(default=None,null=True,blank=True,max_length=40)
    #pik3 = models.CharField(default=None,null=True,blank=True,max_length=40)
    #pik4 = models.CharField(default=None,null=True,blank=True,max_length=40)
    #sinchan = models.CharField(default=None,null=True,blank=True,max_length=20)
    #sinchan_src = models.CharField(default=None,null=True,blank=True,max_length=20)
    #family_member = models.IntegerField(default=None,null=True,blank=True)

    #name1 = models.CharField(default=None,null=True,blank=True,max_length=50)
    #nate1 = models.CharField(default=None,null=True,blank=True,max_length=30)
    #vyavsay1 = models.CharField(default=None,null=True,blank=True,max_length=50)
    #age1 = models.CharField(default=None,null=True,blank=True,max_length=5)

    #name2 = models.CharField(default=None,null=True,blank=True,max_length=50)
    #nate2 = models.CharField(default=None,null=True,blank=True,max_length=30)
    #vyavsay2 = models.CharField(default=None,null=True,blank=True,max_length=50)
    #age2 = models.CharField(default=None,null=True,blank=True,max_length=5)

    #name3 = models.CharField(default=None,null=True,blank=True,max_length=50)
    #nate3 = models.CharField(default=None,null=True,blank=True,max_length=30)
    #vyavsay3 = models.CharField(default=None,null=True,blank=True,max_length=50)
    #age3 = models.CharField(default=None,null=True,blank=True,max_length=5)
    
    #name4 = models.CharField(default=None,null=True,blank=True,max_length=50)
    #nate4 = models.CharField(default=None,null=True,blank=True,max_length=30)
    #vyavsay4 = models.CharField(default=None,null=True,blank=True,max_length=50)
    #age4 = models.CharField(default=None,null=True,blank=True,max_length=5)

    #kiti_shetra = models.CharField(default=None,null=True,blank=True,max_length=50)
    #survvey = models.CharField(default=None,null=True,blank=True,max_length=100)
    #land_type = models.CharField(default=None,null=True,blank=True,max_length=10)
    #bank_yn = models.CharField(default=None,null=True,blank=True,max_length=8)
    #bank_name = models.CharField(default=None,null=True,blank=True,max_length=50)
    #branch = models.CharField(default=None,null=True,blank=True,max_length=40)
    #acc_no = models.CharField(default=None,null=True,blank=True,max_length=20)
    #ifsc = models.CharField(default=None,null=True,blank=True,max_length=20)
    #passbook = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    #bfor_sheti = models.CharField(default=None,null=True,blank=True,max_length=8)
    #year = models.CharField(default=None,null=True,blank=True,max_length=10)
    #reason = models.CharField(default=None,null=True,blank=True,max_length=50)
    #anudan = models.CharField(default=None,null=True,blank=True,max_length=100)
    #place = models.CharField(default=None,null=True,blank=True,max_length=30)
    #dinank = models.DateField(default=None,null=True,blank=True)
    #sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    #arza_name = models.CharField(default=None,null=True,blank=True,max_length=60)
    #gav = models.CharField(default=None,null=True,blank=True,max_length=40)
    #taluka1 = models.CharField(default=None,null=True,blank=True,max_length=40)
