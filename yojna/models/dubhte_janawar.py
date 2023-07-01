from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import UserModel,SchemeModel,SchemeRegistrationModel

class dubhte_janawar(models.Model):
    
    name = models.CharField(max_length=100,default=None,null=True,blank=True)
    address = models.CharField(max_length=170,default=None,null=True,blank=True)
    jat = models.CharField(max_length=80,default=None,null=True,blank=True)
    janwar = models.CharField(max_length=50,default=None,null=True,blank=True)
    sudharit = models.CharField(max_length=50,default=None,null=True,blank=True)
    kilo = models.CharField(max_length=50,default=None,null=True,blank=True)
    sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    nav = models.CharField(max_length=60,default=None,null=True,blank=True)
    patta = models.CharField(max_length=80,default=None,null=True,blank=True)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "dubhte_janawar"
    def __str__(self) -> str:
        return str(self.name)