from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class kendravarti_utpanna(models.Model):
    prakalp = models.CharField(max_length=30,default=None,null=True,blank=True)
    san = models.CharField(max_length=10,default=None,null=True,blank=True)
    jilha = models.CharField(max_length=20,default=None,null=True,blank=True)
    yojna = models.CharField(max_length=120,default=None,null=True,blank=True)
    name = models.CharField(max_length=80,default=None,null=True,blank=True)
    patta = models.CharField(max_length=140,default=None,null=True,blank=True)
    utara = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    ahvaal = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    mobile_no = PhoneNumberField(unique=True, blank=True)
    married = models.CharField(max_length=9,default=None,null=True,blank=True)
    aadim = models.CharField(max_length=20,default=None,null=True,blank=True)
    daridrya_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    income = models.CharField(max_length=15,default=None,null=True,blank=True)
    income_src = models.CharField(max_length=50,default=None,null=True,blank=True)
    bank_name = models.CharField(max_length=80,null=True, blank=True, default=None)
    acc_no = models.BigIntegerField(null=True, blank=True, default=None)
    ifsc = models.CharField(max_length=30,null=True, blank=True, default=None)
    adhar_no = models.BigIntegerField(null=True, blank=True, default=None)
    yojna_yn = models.CharField(max_length=4,default=None,null=True,blank=True)
    yojna_nm = models.CharField(max_length=80,default=None,null=True,blank=True)
    year = models.CharField(max_length=4,default=None,null=True,blank=True)
    jat = models.CharField(max_length=40,default=None,null=True,blank=True)
    jat_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    rahivasi_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "kendravarti_utpanna"
    def __str__(self) -> str:
        return str(self.name)