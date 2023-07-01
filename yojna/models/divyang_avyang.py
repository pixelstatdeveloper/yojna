from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class divyang_avyang(models.Model):
    arjadar_name = models.CharField(max_length=100,default=None,null=True,blank=True)
    patta = models.CharField(default=None,null=True,blank=True,max_length=150)
    dinank = models.DateField(default=None,null=True,blank=True)
    jilha = models.CharField(max_length=20,default=None,null=True,blank=True)
    vivah_dinank = models.DateField(default=None,null=True,blank=True)
    var_nav = models.CharField(max_length=100,default=None,null=True,blank=True)
    var_apangpraman = models.CharField(default=None,null=True,blank=True,max_length=80)
    var_shikshan = models.CharField(default=None,null=True,blank=True,max_length=80)
    var_vyavsay = models.CharField(default=None,null=True,blank=True,max_length=80)
    var_karyalay = models.CharField(default=None,null=True,blank=True,max_length=80)
    var_address = models.CharField(default=None,null=True,blank=True,max_length=150)
    vadhu_nav = models.CharField(max_length=100,default=None,null=True,blank=True)
    vadhu_apangpraman = models.CharField(default=None,null=True,blank=True,max_length=80)
    vadhu_shikshan = models.CharField(default=None,null=True,blank=True,max_length=80)
    vadhu_vyavsay = models.CharField(default=None,null=True,blank=True,max_length=80)
    vadhu_karyalay = models.CharField(default=None,null=True,blank=True,max_length=80)
    vadhu_address = models.CharField(default=None,null=True,blank=True,max_length=150)
    vivah_date = models.DateField(default=None,null=True,blank=True)
    vivah_place = models.CharField(default=None,null=True,blank=True,max_length=50)
    vivah_type = models.CharField(default=None,null=True,blank=True,max_length=7)
    var_pratham = models.CharField(default=None,null=True,blank=True,max_length=4)
    vadhu_pratham = models.CharField(default=None,null=True,blank=True,max_length=4)
    var_vidur = models.CharField(default=None,null=True,blank=True,max_length=4)
    vadhu_vidhva = models.CharField(default=None,null=True,blank=True,max_length=4)
    bfor_yojna = models.CharField(default=None,null=True,blank=True,max_length=4)
    anya_zp = models.CharField(default=None,null=True,blank=True,max_length=4)
    zp_name = models.CharField(default=None,null=True,blank=True,max_length=60)
    zp_dinank = models.DateField(default=None,null=True,blank=True)
    zp_arzadinank = models.DateField(default=None,null=True,blank=True)
    satkar = models.CharField(default=None,null=True,blank=True,max_length=4)
    where = models.CharField(default=None,null=True,blank=True,max_length=50)
    when = models.CharField(default=None,null=True,blank=True,max_length=40)
    var_sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    vadhu_sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)    

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "divyang_avyang"
    def __str__(self) -> str:
        return str(self.arjadar_name)