from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class punyshlok_ahilya(models.Model):
    jilha= models.CharField(max_length=100,null=True, blank=True, default=None)
    san = models.CharField(max_length=100, null=True, blank=True)
    varshat= models.CharField(max_length=100,null=True, blank=True, default=None)
    san1 = models.CharField(max_length=100, null=True, blank=True)
    madhe= models.CharField(max_length=100,null=True, blank=True, default=None)
    name= models.CharField(max_length=100,null=True, blank=True, default=None)
    gav= models.CharField(max_length=100,null=True, blank=True, default=None)
    pin= models.CharField(max_length=100,null=True, blank=True, default=None)
    taluka= models.CharField(max_length=100,null=True, blank=True, default=None)
    jilha2= models.CharField(max_length=100,null=True, blank=True, default=None)
    mobile_number = PhoneNumberField( blank=True)
    email_id = models.EmailField(null=False, blank=False, default=None)
    dhaar_no = models.CharField(max_length=100, null=True, blank=True)
    prakar = models.CharField(max_length=100,default=None,null=True,blank=True)
    vargvari = models.CharField(max_length=100,default=None,null=True,blank=True)
    sarve_no = models.CharField(max_length=100,default=None,null=True,blank=True)
    gav1= models.CharField(max_length=100,null=True, blank=True, default=None)
    pin1= models.CharField(max_length=100,null=True, blank=True, default=None)
    taluka1= models.CharField(max_length=100,null=True, blank=True, default=None)
    jilha1= models.CharField(max_length=100,null=True, blank=True, default=None)
    bank_name= models.CharField(max_length=100,null=True, blank=True, default=None)
    shakha= models.CharField(max_length=100,null=True, blank=True, default=None)
    acc_no= models.CharField(max_length=100,null=True, blank=True, default=None)
    ifsc= models.CharField(max_length=100,null=True, blank=True, default=None)
    doc1 = models.CharField(max_length=50,null=True, blank=True, default=None)
    doc2 = models.CharField(max_length=50,null=True, blank=True, default=None)
    doc3 = models.CharField(max_length=50,null=True, blank=True, default=None)
    doc4 = models.CharField(max_length=50,null=True, blank=True, default=None)
    doc5 = models.CharField(max_length=50,null=True, blank=True, default=None)
    doc6 = models.CharField(max_length=50,null=True, blank=True, default=None)
    doc7 = models.CharField(max_length=50,null=True, blank=True, default=None)
    doc8 = models.CharField(max_length=50,null=True, blank=True, default=None)
    doc9 = models.CharField(max_length=50,null=True, blank=True, default=None)
    thikan= models.CharField(max_length=100,null=True, blank=True, default=None)
    dinank = models.DateField(default=None,null=True,blank=True)
    signature = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    name1= models.CharField(max_length=1000,null=True, blank=True, default=None)
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "punyshlok_ahilya"
        

