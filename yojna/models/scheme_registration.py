from django.db import models
from .base import BaseModel
from .scheme import SchemeModel
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import uuid

class SchemeRegistrationModel(BaseModel):
    PENDING = "Pending"
    VERIFIED = "Verified"
    APPROVED= "Approved"
    REJECTED = "Rejected"
    In_Progress = "In Progress"
    Labarthi = "Labarthi"

    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (VERIFIED, "Verified"),
        (APPROVED, "Approved"),
        (REJECTED,"Rejected"),
        (In_Progress,"In Progress"),
        (Labarthi,"Labarthi")
    ]
    external_id = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True,
                             related_name='user_registrations')

    scheme = models.ForeignKey(SchemeModel, on_delete=models.CASCADE, default=None, null=True, blank=True,
                               related_name='scheme_registrations')
    
    status = models.CharField(max_length=64, choices=STATUS_CHOICES, default=STATUS_CHOICES[0], null=True, blank=True)
    application_id = models.CharField(max_length=1000, null=True, blank=True)
    raised_query = models.TextField(default=None,blank=True,null=True)
    hod_query = models.TextField(default=None,blank=True,null=True)
    cheque_letter = models.FileField(upload_to= 'cheques_letter/', null=True,blank=True,default=None)
    
    class Meta:
        ordering = ['scheme']
        db_table = 'scheme_registration'
        verbose_name = 'Scheme Registration'
        verbose_name_plural = 'Scheme Registrations'

    def __str__(self):
        return "{a}".format(a=self.scheme)



# @receiver(post_save, sender= SchemeRegistrationModel)
# def send_tracking_email(sender, instance,created, **kwargs):
#         if created:
#             return
#         print(instance)
#         send_mail(
#             "योजनेचा अर्ज",
#             f"Your Application status is {instance.status}",
#             settings.EMAIL_HOST_USER,
#             [instance.user.email],
#             fail_silently=False,
#         )
