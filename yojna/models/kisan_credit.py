from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class kisan_credit(models.Model):
    date = models.DateField(default=None,null=True,blank=True)
    name = models.CharField(max_length=80,default=None,null=True,blank=True)
    father = models.CharField(max_length=80,default=None,null=True,blank=True)
    gender = models.CharField(max_length=6,default=None,null=True,blank=True)
    caste = models.CharField(max_length=10,default=None,null=True,blank=True)
    mobile = PhoneNumberField(unique=True, blank=True)
    uid_oreid = models.CharField(max_length=10,default=None,null=True,blank=True)
    adhar_no = models.CharField(max_length=28,default=None,null=True,blank=True)
    id_proof = models.CharField(max_length=30,default=None,null=True,blank=True)
    id_no = models.CharField(max_length=30,default=None,null=True,blank=True)
    state = models.CharField(max_length=25,default=None,null=True,blank=True)
    dist = models.CharField(max_length=25,default=None,null=True,blank=True)
    subdist = models.CharField(max_length=25,default=None,null=True,blank=True)
    village = models.CharField(max_length=25,default=None,null=True,blank=True)
    address = models.CharField(max_length=120,default=None,null=True,blank=True)
    ifsc = models.CharField(max_length=12,default=None,null=True,blank=True)
    state_name = models.CharField(max_length=25,default=None,null=True,blank=True)
    dist_name = models.CharField(max_length=25,default=None,null=True,blank=True)
    bank = models.CharField(max_length=50,default=None,null=True,blank=True)
    branch = models.CharField(max_length=25,default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "kisan_credit"
    def __str__(self) -> str:
        return str(self.name)