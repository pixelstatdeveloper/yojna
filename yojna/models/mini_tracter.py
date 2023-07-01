from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class mini_tra(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=1000,default=None,null=True,blank=True)
    address = models.TextField(default=None,null=True,blank=True)
    mobile_no = PhoneNumberField(unique=True, blank=True)
    gat_name = models.CharField(max_length=1000,default=None,null=True,blank=True)
    karya_address = models.TextField(default=None,null=True,blank=True)
    bachat_no = models.IntegerField(default=None,null=True,blank=True)
    anu_no = models.IntegerField(default=None,null=True,blank=True)
    itar_no = models.IntegerField(default=None,null=True,blank=True)
    registration_no = models.CharField(default=None,null=True,blank=True,max_length=200)
    registration_date = models.DateField(default=None,null=True,blank=True)
    bachat_info = models.TextField(default=None,null=True,blank=True)
    place = models.CharField(max_length=100,default=None,null=True,blank=True)
    app_date = models.DateField(default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media',default=None,null=True,blank=True)
    signature = models.FileField(upload_to='media',default=None,null=True,blank=True)
    class Meta:
        db_table = "Mini_Tra"
    def __str__(self) -> str:
        return str(self.name)

        