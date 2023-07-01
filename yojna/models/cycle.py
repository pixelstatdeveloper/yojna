from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class mada_cycle(models.Model):
    name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    sam_patta = models.CharField(max_length=1000, null=True, blank=True)
    mukkam = models.CharField(max_length=1000, null=True, blank=True)
    post= models.CharField(max_length=100,null=True, blank=True, default=None)
    taluka= models.CharField(max_length=100,null=True, blank=True, default=None)
    jati = models.BooleanField(default=None,null=True,blank=True)
    dakhla = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    jat =  models.CharField(max_length=100, null=True, blank=True)
    potjat =  models.CharField(max_length=100, null=True, blank=True)
    san =  models.CharField(max_length=100, null=True, blank=True)
    iyatta =  models.CharField(max_length=100, null=True, blank=True)
    sch_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    sch_patta = models.CharField(max_length=1000, null=True, blank=True)
    gun = models.CharField(max_length=100, null=True, blank=True)
    mulinmadhun = models.CharField(max_length=100, null=True, blank=True)
    takke = models.CharField(max_length=100, null=True, blank=True)
    san1 =  models.CharField(max_length=100, null=True, blank=True)
    iyatta1 =  models.CharField(max_length=100, null=True, blank=True)
    sch_name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    sch_patta1 = models.CharField(max_length=1000, null=True, blank=True)
    gav_name= models.CharField(max_length=1000,null=True, blank=True, default=None)
    antar =  models.CharField(max_length=100, null=True, blank=True)
    buisness = models.CharField(max_length=1000, null=True, blank=True)
    dakhla1 = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    san2 =  models.CharField(max_length=100, null=True, blank=True)
    utpanna =  models.CharField(max_length=100, null=True, blank=True)
    sthal =  models.CharField(max_length=100, null=True, blank=True)
    form_date = models.DateField(default=None,null=True,blank=True)
    patta = models.CharField(max_length=1000, null=True, blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    photo = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "mada_cycle"
        

