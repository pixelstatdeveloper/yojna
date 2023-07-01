from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class masemari_arth(models.Model):
    san= models.CharField(max_length=100,null=True, blank=True, default=None)
    talav= models.CharField(max_length=100,null=True, blank=True, default=None)
    ekun= models.CharField(max_length=100,null=True, blank=True, default=None)
    sabhasad= models.CharField(max_length=100,null=True, blank=True, default=None)
    name= models.CharField(max_length=100,null=True, blank=True, default=None)
    sahi = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)

    # umedwar_sign = models.FileField(upload_to='signatures', null=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "masemari_arth"
        

