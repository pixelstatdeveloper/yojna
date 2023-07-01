from django.db import models

from .base import BaseModel
from .scheme_registration import SchemeRegistrationModel

import os
import uuid


def scheme_registration_media_directory_path(instance, filename):
    path = os.path.join("scheme_registration", str(instance.scheme_registration.pk))
    file_name = "{a}{b}".format(a=uuid.uuid4(), b=os.path.splitext(filename)[1])
    return os.path.join(path, file_name)


class SchemeRegistrationMediaModel(BaseModel):
    CATEGORY_1 = "जातीचे प्रमाणपत्र"
    CATEGORY_2 = "शेतीचा ७/१२ व ८ अ उतारा"
    CATEGORY_3 = "आधार कार्ड"
    CATEGORY_4 = "पासपोर्ट"
    CATEGORY_5 = "रहिवासी दाखला"
    CATEGORY_6 = "निवडणुक ओळखपत्र"
    CATEGORY_7 = "मालमत्ता नोंदपत्र"
    CATEGORY_8 = "उत्पन्न प्रमाणपत्र"
    CATEGORY_9 = "रेशन कार्ड"
    CATEGORY_10 = "वडिलांचे मृत्यू प्रमाणपत्र (आवश्यक असल्यास)"
    CATEGORY_11 = "१० वी किंवा १२ वी परीक्षेची गुणपत्रिका"
    CATEGORY_12 = "वसतिगृह प्रमाणपत्र (आवश्यक असल्यास)"
    CATEGORY_13 = "पतीचे उत्पन्न प्रमाणपत्र (अर्जदार जर स्त्री आहे आणि विवाहित असल्यास)"
    CATEGORY_14 = "मागासवर्गीय जातीचे प्रमाणपत्र"
    CATEGORY_15 = "ग्रामपंचायत सचिवाचा रहिवासी प्रमाणपत्र"
    CATEGORY_16 = "विवाह नोंदणी दाखला"
    CATEGORY_17 = "जागा उपलब्ध असल्याचे प्रमाणपत्र"
    CATEGORY_18 = "महिला बचत गट सुरु असल्याचे प्रमाणपत्र"
    CATEGORY_19 = "शाळासोडल्याचा दाखला"
    CATEGORY_20 = "ओलिताची सोय असल्याचे प्रमाणपत्र"
    CATEGORY_21 = "वयाचा दाखला"
    CATEGORY_22 = "शेतीचा नकाशा"

    CATEGORY_CHOICES = [
        (CATEGORY_1, "जातीचे प्रमाणपत्र"),
        (CATEGORY_2, "शेतीचा ७/१२ व ८ अ उतारा"),
        (CATEGORY_3, "आधार कार्ड"),
        (CATEGORY_4, "पासपोर्ट"),
        (CATEGORY_5, "रहिवासी दाखला"),
        (CATEGORY_6, "निवडणुक ओळखपत्र"),
        (CATEGORY_7, "मालमत्ता नोंदपत्र"),
        (CATEGORY_8, "उत्पन्न प्रमाणपत्र"),
        (CATEGORY_9, "रेशन कार्"),
        (CATEGORY_10, "वडिलांचे मृत्यू प्रमाणपत्र (आवश्यक असल्यास)"),
        (CATEGORY_11, "१० वी किंवा १२ वी परीक्षेची गुणपत्रिका"),
        (CATEGORY_12, "वसतिगृह प्रमाणपत्र (आवश्यक असल्यास)"),
        (CATEGORY_13, "पतीचे उत्पन्न प्रमाणपत्र (अर्जदार जर स्त्री आहे आणि विवाहित असल्यास)"),
        (CATEGORY_14, "मागासवर्गीय जातीचे प्रमाणपत्र"),
        (CATEGORY_15, "ग्रामपंचायत सचिवाचा रहिवासी प्रमाणपत्र"),
        (CATEGORY_16, "विवाह नोंदणी दाखला"),
        (CATEGORY_17, "जागा उपलब्ध असल्याचे प्रमाणपत्र"),
        (CATEGORY_18, "महिला बचत गट सुरु असल्याचे प्रमाणपत्र"),
        (CATEGORY_19, "शाळासोडल्याचा दाखला"),
        (CATEGORY_20, "ओलिताची सोय असल्याचे प्रमाणपत्र"),
        (CATEGORY_21, "वयाचा दाखला"),
        (CATEGORY_22, "शेतीचा नकाशा"),
    ]

    scheme_registration = models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, default=None, null=True,
                                            blank=True, related_name='scheme_registration_media')



    category = models.CharField(max_length=128, choices=CATEGORY_CHOICES, default=None, null=True, blank=True)
    arza = models.FileField(upload_to=scheme_registration_media_directory_path,  default=None, null=True,
                                 blank=True)

    file_path = models.FileField(upload_to=scheme_registration_media_directory_path, default=None, null=True,
                                 blank=True)

    class Meta:
        ordering = ['scheme_registration']
        db_table = 'scheme_registration_media'
        verbose_name = 'Scheme Registration Media'
        verbose_name_plural = 'Scheme Registration Media'
