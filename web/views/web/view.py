from django.http.response import HttpResponse, HttpResponseRedirect,JsonResponse
from yojna.models.user import User_documents
from django.shortcuts import render
from yojna.services import SmsService
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.conf import settings
from django.shortcuts import redirect
from yojna.models import DepartmentModel, upajivikesathi,andh_vyaktinsathi,mahatmagandhi_reshim,ekatmik_dugdha,sainikshala_adi,rajarshi_shahuscholar,kisan_credit,shubhmangal_nondni,silk_samagra,shaskiy_postbasic,kendra_prashikshan,shaskiy_ashramshala,kendravarti_utpanna,eklavya_school,adivasividyarthi_engraji,anusuchit_scholar,divyang_avyang,antarjatiy_vivah,swayamrojgar_divyang,divyadivyang_anudan,anusuchit_swechha,thakkar,samuhik_vivah,bhumihin_daridrya,anusuchit_shabri,anusuchit_janavare,anusuchit_shelya,anusuchit_50takke,dubhte_janawar,ramai_gharkul,jilhaudyog,sudharitbij, divyang_xerox, divyang_sanganak, magas_shilai, asthivyang_vyakti, karnbadhir_vyakti, navin_rashtriy,punyshlok_ahilya,aarogya_patrika, mini_tra,polis_bhartipurva,zakir_hus,mada_shivnyantra,dharmik_alp,scp_shivnyantra,otsp_cycl,scp_cycl,tsp_cycl,tsp_shivnyantra,mada_cycle,balsangopan,shubh_vivah,otsp_shivnyantra, jilha_pur,din_dayal,masemari_arth,matsyasampada,sanstha_sabhasad,vaiyaktik_sabhasad,vyaktinsathi,gatai_kamgar,shahu_fule,gayakvad,swadhar_yoj,pravinya_rajya,lokshahir,magasvargiy_mula,karmavir,ravidas,ravidas_sanstha,lokshahir_sanstha,bharat_sanstha, pra_dhan, sankalp_skill, pramod_mah, SchemeRegistrationModel, SchemeRegistrationMediaModel, UserModel, SubdepartmentModel, DocumentlinkModel, DepartmentMediaModel,SchemeModel
from django.utils import timezone
from django.contrib.auth import get_user_model
from yojna.services import SchemeRegistrationMediaService
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import smtplib
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views import View
from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse
from django.contrib import messages
import hashlib
import urllib.parse as encoder
import os
import json
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from typing import Any
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



from twilio.rest import Client
# from twilio_api import settings


def handler400(request, exception=None, template_name='web/400.html'):
    response = render(request=request, template_name=template_name)
    response.status_code = 400
    return response


def handler403(request, exception=None, template_name='web/403.html'):
    response = render(request=request, template_name=template_name)
    response.status_code = 403
    return response


def handler404(request, exception=None, template_name='web/404.html'):
    response = render(request=request, template_name=template_name)
    response.status_code = 404
    return response


def handler500(request, exception=None, template_name='web/500.html'):
    response = render(request=request, template_name=template_name)
    response.status_code = 500
    return response


def home(request):
    context = dict()
    context["departments"] = DepartmentModel.objects.all()
    return render(request=request, template_name='web/home.html', context=context)


def sector_show(request, name):
    context = dict()
    return render(request=request, template_name='web/sector_show.html', context=context)


def department_show(request, name):
    context = dict()
    return render(request=request, template_name='web/department_show.html', context=context)

def dep_dashboard(request):
    # Counts 
    schemes_ct = SchemeModel.objects.filter(department=request.user.department,subdepartment=request.user.subdepartment).count()
    applicant = SchemeRegistrationModel.objects.filter(scheme__department=request.user.department,scheme__subdepartment=request.user.subdepartment).count()
    labarthi = SchemeRegistrationModel.objects.filter(scheme__department=request.user.department,scheme__subdepartment=request.user.subdepartment,status="Labarthi").count()
    
    # Pie Chart
    Pending = SchemeRegistrationModel.objects.filter(scheme__department=request.user.department,scheme__subdepartment=request.user.subdepartment, status="Pending").count()
    Verified = SchemeRegistrationModel.objects.filter(scheme__department=request.user.department,scheme__subdepartment=request.user.subdepartment, status="Verified").count()
    Approved = SchemeRegistrationModel.objects.filter(scheme__department=request.user.department,scheme__subdepartment=request.user.subdepartment, status="Approved").count()
    Rejected = SchemeRegistrationModel.objects.filter(scheme__department=request.user.department,scheme__subdepartment=request.user.subdepartment, status="Rejected").count()
    In_Progress = SchemeRegistrationModel.objects.filter(scheme__department=request.user.department,scheme__subdepartment=request.user.subdepartment, status="In Progress").count()

    # Bar Chart
    Schemes = SchemeModel.objects.filter(department=request.user.department,subdepartment=request.user.subdepartment)
    result = []
    for x in Schemes:
        reg_scheme = SchemeRegistrationModel.objects.filter(scheme=x).count()
        result.append(reg_scheme)
    print(result)

    context= {'schemes_ct':schemes_ct,'applicant':applicant,'labh':labarthi,'Pending':Pending,'Verified':Verified,'Approved':Approved,'Rejected':Rejected,'In_Progress':In_Progress,'Schemes':Schemes,'result':result}
    return render(request,"web/admin_dashboard.html",context)

def scheme_index(request,department):
    context = dict()
    context["schemes"] = SchemeModel.objects.filter(department__id=department)
    context["subdeps"] = SubdepartmentModel.objects.filter(department__id=department)
    context['department']= DepartmentModel.objects.get(id= department)
    context['department_media']= DepartmentMediaModel.objects.get(department=context['department'])
    print(request.user) 
    # if request.user!=None:
    if request.user.is_authenticated:
        context['registered']= SchemeRegistrationModel.objects.filter(user=request.user).values_list('scheme__name', flat=True)
    else:
        context['registered']=[]
    return render(request=request, template_name='web/scheme_index.html', context=context)



def scheme_show(request, name):
    context = dict()
    return render(request=request, template_name='web/scheme_show.html', context=context)


def sector_index(request):
    context = dict()
    return render(request=request, template_name='web/sector_index.html', context=context)


def department_index(request):
    context = dict()
    return render(request=request, template_name='web/department_index.html', context=context)

def update_profile(request):
    if request.method == "GET":
        context=dict()
        return render(request=request,template_name='web/update_profile.html',context=context)
    elif request.method == "POST":
        user = request.user
        if request.POST.get('name'):
            user.name = request.POST['name']
        if request.POST.get('email'):
            user.email = request.POST['email']
        if request.POST.get('mobile_number'):
            user.mobile_number = request.POST['mobile_number']
        if request.POST.get('adhaar'):
            user.adhaar_no = request.POST['adhaar']
        if request.POST.get('gender'):
            user.Gender = request.POST['gender']
        if request.POST.get('caste'):
            user.caste = request.POST['caste']
        if request.POST.get('bpl'):
            user.bpl = request.POST['bpl']
        if request.POST.get('bpl_dharak'):
            user.bpl_dharak = request.POST['bpl_dharak']
        if request.POST.get('address'):
            user.address = request.POST['address']
        if request.POST.get('country'):
            user.country = request.POST['country']
        if request.POST.get('state'):
            user.state = request.POST['state']
        if request.POST.get('city'):
            user.city = request.POST['city']
        if request.FILES.get('profile_pic'):
            user.profile_pic=request.FILES['profile_pic']
        user.save()
        messages.success(request, 'Profile Updated successfully !')
        return redirect(reverse('web:profile'))

def sign_up(request):
    context = dict()
    if request.method == 'GET':
        return render(request=request, template_name='web/sign_up.html', context=context)
    elif request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        mobile_number = request.POST.get('mobile_number', None)
        adhaar = request.POST.get('adhaar',None)
        gender = request.POST.get('gender',None)
        country = request.POST.get('country',None)
        state = request.POST.get('state',None)
        city = request.POST.get('city',None)
        address = request.POST.get('address',None)
        caste = request.POST.get('caste',None)
        bpl = request.POST.get('bpl',None)
        bpl_dharak = request.POST.get('bpl_data',None)
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        print(adhaar,gender,bpl_dharak)
        import pdb;pdb.set_trace(adhaar,gender,bpl_dharak)

        if password != confirm_password:
            messages.error(request, 'Passwords don\'t match')
            return redirect(request, 'web/sign_up.html')

        user = get_user_model().objects.create_user(name=name, email=email, password=password,
                                                    mobile_number=mobile_number,adhaar_no = adhaar,caste=caste,Gender=gender,bpl=bpl,bpl_dharak=bpl_dharak)
        if user is not None:
            dj_login(request, user)
            redirect_url = request.GET.get("next", settings.LOGIN_REDIRECT_URL)
            if not redirect_url:
                redirect_url = settings.LOGIN_REDIRECT_URL
            return redirect(redirect_url)
        else:
            pass

class Registration(View):
    def __init__(self):
        super(Registration, self).__init__()
        self.hash_util = os.environ.get('verification_hash') or 'random_string'

    def get(self, request):
        return render(request, 'web/sign_up.html')

    def post(self, request):
        try:
            print(request.POST)
            name = request.POST['name']
            email = request.POST['email']
            mobile_number = request.POST['mobile_number']
            adhaar = request.POST.get('adhaar',None)
            gender = request.POST.get('gender',None)
            caste = request.POST.get('caste',None)
            bpl = request.POST.get('bpl',None)
            bpl_dharak = request.POST.get('bpl_data',None)
            country = request.POST.get('country','')
            state = request.POST.get('state','')
            city = request.POST.get('city','')
            address = request.POST.get('address','')
            profile_pic=request.FILES['profile_pic']
            if bpl_dharak == '':
                bpl_dharak = None
            password = request.POST.get('password', None)
            confirm_password = request.POST.get('confirm_password', None)
            # print(adhaar,gender,bpl_dharak)
            # import pdb;pdb.set_trace()

            if password != confirm_password:
                messages.error(request, 'Passwords don\'t match')
                return redirect(request, 'web/sign_up.html')

            user = get_user_model().objects.create_user(name=name, email=email, password=password,
                                                        mobile_number=mobile_number,adhaar_no = adhaar,caste=caste,Gender=gender,bpl=bpl,bpl_dharak=bpl_dharak,
                                                        city=city,state=state,country=country,address=address,profile_pic=profile_pic)
            user.is_active = True
            user.role = "User"
            user.save()
            html_message = loader.render_to_string(
                                'web/mail_body.html',
                                {
                                    'name':user.name,
                                    'action': 'register',
                                    'url': f"{request.scheme}://{request.get_host()}{reverse('web:sign_in')}"
                                }
                            )
            send_mail("डॉ. बाबासाहेब  आंबेडकर न्याय योजना नोंदणी  ",None,settings.EMAIL_HOST_USER,[user.email],fail_silently=False,html_message=html_message)
            
            ph = (str(user.mobile_number))[3:]
            print(ph)
            params = {
                        "user": "developer",
                        "password": 123456,
                        "msisdn": ph,
                        "sid": "SDCTEC",
                        "msg": "Congratulations, you have registered successfully !",
                        "fl": 0,
                        "gwid": 2
                     }

            link = "http://bullet1.sdctechnologies.co.in:8080/vendorsms/pushsms.aspx"


            requests.get(link+"?"+encoder.urlencode(params))
            messages.success(request, 'नोंदणी केल्याबद्दल धन्यवाद.')
            # hash_object = hashlib.md5((email + self.hash_util).encode())
            # hashed_string = hash_object.hexdigest()

            # subject, from_email, to = 'Verification', settings.EMAIL_HOST_USER, user.email
            # url = f"{request.scheme}://{request.get_host()}{reverse('web:verify')}?key={hashed_string}&email={user.email}"
            # html_content = render_to_string('web/verification_template.html', {'url': url})
            # text_content = strip_tags(html_content)
            # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            # messages.success(request, "We have sent you a verification mail. \
            # Follow the instructions in mail to complete your registration")
        except Exception as e:
            print("hi",e)
        return redirect(reverse("web:sign_in"))

@login_required()
@csrf_exempt
def scheme_registration(request, pk):
    context = dict()
    if request.method == 'GET':
        context["scheme"] = SchemeModel.objects.filter(id=pk).first()
        context['arza_document']=SchemeRegistrationMediaModel.arza
        documents= DocumentlinkModel.objects.filter(scheme=context["scheme"]).values().order_by('created_at')
        context["registration_media"] = documents
        context["doc_link"] = DocumentlinkModel.objects.filter(scheme__name=request.GET.get('scheme', None)).order_by('created_at')
        x=SchemeRegistrationModel.objects.filter(scheme=context["scheme"],user=request.user).count()
        department=context["scheme"].department.id
        if x:
            return redirect(reverse("web:scheme_index",kwargs={'department':department}))
        else:
            return render(request=request, template_name='web/scheme_registration.html', context=context)

    else:
        try:
            register_scheme=SchemeRegistrationModel.objects.get(user=request.user, scheme=SchemeModel.objects.get(pk=pk))
        except:
            register_scheme = SchemeRegistrationModel(user=request.user, scheme=SchemeModel.objects.get(pk=pk))
            register_scheme.status = SchemeRegistrationModel.PENDING
            scheme_count=SchemeRegistrationModel.objects.all().count()+1
            dept_id = str(SchemeModel.objects.get(pk=pk).department.id)[0:3].upper()
            scheme_id = str(SchemeModel.objects.get(pk=pk).id)[0:3].upper()
            register_scheme.application_id=str(dept_id)+str(scheme_id)+str(scheme_count)
            register_scheme.save()
        if not request.FILES.get('arza'):
            print('hi')
            if request.POST.get('app_id'):
                register_scheme.external_id = request.POST.get('app_id')
                register_scheme.save()
                print('App id came')
            elif SchemeModel.objects.get(pk=pk).name=='( DW ) अंध व्यक्तींसाठी साहाय्य भूत साधने व उपकरणांसाठी अर्थसहाय्य करणे':
                up=andh_vyaktinsathi.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसूचित जाती व नवबौध्द घटकांसाठी रमाई घरकुल योजना':
                up=ramai_gharkul.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसूचित जाती व नवबौद्ध घटकांच्या बचत गटांकरीता मिनी ट्रॅक्टरचा पुरवठा योजना':
                up=mini_tra.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='RPL (Recognition of Prior Learning ) आधिच कौशल्य विकास प्रशिक्षण प्राप्त केलेल्या उमेदवारांना प्रमाणपत्राचे वितरण':
                up=upajivikesathi.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='SANKALP - उपजिविकेसाठी कौशल्य संपादन व ज्ञान जागरुकता अभियान':
                up=sankalp_skill.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='जिल्हा पुरस्कृत योजना (DPDC) (जिल्हास्तरीय योजना- जिल्हा नियोजन समिती पुरस्कृत)':
                up=jilha_pur.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='दीनदयाल अंत्योदय योजना- राष्ट्रीय नागरी उपजिवीका अभियान (DAY - NULM)':
                up=din_dayal.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='प्रधानमंत्री कौशल्य विकास योजना (PMKVY ३.0) (केंद्रशासन पुरस्कृत)':
                up=pra_dhan.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='प्रमोद महाजन कौशल्य व उद्योजकता विकास अभियान (PMKUVA) (राज्यशासन पुरस्कृत)':
                up=pramod_mah.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='भारतरत्न डॉ. बाबासाहेब आंबेडकर समाज भूषणपुरस्कार (व्यत्कींसाठी)':
                up=vyaktinsathi.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='साहित्यरत्न लोकशाहीर अण्णाभाऊ साठे पुरस्कार (व्यत्कींसाठी)':
                up=lokshahir.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='संत रविदास पुरस्कार (व्यत्कींसाठी)':
                up=ravidas.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='पद्मश्री कर्मवीर दादासाहेब गायकवाड पुरस्कार (व्यत्कींसाठी)':
                up=karmavir.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='भारतरत्न डॉ. बाबासाहेब आंबेडकर समाज भूषणपुरस्कार (संस्थांसाठी)':
                up=bharat_sanstha.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='साहित्यरत्न लोकशाहीर अण्णाभाऊ साठे पुरस्कार (संस्थांसाठी)':
                up=lokshahir_sanstha.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='	संत रविदास पुरस्कार (संस्थांसाठी)':
                up=ravidas_sanstha.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='शाहू, फुले, आंबेडकर पारितोषिक':
                up=shahu_fule.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='मागासवर्गीय मुलां मुलींचे शासकीय वसतिगृह प्रवेश प्रक्रिया':
                up=magasvargiy_mula.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='डॉ. बाबासाहेब आंबेडकर सामाजिक न्याय प्राविण्य पुरस्कार राज्य स्तरीय विभाग स्तरीय पुरस्कार':
                up=pravinya_rajya.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='पद्मश्री कर्मवीर दादासाहेब गायकवाड पुरस्कार (संस्थांसाठी)':
                up=gayakvad.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='भारतरत्न डॉ. बाबासाहेब आंबेडकर स्वाधार योजना':
                up=swadhar_yoj.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='गटई कामगारांना पत्र्याचे स्टॉल देण्याची योजना':
                up=gatai_kamgar.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            # elif SchemeModel.objects.get(pk=pk).name=='महात्मा गांधी राष्ट्रीय ग्रामीण रोजगार हमी योजना':
            #     up=hami_yojna.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
            #     up.scheme_register=register_scheme
            #     up.save()
            elif SchemeModel.objects.get(pk=pk).name=='	शासकीय जिल्हा ग्रंथालय नागपूर (वैयक्तिक) सभासद होणे':
                up=vaiyaktik_sabhasad.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='	शासकीय जिल्हा ग्रंथालय नागपूर (संस्था) सभासद होणे':
                up=sanstha_sabhasad.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='मासेमारी साधनावर अर्थसहाय्य':
                up=masemari_arth.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='प्रधानमंत्री मत्स्यसंपदा (PMMSY)':
                up=matsyasampada.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अल्पसंख्याक समाजतील उमेदवारांसाठी सुधारित पोलीस भरती पूर्व परीक्षा प्रशिक्षण वर्ग':
                up=polis_bhartipurva.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='डॉ. झाकीर हुसेन मदरसा आधुनिकीकरण योजना':
                up=zakir_hus.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी क्षेत्र उप योजना MADA - पिकोफॉल - शिवणयंत्र':
                up=mada_shivnyantra.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी क्षेत्र उप योजना MADA - सायकल':
                up=mada_cycle.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='बालसंगोपन योजना':
                up=balsangopan.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='शुभमंगल सामुहिक विवाह योजना':
                up=shubh_vivah.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी क्षेत्र उप योजना OTSP - पिकोफॉल - शिवणयंत्र':
                up=otsp_shivnyantra.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी क्षेत्र उपाय योजना SCP - पिकोफॉल - शिवणयंत्र':
                up=scp_shivnyantra.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी क्षेत्र उपाय योजना TSP - पिकोफॉल - शिवणयंत्र':
                up=tsp_shivnyantra.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='	आदिवासी क्षेत्र उप योजना OTSP-सायकल':
                up=otsp_cycl.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी क्षेत्र उपयोजना SCP-सायकल':
                up=scp_cycl.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी क्षेत्र उपाय योजना TSP-सायकल':
                up=tsp_cycl.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अल्पसंख्या शाळांना पायाभूत सुविधा पुरवण्या बाबत':
                up=dharmik_alp.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='नवीन राष्ट्रीय बायोगॅस व सेंदीय खत व्यवस्थापन कार्यक्रम':
                up=navin_rashtriy.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='जमीन आरोग्य पत्रिका योजना':
                up=aarogya_patrika.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='पुण्यश्लोक अहिल्याबाई रोपवाटिका योजना':
                up=punyshlok_ahilya.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='जिल्हा उदयोग केंद्र कर्ज योजना':
                up=jilhaudyog.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='सुधारीत बीज भांडवल योजना':
                up=sudharitbij.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( DW ) अस्थिव्यंग व्यक्तीसाठी कृत्रिम अवयव पुरविणे':
                up=asthivyang_vyakti.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( DW ) कर्णबधिर व्यक्तीसाठी विविध प्रकारची वैयक्तिक श्रवणयंत्र पुरविणे':
                up=karnbadhir_vyakti.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( DW ) दिव्यांग व्यक्तींना स्वयंरोजगारासाठी झेरॉक्स मशीन पुरविणे १०० टक्के अनुदानावर':
                up=divyang_xerox.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( DW ) दिव्यांगांना संगणक प्रशिक्षण-व्यवसाय प्रशिक्षण देणे':
                up=divyang_sanganak.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( SW ) मागासवर्गीय महिलांना शिलाई मशीन पुरवणे':
                up=magas_shilai.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='दुभत्या जनावरांकरिता खाद्य उप्लब्धते करिता सुधारणा कार्यक्रम अंतर्गत १०० टक्के अनुदानावर वैरण बियाणे वाटप':
                up=dubhte_janawar.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसूचित जाती उपयोजना अंतर्गत लाभधारकांना ५0 टक्के अनुदानावर तेलंग विविध जातीच्या कोंबड्यांचे गट वाटप':
                up=anusuchit_50takke.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसूचित जाती उपायोजना अंतर्गत लाभधारकांना ७५ टक्के अनुदानावर दुधाळ जनावरांचे गट वाटप':
                up=anusuchit_janavare.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसूचित जाती उपायोजना अंतर्गत लाभधारकांना ७५ टक्के अनुदानावर शेळ्यांचे गट वाटप':
                up=anusuchit_shelya.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='ठक्कर बाप्पा आदिवासी वस्ती सुधारणा कार्यक्रम':
                up=thakkar.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसूचित जमातीच्या लाभार्थ्यांसाठी शबरी आदिवासी घरकुल योजना':
                up=anusuchit_shabri.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='भूमिहिन दारिद्रय रेषेखालील आदिवासींचे सबळीकरण व स्वाभिमान योजना':
                up=bhumihin_daridrya.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसूचित जमातीच्या सामुहिक विवाह सोहळ्यात सहभागी होणाऱ्या दाम्पत्याकरिता कन्यादान योजना':
                up=samuhik_vivah.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसुचित जमाती करीता स्वेच्छा संस्थाकडुन चालविल्या जाणाऱ्या आश्रमशाळा':
                up=anusuchit_swechha.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( DW ) दिव्यांग अव्यंग व्यक्तीच्या विवाहास प्रोत्साहन देण्यासाठी आर्थिक सहाय्याची योजना':
                up=divyang_avyang.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( DW ) दिव्यांग - दिव्यांग व्यक्तींना विवाहासाठी प्रोत्साहनापर अनुदान देणे':
                up=divyadivyang_anudan.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( DW ) स्वयंरोजगारासाठी दिव्यांग व्यक्तींना वित्तीय साहाय्य (बीजभांडवल)':
                up=swayamrojgar_divyang.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='( SW ) आंतर जातीय विवाह जोडप्यांना प्रोत्साहनपर आर्थिक अनुदान देणे':
                up=antarjatiy_vivah.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='अनुसूचित जमातीच्या मुला-मुलींना परदेशात शिक्षणासाठी शिष्यवृत्ती':
                up=anusuchit_scholar.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी विद्यार्थ्यांना शहरातील इंग्रजी माध्यमाच्या नामांकित निवासी शाळांमध्ये शिक्षण देणे':
                up=adivasividyarthi_engraji.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='आदिवासी विद्यार्थ्यांना सैनिकी शाळेमध्ये शिक्षण देण्यासाठी राज्यातील सैनिकी शाळेमध्ये शिक्षण सुरू करणे':
                up=sainikshala_adi.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='एकलव्य रेसिडेन्शियल पब्लिक स्कूल':
                up=eklavya_school.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='केंद्रवर्ती अर्थसंकल्प उत्पन्न व वैयक्तिक योजना':
                up=kendravarti_utpanna.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='केंद्रवर्ती अर्थसंकल्प प्रशिक्षणाच्या योजना':
                up=kendra_prashikshan.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='शासकीय आश्रमशाळा समूह':
                up=shaskiy_ashramshala.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='शासकीय पोस्टबेसिक आश्रमशाळेत व्यवसाय प्रशिक्षण केंद्र सुरू करणेबाबत':
                up=shaskiy_postbasic.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='किसान क्रेडिट कार्ड':
                up=kisan_credit.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='सिल्क समग्र योजना':
                up=silk_samagra.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='शुभमंगल नोंदणीकृत विवाह योजना':
                up=shubhmangal_nondni.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='कर्मवीर दादासाहेब गायकवाड सबळीकरण व स्वाभिमान योजना':
                up=kbg_sabalikaran.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='राजर्षी शाहू महाराज परदेशात शिष्यवृत्ती योजना':
                up=rajarshi_shahuscholar.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='मगांराग्रारोहयो (मनरेगा) योजना':
                up=mahatmagandhi_reshim.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
            elif SchemeModel.objects.get(pk=pk).name=='एकात्मीक दुग्ध विकास कार्यक्रम':
                up=ekatmik_dugdha.objects.filter(user=request.user, scheme=SchemeModel.objects.get(pk=pk)).first()
                up.scheme_register=register_scheme
                up.save()
         

        a=request.user.email

        # send_mail(
        #     "योजनेचा अर्ज",
        #     "Your Application has been submitted successfully.",
        #     settings.EMAIL_HOST_USER,
        #     [request.user.email],
        #     fail_silently=False,
        # )
        
        html_message = loader.render_to_string(
                                'web/mail_body.html',
                                {
                                    'name':request.user.name,
                                    'action': 'scheme_create',
                                    'scheme_name': register_scheme.scheme.name,
                                    'department_name': register_scheme.scheme.department.name,
                                }
                            )
        send_mail("योजनेचा अर्ज",None,settings.EMAIL_HOST_USER,[request.user.email],fail_silently=False,html_message=html_message)

     
        user=request.user
        ph = (str(user.mobile_number))[3:]
        print(ph)
        params = {
                    "user": "developer",
                    "password": 123456,
                    "msisdn": ph,
                    "sid": "SDCTEC",
                    "msg": "Your Application for the scheme has been submitted successfully !",
                    "fl": 0,
                    "gwid": 2
                }

        link = "http://bullet1.sdctechnologies.co.in:8080/vendorsms/pushsms.aspx"

        requests.get(link+"?"+encoder.urlencode(params))
        # # page = requests.get(link, verify=False)

        print("successfully msg sent")

        # send_mail(
        #     subject='Email Confirmation',
        #     message='Your Appication has been successfully submitted ',
        #     from_email='akash.malabadi@pixelstat.com',
        #     recipient_list=[a],
        #     fail_silently=False,
        # )
        SchemeRegistrationMediaService.handle_uploaded_in_memory_file(register_scheme=register_scheme, files=request.FILES)

        messages.success(request, 'अर्ज केल्याबद्दल धन्यवाद.')

        # print(a)


        print("successfully sent")
        return redirect('web:profile')


def scheme_registration_update(request, pk):
    context = dict()
    if request.method == 'GET':
        context["scheme"] = SchemeModel.objects.filter(id=pk).first()
        context['arza_document']=SchemeRegistrationMediaModel.arza
        documents= DocumentlinkModel.objects.filter(scheme=context["scheme"]).values()
        context["registration_media"] = documents
        context["doc_link"] = DocumentlinkModel.objects.filter(scheme__name=request.GET.get('scheme', None))
        return render(request, 'web/update_registration.html', context)
    else:
        register_scheme = SchemeRegistrationModel.objects.get(user=request.user, scheme=SchemeModel.objects.get(pk=pk))
        SchemeRegistrationMediaModel.objects.filter(scheme_registration=register_scheme).delete()
        print("Working right")
        register_scheme.status = SchemeRegistrationModel.PENDING
        register_scheme.save()
        a=request.user.email

        # send_mail(
        #     "योजनेचा अर्ज",
        #     "Your Application has been submitted successfully.",
        #     settings.EMAIL_HOST_USER,
        #     [request.user.email],
        #     fail_silently=False,
        # )
        user=request.user
        # ph = (str(user.mobile_number))[3:]
        # print(ph)
        # params = {
        #             "user": "developer",
        #             "password": 123456,
        #             "msisdn": ph,
        #             "sid": "SDCTEC",
        #             "msg": "Your Application has submitted successfully !",
        #             "fl": 0,
        #             "gwid": 2
        #         }

        # link = "http://bullet1.sdctechnologies.co.in:8080/vendorsms/pushsms.aspx"


        # requests.get(link+"?"+encoder.urlencode(params))

        print("successfully msg sent")

        # send_mail(
        #     subject='Email Confirmation',
        #     message='Your Appication has been successfully submitted ',
        #     from_email='akash.malabadi@pixelstat.com',
        #     recipient_list=[a],
        #     fail_silently=False,
        # )
        SchemeRegistrationMediaService.handle_uploaded_in_memory_file(register_scheme=register_scheme,
                                                                      files=request.FILES)
        messages.success(request, 'Application request received.')
        print("successfully sent")
        return redirect('web:profile')

@login_required()
def profile(request):
    if request.method=="GET":
        context = dict()
        # context["scheme_registration"] = SchemeRegistrationModel.objects.filter(scheme__name=request.GET.get('scheme_registration', None))
        context['documents']= User_documents.objects.filter(user=request.user)
        context["scheme_name"] = SchemeRegistrationModel.objects.filter(scheme=request.GET.get('scheme_registration', None))
    else:
        try:
            context = dict()
        # context["scheme_registration"] = SchemeRegistrationModel.objects.filter(scheme__name=request.GET.get('scheme_registration', None))
            context['documents']= User_documents.objects.filter(user=request.user)
            context["scheme_name"] = SchemeRegistrationModel.objects.filter(scheme=request.GET.get('scheme_registration', None))

            name=request.POST.get('name')
            file=request.FILES.get('file')
            print(file)
            user=request.user
            obj=User_documents(user=user,document_name=name,document=file)
            obj.save()
        except:
            pass
        return HttpResponseRedirect(reverse("web:profile"))
    return render(request=request, template_name='web/profile.html', context=context)

@login_required()
def applied_schemes(request):
    context = dict()
    # context["scheme_registration"] = SchemeRegistrationModel.objects.filter(scheme__name=request.GET.get('scheme_registration', None))
    context["scheme_name"] = SchemeRegistrationModel.objects.filter(scheme=request.GET.get('scheme_registration', None))
    return render(request=request, template_name='web/applied_schemes.html', context=context)

def sign_in(request):
    context = dict()
    if request.method == 'GET':
        return render(request=request, template_name='web/sign_in.html', context=context)
    else:
        captcha_token=request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LddL5sfAAAAADA9OwJI0bY5Fl1Lc9JV62Qy9r1t"
        cap_data={"secret":cap_secret,"response":captcha_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)
        if cap_json['success']==False:
            messages.error(request,"Invalid Captcha Try Again")
            return redirect("web:sign_in")

    if request.method == 'POST':
        user_id = request.POST.get('mobile_number', None)
        password = request.POST.get('password', None)
        print(user_id,password)
        user = authenticate(mobile_number = user_id,password=password)

        if user is not None:
            dj_login(request, user)
            if request.user.role == "User":
                redirect_url = request.GET.get("next", settings.LOGIN_REDIRECT_URL)
                if not redirect_url:
                    redirect_url = settings.LOGIN_REDIRECT_URL
                return redirect(redirect_url)
            elif request.user.role == "Master collector dpo":
                return redirect("web:master_stats")
            else:

                return redirect("web:depart_1_stats")

        else:
            message = '*Username or password is incorrect'
            context['message'] = message
            # messages.info(request,'Username or password is incorrect')
            return render(request=request, template_name='web/sign_in.html', context=context)


def sign_in_dpo(request):
    context = dict()
    context["role"] = "DPO"
    if request.method == 'GET':
        return render(request=request, template_name='web/sign_in_dpo.html', context=context)
    elif request.method == 'POST':
        user_id = request.POST.get('mobile_number', None)
        password = request.POST.get('password', None)
        print(user_id,password)
        user = authenticate(mobile_number = user_id,password=password)
        if user is not None:
            dj_login(request, user)
            if request.user.role == "User":
                return HttpResponse("<center>404</center>")
            elif request.user.role == "Master collector dpo":
                redirect_url = "web:master_stats"
                return redirect(redirect_url)
            elif request.user.role == "Department admin hod":
                redirect_url = "web:depart_dashboard"
                return redirect(redirect_url)
            elif request.user.role == "Department clerk 1":
                redirect_url = "web:depart_dashboard"
                return redirect(redirect_url)
            else:
                return redirect(reverse("web:depart_1_stats"))
        else:
            message = '*Mobile Number or password is incorrect'
            context['message'] = message
            return render(request=request, template_name='web/sign_in_dpo.html', context=context)

def sign_out_dpo(request):
    dj_logout(request)
    return redirect(reverse('web:sign_dpo'))


def sign_out(request):
    dj_logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


def mobile_verification(request):
    context = dict()
    if request.method == 'GET':
        sms_service_init = SmsService(service_id=settings.TWILIO_NUMBER_VERIFICATION_SERVICE_SID)
        sms_service_init.send_otp(mobile_number=request.user.mobile_number.as_e164)
        return render(request=request, template_name='web/mobile_verification.html', context=context)
    elif request.method == 'POST':
        otp = request.POST.get('otp', None)
        sms_service_init = SmsService(service_id=settings.TWILIO_NUMBER_VERIFICATION_SERVICE_SID)
        is_verified = sms_service_init.verify_otp(mobile_number=request.user.mobile_number.as_e164, otp=otp)
        if is_verified:
            user = request.user
            user.mobile_number_verified_at = timezone.now()
            user.save()
        else:
            pass
        return redirect('web:home')


@login_required()
def department_admin(request):
    context = dict()
    message = "successfully submitted"
    user = request.POST.get('user', None)
    # scheme_name = SchemeRegistrationModel.objects.all()
    # context["scheme_registration"] = SchemeRegistrationModel.objects.filter(scheme__name=request.GET.get('scheme_registration', None))
    scheme_name = SchemeRegistrationModel.objects.all()
    #print(scheme_name)
    return render(request, 'web/department_admin2.html',{'scheme_name': scheme_name})

@login_required()
def department_admin(request):
    context = dict()
    message = "successfully submitted"
    user = request.POST.get('user', None)
    # scheme_name = SchemeRegistrationModel.objects.all()
    # context["scheme_registration"] = SchemeRegistrationModel.objects.filter(scheme__name=request.GET.get('scheme_registration', None))
    scheme_name = SchemeRegistrationModel.objects.all()
    print(scheme_name)
    return render(request, 'web/department_admin.html',{'scheme_name': scheme_name})


@login_required()
def department_admin1(request):
    context = dict()
    message = "successfully submitted"
    user = request.POST.get('user', None)
    scheme_name = SchemeRegistrationModel.objects.all()
    context["scheme_registration"] = SchemeRegistrationModel.objects.filter(scheme__name=request.GET.get('scheme_registration', None))
    scheme_name = SchemeRegistrationModel.objects.all()
    department_name = DepartmentModel.objects.all()
    print(department_name)
    print(scheme_name)
    return render(request, 'web/DPO_scheme.html',{'scheme_name': scheme_name})


@login_required()
def department_admin(request):
    context = dict()
    message = "successfully submitted"
    user = request.POST.get('user', None)
    # scheme_name = SchemeRegistrationModel.objects.all()
    # context["scheme_registration"] = SchemeRegistrationModel.objects.filter(scheme__name=request.GET.get('scheme_registration', None))
    # scheme_name = SchemeRegistrationModel.objects.all()
    department_name = DepartmentModel.objects.all()
    # department_count = DepartmentModel.objects.all().annotate(count=Count('schemes'))
    # print(department_name)
    # print(department_count)
    # print(scheme_name)
    return render(request, 'web/department_admin.html',{'department_name': department_name})

@login_required()
def view_document(request):
    if request.method ==  'GET':
        documents = SchemeRegistrationMediaModel.objects.filter(scheme_registration__in = (SchemeRegistrationModel.objects.filter(user=request.user))).values('category','file_path','arza')

        for i in documents:
            if i['arza'] != '':
                x = i["arza"]
                i['arza'] = f"{request.scheme}://{request.get_host()}/media/{x}"
                print('arza', i['arza'])
            else:
                x = i["file_path"]
                i['file_path'] = f"{request.scheme}://{request.get_host()}/media/{x}"
                print('file',i['file_path'])

        return render(request,'web/user_documents.html',{'docs':documents})


def Department_Clerk_1_view(request):
        context = []
        counter=1
        print(request.user)
        if request.user.subdepartment :

            schemes = SchemeModel.objects.filter(subdepartment = request.user.subdepartment)
        else:
            schemes = SchemeModel.objects.filter(department = request.user.department)

        for i in schemes:
            dic = {}
            dic['scheme_id']=i.id
            dic["scheme_name"] = i.name
            dic['sr_no']=counter
            dic["schemes_user"] = SchemeRegistrationModel.objects.filter(scheme = i).count()
            dic["schemes_pending"] = SchemeRegistrationModel.objects.filter(status = "Pending",scheme = i).count()
            dic["schemes_in_progress"] = SchemeRegistrationModel.objects.filter(status = "In Progress",scheme = i).count()
            dic["schemes_verified"] = SchemeRegistrationModel.objects.filter(status = "Verified",scheme = i).count()

            dic["schemes_approved"] = SchemeRegistrationModel.objects.filter(status = "Approved",scheme = i).count()
            dic["schemes_rejected"] = SchemeRegistrationModel.objects.filter(status = "Rejected",scheme = i).count()
            dic["schemes_labharthi"] = SchemeRegistrationModel.objects.filter(status = "Labarthi",scheme = i).count()
            context.append(dic)
            print(dic)
            counter+=1
        return render(request,"web/department_clerk_1_stats.html",{"context":context})


def Department_clerk_1_scheme(request, scheme=None):
    counter=1
    context=[]
    users = SchemeRegistrationModel.objects.filter(scheme=SchemeModel.objects.get(id=scheme))
    # if request.user.role=='Department clerk 2':
    #     users= users.filter(status="Approved")
    #     print(users.values())
    if users.count() > 0:
        for i in users:
            try:
                dic={}
                dic['sr_no']=counter
                dic['pk'] = i.user.id
                dic['application_id']=i.application_id
                dic['created_at']=i.created_at.strftime('%d %b %Y')
                dic['caste']=i.user.caste
                dic['applicant_name']=i.user.name
                dic['scheme_name']=i.scheme.name
                dic['status']= i.status
                dic['raised_query']= i.raised_query
                dic['hod_query']= i.hod_query
                dic['scheme_id']= i.scheme.id
                context.append(dic)
                counter+=1
            except Exception as e:
                print(e)
    # else:
        # return HttpResponse("<center><h2>NO DATA PRESENT FOR NOW</center></h2>")
    return render(request,"web/department_clerk_1.html",{"context":context,"scheme":scheme})

def user_details_verification(request,pk,scheme_name):

    if request.user.role == "Department clerk 1" and request.method == "POST":
        query = request.POST.get("query",None)

        print(query)
        if query!='':
            scheme = SchemeRegistrationModel.objects.get(user = UserModel.objects.get(pk=pk),scheme=SchemeModel.objects.get(pk=scheme_name))
            scheme.raised_query = query
            scheme.status = "In Progress"
            scheme.save()
            html_message = loader.render_to_string(
                                'web/mail_body.html',
                                {
                                    'name': UserModel.objects.get(pk=pk).name,
                                    'action': 'que',
                                    'scheme_name': scheme.scheme.name,
                                    'department_name': scheme.scheme.department.name,
                                    'reason': scheme.raised_query,
                                    
                                }
                            )
            send_mail("Raise Query:-BANY::Support. तुमचा अर्ज परत करण्यात आला आहे",None,settings.EMAIL_HOST_USER,[UserModel.objects.get(pk=pk).email],fail_silently=False,html_message=html_message)
            

        else:
            scheme = SchemeRegistrationModel.objects.get(user = UserModel.objects.get(pk=pk),scheme=SchemeModel.objects.get(pk=scheme_name))

            scheme.status = "Verified"
            scheme.save()
            html_message = loader.render_to_string(
                                'web/mail_body.html',
                                {
                                    'name': UserModel.objects.get(pk=pk).name,
                                    'action': 'ver',
                                    'scheme_name': scheme.scheme.name,
                                    'department_name': scheme.scheme.department.name,
                                    'reason': scheme.raised_query,
                                }
                            )
            send_mail("Verified:-BANY::Congratulations.",None,settings.EMAIL_HOST_USER,[UserModel.objects.get(pk=pk).email],fail_silently=False,html_message=html_message)


        return redirect("web:depart_1_stats")
    elif request.user.role == "Department admin hod" and request.method == "POST":
        rejected=request.POST.get("rejected",None)
        hod_query = request.POST.get("query",None)
        print('hi ',hod_query)
        if rejected!='':
            scheme = SchemeRegistrationModel.objects.get(user = UserModel.objects.get(pk=pk),scheme=SchemeModel.objects.get(pk=scheme_name))
            scheme.raised_query = rejected
            scheme.status = "Rejected"
            scheme.save()
            html_message = loader.render_to_string(
                                'web/mail_body.html',
                                {
                                    'name': UserModel.objects.get(pk=pk).name,
                                    'action': 'rej',
                                    'scheme_name': scheme.scheme.name,
                                    'department_name': scheme.scheme.department.name,
                                    'reason': scheme.raised_query,
                                }
                            )
            send_mail("Rejected:-BANY::Sorry. तुमचा अर्ज नाकारण्यात आला आहे",None,settings.EMAIL_HOST_USER,[UserModel.objects.get(pk=pk).email],fail_silently=False,html_message=html_message)

        elif hod_query!='':
            scheme = SchemeRegistrationModel.objects.get(user = UserModel.objects.get(pk=pk),scheme=SchemeModel.objects.get(pk=scheme_name))
            scheme.status = "In Progress"
            scheme.hod_query=hod_query
            scheme.save()


        else:
            scheme = SchemeRegistrationModel.objects.get(user = UserModel.objects.get(pk=pk),scheme=SchemeModel.objects.get(pk=scheme_name))
            scheme.status = "Approved"
            scheme.save()
            html_message = loader.render_to_string(
                                'web/mail_body.html',
                                {
                                    'name': UserModel.objects.get(pk=pk).name,
                                    'action': 'apr',
                                    'scheme_name': scheme.scheme.name,
                                    'department_name': scheme.scheme.department.name,
                                }
                            )
            send_mail("Approved:-BANY::Congratulations. तुमचा अर्ज मंजूर करण्यात आला आहे",None,settings.EMAIL_HOST_USER,[UserModel.objects.get(pk=pk).email],fail_silently=False,html_message=html_message)
            
        return redirect("web:depart_1_stats")
    elif (request.user.role == "Department clerk 2" )  and request.method == "POST":


        cheque = request.FILES.get("cheque",None)
        if cheque:
            scheme = SchemeRegistrationModel.objects.get(user = UserModel.objects.get(pk=pk),scheme=SchemeModel.objects.get(pk=scheme_name))
            scheme.cheque_letter = cheque
            scheme.status = "Labarthi"
            scheme.save()

        else:

            send_mail(
            "Letter of Invitation",
            request.POST.get('mail'),
            settings.EMAIL_HOST_USER,
            [UserModel.objects.get(pk=pk).email],
            fail_silently=True,

        )



        return redirect("web:depart_1_stats")

    elif request.method == "GET":
        context = {}
        context['scheme_media'] = SchemeRegistrationMediaModel.objects.filter(scheme_registration = SchemeRegistrationModel.objects.get(user = UserModel.objects.get(pk=pk),scheme = SchemeModel.objects.get(pk = scheme_name) )).values('file_path')
        context['user_data'] = UserModel.objects.get(pk=pk)
        if SchemeModel.objects.get(pk=scheme_name).name == "RPL (Recognition of Prior Learning ) आधिच कौशल्य विकास प्रशिक्षण प्राप्त केलेल्या उमेदवारांना प्रमाणपत्राचे वितरण":
            context['up']=upajivikesathi.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "SANKALP - उपजिविकेसाठी कौशल्य संपादन व ज्ञान जागरुकता अभियान":
            context['up']=sankalp_skill.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "जिल्हा पुरस्कृत योजना (DPDC) (जिल्हास्तरीय योजना- जिल्हा नियोजन समिती पुरस्कृत)":
            context['up']=jilha_pur.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "दीनदयाल अंत्योदय योजना- राष्ट्रीय नागरी उपजिवीका अभियान (DAY - NULM)":
            context['up']=din_dayal.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "प्रधानमंत्री कौशल्य विकास योजना (PMKVY ३.0) (केंद्रशासन पुरस्कृत)":
            context['up']=pra_dhan.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "प्रमोद महाजन कौशल्य व उद्योजकता विकास अभियान (PMKUVA) (राज्यशासन पुरस्कृत)":
            context['up']=pramod_mah.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( DW ) अंध व्यक्तींसाठी साहाय्य भूत साधने व उपकरणांसाठी अर्थसहाय्य करणे":
            context['up']=andh_vyaktinsathi.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसूचित जाती व नवबौध्द घटकांसाठी रमाई घरकुल योजना":
            context['up']=ramai_gharkul.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसूचित जाती व नवबौद्ध घटकांच्या बचत गटांकरीता मिनी ट्रॅक्टरचा पुरवठा योजना":
            context['up']=mini_tra.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "भारतरत्न डॉ. बाबासाहेब आंबेडकर समाज भूषणपुरस्कार (व्यत्कींसाठी)":
            context['up']=vyaktinsathi.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "साहित्यरत्न लोकशाहीर अण्णाभाऊ साठे पुरस्कार (व्यत्कींसाठी)":
            context['up']=lokshahir.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "संत रविदास पुरस्कार (व्यत्कींसाठी)":
            context['up']=ravidas.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "पद्मश्री कर्मवीर दादासाहेब गायकवाड पुरस्कार (व्यत्कींसाठी)":
            context['up']=karmavir.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "भारतरत्न डॉ. बाबासाहेब आंबेडकर समाज भूषणपुरस्कार (संस्थांसाठी)":
            context['up']=bharat_sanstha.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "साहित्यरत्न लोकशाहीर अण्णाभाऊ साठे पुरस्कार (संस्थांसाठी)":
            context['up']=lokshahir_sanstha.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "शाहू, फुले, आंबेडकर पारितोषिक":
            context['up']=shahu_fule.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "मागासवर्गीय मुलां मुलींचे शासकीय वसतिगृह प्रवेश प्रक्रिया":
            context['up']=magasvargiy_mula.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "डॉ. बाबासाहेब आंबेडकर सामाजिक न्याय प्राविण्य पुरस्कार राज्य स्तरीय विभाग स्तरीय पुरस्कार":
            context['up']=pravinya_rajya.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "भारतरत्न डॉ. बाबासाहेब आंबेडकर स्वाधार योजना":
            context['up']=swadhar_yoj.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "संत रविदास पुरस्कार (संस्थांसाठी)":
            context['up']=ravidas_sanstha.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "पद्मश्री कर्मवीर दादासाहेब गायकवाड पुरस्कार (संस्थांसाठी)":
            context['up']=gayakvad.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "गटई कामगारांना पत्र्याचे स्टॉल देण्याची योजना":
            context['up']=gatai_kamgar.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        # elif SchemeModel.objects.get(pk=scheme_name).name == "महात्मा गांधी राष्ट्रीय ग्रामीण रोजगार हमी योजना":
        #     context['up']=hami_yojna.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "शासकीय जिल्हा ग्रंथालय नागपूर (वैयक्तिक) सभासद होणे":
            context['up']=vaiyaktik_sabhasad.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "शासकीय जिल्हा ग्रंथालय नागपूर (संस्था) सभासद होणे":
            context['up']=sanstha_sabhasad.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "मासेमारी साधनावर अर्थसहाय्य":
            context['up']=masemari_arth.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "प्रधानमंत्री मत्स्यसंपदा (PMMSY)":
            context['up']=matsyasampada.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अल्पसंख्याक समाजतील उमेदवारांसाठी सुधारित पोलीस भरती पूर्व परीक्षा प्रशिक्षण वर्ग":
            context['up']=polis_bhartipurva.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "डॉ. झाकीर हुसेन मदरसा आधुनिकीकरण योजना":
            context['up']=zakir_hus.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी क्षेत्र उप योजना MADA - पिकोफॉल - शिवणयंत्र":
            context['up']=mada_shivnyantra.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी क्षेत्र उप योजना MADA - सायकल":
            context['up']=mada_cycle.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "बालसंगोपन योजना":
            context['up']=balsangopan.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "शुभमंगल सामुहिक विवाह योजना":
            context['up']=shubh_vivah.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी क्षेत्र उप योजना OTSP - पिकोफॉल - शिवणयंत्र":
            context['up']=otsp_shivnyantra.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी क्षेत्र उपाय योजना SCP - पिकोफॉल - शिवणयंत्र":
            context['up']=scp_shivnyantra.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी क्षेत्र उपाय योजना TSP - पिकोफॉल - शिवणयंत्र":
            context['up']=tsp_shivnyantra.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी क्षेत्र उप योजना OTSP-सायकल":
            context['up']=otsp_cycl.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी क्षेत्र उपयोजना SCP-सायकल":
            context['up']=scp_cycl.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी क्षेत्र उपाय योजना TSP-सायकल":
            context['up']=tsp_cycl.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अल्पसंख्या शाळांना पायाभूत सुविधा पुरवण्या बाबत":
            context['up']=dharmik_alp.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "नवीन राष्ट्रीय बायोगॅस व सेंदीय खत व्यवस्थापन कार्यक्रम":
            context['up']=navin_rashtriy.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "जमीन आरोग्य पत्रिका योजना":
            context['up']=aarogya_patrika.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "पुण्यश्लोक अहिल्याबाई रोपवाटिका योजना":
            context['up']=punyshlok_ahilya.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "जिल्हा उदयोग केंद्र कर्ज योजना":
            context['up']=jilhaudyog.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "सुधारीत बीज भांडवल योजना":
            context['up']=sudharitbij.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( DW ) अस्थिव्यंग व्यक्तीसाठी कृत्रिम अवयव पुरविणे":
            context['up']=asthivyang_vyakti.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( DW ) कर्णबधिर व्यक्तीसाठी विविध प्रकारची वैयक्तिक श्रवणयंत्र पुरविणे":
            context['up']=karnbadhir_vyakti.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( DW ) दिव्यांग व्यक्तींना स्वयंरोजगारासाठी झेरॉक्स मशीन पुरविणे १०० टक्के अनुदानावर":
            context['up']=divyang_xerox.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( DW ) दिव्यांगांना संगणक प्रशिक्षण-व्यवसाय प्रशिक्षण देणे":
            context['up']=divyang_sanganak.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( SW ) मागासवर्गीय महिलांना शिलाई मशीन पुरवणे":
            context['up']=magas_shilai.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "दुभत्या जनावरांकरिता खाद्य उप्लब्धते करिता सुधारणा कार्यक्रम अंतर्गत १०० टक्के अनुदानावर वैरण बियाणे वाटप":
            context['up']=dubhte_janawar.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसूचित जाती उपयोजना अंतर्गत लाभधारकांना ५0 टक्के अनुदानावर तेलंग विविध जातीच्या कोंबड्यांचे गट वाटप":
            context['up']=anusuchit_50takke.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसूचित जाती उपायोजना अंतर्गत लाभधारकांना ७५ टक्के अनुदानावर दुधाळ जनावरांचे गट वाटप":
            context['up']=anusuchit_janavare.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसूचित जाती उपायोजना अंतर्गत लाभधारकांना ७५ टक्के अनुदानावर शेळ्यांचे गट वाटप":
            context['up']=anusuchit_shelya.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "ठक्कर बाप्पा आदिवासी वस्ती सुधारणा कार्यक्रम":
            context['up']=thakkar.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसूचित जमातीच्या लाभार्थ्यांसाठी शबरी आदिवासी घरकुल योजना":
            context['up']=anusuchit_shabri.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "भूमिहिन दारिद्रय रेषेखालील आदिवासींचे सबळीकरण व स्वाभिमान योजना":
            context['up']=bhumihin_daridrya.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसूचित जमातीच्या सामुहिक विवाह सोहळ्यात सहभागी होणाऱ्या दाम्पत्याकरिता कन्यादान योजना":
            context['up']=samuhik_vivah.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसुचित जमाती करीता स्वेच्छा संस्थाकडुन चालविल्या जाणाऱ्या आश्रमशाळा":
            context['up']=anusuchit_swechha.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( DW ) दिव्यांग अव्यंग व्यक्तीच्या विवाहास प्रोत्साहन देण्यासाठी आर्थिक सहाय्याची योजना":
            context['up']=divyang_avyang.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( DW ) दिव्यांग - दिव्यांग व्यक्तींना विवाहासाठी प्रोत्साहनापर अनुदान देणे":
            context['up']=divyadivyang_anudan.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( DW ) स्वयंरोजगारासाठी दिव्यांग व्यक्तींना वित्तीय साहाय्य (बीजभांडवल)":
            context['up']=swayamrojgar_divyang.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "( SW ) आंतर जातीय विवाह जोडप्यांना प्रोत्साहनपर आर्थिक अनुदान देणे":
            context['up']=antarjatiy_vivah.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "अनुसूचित जमातीच्या मुला-मुलींना परदेशात शिक्षणासाठी शिष्यवृत्ती":
            context['up']=anusuchit_scholar.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी विद्यार्थ्यांना शहरातील इंग्रजी माध्यमाच्या नामांकित निवासी शाळांमध्ये शिक्षण देणे":
            context['up']=adivasividyarthi_engraji.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "आदिवासी विद्यार्थ्यांना सैनिकी शाळेमध्ये शिक्षण देण्यासाठी राज्यातील सैनिकी शाळेमध्ये शिक्षण सुरू करणे":
            context['up']=sainikshala_adi.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "एकलव्य रेसिडेन्शियल पब्लिक स्कूल":
            context['up']=eklavya_school.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "केंद्रवर्ती अर्थसंकल्प उत्पन्न व वैयक्तिक योजना":
            context['up']=kendravarti_utpanna.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "केंद्रवर्ती अर्थसंकल्प प्रशिक्षणाच्या योजना":
            context['up']=kendra_prashikshan.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "शासकीय आश्रमशाळा समूह":
            context['up']=shaskiy_ashramshala.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "शासकीय पोस्टबेसिक आश्रमशाळेत व्यवसाय प्रशिक्षण केंद्र सुरू करणेबाबत":
            context['up']=shaskiy_postbasic.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "किसान क्रेडिट कार्ड":
            context['up']=kisan_credit.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "सिल्क समग्र योजना":
            context['up']=silk_samagra.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "शुभमंगल नोंदणीकृत विवाह योजना":
            context['up']=shubhmangal_nondni.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "कर्मवीर दादासाहेब गायकवाड सबळीकरण व स्वाभिमान योजना":
            context['up']=kbg_sabalikaran.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "राजर्षी शाहू महाराज परदेशात शिष्यवृत्ती योजना":
            context['up']=rajarshi_shahuscholar.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "मगांराग्रारोहयो (मनरेगा) योजना":
            context['up']=mahatmagandhi_reshim.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        elif SchemeModel.objects.get(pk=scheme_name).name == "एकात्मीक दुग्ध विकास कार्यक्रम":
            context['up']=ekatmik_dugdha.objects.filter(user=UserModel.objects.get(pk=pk), scheme=SchemeModel.objects.get(pk=scheme_name)).first()
        
        
        context['scheme']=SchemeModel.objects.get(pk=scheme_name)
        context['documents']= SchemeRegistrationMediaModel.objects.filter(scheme_registration= SchemeRegistrationModel.objects.get(user=context['user_data'], scheme=context['scheme']))
        context['is_arza']=0
        for xxx in context['documents']:
            if xxx.arza is not None:
                context['is_arza']=1
        context['status']=SchemeRegistrationModel.objects.get(user=context['user_data'], scheme=context['scheme']).status
        context['External_ID']=SchemeRegistrationModel.objects.get(user=context['user_data'], scheme=context['scheme'])
        print(context['user_data'].mobile_number)
        return render(request,"web/user_details_check.html",context)

def master_stats(request):
    departments = DepartmentModel.objects.all()
    context = []

    for dep in departments:
        temp = {}
        temp['name'] = dep.name
        temp['id'] = dep.id
        temp['schemes'] = SchemeModel.objects.filter(department=dep.id).count()
        applicants = SchemeRegistrationModel.objects.filter(scheme__department=dep.id)
        temp['applicants'] = applicants.count()
        temp['pending'] = applicants.filter(status='Pending').count()
        temp['progress'] = applicants.filter(status='In Progress').count()
        temp['verified'] = applicants.filter(status='Verified').count()
        temp['approved'] = applicants.filter(status='Approved').count()
        temp['rejected'] = applicants.filter(status='Rejected').count()
        temp['labarthi'] = applicants.filter(status='Labarthi').count()
        context.append(temp)
    return render(request, 'web/master/stats.html', {'context': context})


def master_stats_department(request, department):
    context = []
    schemes = SchemeModel.objects.filter(department__pk=department)

    for scheme in schemes:
        temp = {}
        temp['name'] = scheme.name
        temp['id'] = scheme.id
        applicants = SchemeRegistrationModel.objects.filter(scheme=scheme.id)
        temp['applicants'] = applicants.count()
        temp['pending'] = applicants.filter(status='Pending').count()
        temp['progress'] = applicants.filter(status='In Progress').count()
        temp['approved'] = applicants.filter(status='Approved').count()
        temp['verified'] = applicants.filter(status='Verified').count()
        temp['rejected'] = applicants.filter(status='Rejected').count()
        temp['labarthi'] = applicants.filter(status='Labarthi').count()
        context.append(temp)

    return render(request, 'web/master/department_stats.html', {'context': context, 'id': department})

def master_stats_scheme(request, department, scheme):
    applications = SchemeRegistrationModel.objects.filter(scheme__id=scheme)
    return render(request, 'web/master/scheme_stats.html', {'applications': applications, 'scheme': SchemeModel.objects.get(id=scheme), 'department': DepartmentModel.objects.get(id=department)})

def search_applicant(request,scheme=None):
    context = []
    if request.method == "GET":
        users = SchemeRegistrationModel.objects.filter(scheme=SchemeModel.objects.get(id=scheme))
        a = []
        for i in users:
            a.append(i.user.id)
        if 'term' in request.GET:
            user_name = UserModel.objects.filter(id__in = a)
            user_name = user_name.filter(name__istartswith = request.GET['term'])
            print(user_name)
            c = 6
            names = []
            for i in user_name:
                names.append(i.name)
                c-=1
                if c==0:  break
            return JsonResponse(names,safe=False)
        x = request.GET.get('search_app')
        z = UserModel.objects.filter(id__in = a)
        z = z.filter(name = x).values()
        if request.user.role=='Department clerk 2':
            z= z.filter(status="Approved")
        if z.count() > 0:
            counter = 1
            for i in z:
                tt = SchemeRegistrationModel.objects.get(scheme=SchemeModel.objects.get(id=scheme),user=UserModel.objects.get(id = i['id']))
                try:
                    dic={}
                    dic['sr_no']=counter
                    dic['pk'] = i['id']
                    dic['application_id'] = tt.application_id
                    dic['created_at'] = tt.created_at.strftime('%d %b %Y')
                    dic['applicant_name']=i['name']
                    dic['scheme_name']=tt.scheme.name
                    dic['status']= tt.status
                    dic['raised_query']= tt.raised_query
                    dic['hod_query']= tt.hod_query
                    dic['scheme_id']= tt.scheme.id
                    context.append(dic)
                    counter+=1
                except Exception as e:
                    print(e)
        else:
            return HttpResponse("<center><h2>NO DATA PRESENT FOR NOW</center></h2>")
        print("HELLO",context)
        return render(request,"web/department_clerk_1.html",{"context":context,"scheme":scheme})

def kaushalya_vibhag(request,pk):
    print('hi')
    if upajivikesathi.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = upajivikesathi.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.umedwar_name=request.POST.get('umedwar_name'),
        x.rahivasi=request.POST.get('rahivasi'),
        x.kau_prashikshan=request.POST.get('kau_prashikshan'),
        x.second_name=request.POST.get('second_name'),
        x.fa_name=request.POST.get('fa_name'),
        x.birth_date=request.POST.get('birth_date'),
        x.paripurn_patta=request.POST.get('paripurn_patta'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.adhaar_no=request.POST.get('adhaar_no'),
        x.gender = request.POST.get('gender'),
        x.education = request.POST.get('education'),
        x.shakha=request.POST.get('shakha'),
        x.dharma = request.POST.get('dharma'),
        x.jat = request.POST.get('jat'),
        x.pravarg=request.POST.get('pravarg'),
        x.prashikshan = request.POST.get('prashikshan'),
        x.prashikshan1 = request.POST.get('prashikshan1'),
        x.prashikshan2 = request.POST.get('prashikshan2'),
        x.course_prashikshan=request.POST.get('course_prashikshan'),
        x.course_prashikshan1=request.POST.get('course_prashikshan1'),
        x.course_prashikshan2=request.POST.get('course_prashikshan2'),
        x.vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        x.signature = request.FILES.get('signature')
        # x.umedwar_sign=request.FILES.get('umedwar_sign')
        x.save()
    else:
        x= upajivikesathi(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        umedwar_name=request.POST.get('umedwar_name'),
        second_name=request.POST.get('second_name'),
        fa_name=request.POST.get('fa_name'),
        rahivasi=request.POST.get('rahivasi'),
        kau_prashikshan=request.POST.get('kau_prashikshan'),
        birth_date=request.POST.get('birth_date'),
        paripurn_patta=request.POST.get('paripurn_patta'),
        mobile_number=request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        adhaar_no=request.POST.get('adhaar_no'),
        gender = request.POST.get('gender'),
        education = request.POST.get('education'),
        shakha=request.POST.get('shakha'),
        dharma = request.POST.get('dharma'),
        jat = request.POST.get('jat'),
        pravarg=request.POST.get('pravarg'),
        prashikshan = request.POST.get('prashikshan'),
        prashikshan1 = request.POST.get('prashikshan1'),
        prashikshan2 = request.POST.get('prashikshan2'),
        course_prashikshan=request.POST.get('course_prashikshan'),
        course_prashikshan1=request.POST.get('course_prashikshan1'),
        course_prashikshan2=request.POST.get('course_prashikshan2'),
        vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        signature = request.FILES.get('signature')
        # umedwar_sign=request.FILES.get('umedwar_sign')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def sankalpp(request,pk):
    print('hi')
    if sankalp_skill.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = sankalp_skill.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.umedwar_name=request.POST.get('umedwar_name'),
        x.rahivasi=request.POST.get('rahivasi'),
        x.kau_prashikshan=request.POST.get('kau_prashikshan'),
        x.second_name=request.POST.get('second_name'),
        x.fa_name=request.POST.get('fa_name'),
        x.birth_date=request.POST.get('birth_date'),
        x.paripurn_patta=request.POST.get('paripurn_patta'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.adhaar_no=request.POST.get('adhaar_no'),
        x.gender = request.POST.get('gender'),
        x.education = request.POST.get('education'),
        x.shakha=request.POST.get('shakha'),
        x.dharma = request.POST.get('dharma'),
        x.jat = request.POST.get('jat'),
        x.pravarg=request.POST.get('pravarg'),  
        x.prashikshan = request.POST.get('prashikshan'),
        x.prashikshan1 = request.POST.get('prashikshan1'),
        x.prashikshan2 = request.POST.get('prashikshan2'),
        x.course_prashikshan=request.POST.get('course_prashikshan'),
        x.course_prashikshan1=request.POST.get('course_prashikshan1'),
        x.course_prashikshan2=request.POST.get('course_prashikshan2'),
        x.vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        x.magas= request.POST.get('magas'),
        x.save()
    else:
        x= sankalp_skill(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        umedwar_name=request.POST.get('umedwar_name'),
        rahivasi=request.POST.get('rahivasi'),
        kau_prashikshan=request.POST.get('kau_prashikshan'),
        second_name=request.POST.get('second_name'),
        fa_name=request.POST.get('fa_name'),
        birth_date=request.POST.get('birth_date'),
        paripurn_patta=request.POST.get('paripurn_patta'),
        mobile_number=request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        adhaar_no=request.POST.get('adhaar_no'),
        gender = request.POST.get('gender'),
        education = request.POST.get('education'),
        shakha=request.POST.get('shakha'),
        dharma = request.POST.get('dharma'),
        jat = request.POST.get('jat'),
        pravarg=request.POST.get('pravarg'),
        prashikshan = request.POST.get('prashikshan'),
        prashikshan1 = request.POST.get('prashikshan1'),
        prashikshan2 = request.POST.get('prashikshan2'),
        course_prashikshan=request.POST.get('course_prashikshan'),
        course_prashikshan1=request.POST.get('course_prashikshan1'),
        course_prashikshan2=request.POST.get('course_prashikshan2'),
        vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        magas= request.POST.get('magas'),
        signature = request.FILES.get('signature')
        # umedwar_sign=request.FILES.get('umedwar_sign')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def jilha_puru(request,pk):
    print('hi')
    if jilha_pur.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = jilha_pur.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.umedwar_name=request.POST.get('umedwar_name'),
        x.rahivasi=request.POST.get('rahivasi'),
        x.kau_prashikshan=request.POST.get('kau_prashikshan'),
        x.second_name=request.POST.get('second_name'),
        x.fa_name=request.POST.get('fa_name'),
        x.birth_date=request.POST.get('birth_date'),
        x.paripurn_patta=request.POST.get('paripurn_patta'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.adhaar_no=request.POST.get('adhaar_no'),
        x.gender = request.POST.get('gender'),
        x.education = request.POST.get('education'),
        x.shakha=request.POST.get('shakha'),
        x.dharma = request.POST.get('dharma'),
        x.jat = request.POST.get('jat'),
        x.pravarg=request.POST.get('pravarg'),
        x.prashikshan = request.POST.get('prashikshan'),
        x.prashikshan1 = request.POST.get('prashikshan1'),
        x.prashikshan2 = request.POST.get('prashikshan2'),
        x.course_prashikshan=request.POST.get('course_prashikshan'),
        x.course_prashikshan1=request.POST.get('course_prashikshan1'),
        x.course_prashikshan2=request.POST.get('course_prashikshan2'),
        x.vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        x.save()
    else:
        x= jilha_pur(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        umedwar_name=request.POST.get('umedwar_name'),
        rahivasi=request.POST.get('rahivasi'),
        kau_prashikshan=request.POST.get('kau_prashikshan'),
        second_name=request.POST.get('second_name'),
        fa_name=request.POST.get('fa_name'),
        birth_date=request.POST.get('birth_date'),
        paripurn_patta=request.POST.get('paripurn_patta'),
        mobile_number=request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        adhaar_no=request.POST.get('adhaar_no'),
        gender = request.POST.get('gender'),
        education = request.POST.get('education'),
        shakha=request.POST.get('shakha'),
        dharma = request.POST.get('dharma'),
        jat = request.POST.get('jat'),
        pravarg=request.POST.get('pravarg'),
        prashikshan = request.POST.get('prashikshan'),
        prashikshan1 = request.POST.get('prashikshan1'),
        prashikshan2 = request.POST.get('prashikshan2'),
        course_prashikshan=request.POST.get('course_prashikshan'),
        course_prashikshan1=request.POST.get('course_prashikshan1'),
        course_prashikshan2=request.POST.get('course_prashikshan2'),
        vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        signature = request.FILES.get('signature')
        # umedwar_sign=request.FILES.get('umedwar_sign')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})


def dindayal_ant(request,pk):
    print('hi')
    if din_dayal.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = din_dayal.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.umedwar_name=request.POST.get('umedwar_name'),
        x.rahivasi=request.POST.get('rahivasi'),
        x.kau_prashikshan=request.POST.get('kau_prashikshan'),
        x.second_name=request.POST.get('second_name'),
        x.fa_name=request.POST.get('fa_name'),
        x.birth_date=request.POST.get('birth_date'),
        x.paripurn_patta=request.POST.get('paripurn_patta'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.adhaar_no=request.POST.get('adhaar_no'),
        x.gender = request.POST.get('gender'),
        x.education = request.POST.get('education'),
        x.shakha=request.POST.get('shakha'),
        x.dharma = request.POST.get('dharma'),
        x.jat = request.POST.get('jat'),
        x.pravarg=request.POST.get('pravarg'),
        x.prashikshan = request.POST.get('prashikshan'),
        x.prashikshan1 = request.POST.get('prashikshan1'),
        x.prashikshan2 = request.POST.get('prashikshan2'),
        x.course_prashikshan=request.POST.get('course_prashikshan'),
        x.course_prashikshan1=request.POST.get('course_prashikshan1'),
        x.course_prashikshan2=request.POST.get('course_prashikshan2'),
        x.vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        x.save()
    else:
        x= din_dayal(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        umedwar_name=request.POST.get('umedwar_name'),
        rahivasi=request.POST.get('rahivasi'),
        kau_prashikshan=request.POST.get('kau_prashikshan'),
        second_name=request.POST.get('second_name'),
        fa_name=request.POST.get('fa_name'),
        birth_date=request.POST.get('birth_date'),
        paripurn_patta=request.POST.get('paripurn_patta'),
        mobile_number=request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        adhaar_no=request.POST.get('adhaar_no'),
        gender = request.POST.get('gender'),
        education = request.POST.get('education'),
        shakha=request.POST.get('shakha'),
        dharma = request.POST.get('dharma'),
        jat = request.POST.get('jat'),
        pravarg=request.POST.get('pravarg'),
        prashikshan = request.POST.get('prashikshan'),
        prashikshan1 = request.POST.get('prashikshan1'),
        prashikshan2 = request.POST.get('prashikshan2'),
        course_prashikshan=request.POST.get('course_prashikshan'),
        course_prashikshan1=request.POST.get('course_prashikshan1'),
        course_prashikshan2=request.POST.get('course_prashikshan2'),
        vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        signature = request.FILES.get('signature')
        # umedwar_sign=request.FILES.get('umedwar_sign')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def pradhan_mantri(request,pk):
    print('hi')
    if pra_dhan.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = pra_dhan.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.umedwar_name=request.POST.get('umedwar_name'),
        x.rahivasi=request.POST.get('rahivasi'),
        x.kau_prashikshan=request.POST.get('kau_prashikshan'),
        x.second_name=request.POST.get('second_name'),
        x.fa_name=request.POST.get('fa_name'),
        x.birth_date=request.POST.get('birth_date'),
        x.paripurn_patta=request.POST.get('paripurn_patta'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.adhaar_no=request.POST.get('adhaar_no'),
        x.gender = request.POST.get('gender'),
        x.education = request.POST.get('education'),
        x.shakha=request.POST.get('shakha'),
        x.dharma = request.POST.get('dharma'),
        x.jat = request.POST.get('jat'),
        x.pravarg=request.POST.get('pravarg'),
        x.prashikshan = request.POST.get('prashikshan'),
        x.prashikshan1 = request.POST.get('prashikshan1'),
        x.prashikshan2 = request.POST.get('prashikshan2'),
        x.course_prashikshan=request.POST.get('course_prashikshan'),
        x.course_prashikshan1=request.POST.get('course_prashikshan1'),
        x.course_prashikshan2=request.POST.get('course_prashikshan2'),
        x.vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        x.save()
    else:
        x= pra_dhan(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        umedwar_name=request.POST.get('umedwar_name'),
        rahivasi=request.POST.get('rahivasi'),
        kau_prashikshan=request.POST.get('kau_prashikshan'),
        second_name=request.POST.get('second_name'),
        fa_name=request.POST.get('fa_name'),
        birth_date=request.POST.get('birth_date'),
        paripurn_patta=request.POST.get('paripurn_patta'),
        mobile_number=request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        adhaar_no=request.POST.get('adhaar_no'),
        gender = request.POST.get('gender'),
        education = request.POST.get('education'),
        shakha=request.POST.get('shakha'),
        dharma = request.POST.get('dharma'),
        jat = request.POST.get('jat'),
        pravarg=request.POST.get('pravarg'),
        prashikshan = request.POST.get('prashikshan'),
        prashikshan1 = request.POST.get('prashikshan1'),
        prashikshan2 = request.POST.get('prashikshan2'),
        course_prashikshan=request.POST.get('course_prashikshan'),
        course_prashikshan1=request.POST.get('course_prashikshan1'),
        course_prashikshan2=request.POST.get('course_prashikshan2'),
        vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        signature = request.FILES.get('signature')
        # umedwar_sign=request.FILES.get('umedwar_sign')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def pramod_maha(request,pk):
    print('hi')
    if pramod_mah.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = pramod_mah.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.umedwar_name=request.POST.get('umedwar_name'),
        x.rahivasi=request.POST.get('rahivasi'),
        x.kau_prashikshan=request.POST.get('kau_prashikshan'),
        x.second_name=request.POST.get('second_name'),
        x.fa_name=request.POST.get('fa_name'),
        x.birth_date=request.POST.get('birth_date'),
        x.paripurn_patta=request.POST.get('paripurn_patta'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.adhaar_no=request.POST.get('adhaar_no'),
        x.gender = request.POST.get('gender'),
        x.education = request.POST.get('education'),
        x.shakha=request.POST.get('shakha'),
        x.dharma = request.POST.get('dharma'),
        x.jat = request.POST.get('jat'),
        x.pravarg=request.POST.get('pravarg'),
        x.prashikshan = request.POST.get('prashikshan'),
        x.prashikshan1 = request.POST.get('prashikshan1'),
        x.prashikshan2 = request.POST.get('prashikshan2'),
        x.course_prashikshan=request.POST.get('course_prashikshan'),
        x.course_prashikshan1=request.POST.get('course_prashikshan1'),
        x.course_prashikshan2=request.POST.get('course_prashikshan2'),
        x.vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        x.save()
    else:
        x= pramod_mah(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        umedwar_name=request.POST.get('umedwar_name'),
        rahivasi=request.POST.get('rahivasi'),
        kau_prashikshan=request.POST.get('kau_prashikshan'),
        second_name=request.POST.get('second_name'),
        fa_name=request.POST.get('fa_name'),
        birth_date=request.POST.get('birth_date'),
        paripurn_patta=request.POST.get('paripurn_patta'),
        mobile_number=request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        adhaar_no=request.POST.get('adhaar_no'),
        gender = request.POST.get('gender'),
        education = request.POST.get('education'),
        shakha=request.POST.get('shakha'),
        dharma = request.POST.get('dharma'),
        jat = request.POST.get('jat'),
        pravarg=request.POST.get('pravarg'),
        prashikshan = request.POST.get('prashikshan'),
        prashikshan1 = request.POST.get('prashikshan1'),
        prashikshan2 = request.POST.get('prashikshan2'),
        course_prashikshan=request.POST.get('course_prashikshan'),
        course_prashikshan1=request.POST.get('course_prashikshan1'),
        course_prashikshan2=request.POST.get('course_prashikshan2'),
        vikas_prashikshan=request.POST.get('vikas_prashikshan'),
        signature = request.FILES.get('signature')
        # umedwar_sign=request.FILES.get('umedwar_sign')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def andha_vyaktinsathi(request,pk):
    print('entered in api 1')
    if andh_vyaktinsathi.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = andh_vyaktinsathi.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('sampurna_nav',''),
                x.address= request.POST.get('address',''),
                x.previous_benefit = request.POST.get('previous_benefit',''),
                x.age = request.POST.get('age',''),
                x.gender = request.POST.get('gender',''),
                x.caste = request.POST.get('caste',''),
                x.education = request.POST.get('shikshan',''),
                x.married = request.POST.get('marital_status',''),
                x.income = request.POST.get('yearly_income',''),
                x.handicap_type = request.POST.get('divyang_prakar',''),
                x.percent = request.POST.get('divyang_takke',''),
                x.handicap_certificate_no = request.POST.get('divyang_pramanpatra',''),
                x.form_date = request.POST.get('divyang_date',''),
                x.business = request.POST.get('vyavsay',''),
                x.adhar_card_no = request.POST.get('adhar_number',''),
                x.mobile_no = request.POST.get('mobile_number',''),
                x.avashak_seva = request.POST.get('seva',''),
                x.photo = request.FILES.get('photo',''),
                # x.signature = request.FILES.get('sign','')
                x.save()
    else:
        x = andh_vyaktinsathi(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('sampurna_nav',''),
            address= request.POST.get('address',''),
            previous_benefit = request.POST.get('previous_benefit',''),
            age = request.POST.get('age',0),
            gender = request.POST.get('gender',''),
            caste = request.POST.get('caste',''),
            education = request.POST.get('shikshan',''),
            married = request.POST.get('marital_status',''),
            income = request.POST.get('yearly_income',0),
            handicap_type = request.POST.get('divyang_prakar',''),
            percent = request.POST.get('divyang_takke',''),
            handicap_certificate_no = request.POST.get('divyang_pramanpatra',''),
            form_date = request.POST.get('divyang_date',''),
            business = request.POST.get('vyavsay',''),
            adhar_card_no = request.POST.get('adhar_number',''),
            mobile_no = request.POST.get('mobile_number',''),
            avashak_seva = request.POST.get('seva',''),
            photo = request.FILES.get('photo',''),
            # signature = request.FILES.get('sign',''),
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def ramai_gharkull(request,pk):
    print('entered in api 1')
    if ramai_gharkul.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = ramai_gharkul.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('sampurna_nav',''),
                x.fa_name= request.POST.get('fa_name',''),
                x.cu_address = request.POST.get('cu_address',''),
                x.pe_address = request.POST.get('pe_address',''),
                x.ghar_address = request.POST.get('ghar_address',''),
                x.kshetrafal= request.POST.get('kshetrafal',''),
                x.birth_date = request.POST.get('janma_date',''),
                x.birth_place= request.POST.get('birth_place',''),
                x.age = request.POST.get('age',''),
                x.caste = request.POST.get('caste',''),
                x.education = request.POST.get('shikshan',''),
                x.income = request.POST.get('yearly_income',''),
                x.business = request.POST.get('vyavsay',''),
                x.fa_business = request.POST.get('fa_business',''),
                x.ration_no= request.POST.get('ration_no',''),
                x.photo = request.FILES.get('photo',''),
                x.signature = request.FILES.get('sign',''),
                x.apply_date = request.POST.get('apply_date',''),
                x.name_1= request.POST.get('name_1',''),
                x.pradhanya= request.POST.getlist('pradhanya[]'),
                x.save()
    else:
        x = ramai_gharkul(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('sampurna_nav',''),
            fa_name= request.POST.get('fa_name',''),
            cu_address = request.POST.get('cu_address',''),
            pe_address = request.POST.get('pe_address',''),
            ghar_address = request.POST.get('ghar_address',''),
            kshetrafal= request.POST.get('kshetrafal',''),
            birth_date = request.POST.get('janma_date',''),
            birth_place= request.POST.get('birth_place',''),
            age = request.POST.get('age',0),
            caste = request.POST.get('caste',''),
            education = request.POST.get('shikshan',''),
            income = request.POST.get('yearly_income',0),
            business = request.POST.get('vyavsay',''),
            fa_business = request.POST.get('fa_business',''),
            ration_no= request.POST.get('ration_no',''),
            photo = request.FILES.get('photo',''),
            signature = request.FILES.get('sign',''),
            apply_date = request.POST.get('apply_date',''),
            name_1= request.POST.get('name_1',''),
            pradhanya= request.POST.getlist('pradhanya[]'),
            )
       
        x.save()
    return JsonResponse({'status':200})

def mini(request,pk):
    print('entered in api 1')
    if mini_tra.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = mini_tra.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.address= request.POST.get('address',''),
                x.mobile_no = request.POST.get('mobile_no',''),
                x.gat_name = request.POST.get('gat_name',''),
                x.karya_address = request.POST.get('karya_address',''),
                x.bachat_no= request.POST.get('bachat_no',''),
                x.anu_no = request.POST.get('anu_no',''),
                x.itar_no= request.POST.get('itar_no',''),
                x.registration_no = request.POST.get('registration_no',''),
                x.registration_date = request.POST.get('registration_date',''),
                x.bachat_info = request.POST.get('bachat_info',''),
                x.place = request.POST.get('place',''),
                x.app_date = request.POST.get('app_date',''),
                x.photo = request.FILES.get('photo',''),
                x.signature = request.FILES.get('sign',''),
                x.save()
    else:
        x = mini_tra(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            address= request.POST.get('address',''),
            mobile_no = request.POST.get('mobile_no',''),
            gat_name = request.POST.get('gat_name',''),
            karya_address = request.POST.get('karya_address',''),
            bachat_no= request.POST.get('bachat_no',''),
            anu_no = request.POST.get('anu_no',''),
            itar_no= request.POST.get('itar_no',''),
            registration_no = request.POST.get('registration_no',''),
            registration_date = request.POST.get('registration_date',''),
            bachat_info = request.POST.get('bachat_info',''),
            place = request.POST.get('place',''),
            app_date = request.POST.get('app_date',''),
            photo = request.FILES.get('photo',''),
            signature = request.FILES.get('sign',''),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
def bharatratna(request,pk):
    print('entered in api 1')
    if vyaktinsathi.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = vyaktinsathi.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.birth_date = request.POST.get('birth_date',''),
                x.age= request.POST.get('age',''),
                x.education = request.POST.get('education',''),
                x.business= request.POST.get('business',''),
                x.jat = request.POST.get('jat',''),
                x.patni_hyat = request.POST.get('patni_hyat',''),
                x.samajik = request.POST.get('samajik',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anujati = request.POST.get('anujati',''),
                x.vyakti_sahitya = request.POST.get('vyakti_sahitya',''),
                x.jya_sanstha= request.POST.get('jya_sanstha',''),
                x.samkaly_kshetra = request.POST.get('samkaly_kshetra',''),
                x.karyakartya= request.FILES.get('karyakartya',''),
                x.yapurvi_bahu = request.POST.get('yapurvi_bahu',''),
                x.karkarta_sadhya = request.POST.get('karkarta_sadhya',''),
                x.vidhanmandal = request.POST.get('vidhanmandal',''),
                x.vyakti_karyakarta = request.POST.get('vyakti_karyakarta',''),
                x.vyakti_karyakarta1 = request.FILES.get('vyakti_karyakarta1',''),
                x.shifaras = request.POST.get('shifaras',''),
                x.itar = request.POST.get('itar',''),
                x.pramanpatra = request.POST.get('pramanpatra',''),
                x.hudda = request.POST.get('hudda',''),
                x.thikan = request.POST.get('thikan',''),
                x.form_date = request.POST.get('form_date',''),
                x.signature = request.FILES.get('sign',''),
                x.purava = request.FILES.get('purava',''),
                x.save()
    else:
        x = vyaktinsathi(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            birth_date = request.POST.get('birth_date',''),
            age= request.POST.get('age',''),
            education = request.POST.get('education',''),
            business= request.POST.get('business',''),
            jat = request.POST.get('jat',''),
            patni_hyat = request.POST.get('patni_hyat',''),
            samajik = request.POST.get('samajik',''),
            arj_pur = request.POST.get('arj_pur',''),
            anujati = request.POST.get('anujati',''),
            vyakti_sahitya = request.POST.get('vyakti_sahitya',''),
            jya_sanstha= request.POST.get('jya_sanstha',''),
            samkaly_kshetra = request.POST.get('samkaly_kshetra',''),
            karyakartya= request.FILES.get('karyakartya',''),
            yapurvi_bahu = request.POST.get('yapurvi_bahu',''),
            karkarta_sadhya = request.POST.get('karkarta_sadhya',''),
            vidhanmandal = request.POST.get('vidhanmandal',''),
            vyakti_karyakarta = request.POST.get('vyakti_karyakarta',''),
            vyakti_karyakarta1 = request.FILES.get('vyakti_karyakarta1',''),
            shifaras = request.POST.get('shifaras',''),
            itar = request.POST.get('itar',''),
            pramanpatra = request.POST.get('pramanpatra',''),
            hudda = request.POST.get('hudda',''),
            thikan = request.POST.get('thikan',''),
            form_date = request.POST.get('form_date',''),
            signature = request.FILES.get('sign',''),
            purava = request.FILES.get('purava',''),
            )
       
        x.save()
    return JsonResponse({'status':200})

def lokshahir_anna(request,pk):
    print('entered in api 1')
    if lokshahir.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = lokshahir.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.birth_date = request.POST.get('birth_date',''),
                x.age= request.POST.get('age',''),
                x.education = request.POST.get('education',''),
                x.business= request.POST.get('business',''),
                x.jat = request.POST.get('jat',''),
                x.patni_hyat = request.POST.get('patni_hyat',''),
                x.samajik = request.POST.get('samajik',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anujati = request.POST.get('anujati',''),
                x.vyakti_sahitya = request.POST.get('vyakti_sahitya',''),
                x.jya_sanstha= request.POST.get('jya_sanstha',''),
                x.samkaly_kshetra = request.POST.get('samkaly_kshetra',''),
                x.karyakartya= request.FILES.get('karyakartya',''),
                x.yapurvi_bahu = request.POST.get('yapurvi_bahu',''),
                x.karkarta_sadhya = request.POST.get('karkarta_sadhya',''),
                x.vidhanmandal = request.POST.get('vidhanmandal',''),
                x.vyakti_karyakarta = request.POST.get('vyakti_karyakarta',''),
                x.vyakti_karyakarta1 = request.FILES.get('vyakti_karyakarta1',''),
                x.shifaras = request.POST.get('shifaras',''),
                x.itar = request.POST.get('itar',''),
                x.pramanpatra = request.POST.get('pramanpatra',''),
                x.hudda = request.POST.get('hudda',''),
                x.thikan = request.POST.get('thikan',''),
                x.form_date = request.POST.get('form_date',''),
                x.signature = request.FILES.get('sign',''),
                x.purava = request.FILES.get('purava',''),
                x.save()
    else:
        x = lokshahir(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            birth_date = request.POST.get('birth_date',''),
            age= request.POST.get('age',''),
            education = request.POST.get('education',''),
            business= request.POST.get('business',''),
            jat = request.POST.get('jat',''),
            patni_hyat = request.POST.get('patni_hyat',''),
            samajik = request.POST.get('samajik',''),
            arj_pur = request.POST.get('arj_pur',''),
            anujati = request.POST.get('anujati',''),
            vyakti_sahitya = request.POST.get('vyakti_sahitya',''),
            jya_sanstha= request.POST.get('jya_sanstha',''),
            samkaly_kshetra = request.POST.get('samkaly_kshetra',''),
            karyakartya= request.FILES.get('karyakartya',''),
            yapurvi_bahu = request.POST.get('yapurvi_bahu',''),
            karkarta_sadhya = request.POST.get('karkarta_sadhya',''),
            vidhanmandal = request.POST.get('vidhanmandal',''),
            vyakti_karyakarta = request.POST.get('vyakti_karyakarta',''),
            vyakti_karyakarta1 = request.FILES.get('vyakti_karyakarta1',''),
            shifaras = request.POST.get('shifaras',''),
            itar = request.POST.get('itar',''),
            pramanpatra = request.POST.get('pramanpatra',''),
            hudda = request.POST.get('hudda',''),
            thikan = request.POST.get('thikan',''),
            form_date = request.POST.get('form_date',''),
            signature = request.FILES.get('sign',''),
            purava = request.FILES.get('purava',''),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
def sant_ravidas(request,pk):
    print('entered in api 1')
    if ravidas.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = ravidas.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.birth_date = request.POST.get('birth_date',''),
                x.age= request.POST.get('age',''),
                x.education = request.POST.get('education',''),
                x.business= request.POST.get('business',''),
                x.jat = request.POST.get('jat',''),
                x.patni_hyat = request.POST.get('patni_hyat',''),
                x.samajik = request.POST.get('samajik',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anujati = request.POST.get('anujati',''),
                x.vyakti_sahitya = request.POST.get('vyakti_sahitya',''),
                x.jya_sanstha= request.POST.get('jya_sanstha',''),
                x.samkaly_kshetra = request.POST.get('samkaly_kshetra',''),
                x.karyakartya= request.FILES.get('karyakartya',''),
                x.yapurvi_bahu = request.POST.get('yapurvi_bahu',''),
                x.karkarta_sadhya = request.POST.get('karkarta_sadhya',''),
                x.vidhanmandal = request.POST.get('vidhanmandal',''),
                x.vyakti_karyakarta = request.POST.get('vyakti_karyakarta',''),
                x.vyakti_karyakarta1 = request.FILES.get('vyakti_karyakarta1',''),
                x.shifaras = request.POST.get('shifaras',''),
                x.itar = request.POST.get('itar',''),
                x.pramanpatra = request.POST.get('pramanpatra',''),
                x.hudda = request.POST.get('hudda',''),
                x.thikan = request.POST.get('thikan',''),
                x.form_date = request.POST.get('form_date',''),
                x.signature = request.FILES.get('sign',''),
                x.purava = request.FILES.get('purava',''),
                x.save()
    else:
        x = ravidas(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            birth_date = request.POST.get('birth_date',''),
            age= request.POST.get('age',''),
            education = request.POST.get('education',''),
            business= request.POST.get('business',''),
            jat = request.POST.get('jat',''),
            patni_hyat = request.POST.get('patni_hyat',''),
            samajik = request.POST.get('samajik',''),
            arj_pur = request.POST.get('arj_pur',''),
            anujati = request.POST.get('anujati',''),
            vyakti_sahitya = request.POST.get('vyakti_sahitya',''),
            jya_sanstha= request.POST.get('jya_sanstha',''),
            samkaly_kshetra = request.POST.get('samkaly_kshetra',''),
            karyakartya= request.FILES.get('karyakartya',''),
            yapurvi_bahu = request.POST.get('yapurvi_bahu',''),
            karkarta_sadhya = request.POST.get('karkarta_sadhya',''),
            vidhanmandal = request.POST.get('vidhanmandal',''),
            vyakti_karyakarta = request.POST.get('vyakti_karyakarta',''),
            vyakti_karyakarta1 = request.FILES.get('vyakti_karyakarta1',''),
            shifaras = request.POST.get('shifaras',''),
            itar = request.POST.get('itar',''),
            pramanpatra = request.POST.get('pramanpatra',''),
            hudda = request.POST.get('hudda',''),
            thikan = request.POST.get('thikan',''),
            form_date = request.POST.get('form_date',''),
            signature = request.FILES.get('sign',''),
            purava = request.FILES.get('purava',''),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
def karmavir_dada(request,pk):
    print('entered in api 1')
    if karmavir.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = karmavir.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.birth_date = request.POST.get('birth_date',''),
                x.age= request.POST.get('age',''),
                x.education = request.POST.get('education',''),
                x.business= request.POST.get('business',''),
                x.jat = request.POST.get('jat',''),
                x.patni_hyat = request.POST.get('patni_hyat',''),
                x.samajik = request.POST.get('samajik',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anujati = request.POST.get('anujati',''),
                x.vyakti_sahitya = request.POST.get('vyakti_sahitya',''),
                x.jya_sanstha= request.POST.get('jya_sanstha',''),
                x.samkaly_kshetra = request.POST.get('samkaly_kshetra',''),
                x.karyakartya= request.FILES.get('karyakartya',''),
                x.yapurvi_bahu = request.POST.get('yapurvi_bahu',''),
                x.karkarta_sadhya = request.POST.get('karkarta_sadhya',''),
                x.vidhanmandal = request.POST.get('vidhanmandal',''),
                x.vyakti_karyakarta = request.POST.get('vyakti_karyakarta',''),
                x.vyakti_karyakarta1 = request.FILES.get('vyakti_karyakarta1',''),
                x.shifaras = request.POST.get('shifaras',''),
                x.itar = request.POST.get('itar',''),
                x.pramanpatra = request.POST.get('pramanpatra',''),
                x.hudda = request.POST.get('hudda',''),
                x.thikan = request.POST.get('thikan',''),
                x.form_date = request.POST.get('form_date',''),
                x.signature = request.FILES.get('sign',''),
                x.purava = request.FILES.get('purava',''),
                x.save()
    else:
        x = karmavir(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            birth_date = request.POST.get('birth_date',''),
            age= request.POST.get('age',''),
            education = request.POST.get('education',''),
            business= request.POST.get('business',''),
            jat = request.POST.get('jat',''),
            patni_hyat = request.POST.get('patni_hyat',''),
            samajik = request.POST.get('samajik',''),
            arj_pur = request.POST.get('arj_pur',''),
            anujati = request.POST.get('anujati',''),
            vyakti_sahitya = request.POST.get('vyakti_sahitya',''),
            jya_sanstha= request.POST.get('jya_sanstha',''),
            samkaly_kshetra = request.POST.get('samkaly_kshetra',''),
            karyakartya= request.FILES.get('karyakartya',''),
            yapurvi_bahu = request.POST.get('yapurvi_bahu',''),
            karkarta_sadhya = request.POST.get('karkarta_sadhya',''),
            vidhanmandal = request.POST.get('vidhanmandal',''),
            vyakti_karyakarta = request.POST.get('vyakti_karyakarta',''),
            vyakti_karyakarta1 = request.FILES.get('vyakti_karyakarta1',''),
            shifaras = request.POST.get('shifaras',''),
            itar = request.POST.get('itar',''),
            pramanpatra = request.POST.get('pramanpatra',''),
            hudda = request.POST.get('hudda',''),
            thikan = request.POST.get('thikan',''),
            form_date = request.POST.get('form_date',''),
            signature = request.FILES.get('sign',''),
            purava = request.FILES.get('purava',''),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
def sanstha(request,pk):
    print('entered in api 1')
    if bharat_sanstha.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = bharat_sanstha.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.adhi1_date = request.POST.get('adhi1_date',''),
                x.adhi2_date = request.POST.get('adhi2_date',''),
                x.adhi1 = request.POST.get('adhi1',''),
                x.adhi2 = request.POST.get('adhi2',''),
                x.sambandhit= request.POST.get('sambandhit',''),
                x.upvidhi = request.POST.get('upvidhi',''),
                x.padadhi1_name= request.POST.get('padadhi1_name',''),
                x.padadhi2_name = request.POST.get('padadhi2_name',''),
                x.mob1 = request.POST.get('mob1',''),
                x.mob2 = request.POST.get('mob2',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anubhav = request.POST.get('anubhav',''),
                x.lekha_pari = request.POST.get('lekha_pari',''),
                x.varshik_aha= request.POST.get('varshik_aha',''),
                x.swatantra_lekha = request.POST.get('swatantra_lekha',''),           
                x.sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
                x.upkram = request.POST.get('upkram',''),
                x.vyaktigat = request.POST.get('vyaktigat',''),
                x.sadar_sansthes = request.POST.get('sadar_sansthes',''),
                x.vaishishtya = request.POST.get('vaishishtya',''),
                x.vaishishtya1 = request.FILES.get('vaishishtya1',''),
                x.dakhla = request.FILES.get('dakhla',''),
                x.name2 = request.POST.get('name2',''),           
                x.pari_name1 = request.POST.get('pari_name1',''),
                x.pari_name2 = request.POST.get('pari_name2',''),
                x.pari_name3 = request.POST.get('pari_name3',''),
                x.from1 = request.POST.get('from1',''),
                x.from2 = request.POST.get('from2',''),
                x.from3 = request.POST.get('from3',''),
                x.pari_date1 = request.POST.get('pari_date1',''),
                x.pari_date2 = request.POST.get('pari_date2',''),
                x.pari_date3 = request.POST.get('pari_date3',''),
                x.signature = request.FILES.get('sign',''),
                x.save()
    else:
        x = bharat_sanstha(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            adhi1_date = request.POST.get('adhi1_date',''),
            adhi2_date = request.POST.get('adhi2_date',''),
            adhi1 = request.POST.get('adhi1',''),
            adhi2 = request.POST.get('adhi2',''),
            sambandhit= request.POST.get('sambandhit',''),
            upvidhi = request.POST.get('upvidhi',''),
            padadhi1_name= request.POST.get('padadhi1_name',''),
            padadhi2_name = request.POST.get('padadhi2_name',''),
            mob1 = request.POST.get('mob1',''),
            mob2 = request.POST.get('mob2',''),
            arj_pur = request.POST.get('arj_pur',''),
            anubhav = request.POST.get('anubhav',''),
            lekha_pari = request.POST.get('lekha_pari',''),
            varshik_aha= request.POST.get('varshik_aha',''),
            swatantra_lekha = request.POST.get('swatantra_lekha',''),           
            sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
            upkram = request.POST.get('upkram',''),
            vyaktigat = request.POST.get('vyaktigat',''),
            sadar_sansthes = request.POST.get('sadar_sansthes',''),
            vaishishtya = request.POST.get('vaishishtya',''),
            vaishishtya1 = request.FILES.get('vaishishtya1',''),
            dakhla = request.FILES.get('dakhla',''),
            name2 = request.POST.get('name2',''),           
            pari_name1 = request.POST.get('pari_name1',''),
            pari_name2 = request.POST.get('pari_name2',''),
            pari_name3 = request.POST.get('pari_name3',''),
            from1 = request.POST.get('from1',''),
            from2 = request.POST.get('from2',''),
            from3 = request.POST.get('from3',''),
            pari_date1 = request.POST.get('pari_date1',''),
            pari_date2 = request.POST.get('pari_date2',''),
            pari_date3 = request.POST.get('pari_date3',''),
            signature = request.FILES.get('sign',''),
            )
       
        x.save()
    return JsonResponse({'status':200})

def anna_sanstha(request,pk):
    print('entered in api 1')
    if lokshahir_sanstha.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = lokshahir_sanstha.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.adhi1_date = request.POST.get('adhi1_date',''),
                x.adhi2_date = request.POST.get('adhi2_date',''),
                x.adhi1 = request.POST.get('adhi1',''),
                x.adhi2 = request.POST.get('adhi2',''),
                x.sambandhit= request.POST.get('sambandhit',''),
                x.upvidhi = request.POST.get('upvidhi',''),
                x.padadhi1_name= request.POST.get('padadhi1_name',''),
                x.padadhi2_name = request.POST.get('padadhi2_name',''),
                x.mob1 = request.POST.get('mob1',''),
                x.mob2 = request.POST.get('mob2',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anubhav = request.POST.get('anubhav',''),
                x.lekha_pari = request.POST.get('lekha_pari',''),
                x.varshik_aha= request.POST.get('varshik_aha',''),
                x.swatantra_lekha = request.POST.get('swatantra_lekha',''),           
                x.sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
                x.upkram = request.POST.get('upkram',''),
                x.vyaktigat = request.POST.get('vyaktigat',''),
                x.sadar_sansthes = request.POST.get('sadar_sansthes',''),
                x.vaishishtya = request.POST.get('vaishishtya',''),
                x.vaishishtya1 = request.FILES.get('vaishishtya1',''),
                x.dakhla = request.FILES.get('dakhla',''),
                x.name2 = request.POST.get('name2',''),           
                x.pari_name1 = request.POST.get('pari_name1',''),
                x.pari_name2 = request.POST.get('pari_name2',''),
                x.pari_name3 = request.POST.get('pari_name3',''),
                x.from1 = request.POST.get('from1',''),
                x.from2 = request.POST.get('from2',''),
                x.from3 = request.POST.get('from3',''),
                x.pari_date1 = request.POST.get('pari_date1',''),
                x.pari_date2 = request.POST.get('pari_date2',''),
                x.pari_date3 = request.POST.get('pari_date3',''),
                x.signature = request.FILES.get('sign',''),
                x.save()
    else:
        x = lokshahir_sanstha(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            adhi1_date = request.POST.get('adhi1_date',''),
            adhi2_date = request.POST.get('adhi2_date',''),
            adhi1 = request.POST.get('adhi1',''),
            adhi2 = request.POST.get('adhi2',''),
            sambandhit= request.POST.get('sambandhit',''),
            upvidhi = request.POST.get('upvidhi',''),
            padadhi1_name= request.POST.get('padadhi1_name',''),
            padadhi2_name = request.POST.get('padadhi2_name',''),
            mob1 = request.POST.get('mob1',''),
            mob2 = request.POST.get('mob2',''),
            arj_pur = request.POST.get('arj_pur',''),
            anubhav = request.POST.get('anubhav',''),
            lekha_pari = request.POST.get('lekha_pari',''),
            varshik_aha= request.POST.get('varshik_aha',''),
            swatantra_lekha = request.POST.get('swatantra_lekha',''),           
            sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
            upkram = request.POST.get('upkram',''),
            vyaktigat = request.POST.get('vyaktigat',''),
            sadar_sansthes = request.POST.get('sadar_sansthes',''),
            vaishishtya = request.POST.get('vaishishtya',''),
            vaishishtya1 = request.FILES.get('vaishishtya1',''),
            dakhla = request.FILES.get('dakhla',''),
            name2 = request.POST.get('name2',''),           
            pari_name1 = request.POST.get('pari_name1',''),
            pari_name2 = request.POST.get('pari_name2',''),
            pari_name3 = request.POST.get('pari_name3',''),
            from1 = request.POST.get('from1',''),
            from2 = request.POST.get('from2',''),
            from3 = request.POST.get('from3',''),
            pari_date1 = request.POST.get('pari_date1',''),
            pari_date2 = request.POST.get('pari_date2',''),
            pari_date3 = request.POST.get('pari_date3',''),
            signature = request.FILES.get('sign',''),
            )
       
        x.save()
    return JsonResponse({'status':200})

def sant_sanstha(request,pk):
    print('entered in api 1')
    if ravidas_sanstha.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = ravidas_sanstha.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.adhi1_date = request.POST.get('adhi1_date',''),
                x.adhi2_date = request.POST.get('adhi2_date',''),
                x.adhi1 = request.POST.get('adhi1',''),
                x.adhi2 = request.POST.get('adhi2',''),
                x.sambandhit= request.POST.get('sambandhit',''),
                x.upvidhi = request.POST.get('upvidhi',''),
                x.padadhi1_name= request.POST.get('padadhi1_name',''),
                x.padadhi2_name = request.POST.get('padadhi2_name',''),
                x.mob1 = request.POST.get('mob1',''),
                x.mob2 = request.POST.get('mob2',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anubhav = request.POST.get('anubhav',''),
                x.lekha_pari = request.POST.get('lekha_pari',''),
                x.varshik_aha= request.POST.get('varshik_aha',''),
                x.swatantra_lekha = request.POST.get('swatantra_lekha',''),           
                x.sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
                x.upkram = request.POST.get('upkram',''),
                x.vyaktigat = request.POST.get('vyaktigat',''),
                x.sadar_sansthes = request.POST.get('sadar_sansthes',''),
                x.vaishishtya = request.POST.get('vaishishtya',''),
                x.vaishishtya1 = request.FILES.get('vaishishtya1',''),
                x.dakhla = request.FILES.get('dakhla',''),
                x.name2 = request.POST.get('name2',''),           
                x.pari_name1 = request.POST.get('pari_name1',''),
                x.pari_name2 = request.POST.get('pari_name2',''),
                x.pari_name3 = request.POST.get('pari_name3',''),
                x.from1 = request.POST.get('from1',''),
                x.from2 = request.POST.get('from2',''),
                x.from3 = request.POST.get('from3',''),
                x.pari_date1 = request.POST.get('pari_date1',''),
                x.pari_date2 = request.POST.get('pari_date2',''),
                x.pari_date3 = request.POST.get('pari_date3',''),
                x.signature = request.FILES.get('sign',''),
                x.save()
    else:
        x = ravidas_sanstha(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            adhi1_date = request.POST.get('adhi1_date',''),
            adhi2_date = request.POST.get('adhi2_date',''),
            adhi1 = request.POST.get('adhi1',''),
            adhi2 = request.POST.get('adhi2',''),
            sambandhit= request.POST.get('sambandhit',''),
            upvidhi = request.POST.get('upvidhi',''),
            padadhi1_name= request.POST.get('padadhi1_name',''),
            padadhi2_name = request.POST.get('padadhi2_name',''),
            mob1 = request.POST.get('mob1',''),
            mob2 = request.POST.get('mob2',''),
            arj_pur = request.POST.get('arj_pur',''),
            anubhav = request.POST.get('anubhav',''),
            lekha_pari = request.POST.get('lekha_pari',''),
            varshik_aha= request.POST.get('varshik_aha',''),
            swatantra_lekha = request.POST.get('swatantra_lekha',''),           
            sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
            upkram = request.POST.get('upkram',''),
            vyaktigat = request.POST.get('vyaktigat',''),
            sadar_sansthes = request.POST.get('sadar_sansthes',''),
            vaishishtya = request.POST.get('vaishishtya',''),
            vaishishtya1 = request.FILES.get('vaishishtya1',''),
            dakhla = request.FILES.get('dakhla',''),
            name2 = request.POST.get('name2',''),           
            pari_name1 = request.POST.get('pari_name1',''),
            pari_name2 = request.POST.get('pari_name2',''),
            pari_name3 = request.POST.get('pari_name3',''),
            from1 = request.POST.get('from1',''),
            from2 = request.POST.get('from2',''),
            from3 = request.POST.get('from3',''),
            pari_date1 = request.POST.get('pari_date1',''),
            pari_date2 = request.POST.get('pari_date2',''),
            pari_date3 = request.POST.get('pari_date3',''),
            signature = request.FILES.get('sign',''),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
def shahufule(request,pk):
    print('entered in api 1')
    if shahu_fule.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = shahu_fule.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.adhi1_date = request.POST.get('adhi1_date',''),
                x.adhi2_date = request.POST.get('adhi2_date',''),
                x.adhi1 = request.POST.get('adhi1',''),
                x.adhi2 = request.POST.get('adhi2',''),
                x.sambandhit= request.POST.get('sambandhit',''),
                x.upvidhi = request.POST.get('upvidhi',''),
                x.padadhi1_name= request.POST.get('padadhi1_name',''),
                x.padadhi2_name = request.POST.get('padadhi2_name',''),
                x.mob1 = request.POST.get('mob1',''),
                x.mob2 = request.POST.get('mob2',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anubhav = request.POST.get('anubhav',''),
                x.lekha_pari = request.POST.get('lekha_pari',''),
                x.varshik_aha= request.POST.get('varshik_aha',''),
                x.swatantra_lekha = request.POST.get('swatantra_lekha',''),           
                x.sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
                x.upkram = request.POST.get('upkram',''),
                x.vyaktigat = request.POST.get('vyaktigat',''),
               
                x.sadar_sansthes = request.POST.get('sadar_sansthes',''),
                x.vaishishtya = request.POST.get('vaishishtya',''),
                x.vaishishtya1 = request.FILES.get('vaishishtya1',''),
                x.dakhla = request.FILES.get('dakhla',''),
                x.name2 = request.POST.get('name2',''),           
                x.pari_name1 = request.POST.get('pari_name1',''),
                x.pari_name2 = request.POST.get('pari_name2',''),
                x.pari_name3 = request.POST.get('pari_name3',''),
                x.from1 = request.POST.get('from1',''),
                x.from2 = request.POST.get('from2',''),
                x.from3 = request.POST.get('from3',''),
                x.pari_date1 = request.POST.get('pari_date1',''),
                x.pari_date2 = request.POST.get('pari_date2',''),
                x.pari_date3 = request.POST.get('pari_date3',''),
                x.signature = request.FILES.get('sign',''),
                x.save()
    else:
        x = shahu_fule(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            adhi1_date = request.POST.get('adhi1_date',''),
            adhi2_date = request.POST.get('adhi2_date',''),
            adhi1 = request.POST.get('adhi1',''),
            adhi2 = request.POST.get('adhi2',''),
            sambandhit= request.POST.get('sambandhit',''),
            upvidhi = request.POST.get('upvidhi',''),
            padadhi1_name= request.POST.get('padadhi1_name',''),
            padadhi2_name = request.POST.get('padadhi2_name',''),
            mob1 = request.POST.get('mob1',''),
            mob2 = request.POST.get('mob2',''),
            arj_pur = request.POST.get('arj_pur',''),
            anubhav = request.POST.get('anubhav',''),
            lekha_pari = request.POST.get('lekha_pari',''),
            varshik_aha= request.POST.get('varshik_aha',''),
            swatantra_lekha = request.POST.get('swatantra_lekha',''),           
            sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
            upkram = request.POST.get('upkram',''),
            vyaktigat = request.POST.get('vyaktigat',''),
            sadar_sansthes = request.POST.get('sadar_sansthes',''),
            vaishishtya = request.POST.get('vaishishtya',''),
            vaishishtya1 = request.FILES.get('vaishishtya1',''),
            dakhla = request.FILES.get('dakhla',''),
            name2 = request.POST.get('name2',''),           
            pari_name1 = request.POST.get('pari_name1',''),
            pari_name2 = request.POST.get('pari_name2',''),
            pari_name3 = request.POST.get('pari_name3',''),
            from1 = request.POST.get('from1',''),
            from2 = request.POST.get('from2',''),
            from3 = request.POST.get('from3',''),
            pari_date1 = request.POST.get('pari_date1',''),
            pari_date2 = request.POST.get('pari_date2',''),
            pari_date3 = request.POST.get('pari_date3',''),
            signature = request.FILES.get('sign',''),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
def magas_mul(request,pk):
    print('hi')
    if magasvargiy_mula.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = magasvargiy_mula.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name= request.POST.get('name',''),
        x.jilha_name= request.POST.get('jilha_name',''),
        x.name2= request.POST.get('name2',''),
        x.signature = request.FILES.get('sign',''),
        x.mobile_number = request.POST.get('mobile_number',''),
        x.paripurn_patta = request.POST.get('paripurn_patta',''),
        x.name1 = request.POST.get('name1',''),
        x.moth_name = request.POST.get('moth_name',''),
        x.fa_name = request.POST.get('fa_name',''),
        x.sthanik_name = request.POST.get('sthanik_name',''),
        x.kayam_patta= request.POST.get('kayam_patta',''),
        x.birth_date = request.POST.get('birth_date',''),
        x.birth_place= request.POST.get('birth_place',''),
        x.mobile_number1 = request.POST.get('mobile_number1',''),
        x.adhaar_no = request.POST.get('adhaar_no',''),
        x.email_id = request.POST.get('email_id',''),
        x.pan1_no = request.POST.get('pan1_no',''),
        x.pan2_no = request.POST.get('pan2_no',''),
        x.pravarg = request.POST.get('pravarg',''),
        x.divyang= request.POST.get('divyang',''),
        x.iyatta = request.POST.get('iyatta',''),           
        x.previous_name = request.POST.get('previous_name',''),
        x.previous_address = request.POST.get('previous_address',''),
        x.aajar = request.POST.get('aajar',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.bank_no = request.POST.get('bank_no',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.gunha = request.POST.get('gunha',''),
        x.shasakiy_seva = request.POST.get('shasakiy_seva',''),
        x.income = request.POST.get('income',''),
        x.varsh1 = request.POST.get('varsh1',''),           
        x.varsh2 = request.POST.get('varsh2',''),
        x.varsh3 = request.POST.get('varsh3',''),
        x.iyatta1 = request.POST.get('iyatta1',''),
        x.iyatta2 = request.POST.get('iyatta2',''),
        x.iyatta3 = request.POST.get('iyatta3',''),
        x.takka1 = request.POST.get('takka1',''),
        x.takka2 = request.POST.get('takka2',''),
        x.takka3 = request.POST.get('takka3',''),
        x.maha_name = request.POST.get('maha_name',''),
        x.abhyaskram = request.POST.get('abhyaskram',''),           
        x.pas_varsh = request.POST.get('pas_varsh',''),
        x.charitrya = request.POST.get('charitrya',''),
        x.sakshi_name = request.POST.get('sakshi_name',''),
        x.palak_name = request.POST.get('palak_name',''),
        x.vidya_name = request.POST.get('vidya_name',''),
        x.pravarg_file = request.FILES.get('pravarg_file',''),
        x.divyang_file = request.FILES.get('divyang_file',''),
        x.aajar_file = request.FILES.get('aajar_file',''),
        x.sakshi_signature = request.FILES.get('sakshi_signature',''),
        x.palak_signature = request.FILES.get('palak_signature',''),
        x.vidya_signature = request.FILES.get('vidya_signature',''),
        
        if request.POST.get('gun') == '0':
            x.gunha = True
        else:
            x.gunha = False
        x.save()
    else:
        x= magasvargiy_mula(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name= request.POST.get('name',''),
        jilha_name= request.POST.get('jilha_name',''),
        signature = request.FILES.get('sign',''),
        name2= request.POST.get('name2',''),
        mobile_number = request.POST.get('mobile_number',''),
        paripurn_patta = request.POST.get('paripurn_patta',''),
        name1 = request.POST.get('name1',''),
        moth_name = request.POST.get('moth_name',''),
        fa_name = request.POST.get('fa_name',''),
        sthanik_name = request.POST.get('sthanik_name',''),
        kayam_patta= request.POST.get('kayam_patta',''),
        birth_date = request.POST.get('birth_date',''),
        birth_place= request.POST.get('birth_place',''),
        mobile_number1 = request.POST.get('mobile_number1',''),
        adhaar_no = request.POST.get('adhaar_no',''),
        email_id = request.POST.get('email_id',''),
        pan1_no = request.POST.get('pan1_no',''),
        pan2_no = request.POST.get('pan2_no',''),
        pravarg = request.POST.get('pravarg',''),
        divyang= request.POST.get('divyang',''),
        iyatta = request.POST.get('iyatta',''),           
        previous_name = request.POST.get('previous_name',''),
        previous_address = request.POST.get('previous_address',''),
        bank_name = request.POST.get('bank_name',''),
        bank_no = request.POST.get('bank_no',''),
        ifsc = request.POST.get('ifsc',''),
        aajar = request.POST.get('aajar',''),
        gunha = request.POST.get('gunha',''),
        shasakiy_seva = request.POST.get('shasakiy_seva',''),
        income = request.POST.get('income',''),
        varsh1 = request.POST.get('varsh1',''),           
        varsh2 = request.POST.get('varsh2',''),
        varsh3 = request.POST.get('varsh3',''),
        iyatta1 = request.POST.get('iyatta1',''),
        iyatta2 = request.POST.get('iyatta2',''),
        iyatta3 = request.POST.get('iyatta3',''),
        takka1 = request.POST.get('takka1',''),
        takka2 = request.POST.get('takka2',''),
        takka3 = request.POST.get('takka3',''),
        maha_name = request.POST.get('maha_name',''),
        abhyaskram = request.POST.get('abhyaskram',''),           
        pas_varsh = request.POST.get('pas_varsh',''),
        charitrya = request.POST.get('charitrya',''),
        sakshi_name = request.POST.get('sakshi_name',''),
        palak_name = request.POST.get('palak_name',''),
        vidya_name = request.POST.get('vidya_name',''),
        pravarg_file = request.FILES.get('pravarg_file',''),
        divyang_file = request.FILES.get('divyang_file',''),
        aajar_file = request.FILES.get('aajar_file',''),
        sakshi_signature = request.FILES.get('sakshi_signature',''),
        palak_signature = request.FILES.get('palak_signature',''),
        vidya_signature = request.FILES.get('vidya_signature',''),
        )
        if request.POST.get('gun')=='0':
            x.gunha=True
        else:
            x.gunha=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def pravinya_pur(request,pk):
    print('entered in api 1')
    if pravinya_rajya.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = pravinya_rajya.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.san= request.POST.get('san',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.adhi1_date = request.POST.get('adhi1_date',''),
                x.adhi2_date = request.POST.get('adhi2_date',''),
                x.adhi1 = request.POST.get('adhi1',''),
                x.adhi2 = request.POST.get('adhi2',''),
                x.sambandhit= request.POST.get('sambandhit',''),
                x.upvidhi = request.POST.get('upvidhi',''),
                x.padadhi_info= request.POST.get('padadhi_info',''),
                x.gruhpal_info = request.POST.get('gruhpal_info',''),
                x.anubhav = request.POST.get('anubhav',''),
                x.sanstha_swarup = request.POST.get('sanstha_swarup',''),
                x.sanstha_prakar = request.POST.get('sanstha_prakar',''),
                x.manya_sanstha = request.POST.get('manya_sanstha',''),
                x.pratyaksha = request.POST.get('pratyaksha',''),
                x.lekha_pari = request.POST.get('lekha_pari',''),
                x.varshik_aha= request.POST.get('varshik_aha',''),
                x.shreni = request.POST.get('shreni',''),
                x.upkram = request.POST.get('upkram',''),
                x.swatantra_lekha = request.POST.get('swatantra_lekha',''),           
                x.sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
                x.vidy_sarva = request.POST.get('vidy_sarva',''),
                x.sansthemarfat = request.POST.get('sansthemarfat',''),
                x.pari_name1 = request.POST.get('pari_name1',''),
                x.pari_name2 = request.POST.get('pari_name2',''),
                x.pari_name3 = request.POST.get('pari_name3',''),
                x.from1 = request.POST.get('from1',''),
                x.from2 = request.POST.get('from2',''),
                x.from3 = request.POST.get('from3',''),
                x.pari_date1 = request.POST.get('pari_date1',''),
                x.pari_date2 = request.POST.get('pari_date2',''),
                x.pari_date3 = request.POST.get('pari_date3',''),
                x.sadar_sansthes = request.POST.get('sadar_sansthes',''),           
                x.sansthevirudha = request.POST.get('sansthevirudha',''),
                x.sansthemdhe = request.POST.get('sansthemdhe',''),
                x.vishbadha = request.POST.get('vishbadha',''),
                x.dakhla = request.FILES.get('dakhla',''),
                x.sansth_niyantran = request.POST.get('sansth_niyantran',''),
                x.shera = request.POST.get('shera',''),
                x.name2 = request.POST.get('name2',''),           
                x.signature = request.FILES.get('sign',''),
                x.save()
    else:
        x = pravinya_rajya(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            san= request.POST.get('san',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            adhi1_date = request.POST.get('adhi1_date',''),
            adhi2_date = request.POST.get('adhi2_date',''),
            adhi1 = request.POST.get('adhi1',''),
            adhi2 = request.POST.get('adhi2',''),
            sambandhit= request.POST.get('sambandhit',''),
            upvidhi = request.POST.get('upvidhi',''),
            padadhi_info= request.POST.get('padadhi_info',''),
            gruhpal_info = request.POST.get('gruhpal_info',''),
            anubhav = request.POST.get('anubhav',''),
            sanstha_swarup = request.POST.get('sanstha_swarup',''),
            sanstha_prakar = request.POST.get('sanstha_prakar',''),
            manya_sanstha = request.POST.get('manya_sanstha',''),
            pratyaksha = request.POST.get('pratyaksha',''),
            lekha_pari = request.POST.get('lekha_pari',''),
            varshik_aha= request.POST.get('varshik_aha',''),
            shreni = request.POST.get('shreni',''),
            upkram = request.POST.get('upkram',''),
            swatantra_lekha = request.POST.get('swatantra_lekha',''),           
            sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
            vidy_sarva = request.POST.get('vidy_sarva',''),
            sansthemarfat = request.POST.get('sansthemarfat',''),
            pari_name1 = request.POST.get('pari_name1',''),
            pari_name2 = request.POST.get('pari_name2',''),
            pari_name3 = request.POST.get('pari_name3',''),
            from1 = request.POST.get('from1',''),
            from2 = request.POST.get('from2',''),
            from3 = request.POST.get('from3',''),
            pari_date1 = request.POST.get('pari_date1',''),
            pari_date2 = request.POST.get('pari_date2',''),
            pari_date3 = request.POST.get('pari_date3',''),
            sadar_sansthes = request.POST.get('sadar_sansthes',''),           
            sansthevirudha = request.POST.get('sansthevirudha',''),
            sansthemdhe = request.POST.get('sansthemdhe',''),
            vishbadha = request.POST.get('vishbadha',''),
            dakhla = request.FILES.get('dakhla',''),
            sansth_niyantran = request.POST.get('sansth_niyantran',''),
            shera = request.POST.get('shera',''),
            name2 = request.POST.get('name2',''),           
            signature = request.FILES.get('sign',''),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
def gayak(request,pk):
    print('entered in api 1')
    if gayakvad.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = gayakvad.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.jilha_name= request.POST.get('jilha_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.paripurn_patta = request.POST.get('paripurn_patta',''),
                x.adhi1_date = request.POST.get('adhi1_date',''),
                x.adhi2_date = request.POST.get('adhi2_date',''),
                x.adhi1 = request.POST.get('adhi1',''),
                x.adhi2 = request.POST.get('adhi2',''),
                x.sambandhit= request.POST.get('sambandhit',''),
                x.upvidhi = request.POST.get('upvidhi',''),
                x.padadhi1_name= request.POST.get('padadhi1_name',''),
                x.padadhi2_name = request.POST.get('padadhi2_name',''),
                x.mob1 = request.POST.get('mob1',''),
                x.mob2 = request.POST.get('mob2',''),
                x.arj_pur = request.POST.get('arj_pur',''),
                x.anubhav = request.POST.get('anubhav',''),
                x.lekha_pari = request.POST.get('lekha_pari',''),
                x.varshik_aha= request.POST.get('varshik_aha',''),
                x.swatantra_lekha = request.POST.get('swatantra_lekha',''),           
                x.sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
                x.upkram = request.POST.get('upkram',''),
                x.vyaktigat = request.POST.get('vyaktigat',''),
                x.sadar_sansthes = request.POST.get('sadar_sansthes',''),
                x.vaishishtya = request.POST.get('vaishishtya',''),
                x.vaishishtya1 = request.FILES.get('vaishishtya1',''),
                x.dakhla = request.FILES.get('dakhla',''),
                x.name2 = request.POST.get('name2',''),           
                x.pari_name1 = request.POST.get('pari_name1',''),
                x.pari_name2 = request.POST.get('pari_name2',''),
                x.pari_name3 = request.POST.get('pari_name3',''),
                x.from1 = request.POST.get('from1',''),
                x.from2 = request.POST.get('from2',''),
                x.from3 = request.POST.get('from3',''),
                x.pari_date1 = request.POST.get('pari_date1',''),
                x.pari_date2 = request.POST.get('pari_date2',''),
                x.pari_date3 = request.POST.get('pari_date3',''),
                x.signature = request.FILES.get('sign',''),
                x.save()
    else:
        x = gayakvad(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            jilha_name= request.POST.get('jilha_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            paripurn_patta = request.POST.get('paripurn_patta',''),
            adhi1_date = request.POST.get('adhi1_date',''),
            adhi2_date = request.POST.get('adhi2_date',''),
            adhi1 = request.POST.get('adhi1',''),
            adhi2 = request.POST.get('adhi2',''),
            sambandhit= request.POST.get('sambandhit',''),
            upvidhi = request.POST.get('upvidhi',''),
            padadhi1_name= request.POST.get('padadhi1_name',''),
            padadhi2_name = request.POST.get('padadhi2_name',''),
            mob1 = request.POST.get('mob1',''),
            mob2 = request.POST.get('mob2',''),
            arj_pur = request.POST.get('arj_pur',''),
            anubhav = request.POST.get('anubhav',''),
            lekha_pari = request.POST.get('lekha_pari',''),
            varshik_aha= request.POST.get('varshik_aha',''),
            swatantra_lekha = request.POST.get('swatantra_lekha',''),           
            sambandhit_sanstha = request.POST.get('sambandhit_sanstha',''),
            upkram = request.POST.get('upkram',''),
            vyaktigat = request.POST.get('vyaktigat',''),
            sadar_sansthes = request.POST.get('sadar_sansthes',''),
            vaishishtya = request.POST.get('vaishishtya',''),
            vaishishtya1 = request.FILES.get('vaishishtya1',''),
            dakhla = request.FILES.get('dakhla',''),
            name2 = request.POST.get('name2',''),           
            pari_name1 = request.POST.get('pari_name1',''),
            pari_name2 = request.POST.get('pari_name2',''),
            pari_name3 = request.POST.get('pari_name3',''),
            from1 = request.POST.get('from1',''),
            from2 = request.POST.get('from2',''),
            from3 = request.POST.get('from3',''),
            pari_date1 = request.POST.get('pari_date1',''),
            pari_date2 = request.POST.get('pari_date2',''),
            pari_date3 = request.POST.get('pari_date3',''),
            signature = request.FILES.get('sign',''),
            )
       
        x.save()
    return JsonResponse({'status':200})


def swadhhar(request,pk):
    print('entered in api 1')
    if swadhar_yoj.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = swadhar_yoj.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.place1= request.POST.get('place1',''),
                x.end_date1= request.POST.get('end_date1',''),
                x.arjname= request.POST.get('arjname',''),
                x.mob_number = request.POST.get('mob_number',''),
                x.adhar = request.POST.get('adhar',''),
                x.signature1 = request.FILES.get('signature1',''),
                x.photo = request.FILES.get('photo',''),
                x.name = request.POST.get('name',''),
                x.sur_name = request.POST.get('sur_name',''),
                x.fa_name = request.POST.get('fa_name',''),
                x.name1 = request.POST.get('name1',''),
                x.sur_name1= request.POST.get('sur_name1',''),
                x.fa_name1 = request.POST.get('fa_name1',''),
                x.hus_name= request.POST.get('hus_name',''),
                x.mo_name = request.POST.get('mo_name',''),
                x.pravarg = request.POST.get('pravarg',''),
                x.pot = request.POST.get('pot',''),
                x.ghar_kr = request.POST.get('ghar_kr',''),
                x.rasta = request.POST.get('rasta',''),
                x.khun = request.POST.get('khun',''),
                x.gav = request.POST.get('gav',''),
                x.taluka = request.POST.get('taluka',''),
                x.jilha= request.POST.get('jilha',''),
                x.pin = request.POST.get('pin',''),
                x.praman = request.POST.get('praman',''),
                x.dakhla_date = request.POST.get('dakhla_date',''),           
                x.karya_name = request.POST.get('karya_name',''),
                x.mobile_number = request.POST.get('mobile_number',''),
                x.divyang = request.POST.get('divyang',''),
                x.jilha_name = request.POST.get('jilha_name',''),
                x.praman1 = request.POST.get('praman1',''),
                x.jari_date = request.POST.get('jari_date',''),
                x.jat = request.POST.get('jat',''),
                x.gav1 = request.POST.get('gav1',''),
                x.taluka1 = request.POST.get('taluka1',''),
                x.jilha1 = request.POST.get('jilha1',''),
                x.adhar_card_no = request.POST.get('adhar_card_no',''),
                x.adhar_patta = request.POST.get('adhar_patta',''),
                x.bank_name = request.POST.get('bank_name',''),           
                x.shakha = request.POST.get('shakha',''),
                x.acc_no = request.POST.get('acc_no',''),
                x.ifsc = request.POST.get('ifsc',''),
                x.purava = request.FILES.get('purava',''),
                x.maha_name = request.POST.get('maha_name',''),
                x.maha_patta = request.POST.get('maha_patta',''),
                x.idno = request.POST.get('idno',''),
                x.abhyas_name = request.POST.get('abhyas_name',''),
                x.year = request.POST.get('year',''),           
                x.pravesh_date = request.POST.get('pravesh_date',''),
                x.kalavadhi = request.POST.get('kalavadhi',''),
                x.graduation = request.POST.get('graduation',''),
                x.pravesh_date1 = request.POST.get('pravesh_date1',''),
                x.uttirna = request.POST.get('uttirna',''),
                x.ekun_gun = request.POST.get('ekun_gun',''),
                x.prapta_gun = request.POST.get('prapta_gun',''),
                x.takka = request.POST.get('takka',''),
                x.pravesh_date2 = request.POST.get('pravesh_date2',''),
                x.uttirna1 = request.POST.get('uttirna1',''),
                x.ekun_gun1 = request.POST.get('ekun_gun1',''),
                x.prapta_gun1 = request.POST.get('prapta_gun1',''),
                x.takka1 = request.POST.get('takka1',''),
                x.pravesh_date3 = request.POST.get('pravesh_date3',''),
                x.uttirna2 = request.POST.get('uttirna2',''),
                x.ekun_gun2 = request.POST.get('ekun_gun2',''),
                x.prapta_gun2 = request.POST.get('prapta_gun2',''),
                x.takka2 = request.POST.get('takka2',''),
                x.fee = request.POST.get('fee',''),
                x.userid = request.POST.get('userid',''),
                x.palak_name = request.POST.get('palak_name',''),
                x.nate = request.POST.get('nate',''),
                x.mrutyu_purava = request.FILES.get('mrutyu_purava',''),
                x.business = request.POST.get('business',''),
                x.business_patta = request.POST.get('business_patta',''),
                x.income = request.POST.get('income',''),
                x.income_yr = request.POST.get('income_yr',''),
                x.place = request.POST.get('place',''),
                x.end_date = request.POST.get('end_date',''),
                x.sakshi1 = request.POST.get('sakshi1',''),
                x.sakshi2 = request.POST.get('sakshi2',''),
                x.sakshi1_sign = request.FILES.get('sakshi1_sign',''),
                x.sakshi2_sign = request.FILES.get('sakshi2_sign',''),
                x.signature = request.FILES.get('signature',''),
                x.save()
    else:
        x = swadhar_yoj(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            place1= request.POST.get('place1',''),
            end_date1= request.POST.get('end_date1',''),
            arjname= request.POST.get('arjname',''),
            mob_number = request.POST.get('mob_number',''),
            adhar = request.POST.get('adhar',''),
            signature1 = request.FILES.get('signature1',''),
            photo = request.FILES.get('photo',''),
            name = request.POST.get('name',''),
            sur_name = request.POST.get('sur_name',''),
            fa_name = request.POST.get('fa_name',''),
            name1 = request.POST.get('name1',''),
            sur_name1= request.POST.get('sur_name1',''),
            fa_name1 = request.POST.get('fa_name1',''),
            hus_name= request.POST.get('hus_name',''),
            mo_name = request.POST.get('mo_name',''),
            pravarg = request.POST.get('pravarg',''),
            pot = request.POST.get('pot',''),
            ghar_kr = request.POST.get('ghar_kr',''),
            rasta = request.POST.get('rasta',''),
            khun = request.POST.get('khun',''),
            gav = request.POST.get('gav',''),
            taluka = request.POST.get('taluka',''),
            jilha= request.POST.get('jilha',''),
            pin = request.POST.get('pin',''),
            praman = request.POST.get('praman',''),
            dakhla_date = request.POST.get('dakhla_date',''),           
            karya_name = request.POST.get('karya_name',''),
            mobile_number = request.POST.get('mobile_number',''),
            divyang = request.POST.get('divyang',''),
            jilha_name = request.POST.get('jilha_name',''),
            praman1 = request.POST.get('praman1',''),
            jari_date = request.POST.get('jari_date',''),
            jat = request.POST.get('jat',''),
            gav1 = request.POST.get('gav1',''),
            taluka1 = request.POST.get('taluka1',''),
            jilha1 = request.POST.get('jilha1',''),
            adhar_card_no = request.POST.get('adhar_card_no',''),
            adhar_patta = request.POST.get('adhar_patta',''),
            bank_name = request.POST.get('bank_name',''),           
            shakha = request.POST.get('shakha',''),
            acc_no = request.POST.get('acc_no',''),
            ifsc = request.POST.get('ifsc',''),
            purava = request.FILES.get('purava',''),
            maha_name = request.POST.get('maha_name',''),
            maha_patta = request.POST.get('maha_patta',''),
            idno = request.POST.get('idno',''),
            abhyas_name = request.POST.get('abhyas_name',''),
            year = request.POST.get('year',''),           
            pravesh_date = request.POST.get('pravesh_date',''),
            kalavadhi = request.POST.get('kalavadhi',''),
            graduation = request.POST.get('graduation',''),
            pravesh_date1 = request.POST.get('pravesh_date1',''),
            uttirna = request.POST.get('uttirna',''),
            ekun_gun = request.POST.get('ekun_gun',''),
            prapta_gun = request.POST.get('prapta_gun',''),
            takka = request.POST.get('takka',''),
            pravesh_date2 = request.POST.get('pravesh_date2',''),
            uttirna1 = request.POST.get('uttirna1',''),
            ekun_gun1 = request.POST.get('ekun_gun1',''),
            prapta_gun1 = request.POST.get('prapta_gun1',''),
            takka1 = request.POST.get('takka1',''),
            pravesh_date3 = request.POST.get('pravesh_date3',''),
            uttirna2 = request.POST.get('uttirna2',''),
            ekun_gun2 = request.POST.get('ekun_gun2',''),
            prapta_gun2 = request.POST.get('prapta_gun2',''),
            takka2 = request.POST.get('takka2',''),
            fee = request.POST.get('fee',''),
            userid = request.POST.get('userid',''),
            palak_name = request.POST.get('palak_name',''),
            nate = request.POST.get('nate',''),
            mrutyu_purava = request.FILES.get('mrutyu_purava',''),
            business = request.POST.get('business',''),
            business_patta = request.POST.get('business_patta',''),
            income = request.POST.get('income',''),
            income_yr = request.POST.get('income_yr',''),
            place = request.POST.get('place',''),
            end_date = request.POST.get('end_date',''),
            sakshi1 = request.POST.get('sakshi1',''),
            sakshi2 = request.POST.get('sakshi2',''),
            sakshi1_sign = request.FILES.get('sakshi1_sign',''),
            sakshi2_sign = request.FILES.get('sakshi2_sign',''),
            signature = request.FILES.get('signature',''),
            )
        x.save()
    return JsonResponse({'status':200})
    
def gatai_kam(request,pk):
    print('entered in api 1')
    if gatai_kamgar.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = gatai_kamgar.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.name= request.POST.get('name',''),
                x.fa_name= request.POST.get('fa_name',''),
                x.cu_address = request.POST.get('cu_address',''),
                x.pe_address = request.POST.get('pe_address',''),
                x.stall_address = request.POST.get('stall_address',''),
                x.jaga_tapshil= request.FILES.get('jaga_tapshil',''),
                x.loksankhya= request.POST.get('loksankhya',''),
                x.mobile_number= request.POST.get('mobile_number',''),
                x.birth_date = request.POST.get('birth_date',''),
                x.birth_place= request.POST.get('birth_place',''),
                x.age = request.POST.get('age',''),
                x.caste = request.POST.get('caste',''),
                x.pot_caste = request.POST.get('pot_caste',''),
                x.education = request.POST.get('education',''),
                x.income = request.POST.get('income',''),
                x.business = request.POST.get('business',''),
                x.fa_business = request.POST.get('fa_business',''),
                x.ration_no= request.POST.get('ration_no',''),
                x.photo = request.FILES.get('photo',''),
                x.signature = request.FILES.get('signature',''),
                x.apply_date = request.POST.get('apply_date',''),
                x.name_1= request.POST.get('name_1',''),
                x.vykti_name = request.POST.get('vykti_name',''),
                x.age1= request.POST.get('age1',''),
                x.nate = request.POST.get('nate',''),
                x.nokri = request.POST.get('nokri',''),
                x.masik_utpanna = request.POST.get('masik_utpanna',''),
                x.varshik_utpanna = request.POST.get('varshik_utpanna',''),
                x.vykti_name1 = request.POST.get('vykti_name1',''),
                x.age2 = request.POST.get('age2',''),
                x.nate1 = request.POST.get('nate1',''),
                x.nokri1= request.POST.get('nokri1',''),
                x.masik_utpanna1 = request.POST.get('masik_utpanna1',''),
                x.varshik_utpanna1 = request.POST.get('varshik_utpanna1',''),
                x.vykti_name2 = request.POST.get('vykti_name2',''),
                x.age3 = request.POST.get('age3',''),
                x.nate2 = request.POST.get('nate2',''),
                x.nokri2= request.POST.get('nokri2',''),
                x.masik_utpanna2 = request.POST.get('masik_utpanna2',''),
                x.varshik_utpanna2 = request.POST.get('varshik_utpanna2',''),
                x.vykti_name3 = request.POST.get('vykti_name3',''),
                x.age4 = request.POST.get('age4',''),
                x.nate3 = request.POST.get('nate3',''),
                x.bank_name3= request.POST.get('bank_name3',''),
                x.karj3 = request.POST.get('karj3',''),
                x.thakbaki3 = request.POST.get('thakbaki3',''),
                x.mahamandal3 = request.POST.get('mahamandal3',''),
                x.thakbaki_3 = request.POST.get('thakbaki_3',''),
                x.vykti_name4 = request.POST.get('vykti_name4',''),
                x.age5 = request.POST.get('age5',''),
                x.nate4 = request.POST.get('nate4',''),
                x.bank_name4= request.POST.get('bank_name4',''),
                x.karj4 = request.POST.get('karj4',''),
                x.thakbaki4 = request.POST.get('thakbaki4',''),
                x.mahamandal4 = request.POST.get('mahamandal4',''),
                x.thakbaki_4 = request.POST.get('thakbaki_4',''),
                x.vykti_name5 = request.POST.get('vykti_name5',''),
                x.age6 = request.POST.get('age6',''),
                x.nate5 = request.POST.get('nate5',''),
                x.bank_name5= request.POST.get('bank_name5',''),
                x.karj5 = request.POST.get('karj5',''),
                x.thakbaki5 = request.POST.get('thakbaki5',''),
                x.mahamandal5 = request.POST.get('mahamandal5',''),
                x.thakbaki_5 = request.POST.get('thakbaki_5',''),
                x.vykti_name6 = request.POST.get('vykti_name6',''),
                x.age7 = request.POST.get('age7',''),
                x.nate6 = request.POST.get('nate6',''),
                x.bank_name6= request.POST.get('bank_name6',''),
                x.karj6 = request.POST.get('karj6',''),
                x.thakbaki6 = request.POST.get('thakbaki6',''),
                x.mahamandal6 = request.POST.get('mahamandal6',''),
                x.thakbaki_6 = request.POST.get('thakbaki_6',''),
                x.save()
    else:
        x = gatai_kamgar(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            name= request.POST.get('name',''),
            fa_name= request.POST.get('fa_name',''),
            cu_address = request.POST.get('cu_address',''),
            pe_address = request.POST.get('pe_address',''),
            stall_address = request.POST.get('stall_address',''),
            jaga_tapshil= request.FILES.get('jaga_tapshil',''),
            loksankhya= request.POST.get('loksankhya',''),
            mobile_number= request.POST.get('mobile_number',''),
            birth_date = request.POST.get('birth_date',''),
            birth_place= request.POST.get('birth_place',''),
            age = request.POST.get('age',''),
            caste = request.POST.get('caste',''),
            pot_caste = request.POST.get('pot_caste',''),
            education = request.POST.get('education',''),
            income = request.POST.get('income',''),
            business = request.POST.get('business',''),
            fa_business = request.POST.get('fa_business',''),
            ration_no= request.POST.get('ration_no',''),
            photo = request.FILES.get('photo',''),
            signature = request.FILES.get('signature',''),
            apply_date = request.POST.get('apply_date',''),
            name_1= request.POST.get('name_1',''),
            vykti_name = request.POST.get('vykti_name',''),
            age1= request.POST.get('age1',''),
            nate = request.POST.get('nate',''),
            nokri = request.POST.get('nokri',''),
            masik_utpanna = request.POST.get('masik_utpanna',''),
            varshik_utpanna = request.POST.get('varshik_utpanna',''),
            vykti_name1 = request.POST.get('vykti_name1',''),
            age2 = request.POST.get('age2',''),
            nate1 = request.POST.get('nate1',''),
            nokri1= request.POST.get('nokri1',''),
            masik_utpanna1 = request.POST.get('masik_utpanna1',''),
            varshik_utpanna1 = request.POST.get('varshik_utpanna1',''),
            vykti_name2 = request.POST.get('vykti_name2',''),
            age3 = request.POST.get('age3',''),
            nate2 = request.POST.get('nate2',''),
            nokri2= request.POST.get('nokri2',''),
            masik_utpanna2 = request.POST.get('masik_utpanna2',''),
            varshik_utpanna2 = request.POST.get('varshik_utpanna2',''),
            vykti_name3 = request.POST.get('vykti_name3',''),
            age4 = request.POST.get('age4',''),
            nate3 = request.POST.get('nate3',''),
            bank_name3= request.POST.get('bank_name3',''),
            karj3 = request.POST.get('karj3',''),
            thakbaki3 = request.POST.get('thakbaki3',''),
            mahamandal3 = request.POST.get('mahamandal3',''),
            thakbaki_3 = request.POST.get('thakbaki_3',''),
            vykti_name4 = request.POST.get('vykti_name4',''),
            age5 = request.POST.get('age5',''),
            nate4 = request.POST.get('nate4',''),
            bank_name4= request.POST.get('bank_name4',''),
            karj4 = request.POST.get('karj4',''),
            thakbaki4 = request.POST.get('thakbaki4',''),
            mahamandal4 = request.POST.get('mahamandal4',''),
            thakbaki_4 = request.POST.get('thakbaki_4',''),
            vykti_name5 = request.POST.get('vykti_name5',''),
            age6 = request.POST.get('age6',''),
            nate5 = request.POST.get('nate5',''),
            bank_name5= request.POST.get('bank_name5',''),
            karj5 = request.POST.get('karj5',''),
            thakbaki5 = request.POST.get('thakbaki5',''),
            mahamandal5 = request.POST.get('mahamandal5',''),
            thakbaki_5 = request.POST.get('thakbaki_5',''),
            vykti_name6 = request.POST.get('vykti_name6',''),
            age7 = request.POST.get('age7',''),
            nate6 = request.POST.get('nate6',''),
            bank_name6= request.POST.get('bank_name6',''),
            karj6 = request.POST.get('karj6',''),
            thakbaki6 = request.POST.get('thakbaki6',''),
            mahamandal6 = request.POST.get('mahamandal6',''),
            thakbaki_6 = request.POST.get('thakbaki_6',''),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
# def rojgar_hami(request,pk):
#     print('hi')
#     if hami_yojna.objects.filter(user=request.user,
#         scheme=SchemeModel.objects.get(pk=pk)).exists():
#         x = hami_yojna.objects.get(user=request.user,
#         scheme=SchemeModel.objects.get(pk=pk))
#         x.karyalay1=request.POST.get('karyalay1'),
#         x.mobile_number=request.POST.get('mobile_number'),
#         x.form_date=request.POST.get('form_date'),
#         x.karyalay2=request.POST.get('karyalay2'),
#         x.yoj_name=request.POST.get('yoj_name'),
#         x.name=request.POST.get('name'),
#         x.gender=request.POST.get('gender'),
#         x.birth_date=request.POST.get('birth_date'),
#         x.jat = request.POST.get('jat'),
#         x.mu_post = request.POST.get('mu_post'),
#         x.taluka=request.POST.get('taluka'),
#         x.jilha = request.POST.get('jilha'),
#         x.mobile_number1 = request.POST.get('mobile_number1'),
#         x.adhaar_no=request.POST.get('adhaar_no'),
#         x.education = request.POST.get('education'),
#         x.bank_name=request.POST.get('bank_name'),
#         x.khate_kr=request.POST.get('khate_kr'),
#         x.shakha = request.POST.get('shakha'),
#         x.ifsc = request.POST.get('ifsc'),
#         x.jamin_prakar=request.POST.get('jamin_prakar'),
#         x.gat_kr = request.POST.get('gat_kr'),
#         x.kshetra = request.POST.get('kshetra'),
#         x.pike=request.POST.get('pike'),
#         x.tuti_kshetra = request.POST.get('tuti_kshetra'),
#         x.sinchan=request.POST.get('sinchan'),
#         x.sinchan_kalavadhi=request.POST.get('sinchan_kalavadhi'),
        
#         if request.POST.get('vij') == '0':
#             x.vij_jodni = True
#         else:
#             x.vij_jodni = False
#         x.signature = request.FILES.get('signature')
#         if request.POST.get('gru') == '0':
#             x.gruh_vyavstha = True
#         else:
#             x.gruh_vyavstha = False
#         x.shetkari_varg=request.POST.get('shetkari_varg'),
#         if request.POST.get('maj') == '0':
#             x.majur = True
#         else:
#             x.majur = False
#         x.bplkard=request.POST.get('bplkard'),
#         if request.POST.get('dar') == '0':
#             x.daridrya = True
#         else:
#             x.daridrya = False
#         x.shri=request.POST.get('shri'),
#         if request.POST.get('non') == '0':
#             x.nondani_fee = True
#         else:
#             x.nondani_fee = False
#         x.padnam = request.POST.get('padnam'),
#         x.karyalay3=request.POST.get('karyalay3'),
#         x.shetkari_name=request.POST.get('shetkari_name'),
#         # x.umedwar_sign=request.FILES.get('umedwar_sign')
#         x.save()
#     else:
#         x= hami_yojna(
#         user=request.user,
#         scheme=SchemeModel.objects.get(pk=pk),
#         karyalay1=request.POST.get('karyalay1'),
#         mobile_number=request.POST.get('mobile_number'),
#         form_date=request.POST.get('form_date'),
#         karyalay2=request.POST.get('karyalay2'),
#         yoj_name=request.POST.get('yoj_name'),
#         name=request.POST.get('name'),
#         gender=request.POST.get('gender'),
#         birth_date=request.POST.get('birth_date'),
#         jat = request.POST.get('jat'),
#         mu_post = request.POST.get('mu_post'),
#         taluka=request.POST.get('taluka'),
#         jilha = request.POST.get('jilha'),
#         mobile_number1 = request.POST.get('mobile_number1'),
#         adhaar_no=request.POST.get('adhaar_no'),
#         education = request.POST.get('education'),
#         bank_name=request.POST.get('bank_name'),
#         khate_kr=request.POST.get('khate_kr'),
#         shakha = request.POST.get('shakha'),
#         ifsc = request.POST.get('ifsc'),
#         jamin_prakar=request.POST.get('jamin_prakar'),
#         gat_kr = request.POST.get('gat_kr'),
#         kshetra = request.POST.get('kshetra'),
#         pike=request.POST.get('pike'),
#         tuti_kshetra = request.POST.get('tuti_kshetra'),
#         sinchan=request.POST.get('sinchan'),
#         sinchan_kalavadhi=request.POST.get('sinchan_kalavadhi'),
#         signature = request.FILES.get('signature'),
#         shetkari_varg=request.POST.get('shetkari_varg'),
#         bplkard=request.POST.get('bplkard'),
#         shri=request.POST.get('shri'),
#         padnam = request.POST.get('padnam'),
#         karyalay3=request.POST.get('karyalay3'),
#         shetkari_name=request.POST.get('shetkari_name')
#         )
#         if request.POST.get('vij') == '0':
#             x.vij_jodni = True
#         else:
#             x.vij_jodni = False
#         x.save()
#         print("X: ",x)
#         if request.POST.get('gru') == '0':
#             x.gruh_vyavstha = True
#         else:
#             x.gruh_vyavstha = False
#         x.save()
#         print("X: ",x)
#         if request.POST.get('maj') == '0':
#             x.majur = True
#         else:
#             x.majur = False
#         x.save()
#         print("X: ",x)
#         if request.POST.get('dar') == '0':
#             x.daridrya = True
#         else:
#             x.daridrya = False
#         x.save()
#         print("X: ",x)
#         if request.POST.get('non') == '0':
#             x.nondani_fee = True
#         else:
#             x.nondani_fee = False
#         x.save()
#         print("X: ",x)
#     return JsonResponse({'status':200})
    
def vai_sabha(request,pk):
    print('entered in api 1')
    if vaiyaktik_sabhasad.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = vaiyaktik_sabhasad.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.shri= request.POST.get('shri'),
                x.form_date= request.POST.get('form_date'),
                x.name3 = request.POST.get('name3',''),
                x.form_date1 = request.POST.get('form_date1'),
                x.name = request.POST.get('name',''),
                x.birth_date= request.POST.get('birth_date'),
                x.patta = request.POST.get('patta'),
                x.mobile_number= request.POST.get('mobile_number'),
                x.email_id = request.POST.get('email_id'),
                x.patta1 = request.POST.get('patta1'),
                x.business = request.POST.get('business'),
                x.name1 = request.POST.get('name1',''),
                x.patta2 = request.POST.get('patta2',''),
                x.mobile_number1 = request.POST.get('mobile_number1'),
                x.photo = request.FILES.get('photo',''),
                x.singh = request.FILES.get('singh'),
                x.save()
    else:
        x = vaiyaktik_sabhasad(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            shri= request.POST.get('shri'),
            form_date= request.POST.get('form_date'),
            name3 = request.POST.get('name3'),
            form_date1 = request.POST.get('form_date1'),
            name = request.POST.get('name'),
            birth_date= request.POST.get('birth_date'),
            patta = request.POST.get('patta'),
            mobile_number= request.POST.get('mobile_number'),
            email_id = request.POST.get('email_id'),
            patta1 = request.POST.get('patta1'),
            business = request.POST.get('business'),
            name1 = request.POST.get('name1'),
            patta2 = request.POST.get('patta2'),
            mobile_number1 = request.POST.get('mobile_number1'),
            photo = request.FILES.get('photo'),
            singh = request.FILES.get('singh'),
            )
       
        x.save()
    return JsonResponse({'status':200})

def sanstha_sabha(request,pk):
    print('entered in api 1')
    if sanstha_sabhasad.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = sanstha_sabhasad.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.sansname= request.POST.get('sansname'),
                x.form_date= request.POST.get('form_date'),
                x.name3 = request.POST.get('name3',''),
                x.form_date1 = request.POST.get('form_date1'),
                x.sansthaname = request.POST.get('sansthaname',''),
                x.patta= request.POST.get('patta'),
                x.non_kr = request.POST.get('non_kr'),
                x.sachivname1= request.POST.get('sachivname1'),
                x.patta2 = request.POST.get('patta2'),
                x.granth_sankhya = request.POST.get('granth_sankhya'),
                x.sabh_sankhya = request.POST.get('sabh_sankhya'),
                x.devghevi = request.POST.get('devghevi',''),
                x.tharav_kr = request.POST.get('tharav_kr',''),
                x.tharav_date = request.POST.get('tharav_date'),
                x.karya_sadasya1 = request.POST.get('karya_sadasya1'),
                x.karya_sadasya2 = request.POST.get('karya_sadasya2'),
                x.karya_sadasya3 = request.POST.get('karya_sadasya3'),
                x.karya_sadasya4 = request.POST.get('karya_sadasya4',''),
                x.karya_sadasya5 = request.POST.get('karya_sadasya5',''),
                x.karya_sadasya6 = request.POST.get('karya_sadasya6'),
                x.karya_sadasya7 = request.POST.get('karya_sadasya7'),
                x.itar = request.POST.get('itar'),
                x.shri = request.POST.get('shri'),
                x.satyaprat = request.FILES.get('satyaprat',''),
                x.singh = request.FILES.get('singh'),
                x.satyaprat1 = request.FILES.get('satyaprat1'),
                x.shikka = request.FILES.get('shikka',''),
                x.save()
    else:
        x = sanstha_sabhasad(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            sansname= request.POST.get('sansname'),
            form_date= request.POST.get('form_date'),
            name3 = request.POST.get('name3',''),
            form_date1 = request.POST.get('form_date1'),
            sansthaname = request.POST.get('sansthaname',''),
            patta= request.POST.get('patta'),
            non_kr = request.POST.get('non_kr'),
            sachivname1= request.POST.get('sachivname1'),
            patta2 = request.POST.get('patta2'),
            granth_sankhya = request.POST.get('granth_sankhya'),
            sabh_sankhya = request.POST.get('sabh_sankhya'),
            devghevi = request.POST.get('devghevi',''),
            tharav_kr = request.POST.get('tharav_kr',''),
            tharav_date = request.POST.get('tharav_date'),
            karya_sadasya1 = request.POST.get('karya_sadasya1'),
            karya_sadasya2 = request.POST.get('karya_sadasya2'),
            karya_sadasya3 = request.POST.get('karya_sadasya3'),
            karya_sadasya4 = request.POST.get('karya_sadasya4',''),
            karya_sadasya5 = request.POST.get('karya_sadasya5',''),
            karya_sadasya6 = request.POST.get('karya_sadasya6'),
            karya_sadasya7 = request.POST.get('karya_sadasya7'),
            itar = request.POST.get('itar'),
            shri = request.POST.get('shri'),
            satyaprat = request.FILES.get('satyaprat',''),
            singh = request.FILES.get('singh'),
            satyaprat1 = request.FILES.get('satyaprat1'),
            shikka = request.FILES.get('shikka',''),
            )
       
        x.save()
    return JsonResponse({'status':200})

def arthasahayy(request,pk):
    print('entered in api 1')
    if masemari_arth.objects.filter(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk)).exists():
                x = masemari_arth.objects.get(user=request.user,
                scheme=SchemeModel.objects.get(pk=pk))
                x.san= request.POST.get('san'),
                x.talav= request.POST.get('talav'),
                x.ekun = request.POST.get('ekun',),
                x.sabhasad = request.POST.get('sabhasad'),
                x.name = request.POST.get('name'),
                x.sahi = request.FILES.get('sahi'),
                x.save()
    else:
        x = masemari_arth(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
            san= request.POST.get('san'),
            talav= request.POST.get('talav'),
            ekun = request.POST.get('ekun',),
            sabhasad = request.POST.get('sabhasad'),
            name = request.POST.get('name'),
            sahi = request.FILES.get('sahi'),
            )
       
        x.save()
    return JsonResponse({'status':200})
    
def pradhan_pmmsy(request,pk):
    print('hi')
    if matsyasampada.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = matsyasampada.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.own=request.POST.get('own'),
        x.lease=request.POST.get('lease'),
        x.trained=request.POST.get('trained'),
        x.experienced=request.POST.get('experienced'),
        x.benificiaries=request.POST.get('benificiaries'),
        x.category=request.POST.get('category'),
        x.door=request.POST.get('door'),
        x.village=request.POST.get('village'),
        x.dis=request.POST.get('dis'),
        x.state=request.POST.get('state'),
        x.pin=request.POST.get('pin'),
        x.area = request.POST.get('area'),
        x.period = request.POST.get('period'),
        x.site_addr = request.POST.get('site_addr'),
        x.village1=request.POST.get('village1'),
        x.dis1 = request.POST.get('dis1'),
        x.state1=request.POST.get('state1'),
        x.pin1=request.POST.get('pin1'),
        x.land_no = request.POST.get('land_no'),
        x.mobile = request.POST.get('mobile'),
        x.email_id=request.POST.get('email_id'),
        x.total = request.POST.get('total'),
        x.gen = request.POST.get('gen'),
        x.sc=request.POST.get('sc'),
        x.st = request.POST.get('st'),
        x.women=request.POST.get('women'),
        x.govt=request.POST.get('govt'),
        x.total1=request.POST.get('total1'),
        x.gen1=request.POST.get('gen1'),
        x.sc1=request.POST.get('sc1'),
        x.st1 = request.POST.get('st1'),
        x.women1 = request.POST.get('women1'),
        x.govt1 = request.POST.get('govt1'),
        x.total2=request.POST.get('total2'),
        x.gen2 = request.POST.get('gen2'),
        x.sc2=request.POST.get('sc2'),
        x.st2=request.POST.get('st2'),
        x.women2 = request.POST.get('women2'),
        x.govt2 = request.POST.get('govt2'),
        x.pro_item=request.POST.get('pro_item'),
        x.type_pro = request.POST.get('type_pro'),
        x.pre_inv = request.POST.get('pre_inv'),
        x.subcompo= request.POST.getlist('subcompo[]'),
        x.activity = request.POST.get('activity'),
        x.capacity=request.POST.get('capacity'),
        x.capital_details = request.POST.get('capital_details'),
        x.nounits=request.POST.get('nounits'),
        x.unitcost=request.POST.get('unitcost'),
        x.tocost = request.POST.get('tocost'),
        x.operation_details=request.POST.get('operation_details'),
        x.nounits1 = request.POST.get('nounits1'),
        x.unitcost1 = request.POST.get('unitcost1'),
        x.tocost1 = request.POST.get('tocost1'),
        x.total_details=request.POST.get('total_details'),
        x.nounits2 = request.POST.get('nounits2'),
        x.unitcost2=request.POST.get('unitcost2'),
        x.tocost2=request.POST.get('tocost2'),
        x.sig = request.FILES.get('sig')
        x.photo = request.FILES.get('photo')
        x.banking_assi=request.POST.get('banking_assi'),
        x.parti_bank=request.POST.get('parti_bank'),
        x.name1 = request.POST.get('name1'),
        x.name2=request.POST.get('name2'),
        x.name3=request.POST.get('name3'),
        x.state_contri=request.POST.get('state_contri'),
        x.beni_contri=request.POST.get('beni_contri'),
        x.save()
    else:
        x= matsyasampada(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        own=request.POST.get('own'),
        lease=request.POST.get('lease'),
        trained=request.POST.get('trained'),
        experienced=request.POST.get('experienced'),
        benificiaries=request.POST.get('benificiaries'),
        category=request.POST.get('category'),
        door=request.POST.get('door'),
        village=request.POST.get('village'),
        dis=request.POST.get('dis'),
        state=request.POST.get('state'),
        pin=request.POST.get('pin'),
        area = request.POST.get('area'),
        period = request.POST.get('period'),
        site_addr = request.POST.get('site_addr'),
        village1=request.POST.get('village1'),
        dis1 = request.POST.get('dis1'),
        state1=request.POST.get('state1'),
        pin1=request.POST.get('pin1'),
        land_no = request.POST.get('land_no'),
        mobile = request.POST.get('mobile'),
        email_id=request.POST.get('email_id'),
        total = request.POST.get('total'),
        gen = request.POST.get('gen'),
        sc=request.POST.get('sc'),
        st = request.POST.get('st'),
        women=request.POST.get('women'),
        govt=request.POST.get('govt'),
        total1=request.POST.get('total1'),
        gen1=request.POST.get('gen1'),
        sc1=request.POST.get('sc1'),
        st1 = request.POST.get('st1'),
        women1 = request.POST.get('women1'),
        govt1 = request.POST.get('govt1'),
        total2=request.POST.get('total2'),
        gen2 = request.POST.get('gen2'),
        sc2=request.POST.get('sc2'),
        st2=request.POST.get('st2'),
        women2 = request.POST.get('women2'),
        govt2 = request.POST.get('govt2'),
        pro_item=request.POST.get('pro_item'),
        pre_inv = request.POST.get('pre_inv'),
        type_pro = request.POST.get('type_pro'),
        subcompo= request.POST.getlist('subcompo[]'),
        activity = request.POST.get('activity'),
        capacity=request.POST.get('capacity'),
        capital_details = request.POST.get('capital_details'),
        nounits=request.POST.get('nounits'),
        unitcost=request.POST.get('unitcost'),
        tocost = request.POST.get('tocost'),
        operation_details=request.POST.get('operation_details'),
        nounits1 = request.POST.get('nounits1'),
        unitcost1 = request.POST.get('unitcost1'),
        tocost1 = request.POST.get('tocost1'),
        total_details=request.POST.get('total_details'),
        nounits2 = request.POST.get('nounits2'),
        unitcost2=request.POST.get('unitcost2'),
        tocost2=request.POST.get('tocost2'),
        sig = request.FILES.get('sig'),
        photo = request.FILES.get('photo'),
        banking_assi=request.POST.get('banking_assi'),
        parti_bank=request.POST.get('parti_bank'),
        name1 = request.POST.get('name1'),
        name2=request.POST.get('name2'),
        name3=request.POST.get('name3'),
        state_contri=request.POST.get('state_contri'),
        beni_contri=request.POST.get('beni_contri'),
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def polisbharti(request,pk):
    print('hi')
    if polis_bhartipurva.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = polis_bhartipurva.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.rahivasi=request.POST.get('rahivasi'),
        x.fa_name=request.POST.get('fa_name'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.paripurn_patta=request.POST.get('paripurn_patta'),
        x.dharma=request.POST.get('dharma'),
        x.dharma_dakhla=request.FILES.get('dharma_dakhla'),
        x.jat=request.POST.get('jat'),
        x.varshik_utpanna=request.POST.get('varshik_utpanna'),
        x.dakhla = request.FILES.get('dakhla'),
        x.rahi_dakhla=request.FILES.get('rahi_dakhla'),
        x.hsc = request.POST.get('hsc'),
        x.hsc_dakhla=request.FILES.get('hsc_dakhla'),
        x.unchi = request.POST.get('unchi'),
        x.chhati=request.POST.get('chhati'),
        x.fugvun = request.POST.get('fugvun'),
        x.seva_kard=request.POST.get('seva_kard'),
        x.birth_date=request.POST.get('birth_date'),
        x.birth_date1=request.POST.get('birth_date1'),
        x.varsh = request.POST.get('varsh'),
        x.mahina = request.POST.get('mahina'),
        x.divas=request.POST.get('divas'),
        x.signature=request.FILES.get('signature'),
        x.name1 = request.POST.get('name1'),
        x.form_date = request.POST.get('form_date'),
        x.mobile_number1=request.POST.get('mobile_number1'),
        # x.umedwar_sign=request.FILES.get('umedwar_sign')
        x.save()
    else:
        x= polis_bhartipurva(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        rahivasi=request.POST.get('rahivasi'),
        fa_name=request.POST.get('fa_name'),
        mobile_number=request.POST.get('mobile_number'),
        paripurn_patta=request.POST.get('paripurn_patta'),
        dharma=request.POST.get('dharma'),
        dharma_dakhla=request.FILES.get('dharma_dakhla'),
        jat=request.POST.get('jat'),
        varshik_utpanna=request.POST.get('varshik_utpanna'),
        dakhla = request.FILES.get('dakhla'),
        rahi_dakhla=request.FILES.get('rahi_dakhla'),
        hsc = request.POST.get('hsc'),
        hsc_dakhla=request.FILES.get('hsc_dakhla'),
        unchi = request.POST.get('unchi'),
        chhati=request.POST.get('chhati'),
        fugvun = request.POST.get('fugvun'),
        seva_kard=request.POST.get('seva_kard'),
        birth_date=request.POST.get('birth_date'),
        birth_date1=request.POST.get('birth_date1'),
        varsh = request.POST.get('varsh'),
        mahina = request.POST.get('mahina'),
        divas=request.POST.get('divas'),
        signature=request.FILES.get('signature'),
        name1 = request.POST.get('name1'),
        form_date = request.POST.get('form_date'),
        mobile_number1=request.POST.get('mobile_number1'),
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def zakir_husen(request,pk):
    print('hi')
    if zakir_hus.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = zakir_hus.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.madarsa_name=request.POST.get('madarsa_name'),
        x.madarsa_patta=request.POST.get('madarsa_patta'),
        x.malkichi=request.POST.get('malkichi'),
        x.upkram=request.POST.get('upkram'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.sanstha_name=request.POST.get('sanstha_name'),
        x.sanstha_patta=request.POST.get('sanstha_patta'),
        x.mobile_number1=request.POST.get('mobile_number1'),
        x.email_id1=request.POST.get('email_id1'),
        x.adhyaksh_name=request.POST.get('adhyaksh_name'),
        x.adhyaksh_patta=request.POST.get('adhyaksh_patta'),
        x.mobile_number2=request.POST.get('mobile_number2'),
        x.sachiv_name=request.POST.get('sachiv_name'),
        x.sachiv_patta=request.POST.get('sachiv_patta'),
        x.mobile_number3=request.POST.get('mobile_number3'),
        x.nondani_kr=request.POST.get('nondani_kr'),
        x.bank_name=request.POST.get('bank_name'),
        x.acc_no=request.POST.get('acc_no'),
        x.ifsc=request.POST.get('ifsc'),
        x.patsankhya=request.POST.get('patsankhya'),
        x.madhyam=request.POST.get('madhyam'),
        x.e_mahiti=request.POST.get('e_mahiti'),
        x.soi_suvidha=request.POST.get('soi_suvidha'),
        x.kho_sankhya1=request.POST.get('kho_sankhya1'),
        x.kho_sankhya2=request.POST.get('kho_sankhya2'),
        x.kho_sankhya3=request.POST.get('kho_sankhya3'),
        x.kho_sankhya4=request.POST.get('kho_sankhya4'),
        x.kshetrafal1=request.POST.get('kshetrafal1'),
        x.kshetrafal2=request.POST.get('kshetrafal2'),
        x.kshetrafal3=request.POST.get('kshetrafal3'),
        x.kshetrafal4=request.POST.get('kshetrafal4'),
        x.pinych_pani=request.POST.get('pinych_pani'),
        x.utara=request.FILES.get('utara'),
        x.tapshil=request.POST.get('tapshil'),
        x.nutanikaran1=request.POST.get('nutanikaran1'),
        x.nutanikaran2=request.POST.get('nutanikaran2'),
        x.nutanikaran3=request.POST.get('nutanikaran3'),
        x.nutanikaran4=request.POST.get('nutanikaran4'),
        x.dagduji1=request.POST.get('dagduji1'),
        x.dagduji2=request.POST.get('dagduji2'),
        x.dagduji3=request.POST.get('dagduji3'),
        x.dagduji4=request.POST.get('dagduji4'),
        x.chhat1=request.POST.get('chhat1'),
        x.chhat2=request.POST.get('chhat2'),
        x.chhat3=request.POST.get('chhat3'),
        x.chhat4=request.POST.get('chhat4'),
        x.farshi1=request.POST.get('farshi1'),
        x.farshi2=request.POST.get('farshi2'),
        x.farshi3=request.POST.get('farshi3'),
        x.farshi4=request.POST.get('farshi4'),
        x.itar1=request.POST.get('itar1'),
        x.itar2=request.POST.get('itar2'),
        x.itar3=request.POST.get('itar3'),
        x.itar4=request.POST.get('itar4'),
        x.kooler1=request.POST.get('kooler1'),
        x.kooler2=request.POST.get('kooler2'),
        x.kooler3=request.POST.get('kooler3'),
        x.kooler4=request.POST.get('kooler4'),
        x.swachhata1=request.POST.get('swachhata1'),
        x.swachhata2=request.POST.get('swachhata2'),
        x.swachhata3=request.POST.get('swachhata3'),
        x.swachhata4=request.POST.get('swachhata4'),
        x.swachhtagruhe1=request.POST.get('swachhtagruhe1'),
        x.swachhtagruhe2=request.POST.get('swachhtagruhe2'),
        x.swachhtagruhe3=request.POST.get('swachhtagruhe3'),
        x.swachhtagruhe4=request.POST.get('swachhtagruhe4'),
        x.furniture1=request.POST.get('furniture1'),
        x.furniture2=request.POST.get('furniture2'),
        x.furniture3=request.POST.get('furniture3'),
        x.furniture4=request.POST.get('furniture4'),
        x.benches1=request.POST.get('benches1'),
        x.benches2=request.POST.get('benches2'),
        x.benches3=request.POST.get('benches3'),
        x.benches4=request.POST.get('benches4'),
        x.inverter1=request.POST.get('inverter1'),
        x.inverter2=request.POST.get('inverter2'),
        x.inverter3=request.POST.get('inverter3'),
        x.inverter4=request.POST.get('inverter4'),
        x.imarat1=request.POST.get('imarat1'),
        x.imarat2=request.POST.get('imarat2'),
        x.imarat3=request.POST.get('imarat3'),
        x.imarat4=request.POST.get('imarat4'),
        x.sanganak1=request.POST.get('sanganak1'),
        x.sanganak2=request.POST.get('sanganak2'),
        x.sanganak3=request.POST.get('sanganak3'),
        x.sanganak4=request.POST.get('sanganak4'),
        x.sankhya1=request.POST.get('sankhya1'),
        x.sankhya2=request.POST.get('sankhya2'),
        x.sankhya3=request.POST.get('sankhya3'),
        x.sankhya4=request.POST.get('sankhya4'),
        x.printers1=request.POST.get('printers1'),
        x.printers2=request.POST.get('printers2'),
        x.printers3=request.POST.get('printers3'),
        x.printers4=request.POST.get('printers4'),
        x.software1=request.POST.get('software1'),
        x.software2=request.POST.get('software2'),
        x.software3=request.POST.get('software3'),
        x.software4=request.POST.get('software4'),
        x.itar_sahity1=request.POST.get('itar_sahity1'),
        x.itar_sahity2=request.POST.get('itar_sahity2'),
        x.itar_sahity3=request.POST.get('itar_sahity3'),
        x.itar_sahity4=request.POST.get('itar_sahity4'),
        x.prayogshala1=request.POST.get('prayogshala1'),
        x.prayogshala2=request.POST.get('prayogshala2'),
        x.prayogshala3=request.POST.get('prayogshala3'),
        x.prayogshala4=request.POST.get('prayogshala4'),
        x.granthalay1=request.POST.get('granthalay1'),
        x.granthalay2=request.POST.get('granthalay2'),
        x.granthalay3=request.POST.get('granthalay3'),
        x.granthalay4=request.POST.get('granthalay4'),
        x.book_bank1=request.POST.get('book_bank1'),
        x.book_bank2=request.POST.get('book_bank2'),
        x.book_bank3=request.POST.get('book_bank3'),
        x.book_bank4=request.POST.get('book_bank4'),
        x.pustke_khredi1=request.POST.get('pustke_khredi1'),
        x.pustke_khredi2=request.POST.get('pustke_khredi2'),
        x.pustke_khredi3=request.POST.get('pustke_khredi3'),
        x.pustke_khredi4=request.POST.get('pustke_khredi4'),
        x.mandhan=request.POST.get('mandhan'),
        x.magni=request.POST.get('magni'),
        x.mi=request.POST.get('mi'),
        x.hudda=request.POST.get('hudda'),
        x.pramanit=request.POST.get('pramanit'),
        x.sansthedvara=request.POST.get('sansthedvara'),
        x.sanchalit=request.POST.get('sanchalit'),
        x.signature=request.FILES.get('signature'),
        x.name=request.POST.get('name'),
        x.shikka=request.FILES.get('shikka'),
        x.photo1=request.FILES.get('photo1'),
        x.photo2=request.FILES.get('photo2'),
     
        # x.umedwar_sign=request.FILES.get('umedwar_sign')
        x.save()
    else:
        x= zakir_hus(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        madarsa_name=request.POST.get('madarsa_name'),
        madarsa_patta=request.POST.get('madarsa_patta'),
        malkichi=request.POST.get('malkichi'),
        upkram=request.POST.get('upkram'),
        mobile_number=request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        sanstha_name=request.POST.get('sanstha_name'),
        sanstha_patta=request.POST.get('sanstha_patta'),
        mobile_number1=request.POST.get('mobile_number1'),
        email_id1=request.POST.get('email_id1'),
        adhyaksh_name=request.POST.get('adhyaksh_name'),
        adhyaksh_patta=request.POST.get('adhyaksh_patta'),
        mobile_number2=request.POST.get('mobile_number2'),
        sachiv_name=request.POST.get('sachiv_name'),
        sachiv_patta=request.POST.get('sachiv_patta'),
        mobile_number3=request.POST.get('mobile_number3'),
        nondani_kr=request.POST.get('nondani_kr'),
        bank_name=request.POST.get('bank_name'),
        acc_no=request.POST.get('acc_no'),
        ifsc=request.POST.get('ifsc'),
        patsankhya=request.POST.get('patsankhya'),
        madhyam=request.POST.get('madhyam'),
        e_mahiti=request.POST.get('e_mahiti'),
        soi_suvidha=request.POST.get('soi_suvidha'),
        kho_sankhya1=request.POST.get('kho_sankhya1'),
        kho_sankhya2=request.POST.get('kho_sankhya2'),
        kho_sankhya3=request.POST.get('kho_sankhya3'),
        kho_sankhya4=request.POST.get('kho_sankhya4'),
        kshetrafal1=request.POST.get('kshetrafal1'),
        kshetrafal2=request.POST.get('kshetrafal2'),
        kshetrafal3=request.POST.get('kshetrafal3'),
        kshetrafal4=request.POST.get('kshetrafal4'),
        pinych_pani=request.POST.get('pinych_pani'),
        utara=request.FILES.get('utara'),
        tapshil=request.POST.get('tapshil'),
        nutanikaran1=request.POST.get('nutanikaran1'),
        nutanikaran2=request.POST.get('nutanikaran2'),
        nutanikaran3=request.POST.get('nutanikaran3'),
        nutanikaran4=request.POST.get('nutanikaran4'),
        dagduji1=request.POST.get('dagduji1'),
        dagduji2=request.POST.get('dagduji2'),
        dagduji3=request.POST.get('dagduji3'),
        dagduji4=request.POST.get('dagduji4'),
        chhat1=request.POST.get('chhat1'),
        chhat2=request.POST.get('chhat2'),
        chhat3=request.POST.get('chhat3'),
        chhat4=request.POST.get('chhat4'),
        farshi1=request.POST.get('farshi1'),
        farshi2=request.POST.get('farshi2'),
        farshi3=request.POST.get('farshi3'),
        farshi4=request.POST.get('farshi4'),
        itar1=request.POST.get('itar1'),
        itar2=request.POST.get('itar2'),
        itar3=request.POST.get('itar3'),
        itar4=request.POST.get('itar4'),
        kooler1=request.POST.get('kooler1'),
        kooler2=request.POST.get('kooler2'),
        kooler3=request.POST.get('kooler3'),
        kooler4=request.POST.get('kooler4'),
        swachhata1=request.POST.get('swachhata1'),
        swachhata2=request.POST.get('swachhata2'),
        swachhata3=request.POST.get('swachhata3'),
        swachhata4=request.POST.get('swachhata4'),
        swachhtagruhe1=request.POST.get('swachhtagruhe1'),
        swachhtagruhe2=request.POST.get('swachhtagruhe2'),
        swachhtagruhe3=request.POST.get('swachhtagruhe3'),
        swachhtagruhe4=request.POST.get('swachhtagruhe4'),
        furniture1=request.POST.get('furniture1'),
        furniture2=request.POST.get('furniture2'),
        furniture3=request.POST.get('furniture3'),
        furniture4=request.POST.get('furniture4'),
        benches1=request.POST.get('benches1'),
        benches2=request.POST.get('benches2'),
        benches3=request.POST.get('benches3'),
        benches4=request.POST.get('benches4'),
        inverter1=request.POST.get('inverter1'),
        inverter2=request.POST.get('inverter2'),
        inverter3=request.POST.get('inverter3'),
        inverter4=request.POST.get('inverter4'),
        imarat1=request.POST.get('imarat1'),
        imarat2=request.POST.get('imarat2'),
        imarat3=request.POST.get('imarat3'),
        imarat4=request.POST.get('imarat4'),
        sanganak1=request.POST.get('sanganak1'),
        sanganak2=request.POST.get('sanganak2'),
        sanganak3=request.POST.get('sanganak3'),
        sanganak4=request.POST.get('sanganak4'),
        sankhya1=request.POST.get('sankhya1'),
        sankhya2=request.POST.get('sankhya2'),
        sankhya3=request.POST.get('sankhya3'),
        sankhya4=request.POST.get('sankhya4'),
        printers1=request.POST.get('printers1'),
        printers2=request.POST.get('printers2'),
        printers3=request.POST.get('printers3'),
        printers4=request.POST.get('printers4'),
        software1=request.POST.get('software1'),
        software2=request.POST.get('software2'),
        software3=request.POST.get('software3'),
        software4=request.POST.get('software4'),
        itar_sahity1=request.POST.get('itar_sahity1'),
        itar_sahity2=request.POST.get('itar_sahity2'),
        itar_sahity3=request.POST.get('itar_sahity3'),
        itar_sahity4=request.POST.get('itar_sahity4'),
        prayogshala1=request.POST.get('prayogshala1'),
        prayogshala2=request.POST.get('prayogshala2'),
        prayogshala3=request.POST.get('prayogshala3'),
        prayogshala4=request.POST.get('prayogshala4'),
        granthalay1=request.POST.get('granthalay1'),
        granthalay2=request.POST.get('granthalay2'),
        granthalay3=request.POST.get('granthalay3'),
        granthalay4=request.POST.get('granthalay4'),
        book_bank1=request.POST.get('book_bank1'),
        book_bank2=request.POST.get('book_bank2'),
        book_bank3=request.POST.get('book_bank3'),
        book_bank4=request.POST.get('book_bank4'),
        pustke_khredi1=request.POST.get('pustke_khredi1'),
        pustke_khredi2=request.POST.get('pustke_khredi2'),
        pustke_khredi3=request.POST.get('pustke_khredi3'),
        pustke_khredi4=request.POST.get('pustke_khredi4'),
        mandhan=request.POST.get('mandhan'),
        magni=request.POST.get('magni'),
        mi=request.POST.get('mi'),
        hudda=request.POST.get('hudda'),
        pramanit=request.POST.get('pramanit'),
        sansthedvara=request.POST.get('sansthedvara'),
        sanchalit=request.POST.get('sanchalit'),
        signature=request.FILES.get('signature'),
        name=request.POST.get('name'),
        shikka=request.FILES.get('shikka'),
        photo1=request.FILES.get('photo1'),
        photo2=request.FILES.get('photo2'),
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def shivanyantra(request,pk):
    print('hi')
    if mada_shivnyantra.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = mada_shivnyantra.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.mukkam=request.POST.get('mukkam'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.birth_date=request.POST.get('birth_date'),
        x.dakhla = request.FILES.get('dakhla'),
        x.jat=request.POST.get('jat'),
        x.potjat=request.POST.get('potjat'),
        x.vivahit=request.POST.getlist('vivahit[]'),
        x.patiname = request.POST.get('patiname'),
        x.buisness = request.POST.get('buisness'),
        x.income=request.POST.get('income'),
        x.fa_name = request.POST.get('fa_name'),
        x.buisness1 = request.POST.get('buisness1'),
        x.income1=request.POST.get('income1'),  
        x.income2 = request.POST.get('income2'), 
        x.dakhla1=request.FILES.get('dakhla1'),
        x.buisness2=request.POST.get('buisness2'),
        x.income3= request.POST.get('income3'),
        x.prashikshan=request.POST.get('prashikshan'),
        x.pramanpatra= request.FILES.get('pramanpatra'),
        x.prashikshan1=request.POST.get('prashikshan1'),
        x.pramanpatra2= request.FILES.get('pramanpatra2'),
        x.sthal=request.POST.get('sthal'),
        x.form_date=request.POST.get('form_date'),
        x.patta=request.POST.get('patta'),
        x.signature= request.FILES.get('signature'),
        x.photo= request.FILES.get('photo'),
        x.tc= request.FILES.get('tc'),
        
        if request.POST.get('ja') == '0':
            x.jati = True
        else:
            x.jati = False
        x.save()
    else:
        x= mada_shivnyantra(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        mukkam=request.POST.get('mukkam'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        birth_date=request.POST.get('birth_date'),
        dakhla = request.FILES.get('dakhla'),
        jat=request.POST.get('jat'),
        potjat=request.POST.get('potjat'),
        vivahit=request.POST.getlist('vivahit[]'),
        patiname = request.POST.get('patiname'),
        buisness = request.POST.get('buisness'),
        income=request.POST.get('income'),
        fa_name = request.POST.get('fa_name'),
        buisness1 = request.POST.get('buisness1'),
        income1=request.POST.get('income1'),  
        income2 = request.POST.get('income2'), 
        dakhla1=request.FILES.get('dakhla1'),
        buisness2=request.POST.get('buisness2'),
        income3= request.POST.get('income3'),
        prashikshan=request.POST.get('prashikshan'),
        pramanpatra= request.FILES.get('pramanpatra'),
        prashikshan1=request.POST.get('prashikshan1'),
        pramanpatra2= request.FILES.get('pramanpatra2'),
        sthal=request.POST.get('sthal'),
        form_date=request.POST.get('form_date'),
        patta=request.POST.get('patta'),
        signature= request.FILES.get('signature'),
        photo= request.FILES.get('photo'),
        tc= request.FILES.get('tc'),
        
        )
        if request.POST.get('ja')=='0':
            x.jati=True
        else:
            x.jati=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def mada_cycl(request,pk):
    print('hi')
    if mada_cycle.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = mada_cycle.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.mukkam=request.POST.get('mukkam'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.dakhla = request.FILES.get('dakhla'),
        x.jat=request.POST.get('jat'),
        x.potjat=request.POST.get('potjat'),
        x.san = request.POST.get('san'),
        x.iyatta = request.POST.get('iyatta'),
        x.sch_name = request.POST.get('sch_name'),
        x.sch_patta=request.POST.get('sch_patta'),
        x.gun = request.POST.get('gun'),
        x.mulinmadhun = request.POST.get('mulinmadhun'),
        x.takke=request.POST.get('takke'),  
        x.san1 = request.POST.get('san1'), 
        x.iyatta1=request.POST.get('iyatta1'),
        x.sch_name1= request.POST.get('sch_name1'),
        x.sch_patta1=request.POST.get('sch_patta1'),
        x.gav_name=request.POST.get('gav_name'),
        x.antar=request.POST.get('antar'),
        x.utpanna=request.POST.get('utpanna'),
        x.buisness=request.POST.get('buisness'),
        x.dakhla1 = request.FILES.get('dakhla1'),
        x.san2=request.POST.get('san2'),
        x.sthal=request.POST.get('sthal'),
        x.form_date=request.POST.get('form_date'),
        x.patta=request.POST.get('patta'),
        x.signature= request.FILES.get('signature'),
        x.photo= request.FILES.get('photo'),
        
        if request.POST.get('jatii') == '0':
            x.jati = True
        else:
            x.jati = False
        x.save()
    else:
        x= mada_cycle(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        mukkam=request.POST.get('mukkam'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        dakhla = request.FILES.get('dakhla'),
        jat=request.POST.get('jat'),
        potjat=request.POST.get('potjat'),
        san = request.POST.get('san'),
        iyatta = request.POST.get('iyatta'),
        sch_name = request.POST.get('sch_name'),
        sch_patta=request.POST.get('sch_patta'),
        gun = request.POST.get('gun'),
        mulinmadhun = request.POST.get('mulinmadhun'),
        takke=request.POST.get('takke'),  
        san1 = request.POST.get('san1'), 
        iyatta1=request.POST.get('iyatta1'),
        sch_name1= request.POST.get('sch_name1'),
        sch_patta1=request.POST.get('sch_patta1'),
        gav_name=request.POST.get('gav_name'),
        antar=request.POST.get('antar'),
        utpanna=request.POST.get('utpanna'),
        buisness=request.POST.get('buisness'),
        dakhla1 = request.FILES.get('dakhla1'),
        san2=request.POST.get('san2'),
        sthal=request.POST.get('sthal'),
        form_date=request.POST.get('form_date'),
        patta=request.POST.get('patta'),
        signature= request.FILES.get('signature'),
        photo= request.FILES.get('photo'),
        
        )
        if request.POST.get('jatii')=='0':
            x.jati=True
        else:
            x.jati=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def balsango(request,pk):
    print('hi')
    if balsangopan.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = balsangopan.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.age=request.POST.get('age'),
        x.birth_date=request.POST.get('birth_date'),
        x.education=request.POST.get('education'),
        x.palak_name=request.POST.get('palak_name'),
        x.patta =request.POST.get('patta'),
        x.palak_name1=request.POST.get('palak_name1'),
        x.patta1=request.POST.get('patta1'),
        x.nate = request.POST.get('nate'),
        x.income = request.POST.get('income'),
        x.buisness = request.POST.get('buisness'),
        x.mahiti=request.POST.getlist('mahiti[]'),
        x.sthiti = request.POST.get('sthiti'),
        x.bhau = request.POST.get('bhau'),
        x.bahin=request.POST.get('bahin'),  
        x.aaji = request.POST.get('aaji'), 
        x.name1=request.POST.get('name1'),
        x.patta2= request.POST.get('patta2'),
        x.signature= request.FILES.get('signature'),

        if request.POST.get('aa') == '0':
            x.aai = True
        else:
            x.aai = False
    
        if request.POST.get('va') == '0':
            x.vadil = True
        else:
            x.vadil = False
        x.save()
    else:
        x= balsangopan(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        age=request.POST.get('age'),
        birth_date=request.POST.get('birth_date'),
        education=request.POST.get('education'),
        palak_name=request.POST.get('palak_name'),
        patta =request.POST.get('patta'),
        palak_name1=request.POST.get('palak_name1'),
        patta1=request.POST.get('patta1'),
        nate = request.POST.get('nate'),
        income = request.POST.get('income'),
        buisness = request.POST.get('buisness'),
        mahiti=request.POST.getlist('mahiti[]'),
        sthiti = request.POST.get('sthiti'),
        bhau = request.POST.get('bhau'),
        bahin=request.POST.get('bahin'),  
        aaji = request.POST.get('aaji'), 
        name1=request.POST.get('name1'),
        patta2= request.POST.get('patta2'),
        signature= request.FILES.get('signature'),
        
        )
        if request.POST.get('aa') == '0':
            x.aai = True
        else:
            x.aai = False
        x.save()
        print("X: ",x)
        if request.POST.get('va') == '0':
            x.vadil = True
        else:
            x.vadil = False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def samuhik_viva(request,pk):
    print('hi')
    if shubh_vivah.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = shubh_vivah.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.buisness=request.POST.get('buisness'),
        x.girl_name =request.POST.get('girl_name'),
        x.age=request.POST.get('age'),
        x.vivah_date=request.POST.get('vivah_date'),
        x.sanstha = request.POST.get('sanstha'),
        x.adhaar_no = request.POST.get('adhaar_no'),
        x.bank_name = request.POST.get('bank_name'),
        x.acc_no=request.POST.get('acc_no'),
        x.ifsc = request.POST.get('ifsc'),
        x.name1 = request.POST.get('name1'),
        x.form_date=request.POST.get('form_date'), 
        x.signature= request.FILES.get('signature'), 
        x.var_name = request.POST.get('var_name'), 
        x.age1=request.POST.get('age1'),
        x.birth_date= request.POST.get('birth_date'),
        x.education=request.POST.get('education'),
        x.gav=request.POST.get('gav'),
        x.taluka1=request.POST.get('taluka1'),
        x.jilha=request.POST.get('jilha'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.palak_patta =request.POST.get('palak_patta'),
        x.mobile_number1=request.POST.get('mobile_number1'),
        x.mobile_number2=request.POST.get('mobile_number2'),
        x.var_photo= request.FILES.get('var_photo'), 
        x.vadhu_name = request.POST.get('vadhu_name'),
        x.age2 = request.POST.get('age2'),
        x.birth_date1 = request.POST.get('birth_date1'),
        x.education1=request.POST.get('education1'),
        x.gav1 = request.POST.get('gav1'),
        x.taluka2 = request.POST.get('taluka2'),
        x.jilha1=request.POST.get('jilha1'),
        x.mobile_number3=request.POST.get('mobile_number3'),
        x.palak_patta1=request.POST.get('palak_patta1'),
        x.mobile_number4=request.POST.get('mobile_number4'),
        x.mobile_number5=request.POST.get('mobile_number5'),
        x.vadhu_photo= request.FILES.get('vadhu_photo'), 
        x.sans_name=request.POST.get('sans_name'),
        x.thikan =request.POST.get('thikan'),
        x.tarikh=request.POST.get('tarikh'),
        x.padhat=request.POST.get('padhat'),
        x.var_sign= request.FILES.get('var_sign'), 
        x.vadhu_sign= request.FILES.get('vadhu_sign'), 
        
        if request.POST.get('varr') == '0':
            x.var = True
        else:
            x.var = False
    
        if request.POST.get('vadh') == '0':
            x.vadhu = True
        else:
            x.vadhu = False

        if request.POST.get('vid') == '0':
            x.vidhva = True
        else:
            x.vidhva = False

        if request.POST.get('vidu') == '0':
            x.vidur = True
        else:
            x.vidur = False

        if request.POST.get('arth') == '0':
            x.arthsahayya = True
        else:
            x.arthsahayya = False

        if request.POST.get('ar') == '0':
            x.arj = True
        else:
            x.arj = False
        x.save()
    else:
        x= shubh_vivah(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        buisness=request.POST.get('buisness'),
        girl_name =request.POST.get('girl_name'),
        age=request.POST.get('age'),
        vivah_date=request.POST.get('vivah_date'),
        sanstha = request.POST.get('sanstha'),
        adhaar_no = request.POST.get('adhaar_no'),
        bank_name = request.POST.get('bank_name'),
        acc_no=request.POST.get('acc_no'),
        ifsc = request.POST.get('ifsc'),
        name1 = request.POST.get('name1'),
        form_date=request.POST.get('form_date'), 
        signature= request.FILES.get('signature'), 
        var_name = request.POST.get('var_name'), 
        age1=request.POST.get('age1'),
        birth_date= request.POST.get('birth_date'),
        education=request.POST.get('education'),
        gav=request.POST.get('gav'),
        taluka1=request.POST.get('taluka1'),
        jilha=request.POST.get('jilha'),
        mobile_number=request.POST.get('mobile_number'),
        palak_patta =request.POST.get('palak_patta'),
        mobile_number1=request.POST.get('mobile_number1'),
        mobile_number2=request.POST.get('mobile_number2'),
        var_photo= request.FILES.get('var_photo'), 
        vadhu_name = request.POST.get('vadhu_name'),
        age2 = request.POST.get('age2'),
        birth_date1 = request.POST.get('birth_date1'),
        education1=request.POST.get('education1'),
        gav1 = request.POST.get('gav1'),
        taluka2 = request.POST.get('taluka2'),
        jilha1=request.POST.get('jilha1'),
        mobile_number3=request.POST.get('mobile_number3'),
        palak_patta1=request.POST.get('palak_patta1'),
        mobile_number4=request.POST.get('mobile_number4'),
        mobile_number5=request.POST.get('mobile_number5'),
        vadhu_photo= request.FILES.get('vadhu_photo'), 
        sans_name=request.POST.get('sans_name'),
        thikan =request.POST.get('thikan'),
        tarikh=request.POST.get('tarikh'),
        padhat=request.POST.get('padhat'),
        var_sign= request.FILES.get('var_sign'), 
        vadhu_sign= request.FILES.get('vadhu_sign'), 
        
        )
        if request.POST.get('varr') == '0':
            x.var = True
        else:
            x.var = False
        x.save()
        print("X: ",x)
        if request.POST.get('vadh') == '0':
            x.vadhu = True
        else:
            x.vadhu = False
        x.save()
        print("X: ",x)
        if request.POST.get('vid') == '0':
            x.vidhva = True
        else:
            x.vidhva = False
        x.save()
        print("X: ",x)
        if request.POST.get('vidu') == '0':
            x.vidur = True
        else:
            x.vidur = False
        x.save()
        print("X: ",x)
        if request.POST.get('arth') == '0':
            x.arthsahayya = True
        else:
            x.arthsahayya = False
        x.save()
        print("X: ",x)
        if request.POST.get('ar') == '0':
            x.arj = True
        else:
            x.arj = False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def ot_shivanyantra(request,pk):
    print('hi')
    if otsp_shivnyantra.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = otsp_shivnyantra.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.mukkam=request.POST.get('mukkam'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.birth_date=request.POST.get('birth_date'),
        x.dakhla = request.FILES.get('dakhla'),
        x.jat=request.POST.get('jat'),
        x.potjat=request.POST.get('potjat'),
        x.vivahit=request.POST.getlist('vivahit[]'),
        x.patiname = request.POST.get('patiname'),
        x.buisness = request.POST.get('buisness'),
        x.income=request.POST.get('income'),
        x.fa_name = request.POST.get('fa_name'),
        x.buisness1 = request.POST.get('buisness1'),
        x.income1=request.POST.get('income1'),  
        x.income2 = request.POST.get('income2'), 
        x.dakhla1=request.FILES.get('dakhla1'),
        x.buisness2=request.POST.get('buisness2'),
        x.income3= request.POST.get('income3'),
        x.prashikshan=request.POST.get('prashikshan'),
        x.pramanpatra= request.FILES.get('pramanpatra'),
        x.prashikshan1=request.POST.get('prashikshan1'),
        x.pramanpatra2= request.FILES.get('pramanpatra2'),
        x.sthal=request.POST.get('sthal'),
        x.form_date=request.POST.get('form_date'),
        x.patta=request.POST.get('patta'),
        x.signature= request.FILES.get('signature'),
        x.photo= request.FILES.get('photo'),
        x.tc= request.FILES.get('tc'),
        
        if request.POST.get('ja') == '0':
            x.jati = True
        else:
            x.jati = False
        x.save()
    else:
        x= otsp_shivnyantra(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        mukkam=request.POST.get('mukkam'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        birth_date=request.POST.get('birth_date'),
        dakhla = request.FILES.get('dakhla'),
        jat=request.POST.get('jat'),
        potjat=request.POST.get('potjat'),
        vivahit=request.POST.getlist('vivahit[]'),
        patiname = request.POST.get('patiname'),
        buisness = request.POST.get('buisness'),
        income=request.POST.get('income'),
        fa_name = request.POST.get('fa_name'),
        buisness1 = request.POST.get('buisness1'),
        income1=request.POST.get('income1'),  
        income2 = request.POST.get('income2'), 
        dakhla1=request.FILES.get('dakhla1'),
        buisness2=request.POST.get('buisness2'),
        income3= request.POST.get('income3'),
        prashikshan=request.POST.get('prashikshan'),
        pramanpatra= request.FILES.get('pramanpatra'),
        prashikshan1=request.POST.get('prashikshan1'),
        pramanpatra2= request.FILES.get('pramanpatra2'),
        sthal=request.POST.get('sthal'),
        form_date=request.POST.get('form_date'),
        patta=request.POST.get('patta'),
        signature= request.FILES.get('signature'),
        photo= request.FILES.get('photo'),
        tc= request.FILES.get('tc'),
        
        )
        if request.POST.get('ja')=='0':
            x.jati=True
        else:
            x.jati=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def sc_shivanyantra(request,pk):
    print('hi')
    if scp_shivnyantra.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = scp_shivnyantra.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.mukkam=request.POST.get('mukkam'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.birth_date=request.POST.get('birth_date'),
        x.dakhla = request.FILES.get('dakhla'),
        x.jat=request.POST.get('jat'),
        x.potjat=request.POST.get('potjat'),
        x.vivahit=request.POST.getlist('vivahit[]'),
        x.patiname = request.POST.get('patiname'),
        x.buisness = request.POST.get('buisness'),
        x.income=request.POST.get('income'),
        x.fa_name = request.POST.get('fa_name'),
        x.buisness1 = request.POST.get('buisness1'),
        x.income1=request.POST.get('income1'),  
        x.income2 = request.POST.get('income2'), 
        x.dakhla1=request.FILES.get('dakhla1'),
        x.buisness2=request.POST.get('buisness2'),
        x.income3= request.POST.get('income3'),
        x.prashikshan=request.POST.get('prashikshan'),
        x.pramanpatra= request.FILES.get('pramanpatra'),
        x.prashikshan1=request.POST.get('prashikshan1'),
        x.pramanpatra2= request.FILES.get('pramanpatra2'),
        x.sthal=request.POST.get('sthal'),
        x.form_date=request.POST.get('form_date'),
        x.patta=request.POST.get('patta'),
        x.signature= request.FILES.get('signature'),
        x.photo= request.FILES.get('photo'),
        x.tc= request.FILES.get('tc'),
        
        if request.POST.get('ja') == '0':
            x.jati = True
        else:
            x.jati = False
        x.save()
    else:
        x= scp_shivnyantra(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        mukkam=request.POST.get('mukkam'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        birth_date=request.POST.get('birth_date'),
        dakhla = request.FILES.get('dakhla'),
        jat=request.POST.get('jat'),
        potjat=request.POST.get('potjat'),
        vivahit=request.POST.getlist('vivahit[]'),
        patiname = request.POST.get('patiname'),
        buisness = request.POST.get('buisness'),
        income=request.POST.get('income'),
        fa_name = request.POST.get('fa_name'),
        buisness1 = request.POST.get('buisness1'),
        income1=request.POST.get('income1'),  
        income2 = request.POST.get('income2'), 
        dakhla1=request.FILES.get('dakhla1'),
        buisness2=request.POST.get('buisness2'),
        income3= request.POST.get('income3'),
        prashikshan=request.POST.get('prashikshan'),
        pramanpatra= request.FILES.get('pramanpatra'),
        prashikshan1=request.POST.get('prashikshan1'),
        pramanpatra2= request.FILES.get('pramanpatra2'),
        sthal=request.POST.get('sthal'),
        form_date=request.POST.get('form_date'),
        patta=request.POST.get('patta'),
        signature= request.FILES.get('signature'),
        photo= request.FILES.get('photo'),
        tc= request.FILES.get('tc'),
        
        )
        if request.POST.get('ja')=='0':
            x.jati=True
        else:
            x.jati=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def tsp_shivanyantra(request,pk):
    print('hi')
    if tsp_shivnyantra.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = tsp_shivnyantra.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.mukkam=request.POST.get('mukkam'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.birth_date=request.POST.get('birth_date'),
        x.dakhla = request.FILES.get('dakhla'),
        x.jat=request.POST.get('jat'),
        x.potjat=request.POST.get('potjat'),
        x.vivahit=request.POST.getlist('vivahit[]'),
        x.patiname = request.POST.get('patiname'),
        x.buisness = request.POST.get('buisness'),
        x.income=request.POST.get('income'),
        x.fa_name = request.POST.get('fa_name'),
        x.buisness1 = request.POST.get('buisness1'),
        x.income1=request.POST.get('income1'),  
        x.income2 = request.POST.get('income2'), 
        x.dakhla1=request.FILES.get('dakhla1'),
        x.buisness2=request.POST.get('buisness2'),
        x.income3= request.POST.get('income3'),
        x.prashikshan=request.POST.get('prashikshan'),
        x.pramanpatra= request.FILES.get('pramanpatra'),
        x.prashikshan1=request.POST.get('prashikshan1'),
        x.pramanpatra2= request.FILES.get('pramanpatra2'),
        x.sthal=request.POST.get('sthal'),
        x.form_date=request.POST.get('form_date'),
        x.patta=request.POST.get('patta'),
        x.signature= request.FILES.get('signature'),
        x.photo= request.FILES.get('photo'),
        x.tc= request.FILES.get('tc'),
        
        if request.POST.get('ja') == '0':
            x.jati = True
        else:
            x.jati = False
        x.save()
    else:
        x= tsp_shivnyantra(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        mukkam=request.POST.get('mukkam'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        birth_date=request.POST.get('birth_date'),
        dakhla = request.FILES.get('dakhla'),
        jat=request.POST.get('jat'),
        potjat=request.POST.get('potjat'),
        vivahit=request.POST.getlist('vivahit[]'),
        patiname = request.POST.get('patiname'),
        buisness = request.POST.get('buisness'),
        income=request.POST.get('income'),
        fa_name = request.POST.get('fa_name'),
        buisness1 = request.POST.get('buisness1'),
        income1=request.POST.get('income1'),  
        income2 = request.POST.get('income2'), 
        dakhla1=request.FILES.get('dakhla1'),
        buisness2=request.POST.get('buisness2'),
        income3= request.POST.get('income3'),
        prashikshan=request.POST.get('prashikshan'),
        pramanpatra= request.FILES.get('pramanpatra'),
        prashikshan1=request.POST.get('prashikshan1'),
        pramanpatra2= request.FILES.get('pramanpatra2'),
        sthal=request.POST.get('sthal'),
        form_date=request.POST.get('form_date'),
        patta=request.POST.get('patta'),
        signature= request.FILES.get('signature'),
        photo= request.FILES.get('photo'),
        tc= request.FILES.get('tc'),
        
        )
        if request.POST.get('ja')=='0':
            x.jati=True
        else:
            x.jati=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def otsp_cyc(request,pk):
    print('hi')
    if otsp_cycl.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = otsp_cycl.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.mukkam=request.POST.get('mukkam'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.dakhla = request.FILES.get('dakhla'),
        x.jat=request.POST.get('jat'),
        x.potjat=request.POST.get('potjat'),
        x.san = request.POST.get('san'),
        x.iyatta = request.POST.get('iyatta'),
        x.sch_name = request.POST.get('sch_name'),
        x.sch_patta=request.POST.get('sch_patta'),
        x.gun = request.POST.get('gun'),
        x.mulinmadhun = request.POST.get('mulinmadhun'),
        x.takke=request.POST.get('takke'),  
        x.san1 = request.POST.get('san1'), 
        x.iyatta1=request.POST.get('iyatta1'),
        x.sch_name1= request.POST.get('sch_name1'),
        x.sch_patta1=request.POST.get('sch_patta1'),
        x.gav_name=request.POST.get('gav_name'),
        x.antar=request.POST.get('antar'),
        x.utpanna=request.POST.get('utpanna'),
        x.buisness=request.POST.get('buisness'),
        x.dakhla1 = request.FILES.get('dakhla1'),
        x.san2=request.POST.get('san2'),
        x.sthal=request.POST.get('sthal'),
        x.form_date=request.POST.get('form_date'),
        x.patta=request.POST.get('patta'),
        x.signature= request.FILES.get('signature'),
        x.photo= request.FILES.get('photo'),
        
        if request.POST.get('jatii') == '0':
            x.jati = True
        else:
            x.jati = False
        x.save()
    else:
        x= otsp_cycl(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        mukkam=request.POST.get('mukkam'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        dakhla = request.FILES.get('dakhla'),
        jat=request.POST.get('jat'),
        potjat=request.POST.get('potjat'),
        san = request.POST.get('san'),
        iyatta = request.POST.get('iyatta'),
        sch_name = request.POST.get('sch_name'),
        sch_patta=request.POST.get('sch_patta'),
        gun = request.POST.get('gun'),
        mulinmadhun = request.POST.get('mulinmadhun'),
        takke=request.POST.get('takke'),  
        san1 = request.POST.get('san1'), 
        iyatta1=request.POST.get('iyatta1'),
        sch_name1= request.POST.get('sch_name1'),
        sch_patta1=request.POST.get('sch_patta1'),
        gav_name=request.POST.get('gav_name'),
        antar=request.POST.get('antar'),
        utpanna=request.POST.get('utpanna'),
        buisness=request.POST.get('buisness'),
        dakhla1 = request.FILES.get('dakhla1'),
        san2=request.POST.get('san2'),
        sthal=request.POST.get('sthal'),
        form_date=request.POST.get('form_date'),
        patta=request.POST.get('patta'),
        signature= request.FILES.get('signature'),
        photo= request.FILES.get('photo'),
        
        )
        if request.POST.get('jatii')=='0':
            x.jati=True
        else:
            x.jati=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def scp_cyc(request,pk):
    print('hi')
    if scp_cycl.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = scp_cycl.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.mukkam=request.POST.get('mukkam'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.dakhla = request.FILES.get('dakhla'),
        x.jat=request.POST.get('jat'),
        x.potjat=request.POST.get('potjat'),
        x.san = request.POST.get('san'),
        x.iyatta = request.POST.get('iyatta'),
        x.sch_name = request.POST.get('sch_name'),
        x.sch_patta=request.POST.get('sch_patta'),
        x.gun = request.POST.get('gun'),
        x.mulinmadhun = request.POST.get('mulinmadhun'),
        x.takke=request.POST.get('takke'),  
        x.san1 = request.POST.get('san1'), 
        x.iyatta1=request.POST.get('iyatta1'),
        x.sch_name1= request.POST.get('sch_name1'),
        x.sch_patta1=request.POST.get('sch_patta1'),
        x.gav_name=request.POST.get('gav_name'),
        x.antar=request.POST.get('antar'),
        x.utpanna=request.POST.get('utpanna'),
        x.buisness=request.POST.get('buisness'),
        x.dakhla1 = request.FILES.get('dakhla1'),
        x.san2=request.POST.get('san2'),
        x.sthal=request.POST.get('sthal'),
        x.form_date=request.POST.get('form_date'),
        x.patta=request.POST.get('patta'),
        x.signature= request.FILES.get('signature'),
        x.photo= request.FILES.get('photo'),
        
        if request.POST.get('jatii') == '0':
            x.jati = True
        else:
            x.jati = False
        x.save()
    else:
        x= scp_cycl(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        mukkam=request.POST.get('mukkam'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        dakhla = request.FILES.get('dakhla'),
        jat=request.POST.get('jat'),
        potjat=request.POST.get('potjat'),
        san = request.POST.get('san'),
        iyatta = request.POST.get('iyatta'),
        sch_name = request.POST.get('sch_name'),
        sch_patta=request.POST.get('sch_patta'),
        gun = request.POST.get('gun'),
        mulinmadhun = request.POST.get('mulinmadhun'),
        takke=request.POST.get('takke'),  
        san1 = request.POST.get('san1'), 
        iyatta1=request.POST.get('iyatta1'),
        sch_name1= request.POST.get('sch_name1'),
        sch_patta1=request.POST.get('sch_patta1'),
        gav_name=request.POST.get('gav_name'),
        antar=request.POST.get('antar'),
        utpanna=request.POST.get('utpanna'),
        buisness=request.POST.get('buisness'),
        dakhla1 = request.FILES.get('dakhla1'),
        san2=request.POST.get('san2'),
        sthal=request.POST.get('sthal'),
        form_date=request.POST.get('form_date'),
        patta=request.POST.get('patta'),
        signature= request.FILES.get('signature'),
        photo= request.FILES.get('photo'),
        
        )
        if request.POST.get('jatii')=='0':
            x.jati=True
        else:
            x.jati=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def tsp_cyc(request,pk):
    print('hi')
    if tsp_cycl.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = tsp_cycl.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.name=request.POST.get('name'),
        x.sam_patta=request.POST.get('sam_patta'),
        x.mukkam=request.POST.get('mukkam'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.dakhla = request.FILES.get('dakhla'),
        x.jat=request.POST.get('jat'),
        x.potjat=request.POST.get('potjat'),
        x.san = request.POST.get('san'),
        x.iyatta = request.POST.get('iyatta'),
        x.sch_name = request.POST.get('sch_name'),
        x.sch_patta=request.POST.get('sch_patta'),
        x.gun = request.POST.get('gun'),
        x.mulinmadhun = request.POST.get('mulinmadhun'),
        x.takke=request.POST.get('takke'),  
        x.san1 = request.POST.get('san1'), 
        x.iyatta1=request.POST.get('iyatta1'),
        x.sch_name1= request.POST.get('sch_name1'),
        x.sch_patta1=request.POST.get('sch_patta1'),
        x.gav_name=request.POST.get('gav_name'),
        x.antar=request.POST.get('antar'),
        x.utpanna=request.POST.get('utpanna'),
        x.buisness=request.POST.get('buisness'),
        x.dakhla1 = request.FILES.get('dakhla1'),
        x.san2=request.POST.get('san2'),
        x.sthal=request.POST.get('sthal'),
        x.form_date=request.POST.get('form_date'),
        x.patta=request.POST.get('patta'),
        x.signature= request.FILES.get('signature'),
        x.photo= request.FILES.get('photo'),
        
        if request.POST.get('jatii') == '0':
            x.jati = True
        else:
            x.jati = False
        x.save()
    else:
        x= tsp_cycl(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        name=request.POST.get('name'),
        sam_patta=request.POST.get('sam_patta'),
        mukkam=request.POST.get('mukkam'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        dakhla = request.FILES.get('dakhla'),
        jat=request.POST.get('jat'),
        potjat=request.POST.get('potjat'),
        san = request.POST.get('san'),
        iyatta = request.POST.get('iyatta'),
        sch_name = request.POST.get('sch_name'),
        sch_patta=request.POST.get('sch_patta'),
        gun = request.POST.get('gun'),
        mulinmadhun = request.POST.get('mulinmadhun'),
        takke=request.POST.get('takke'),  
        san1 = request.POST.get('san1'), 
        iyatta1=request.POST.get('iyatta1'),
        sch_name1= request.POST.get('sch_name1'),
        sch_patta1=request.POST.get('sch_patta1'),
        gav_name=request.POST.get('gav_name'),
        antar=request.POST.get('antar'),
        utpanna=request.POST.get('utpanna'),
        buisness=request.POST.get('buisness'),
        dakhla1 = request.FILES.get('dakhla1'),
        san2=request.POST.get('san2'),
        sthal=request.POST.get('sthal'),
        form_date=request.POST.get('form_date'),
        patta=request.POST.get('patta'),
        signature= request.FILES.get('signature'),
        photo= request.FILES.get('photo'),
        
        )
        if request.POST.get('jatii')=='0':
            x.jati=True
        else:
            x.jati=False
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def dharmik_alpp(request,pk):
    print('hi')
    if dharmik_alp.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = dharmik_alp.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.sch_name=request.POST.get('sch_name'),
        x.anudan=request.POST.get('anudan'),
        x.nidhi=request.POST.get('nidhi'),
        x.patta=request.POST.get('patta'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.code=request.POST.get('code'),
        x.sch_sanstha=request.POST.get('sch_sanstha'),
        x.sanstha_patta=request.POST.get('sanstha_patta'),
        x.mobile_number1=request.POST.get('mobile_number1'),
        x.pracharya_name=request.POST.get('pracharya_name'),
        x.acc_no=request.POST.get('acc_no'),
        x.ifsc=request.POST.get('ifsc'),
        x.nondani_kr1=request.POST.get('nondani_kr1'),
        x.nondani_kr2=request.POST.get('nondani_kr2'),
        x.nondani_kr3=request.POST.get('nondani_kr3'),
        x.nondani_kr4=request.POST.get('nondani_kr4'),
        x.nondani_kr5=request.POST.get('nondani_kr5'),
        x.tarikh=request.POST.get('tarikh'),
        x.manjur1=request.POST.get('manjur1'),
        x.manjur2=request.POST.get('manjur2'),
        x.manjur3=request.POST.get('manjur3'),
        x.chalu1=request.POST.get('chalu1'),
        x.chalu2=request.POST.get('chalu2'),
        x.chalu3=request.POST.get('chalu3'),
        x.abhyaskram=request.POST.getlist('abhyaskram[]'),
        x.madhyam=request.POST.get('madhyam'),
        x.sankhya=request.POST.get('sankhya'),
        x.imaratimdhe=request.POST.get('imaratimdhe'),
        x.aavashyak_bandh=request.POST.get('aavashyak_bandh'),
        x.mahila1=request.POST.get('mahila1'),
        x.mahila2=request.POST.get('mahila2'),
        x.purush1=request.POST.get('purush1'),
        x.purush2=request.POST.get('purush2'),
        x.pani=request.POST.get('pani'),
        x.nutanikaran1=request.POST.get('nutanikaran1'),
        x.nutanikaran2=request.POST.get('nutanikaran2'),
        x.nutanikaran3=request.POST.get('nutanikaran3'),
        x.nutanikaran4=request.POST.get('nutanikaran4'),
        x.dagduji1=request.POST.get('dagduji1'),
        x.dagduji2=request.POST.get('dagduji2'),
        x.dagduji3=request.POST.get('dagduji3'),
        x.dagduji4=request.POST.get('dagduji4'),
        x.chhat1=request.POST.get('chhat1'),
        x.chhat2=request.POST.get('chhat2'),
        x.chhat3=request.POST.get('chhat3'),
        x.chhat4=request.POST.get('chhat4'),
        x.farshi1=request.POST.get('farshi1'),
        x.farshi2=request.POST.get('farshi2'),
        x.farshi3=request.POST.get('farshi3'),
        x.farshi4=request.POST.get('farshi4'),
        x.kooler1=request.POST.get('kooler1'),
        x.kooler2=request.POST.get('kooler2'),
        x.kooler3=request.POST.get('kooler3'),
        x.kooler4=request.POST.get('kooler4'),
        x.kits1=request.POST.get('kits1'),
        x.kits2=request.POST.get('kits2'),
        x.kits3=request.POST.get('kits3'),
        x.kits4=request.POST.get('kits4'),
        x.pustke_khredi1=request.POST.get('pustke_khredi1'),
        x.pustke_khredi2=request.POST.get('pustke_khredi2'),
        x.pustke_khredi3=request.POST.get('pustke_khredi3'),
        x.pustke_khredi4=request.POST.get('pustke_khredi4'),
        x.itar_khredi1=request.POST.get('itar_khredi1'),
        x.itar_khredi2=request.POST.get('itar_khredi2'),
        x.itar_khredi3=request.POST.get('itar_khredi3'),
        x.itar_khredi4=request.POST.get('itar_khredi4'),
        x.prayogshala1=request.POST.get('prayogshala1'),
        x.prayogshala2=request.POST.get('prayogshala2'),
        x.prayogshala3=request.POST.get('prayogshala3'),
        x.prayogshala4=request.POST.get('prayogshala4'),
        x.sanganak1=request.POST.get('sanganak1'),
        x.sanganak2=request.POST.get('sanganak2'),
        x.sanganak3=request.POST.get('sanganak3'),
        x.sanganak4=request.POST.get('sanganak4'),
        x.sankhya1=request.POST.get('sankhya1'),
        x.sankhya2=request.POST.get('sankhya2'),
        x.sankhya3=request.POST.get('sankhya3'),
        x.sankhya4=request.POST.get('sankhya4'),
        x.printers1=request.POST.get('printers1'),
        x.printers2=request.POST.get('printers2'),
        x.printers3=request.POST.get('printers3'),
        x.printers4=request.POST.get('printers4'),
        x.software1=request.POST.get('software1'),
        x.software2=request.POST.get('software2'),
        x.software3=request.POST.get('software3'),
        x.software4=request.POST.get('software4'),
        x.itar_sahity1=request.POST.get('itar_sahity1'),
        x.itar_sahity2=request.POST.get('itar_sahity2'),
        x.itar_sahity3=request.POST.get('itar_sahity3'),
        x.itar_sahity4=request.POST.get('itar_sahity4'),
        x.swachhtagruhe1=request.POST.get('swachhtagruhe1'),
        x.swachhtagruhe2=request.POST.get('swachhtagruhe2'),
        x.swachhtagruhe3=request.POST.get('swachhtagruhe3'),
        x.swachhtagruhe4=request.POST.get('swachhtagruhe4'),
        x.durusti1=request.POST.get('durusti1'),
        x.durusti2=request.POST.get('durusti2'),
        x.durusti3=request.POST.get('durusti3'),
        x.durusti4=request.POST.get('durusti4'),
        x.new_swachhtagruhe1=request.POST.get('new_swachhtagruhe1'),
        x.new_swachhtagruhe2=request.POST.get('new_swachhtagruhe2'),
        x.new_swachhtagruhe3=request.POST.get('new_swachhtagruhe3'),
        x.new_swachhtagruhe4=request.POST.get('new_swachhtagruhe4'),
        x.furniture1=request.POST.get('furniture1'),
        x.furniture2=request.POST.get('furniture2'),
        x.furniture3=request.POST.get('furniture3'),
        x.furniture4=request.POST.get('furniture4'),
        x.benches1=request.POST.get('benches1'),
        x.benches2=request.POST.get('benches2'),
        x.benches3=request.POST.get('benches3'),
        x.benches4=request.POST.get('benches4'),
        x.inverter1=request.POST.get('inverter1'),
        x.inverter2=request.POST.get('inverter2'),
        x.inverter3=request.POST.get('inverter3'),
        x.inverter4=request.POST.get('inverter4'),
        x.xerox1=request.POST.get('xerox1'),
        x.xerox2=request.POST.get('xerox2'),
        x.xerox3=request.POST.get('xerox3'),
        x.xerox4=request.POST.get('xerox4'),
        x.material1=request.POST.get('material1'),
        x.material2=request.POST.get('material2'),
        x.material3=request.POST.get('material3'),
        x.material4=request.POST.get('material4'),
        x.elearning1=request.POST.get('elearning1'),
        x.elearning2=request.POST.get('elearning2'),
        x.elearning3=request.POST.get('elearning3'),
        x.elearning4=request.POST.get('elearning4'),
        x.hardware1=request.POST.get('hardware1'),
        x.hardware2=request.POST.get('hardware2'),
        x.hardware3=request.POST.get('hardware3'),
        x.hardware4=request.POST.get('hardware4'),
        x.ekun1=request.POST.get('ekun1'),
        x.ekun2=request.POST.get('ekun2'),
        x.ekun3=request.POST.get('ekun3'),
        x.ekun4=request.POST.get('ekun4'),
        x.ekun_rakkam1=request.POST.get('ekun_rakkam1'),
        x.arthik_vrsh1=request.POST.get('arthik_vrsh1'),
        x.arthik_vrsh2=request.POST.get('arthik_vrsh2'),
        x.rakkam1=request.POST.get('rakkam1'),
        x.rakkam2=request.POST.get('rakkam2'),
        x.prayojan1=request.POST.get('prayojan1'),
        x.prayojan2=request.POST.get('prayojan2'),
        x.mi=request.POST.get('mi'),
        x.hudda=request.POST.get('hudda'),
        x.pramanit=request.POST.get('pramanit'),
        x.sansthedvara=request.POST.get('sansthedvara'),
        x.sanchalit=request.POST.get('sanchalit'),
        x.signature=request.FILES.get('signature'),
        x.name=request.POST.get('name'),
        x.shikka=request.FILES.get('shikka'),
        x.photo1=request.FILES.get('photo1'),
        
        # x.umedwar_sign=request.FILES.get('umedwar_sign')
        x.save()
    else:
        x= dharmik_alp(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        sch_name=request.POST.get('sch_name'),
        anudan=request.POST.get('anudan'),
        nidhi=request.POST.get('nidhi'),
        patta=request.POST.get('patta'),
        mobile_number=request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        code=request.POST.get('code'),
        sch_sanstha=request.POST.get('sch_sanstha'),
        sanstha_patta=request.POST.get('sanstha_patta'),
        mobile_number1=request.POST.get('mobile_number1'),
        pracharya_name=request.POST.get('pracharya_name'),
        acc_no=request.POST.get('acc_no'),
        ifsc=request.POST.get('ifsc'),
        nondani_kr1=request.POST.get('nondani_kr1'),
        nondani_kr2=request.POST.get('nondani_kr2'),
        nondani_kr3=request.POST.get('nondani_kr3'),
        nondani_kr4=request.POST.get('nondani_kr4'),
        nondani_kr5=request.POST.get('nondani_kr5'),
        tarikh=request.POST.get('tarikh'),
        manjur1=request.POST.get('manjur1'),
        manjur2=request.POST.get('manjur2'),
        manjur3=request.POST.get('manjur3'),
        chalu1=request.POST.get('chalu1'),
        chalu2=request.POST.get('chalu2'),
        chalu3=request.POST.get('chalu3'),
        abhyaskram=request.POST.getlist('abhyaskram[]'),
        madhyam=request.POST.get('madhyam'),
        sankhya=request.POST.get('sankhya'),
        imaratimdhe=request.POST.get('imaratimdhe'),
        aavashyak_bandh=request.POST.get('aavashyak_bandh'),
        mahila1=request.POST.get('mahila1'),
        mahila2=request.POST.get('mahila2'),
        purush1=request.POST.get('purush1'),
        purush2=request.POST.get('purush2'),
        pani=request.POST.get('pani'),
        nutanikaran1=request.POST.get('nutanikaran1'),
        nutanikaran2=request.POST.get('nutanikaran2'),
        nutanikaran3=request.POST.get('nutanikaran3'),
        nutanikaran4=request.POST.get('nutanikaran4'),
        dagduji1=request.POST.get('dagduji1'),
        dagduji2=request.POST.get('dagduji2'),
        dagduji3=request.POST.get('dagduji3'),
        dagduji4=request.POST.get('dagduji4'),
        chhat1=request.POST.get('chhat1'),
        chhat2=request.POST.get('chhat2'),
        chhat3=request.POST.get('chhat3'),
        chhat4=request.POST.get('chhat4'),
        farshi1=request.POST.get('farshi1'),
        farshi2=request.POST.get('farshi2'),
        farshi3=request.POST.get('farshi3'),
        farshi4=request.POST.get('farshi4'),
        kooler1=request.POST.get('kooler1'),
        kooler2=request.POST.get('kooler2'),
        kooler3=request.POST.get('kooler3'),
        kooler4=request.POST.get('kooler4'),
        kits1=request.POST.get('kits1'),
        kits2=request.POST.get('kits2'),
        kits3=request.POST.get('kits3'),
        kits4=request.POST.get('kits4'),
        pustke_khredi1=request.POST.get('pustke_khredi1'),
        pustke_khredi2=request.POST.get('pustke_khredi2'),
        pustke_khredi3=request.POST.get('pustke_khredi3'),
        pustke_khredi4=request.POST.get('pustke_khredi4'),
        itar_khredi1=request.POST.get('itar_khredi1'),
        itar_khredi2=request.POST.get('itar_khredi2'),
        itar_khredi3=request.POST.get('itar_khredi3'),
        itar_khredi4=request.POST.get('itar_khredi4'),
        prayogshala1=request.POST.get('prayogshala1'),
        prayogshala2=request.POST.get('prayogshala2'),
        prayogshala3=request.POST.get('prayogshala3'),
        prayogshala4=request.POST.get('prayogshala4'),
        sanganak1=request.POST.get('sanganak1'),
        sanganak2=request.POST.get('sanganak2'),
        sanganak3=request.POST.get('sanganak3'),
        sanganak4=request.POST.get('sanganak4'),
        sankhya1=request.POST.get('sankhya1'),
        sankhya2=request.POST.get('sankhya2'),
        sankhya3=request.POST.get('sankhya3'),
        sankhya4=request.POST.get('sankhya4'),
        printers1=request.POST.get('printers1'),
        printers2=request.POST.get('printers2'),
        printers3=request.POST.get('printers3'),
        printers4=request.POST.get('printers4'),
        software1=request.POST.get('software1'),
        software2=request.POST.get('software2'),
        software3=request.POST.get('software3'),
        software4=request.POST.get('software4'),
        itar_sahity1=request.POST.get('itar_sahity1'),
        itar_sahity2=request.POST.get('itar_sahity2'),
        itar_sahity3=request.POST.get('itar_sahity3'),
        itar_sahity4=request.POST.get('itar_sahity4'),
        swachhtagruhe1=request.POST.get('swachhtagruhe1'),
        swachhtagruhe2=request.POST.get('swachhtagruhe2'),
        swachhtagruhe3=request.POST.get('swachhtagruhe3'),
        swachhtagruhe4=request.POST.get('swachhtagruhe4'),
        durusti1=request.POST.get('durusti1'),
        durusti2=request.POST.get('durusti2'),
        durusti3=request.POST.get('durusti3'),
        durusti4=request.POST.get('durusti4'),
        new_swachhtagruhe1=request.POST.get('new_swachhtagruhe1'),
        new_swachhtagruhe2=request.POST.get('new_swachhtagruhe2'),
        new_swachhtagruhe3=request.POST.get('new_swachhtagruhe3'),
        new_swachhtagruhe4=request.POST.get('new_swachhtagruhe4'),
        furniture1=request.POST.get('furniture1'),
        furniture2=request.POST.get('furniture2'),
        furniture3=request.POST.get('furniture3'),
        furniture4=request.POST.get('furniture4'),
        benches1=request.POST.get('benches1'),
        benches2=request.POST.get('benches2'),
        benches3=request.POST.get('benches3'),
        benches4=request.POST.get('benches4'),
        inverter1=request.POST.get('inverter1'),
        inverter2=request.POST.get('inverter2'),
        inverter3=request.POST.get('inverter3'),
        inverter4=request.POST.get('inverter4'),
        xerox1=request.POST.get('xerox1'),
        xerox2=request.POST.get('xerox2'),
        xerox3=request.POST.get('xerox3'),
        xerox4=request.POST.get('xerox4'),
        material1=request.POST.get('material1'),
        material2=request.POST.get('material2'),
        material3=request.POST.get('material3'),
        material4=request.POST.get('material4'),
        elearning1=request.POST.get('elearning1'),
        elearning2=request.POST.get('elearning2'),
        elearning3=request.POST.get('elearning3'),
        elearning4=request.POST.get('elearning4'),
        hardware1=request.POST.get('hardware1'),
        hardware2=request.POST.get('hardware2'),
        hardware3=request.POST.get('hardware3'),
        hardware4=request.POST.get('hardware4'),
        ekun1=request.POST.get('ekun1'),
        ekun2=request.POST.get('ekun2'),
        ekun3=request.POST.get('ekun3'),
        ekun4=request.POST.get('ekun4'),
        ekun_rakkam1=request.POST.get('ekun_rakkam1'),
        arthik_vrsh1=request.POST.get('arthik_vrsh1'),
        arthik_vrsh2=request.POST.get('arthik_vrsh2'),
        rakkam1=request.POST.get('rakkam1'),
        rakkam2=request.POST.get('rakkam2'),
        prayojan1=request.POST.get('prayojan1'),
        prayojan2=request.POST.get('prayojan2'),
        mi=request.POST.get('mi'),
        hudda=request.POST.get('hudda'),
        pramanit=request.POST.get('pramanit'),
        sansthedvara=request.POST.get('sansthedvara'),
        sanchalit=request.POST.get('sanchalit'),
        signature=request.FILES.get('signature'),
        name=request.POST.get('name'),
        shikka=request.FILES.get('shikka'),
        photo1=request.FILES.get('photo1'),
        photo2=request.FILES.get('photo2'),
        )
        
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})
    
def navin_biogas(request,pk):
    print('hi')
    if navin_rashtriy.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = navin_rashtriy.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.samiti=request.POST.get('samiti'),
        x.name=request.POST.get('name'),
        x.sanyantra=request.POST.get('sanyantra'),
        x.sandas=request.POST.get('sandas'),
        x.gas_sway=request.POST.get('gas_sway'),
        x.shetmajur=request.POST.get('shetmajur'),
        x.patta=request.POST.get('patta'),
        x.jirayat=request.POST.get('jirayat'),
        x.bagayat=request.POST.get('bagayat'),
        x.ekun=request.POST.get('ekun'),
        x.mothi=request.POST.get('mothi'),
        x.lahan=request.POST.get('lahan'),
        x.jan_ekun=request.POST.get('jan_ekun'),
        x.sandas_sankhya = request.POST.get('sandas_sankhya'),
        x.vyakti_mothi = request.POST.get('vyakti_mothi'),
        x.vyakti_lahan=request.POST.get('vyakti_lahan'),
        x.vyakti_ekun = request.POST.get('vyakti_ekun'),
        x.rakkam = request.POST.get('rakkam'),
        x.ghanmiter=request.POST.get('ghanmiter'),
        x.prakar = request.POST.get('prakar'),
        x.akar=request.POST.get('akar'),
        x.name1=request.POST.get('name1'),
        x.patta1 = request.POST.get('patta1'),
        x.arj_name1 = request.POST.get('arj_name1'),
        x.he_aar=request.POST.get('he_aar'),
        x.sankhya = request.POST.get('sankhya'),
        x.pra_akar = request.POST.get('pra_akar'),
        x.arj_name2=request.POST.get('arj_name2'),
        x.he_aar2=request.POST.get('he_aar2'),
        x.sankhya2 = request.POST.get('sankhya2'),
        x.pra_akar2 = request.POST.get('pra_akar2'),
        x.signature = request.FILES.get('signature'),
        x.save()
    else:
        x= navin_rashtriy(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        samiti=request.POST.get('samiti'),
        name=request.POST.get('name'),
        sanyantra=request.POST.get('sanyantra'),
        sandas=request.POST.get('sandas'),
        gas_sway=request.POST.get('gas_sway'),
        shetmajur=request.POST.get('shetmajur'),
        patta=request.POST.get('patta'),
        jirayat=request.POST.get('jirayat'),
        bagayat=request.POST.get('bagayat'),
        ekun=request.POST.get('ekun'),
        mothi=request.POST.get('mothi'),
        lahan=request.POST.get('lahan'),
        jan_ekun=request.POST.get('jan_ekun'),
        sandas_sankhya = request.POST.get('sandas_sankhya'),
        vyakti_mothi = request.POST.get('vyakti_mothi'),
        vyakti_lahan=request.POST.get('vyakti_lahan'),
        vyakti_ekun = request.POST.get('vyakti_ekun'),
        rakkam = request.POST.get('rakkam'),
        ghanmiter=request.POST.get('ghanmiter'),
        prakar = request.POST.get('prakar'),
        akar=request.POST.get('akar'),
        name1=request.POST.get('name1'),
        patta1 = request.POST.get('patta1'),
        arj_name1 = request.POST.get('arj_name1'),
        he_aar=request.POST.get('he_aar'),
        sankhya = request.POST.get('sankhya'),
        pra_akar = request.POST.get('pra_akar'),
        arj_name2=request.POST.get('arj_name2'),
        he_aar2=request.POST.get('he_aar2'),
        sankhya2 = request.POST.get('sankhya2'),
        pra_akar2 = request.POST.get('pra_akar2'),
        signature = request.FILES.get('signature'),
        )
        x.save()
        print("X: ",x)
        
    return JsonResponse({'status':200})

def jamin_patrika(request,pk):
    print('hi')
    if aarogya_patrika.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = aarogya_patrika.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.namuna=request.POST.get('namuna'),
        x.namuna_tarikh=request.POST.get('namuna_tarikh'),
        x.shetkari_name=request.POST.get('shetkari_name'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.mrud_namuna=request.POST.getlist('mrud_namuna[]'),
        x.gav=request.POST.get('gav'),
        x.post=request.POST.get('post'),
        x.taluka=request.POST.get('taluka'),
        x.jilha = request.POST.get('jilha'),
        x.sarve = request.POST.get('sarve'),
        x.jamin_utara=request.POST.getlist('jamin_utara[]'),
        x.panyacha = request.POST.getlist('panyacha[]'),
        x.lakshne = request.POST.get('lakshne'),
        x.jamin_kholi = request.POST.getlist('jamin_kholi[]'),
        x.pik1 = request.POST.get('pik1'),
        x.pik2=request.POST.get('pik2'),
        x.korad=request.POST.get('korad'),
        x.kshetra = request.POST.get('kshetra'),
        x.hangam_pik = request.POST.get('hangam_pik'),
        x.signature = request.FILES.get('signature'),
        x.name1 = request.POST.get('name1'),
        x.save()
    else:
        x= aarogya_patrika(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        namuna=request.POST.get('namuna'),
        namuna_tarikh=request.POST.get('namuna_tarikh'),
        shetkari_name=request.POST.get('shetkari_name'),
        mobile_number=request.POST.get('mobile_number'),
        mrud_namuna=request.POST.getlist('mrud_namuna[]'),
        gav=request.POST.get('gav'),
        post=request.POST.get('post'),
        taluka=request.POST.get('taluka'),
        jilha = request.POST.get('jilha'),
        sarve = request.POST.get('sarve'),
        jamin_utara=request.POST.getlist('jamin_utara[]'),
        panyacha = request.POST.getlist('panyacha[]'),
        lakshne = request.POST.get('lakshne'),
        jamin_kholi = request.POST.getlist('jamin_kholi[]'),
        pik1 = request.POST.get('pik1'),
        pik2=request.POST.get('pik2'),
        korad=request.POST.get('korad'),
        kshetra = request.POST.get('kshetra'),
        hangam_pik = request.POST.get('hangam_pik'),
        signature = request.FILES.get('signature'),
        name1 = request.POST.get('name1'),
        )
        x.save()
       
        
    return JsonResponse({'status':200})

def ropvatika(request,pk):
    print('hi')
    if punyshlok_ahilya.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = punyshlok_ahilya.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))
        x.jilha=request.POST.get('jilha'),
        x.san=request.POST.get('san'),
        x.doc1=request.POST.get('doc1'),
        x.doc2=request.POST.get('doc2'),
        x.doc3=request.POST.get('doc3'),
        x.doc4=request.POST.get('doc4'),
        x.doc5=request.POST.get('doc5'),
        x.doc6=request.POST.get('doc6'),
        x.doc7=request.POST.get('doc7'),
        x.doc8=request.POST.get('doc8'),
        x.doc9=request.POST.get('doc9'),
        x.varshat=request.POST.get('varshat'),
        x.san1=request.POST.get('san1'),
        x.madhe=request.POST.get('madhe'),
        x.name=request.POST.get('name'),
        x.gav=request.POST.get('gav'),
        x.pin = request.POST.get('pin'),
        x.taluka = request.POST.get('taluka'),
        x.jilha2 = request.POST.get('jilha2'),
        x.mobile_number = request.POST.get('mobile_number'),
        x.email_id=request.POST.get('email_id'),
        x.dhaar_no=request.POST.get('dhaar_no'),
        x.prakar = request.POST.get('prakar'),
        x.vargvari = request.POST.get('vargvari'),
        x.sarve_no=request.POST.get('sarve_no'),
        x.gav1=request.POST.get('gav1'),
        x.pin1=request.POST.get('pin1'),
        x.taluka1=request.POST.get('taluka1'),
        x.jilha1=request.POST.get('jilha1'),
        x.bank_name=request.POST.get('bank_name'),
        x.shakha=request.POST.get('shakha'),
        x.acc_no = request.POST.get('acc_no'),
        x.ifsc = request.POST.get('ifsc'),
        x.thikan = request.POST.get('thikan'),
        x.dinank = request.POST.get('dinank'),
        x.signature = request.FILES.get('signature'),
        x.name1 = request.POST.get('name1'),
        x.save()
    else:
        x= punyshlok_ahilya(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        jilha=request.POST.get('jilha'),
        san=request.POST.get('san'),
        doc1=request.POST.get('doc1'),
        doc2=request.POST.get('doc2'),
        doc3=request.POST.get('doc3'),
        doc4=request.POST.get('doc4'),
        doc5=request.POST.get('doc5'),
        doc6=request.POST.get('doc6'),
        doc7=request.POST.get('doc7'),
        doc8=request.POST.get('doc8'),
        doc9=request.POST.get('doc9'),
        varshat=request.POST.get('varshat'),
        san1=request.POST.get('san1'),
        madhe=request.POST.get('madhe'),
        name=request.POST.get('name'),
        gav=request.POST.get('gav'),
        pin = request.POST.get('pin'),
        taluka = request.POST.get('taluka'),
        jilha2 = request.POST.get('jilha2'),
        mobile_number = request.POST.get('mobile_number'),
        email_id=request.POST.get('email_id'),
        dhaar_no=request.POST.get('dhaar_no'),
        prakar = request.POST.get('prakar'),
        vargvari = request.POST.get('vargvari'),
        sarve_no=request.POST.get('sarve_no'),
        gav1=request.POST.get('gav1'),
        pin1=request.POST.get('pin1'),
        taluka1=request.POST.get('taluka1'),
        jilha1=request.POST.get('jilha1'),
        bank_name=request.POST.get('bank_name'),
        shakha=request.POST.get('shakha'),
        acc_no = request.POST.get('acc_no'),
        ifsc = request.POST.get('ifsc'),
        thikan = request.POST.get('thikan'),
        dinank = request.POST.get('dinank'),
        signature = request.FILES.get('signature'),
        name1 = request.POST.get('name1'),
        )
        x.save()
        print("X: ",x)
       
        
    return JsonResponse({'status':200})

def jilha_udyog(request,pk):
    print('hi')
    if jilhaudyog.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = jilhaudyog.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))

        x.prakaran_no=request.POST.get('prakaran_no'),
        x.pra_date=request.POST.get('pra_date'),
        x.sthayi_vid=request.POST.get('sthayi_vid'),
        x.khrch=request.POST.get('khrch'),
        x.name=request.POST.get('name'),
        x.money_char=request.POST.get('money_char'),
        x.money_num=request.POST.get('money_num'),
        x.candname=request.POST.get('candname'),
        x.candaddress=request.POST.get('candaddress'),
        x.mobile_number=request.POST.get('mobile_number'),
        x.varg_jat=request.POST.get('varg_jat'),
        x.compor_pedhi=request.POST.get('compor_pedhi'),
        x.business_name=request.POST.get('business_name'),
        x.work=request.POST.get('work'),
        x.ownerpartner_nameinvest=request.POST.get('ownerpartner_nameinvest'),
        x.sanchalak_name=request.POST.get('sanchalak_name'),
        x.construction=request.POST.get('construction'),
        x.land=request.POST.get('land'),
        x.machines=request.POST.get('machines'),
        x.work_expenditure=request.POST.get('work_expenditure'),
        x.total=request.POST.get('total'),
        x.Azamin=request.POST.get('Azamin'),
        x.Aemarat=request.POST.get('Aemarat'),
        x.Amachine=request.POST.get('Amachine'),
        x.Atotal_amount=request.POST.get('Atotal_amount'),
        x.Bzamin=request.POST.get('Bzamin'),
        x.Bemarat=request.POST.get('Bemarat'),
        x.Bmachine=request.POST.get('Bmachine'),
        x.Btotal_amount=request.POST.get('Btotal_amount'),
        x.business_info = request.FILES.get('business_info'),
        x.paratfed=request.POST.get('paratfed'),
        x.insurance=request.POST.get('insurance'),
        x.bankname=request.POST.get('bankname'),
        x.isloan=request.POST.get('isloan'),
        x.employees=request.POST.get('employees'),
        x.technician=request.POST.get('technician'),
        x.govenrnment_loan=request.POST.get('govenrnment_loan'),
        x.sambhavya_profit=request.POST.get('sambhavya_profit'),
        x.total_income=request.POST.get('total_income'),
        x.mal_exp=request.POST.get('mal_exp'),
        x.majuri_exp=request.POST.get('majuri_exp'),
        x.rent_exp=request.POST.get('rent_exp'),
        x.light_exp=request.POST.get('light_exp'),
        x.kirkol_exp=request.POST.get('kirkol_exp'),
        x.total_exp=request.POST.get('total_exp'),
        x.profit=request.POST.get('profit'),
        x.prashaskiy_exp=request.POST.get('prashaskiy_exp'),
        x.ownerpartner_exp=request.POST.get('ownerpartner_exp'),
        x.intrest_exp=request.POST.get('intrest_exp'),
        x.tax_exp=request.POST.get('tax_exp'),
        x.total_poit=request.POST.get('total_poit'),
        x.onlyprofit=request.POST.get('onlyprofit'),
        x.moneywith_u=request.POST.get('moneywith_u'),
        x.date=request.POST.get('date'),
        x.sign = request.FILES.get('sign'),
        x.kutumb=request.POST.get('kutumb'),
        x.chitnis=request.POST.get('chitnis'),
        x.photo = request.FILES.get('photo'),
        x.save()

    else:
        x = jilhaudyog(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        prakaran_no=request.POST.get('prakaran_no'),
        pra_date=request.POST.get('pra_date'),
        name=request.POST.get('name'),
        money_char=request.POST.get('money_char'),
        sthayi_vid=request.POST.get('sthayi_vid'),
        khrch=request.POST.get('khrch'),
        money_num=request.POST.get('money_num'),
        candname=request.POST.get('candname'),
        candaddress=request.POST.get('candaddress'),
        mobile_number=request.POST.get('mobile_number'),
        varg_jat=request.POST.get('varg_jat'),
        compor_pedhi=request.POST.get('compor_pedhi'),
        business_name=request.POST.get('business_name'),
        work=request.POST.get('work'),
        ownerpartner_nameinvest=request.POST.get('ownerpartner_nameinvest'),
        sanchalak_name=request.POST.get('sanchalak_name'),
        construction=request.POST.get('construction'),
        land=request.POST.get('land'),
        machines=request.POST.get('machines'),
        work_expenditure=request.POST.get('work_expenditure'),
        total=request.POST.get('total'),
        Azamin=request.POST.get('Azamin'),
        Aemarat=request.POST.get('Aemarat'),
        Amachine=request.POST.get('Amachine'),
        Atotal_amount=request.POST.get('Atotal_amount'),
        Bzamin=request.POST.get('Bzamin'),
        Bemarat=request.POST.get('Bemarat'),
        Bmachine=request.POST.get('Bmachine'),
        Btotal_amount=request.POST.get('Btotal_amount'),
        business_info = request.FILES.get('business_info'),
        paratfed=request.POST.get('paratfed'),
        insurance=request.POST.get('insurance'),
        bankname=request.POST.get('bankname'),
        isloan=request.POST.get('isloan'),
        employees=request.POST.get('employees'),
        technician=request.POST.get('technician'),
        govenrnment_loan=request.POST.get('govenrnment_loan'),
        sambhavya_profit=request.POST.get('sambhavya_profit'),
        total_income=request.POST.get('total_income'),
        mal_exp=request.POST.get('mal_exp'),
        majuri_exp=request.POST.get('majuri_exp'),
        rent_exp=request.POST.get('rent_exp'),
        light_exp=request.POST.get('light_exp'),
        kirkol_exp=request.POST.get('kirkol_exp'),
        total_exp=request.POST.get('total_exp'),
        profit=request.POST.get('profit'),
        prashaskiy_exp=request.POST.get('prashaskiy_exp'),
        ownerpartner_exp=request.POST.get('ownerpartner_exp'),
        intrest_exp=request.POST.get('intrest_exp'),
        tax_exp=request.POST.get('tax_exp'),
        total_poit=request.POST.get('total_poit'),
        onlyprofit=request.POST.get('onlyprofit'),
        moneywith_u=request.POST.get('moneywith_u'),
        date=request.POST.get('date'),
        sign = request.FILES.get('sign'),
        kutumb=request.POST.get('kutumb'),
        chitnis=request.POST.get('chitnis'),
        photo = request.FILES.get('photo'),
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})


def sudharit_bij(request,pk):
    print('hi')
    if sudharitbij.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = sudharitbij.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))

        x.prakrn_no=request.POST.get('prakrn_no'),
        x.pra_date=request.POST.get('pra_date'),
        x.fullname=request.POST.get('fullname'),
        x.address=request.POST.get('address'),
        x.pincode=request.POST.get('pincode'),
        x.tel_no=request.POST.get('tel_no'),
        x.mobile_no=request.POST.get('mobile_no'),
        x.bformarry_name=request.POST.get('bformarry_name'),
        x.current_edu = request.POST.get('current_edu'),
        x.current_job = request.POST.get('current_job'),
        x.business = request.POST.get('business'),
        x.loan = request.POST.get('loan'),
        x.dukan = request.POST.get('dukan'),
        x.qual=request.POST.get('qual'),
        x.birthdate=request.POST.get('birthdate'),
        x.age=request.POST.get('age'),
        x.varg_jat=request.POST.get('varg_jat'),
        x.certificate = request.FILES.get('certificate'),
        x.school_nmadrs=request.POST.get('school_nmadrs'),
        x.college_nmadrs=request.POST.get('college_nmadrs'),
        x.edu_leave=request.POST.get('edu_leave'),
        x.lastexam=request.POST.get('lastexam'),
        x.doing=request.POST.get('doing'),
        x.yojna_nm=request.POST.get('yojna_nm'),
        x.technical_edu=request.POST.get('technical_edu'),
        x.fatherhusband_name=request.POST.get('fatherhusband_name'),
        x.fatherhusband_address=request.POST.get('fatherhusband_address'),
        x.sheti=request.POST.get('sheti'),
        x.vyavsay=request.POST.get('vyavsay'),
        x.naukri=request.POST.get('naukri'),
        x.living_homeprice=request.POST.get('living_homeprice'),
        x.sheti_hector=request.POST.get('sheti_hector'),
        x.sheti_hectorprice=request.POST.get('sheti_hectorprice'),
        x.vyavsay_name=request.POST.get('vyavsay_name'),
        x.plotarea_name=request.POST.get('plotarea_name'),
        x.plotarea_price=request.POST.get('plotarea_price'),
        x.arja_name=request.POST.get('arja_name'),
        x.arja_age=request.POST.get('arja_age'),
        x.fathername=request.POST.get('fathername'),
        x.father_age=request.POST.get('father_age'),
        x.mothername=request.POST.get('mothername'),
        x.mother_age=request.POST.get('mother_age'),
        x.bro_sisname1=request.POST.get('bro_sisname1'),
        x.bro_sisage1=request.POST.get('bro_sisage1'),
        x.bro_sisname2=request.POST.get('bro_sisname2'),
        x.bro_sisage2=request.POST.get('bro_sisage2'),
        x.bro_sisname3=request.POST.get('bro_sisname3'),
        x.bro_sisage3=request.POST.get('bro_sisage3'),
        x.huswife_name=request.POST.get('huswife_name'),
        x.huswife_age=request.POST.get('huswife_age'),
        x.any_loan=request.POST.get('any_loan'),
        x.rationno_date=request.POST.get('rationno_date'),
        x.adhaar_no=request.POST.get('adhaar_no'),
        x.serviceno_date=request.POST.get('serviceno_date'),
        x.olakh1=request.POST.get('olakh1'),
        x.olakh2=request.POST.get('olakh2'),
        x.malmatta=request.POST.get('malmatta'),
        x.malak_name=request.POST.get('malak_name'),
        x.jamanatdar1=request.POST.get('jamanatdar1'),
        x.jamanatdar2=request.POST.get('jamanatdar2'),
        x.bankname_ac=request.POST.get('bankname_ac'),
        x.arjadar_date=request.POST.get('arjadar_date'),
        x.arjadar_sign = request.FILES.get('arjadar_sign'),
        x.fatherhusband_date=request.POST.get('fatherhusband_date'),
        x.fatherhusband_sign = request.FILES.get('fatherhusband_sign'),
        x.udyogname=request.POST.get('udyogname'),
        x.udyogaddress=request.POST.get('udyogaddress'),
        x.manakname_address=request.POST.get('manakname_address'),
        x.mobno=request.POST.get('mobno'),
        x.pra_rent=request.POST.get('pra_rent'),
        x.samatipatra = request.FILES.get('samatipatra'),
        x.niwad=request.POST.get('niwad'),
        x.shed=request.POST.get('shed'),
        x.machines=request.POST.get('machines'),
        x.furniture=request.POST.get('furniture'),
        x.start_mal=request.POST.get('start_mal'),
        x.milk_animal=request.POST.get('milk_animal'),
        x.light=request.POST.get('light'),
        x.other=request.POST.get('other'),
        x.total_karz=request.POST.get('total_karz'),
        x.loan_bank=request.POST.get('loan_bank'),
        x.bank_karz=request.POST.get('bank_karz'),
        x.jilha_udyog=request.POST.get('jilha_udyog'),
        x.swata_bhandwal=request.POST.get('swata_bhandwal'),
        x.totla_amount=request.POST.get('totla_amount'),
        x.machine_nameaddress=request.POST.get('machine_nameaddress'),
        x.electricity_need=request.POST.get('electricity_need'),
        x.rozgar=request.POST.get('rozgar'),
        x.monthly_sale=request.POST.get('monthly_sale'),
        x.masik_kharch=request.POST.get('masik_kharch'),
        x.dhokla_nafa=request.POST.get('dhokla_nafa'),
        x.bank_hafta=request.POST.get('bank_hafta'),
        x.kutumb_kharch=request.POST.get('kutumb_kharch'),
        x.final_sign = request.FILES.get('final_sign'),
        x.sampurn_nav=request.POST.get('sampurn_nav'),
        x.photo = request.FILES.get('photo'),
        x.save()

    else:
        x= sudharitbij(
        user=request.user,
        scheme=SchemeModel.objects.get(pk=pk),
        prakrn_no=request.POST.get('prakrn_no'),
        pra_date=request.POST.get('pra_date'),
        fullname=request.POST.get('fullname'),
        address=request.POST.get('address'),
        pincode=request.POST.get('pincode'),
        tel_no=request.POST.get('tel_no'),
        mobile_no=request.POST.get('mobile_no'),
        bformarry_name=request.POST.get('bformarry_name'),
        qual=request.POST.get('qual'),
        birthdate=request.POST.get('birthdate'),
        age=request.POST.get('age'),
        varg_jat=request.POST.get('varg_jat'),
        certificate = request.FILES.get('certificate'),
        current_edu = request.POST.get('current_edu'),
        current_job = request.POST.get('current_job'),
        business = request.POST.get('business'),
        loan = request.POST.get('loan'),
        dukan = request.POST.get('dukan'),
        school_nmadrs=request.POST.get('school_nmadrs'),
        college_nmadrs=request.POST.get('college_nmadrs'),
        edu_leave=request.POST.get('edu_leave'),
        lastexam=request.POST.get('lastexam'),
        doing=request.POST.get('doing'),
        yojna_nm=request.POST.get('yojna_nm'),
        technical_edu=request.POST.get('technical_edu'),
        fatherhusband_name=request.POST.get('fatherhusband_name'),
        fatherhusband_address=request.POST.get('fatherhusband_address'),
        sheti=request.POST.get('sheti'),
        vyavsay=request.POST.get('vyavsay'),
        naukri=request.POST.get('naukri'),
        living_homeprice=request.POST.get('living_homeprice'),
        sheti_hector=request.POST.get('sheti_hector'),
        sheti_hectorprice=request.POST.get('sheti_hectorprice'),
        vyavsay_name=request.POST.get('vyavsay_name'),
        plotarea_name=request.POST.get('plotarea_name'),
        plotarea_price=request.POST.get('plotarea_price'),
        arja_name=request.POST.get('arja_name'),
        arja_age=request.POST.get('arja_age'),
        fathername=request.POST.get('fathername'),
        father_age=request.POST.get('father_age'),
        mothername=request.POST.get('mothername'),
        mother_age=request.POST.get('mother_age'),
        bro_sisname1=request.POST.get('bro_sisname1'),
        bro_sisage1=request.POST.get('bro_sisage1'),
        bro_sisname2=request.POST.get('bro_sisname2'),
        bro_sisage2=request.POST.get('bro_sisage2'),
        bro_sisname3=request.POST.get('bro_sisname3'),
        bro_sisage3=request.POST.get('bro_sisage3'),
        huswife_name=request.POST.get('huswife_name'),
        huswife_age=request.POST.get('huswife_age'),
        any_loan=request.POST.get('any_loan'),
        rationno_date=request.POST.get('rationno_date'),
        adhaar_no=request.POST.get('adhaar_no'),
        serviceno_date=request.POST.get('serviceno_date'),
        olakh1=request.POST.get('olakh1'),
        olakh2=request.POST.get('olakh2'),
        malmatta=request.POST.get('malmatta'),
        malak_name=request.POST.get('malak_name'),
        jamanatdar1=request.POST.get('jamanatdar1'),
        jamanatdar2=request.POST.get('jamanatdar2'),
        bankname_ac=request.POST.get('bankname_ac'),
        arjadar_date=request.POST.get('arjadar_date'),
        arjadar_sign = request.FILES.get('arjadar_sign'),
        fatherhusband_date=request.POST.get('fatherhusband_date'),
        fatherhusband_sign = request.FILES.get('fatherhusband_sign'),
        udyogname=request.POST.get('udyogname'),
        udyogaddress=request.POST.get('udyogaddress'),
        manakname_address=request.POST.get('manakname_address'),
        mobno=request.POST.get('mobno'),
        pra_rent=request.POST.get('pra_rent'),
        samatipatra = request.FILES.get('samatipatra'),
        niwad=request.POST.get('niwad'),
        shed=request.POST.get('shed'),
        machines=request.POST.get('machines'),
        furniture=request.POST.get('furniture'),
        start_mal=request.POST.get('start_mal'),
        milk_animal=request.POST.get('milk_animal'),
        light=request.POST.get('light'),
        other=request.POST.get('other'),
        total_karz=request.POST.get('total_karz'),
        loan_bank=request.POST.get('loan_bank'),
        bank_karz=request.POST.get('bank_karz'),
        jilha_udyog=request.POST.get('jilha_udyog'),
        swata_bhandwal=request.POST.get('swata_bhandwal'),
        totla_amount=request.POST.get('totla_amount'),
        machine_nameaddress=request.POST.get('machine_nameaddress'),
        electricity_need=request.POST.get('electricity_need'),
        rozgar=request.POST.get('rozgar'),
        monthly_sale=request.POST.get('monthly_sale'),
        masik_kharch=request.POST.get('masik_kharch'),
        dhokla_nafa=request.POST.get('dhokla_nafa'),
        bank_hafta=request.POST.get('bank_hafta'),
        kutumb_kharch=request.POST.get('kutumb_kharch'),
        final_sign = request.FILES.get('final_sign'),
        sampurn_nav=request.POST.get('sampurn_nav'),
        photo = request.FILES.get('photo')
        )
        x.save()
        print("X: ",x)

    return JsonResponse({'status':200})
    
def asthivyang_vyaktisathi(request,pk):
    print('entered in api 1')
    if asthivyang_vyakti.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = asthivyang_vyakti.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('sampurna_nav',''),
        x.birthdate_age = request.POST.get('birthdate_age',''),
        x.birth_date = request.POST.get('birth_date',''),
        x.previous_benefit = request.POST.get('previous_benefit',''),
        x.gender = request.POST.get('gender',''),
        x.caste = request.POST.get('caste',''),
        x.education = request.POST.get('shikshan',''),
        x.married = request.POST.get('married',''),
        x.income = request.POST.get('income',''),
        x.handicap_type = request.POST.get('handicap_type',''),
        x.percent = request.POST.get('percent',''),
        x.handicap_certificate_no = request.POST.get('certificate_no',''),
        x.form_date = request.POST.get('form_date',''),
        x.business = request.POST.get('vyavsay',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.address = request.POST.get('address',''),
        x.mobile_no = request.POST.get('mobile_number',''),
        x.avashak_seva = request.POST.get('seva',''),
        x.photo = request.FILES.get('photo',''),
        x.signature = request.FILES.get('sign',''),
        x.save()
    else:
        x = asthivyang_vyakti(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('sampurna_nav',''),
        birthdate_age = request.POST.get('birthdate_age',''),
        birth_date = request.POST.get('birth_date',''),
        previous_benefit = request.POST.get('previous_benefit',''),
        gender = request.POST.get('gender',''),
        caste = request.POST.get('caste',''),
        education = request.POST.get('shikshan',''),
        married = request.POST.get('married',''),
        income = request.POST.get('income',''),
        handicap_type = request.POST.get('handicap_type',''),
        percent = request.POST.get('percent',''),
        handicap_certificate_no = request.POST.get('certificate_no',''),
        form_date = request.POST.get('form_date',''),
        business = request.POST.get('vyavsay',''),
        adhar_no = request.POST.get('adhar_no',''),
        address = request.POST.get('address',''),
        mobile_no = request.POST.get('mobile_number',''),
        avashak_seva = request.POST.get('seva',''),
        photo = request.FILES.get('photo',''),
        signature = request.FILES.get('sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})        
        

def karnbadhir_vyaktisathi(request,pk):
    print('entered in api 1')
    if karnbadhir_vyakti.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = karnbadhir_vyakti.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('sampurna_nav',''),
        x.birthdate_age = request.POST.get('birthdate_age',''),
        x.birth_date = request.POST.get('birth_date',''),
        x.previous_benefit = request.POST.get('previous_benefit',''),
        x.gender = request.POST.get('gender',''),
        x.caste = request.POST.get('caste',''),
        x.education = request.POST.get('shikshan',''),
        x.married = request.POST.get('married',''),
        x.income = request.POST.get('income',''),
        x.handicap_type = request.POST.get('handicap_type',''),
        x.percent = request.POST.get('percent',''),
        x.handicap_certificate_no = request.POST.get('certificate_no',''),
        x.form_date = request.POST.get('form_date',''),
        x.business = request.POST.get('vyavsay',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.address = request.POST.get('address',''),
        x.mobile_no = request.POST.get('mobile_number',''),
        x.avashak_seva = request.POST.get('seva',''),
        x.photo = request.FILES.get('photo',''),
        x.signature = request.FILES.get('sign',''),
        x.save()
    else:
        x = karnbadhir_vyakti(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('sampurna_nav',''),
        birthdate_age = request.POST.get('birthdate_age',''),
        previous_benefit = request.POST.get('previous_benefit',''),
        birth_date = request.POST.get('birth_date',''),
        gender = request.POST.get('gender',''),
        caste = request.POST.get('caste',''),
        education = request.POST.get('shikshan',''),
        married = request.POST.get('married',''),
        income = request.POST.get('income',''),
        handicap_type = request.POST.get('handicap_type',''),
        percent = request.POST.get('percent',''),
        handicap_certificate_no = request.POST.get('certificate_no',''),
        form_date = request.POST.get('form_date',''),
        business = request.POST.get('vyavsay',''),
        adhar_no = request.POST.get('adhar_no',''),
        address = request.POST.get('address',''),
        mobile_no = request.POST.get('mobile_number',''),
        avashak_seva = request.POST.get('seva',''),
        photo = request.FILES.get('photo',''),
        signature = request.FILES.get('sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def divyangvyakti_xerox(request,pk):
    print('entered in api 1')
    if divyang_xerox.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = divyang_xerox.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('sampurna_nav',''),
        x.birthdate_age = request.POST.get('birthdate_age',''),
        x.birth_date = request.POST.get('birth_date',''),
        x.previous_benefit = request.POST.get('previous_benefit',''),
        x.gender = request.POST.get('gender',''),
        x.caste = request.POST.get('caste',''),
        x.education = request.POST.get('shikshan',''),
        x.married = request.POST.get('married',''),
        x.income = request.POST.get('income',''),
        x.handicap_type = request.POST.get('handicap_type',''),
        x.percent = request.POST.get('percent',''),
        x.handicap_certificate_no = request.POST.get('certificate_no',''),
        x.form_date = request.POST.get('form_date',''),
        x.business = request.POST.get('vyavsay',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.address = request.POST.get('address',''),
        x.mobile_no = request.POST.get('mobile_number',''),
        x.avashak_seva = request.POST.get('seva',''),
        x.photo = request.FILES.get('photo',''),
        x.signature = request.FILES.get('sign','')
        x.save()
    else:
        x = divyang_xerox(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('sampurna_nav',''),
        birthdate_age = request.POST.get('birthdate_age',''),
        birth_date = request.POST.get('birth_date',''),
        previous_benefit = request.POST.get('previous_benefit',''),
        gender = request.POST.get('gender',''),
        caste = request.POST.get('caste',''),
        education = request.POST.get('shikshan',''),
        married = request.POST.get('married',''),
        income = request.POST.get('income',''),
        handicap_type = request.POST.get('handicap_type',''),
        percent = request.POST.get('percent',''),
        handicap_certificate_no = request.POST.get('certificate_no',''),
        form_date = request.POST.get('form_date',''),
        business = request.POST.get('vyavsay',''),
        adhar_no = request.POST.get('adhar_no',''),
        address = request.POST.get('address',''),
        mobile_no = request.POST.get('mobile_number',''),
        avashak_seva = request.POST.get('seva',''),
        photo = request.FILES.get('photo',''),
        signature = request.FILES.get('sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})       
 

def divyang_sanganakedu(request,pk):
    print('entered in api 1')
    if divyang_sanganak.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = divyang_sanganak.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('sampurna_nav',''),
        x.birthdate_age = request.POST.get('birthdate_age',''),
        x.birth_date = request.POST.get('birth_date',''),
        x.previous_benefit = request.POST.get('previous_benefit',''),
        x.gender = request.POST.get('gender',''),
        x.caste = request.POST.get('caste',''),
        x.education = request.POST.get('shikshan',''),
        x.married = request.POST.get('married',''),
        x.income = request.POST.get('income',''),
        x.handicap_type = request.POST.get('handicap_type',''),
        x.percent = request.POST.get('percent',''),
        x.handicap_certificate_no = request.POST.get('certificate_no',''),
        x.form_date = request.POST.get('form_date',''),
        x.business = request.POST.get('vyavsay',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.address = request.POST.get('address',''),
        x.mobile_no = request.POST.get('mobile_number',''),
        x.avashak_seva = request.POST.get('seva',''),
        x.photo = request.FILES.get('photo',''),
        x.signature = request.FILES.get('sign','')
        x.save()
    else:
        x = divyang_sanganak(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('sampurna_nav',''),
        birthdate_age = request.POST.get('birthdate_age',''),
        birth_date = request.POST.get('birth_date',''),
        previous_benefit = request.POST.get('previous_benefit',''),
        gender = request.POST.get('gender',''),
        caste = request.POST.get('caste',''),
        education = request.POST.get('shikshan',''),
        married = request.POST.get('married',''),
        income = request.POST.get('income',''),
        handicap_type = request.POST.get('handicap_type',''),
        percent = request.POST.get('percent',''),
        handicap_certificate_no = request.POST.get('certificate_no',''),
        form_date = request.POST.get('form_date',''),
        business = request.POST.get('vyavsay',''),
        adhar_no = request.POST.get('adhar_no',''),
        address = request.POST.get('address',''),
        mobile_no = request.POST.get('mobile_number',''),
        avashak_seva = request.POST.get('seva',''),
        photo = request.FILES.get('photo',''),
        signature = request.FILES.get('sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})


def magasvargiy_shilai(request,pk):
    print('entered in api 1')
    if magas_shilai.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = magas_shilai.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('sampurna_nav',''),
        x.address = request.POST.get('address',''),
        x.panchayat_prabhag = request.POST.get('panchayat_prabhag',''),
        x.zp_prabhag = request.POST.get('zp_prabhag',''),
        x.yojna_name = request.POST.get('yojna_name',''),
        x.jat = request.POST.get('jat',''),
        x.caste = request.POST.get('caste',''),
        x.birthdate = request.POST.get('birthdate',''),
        x.education = request.POST.get('shikshan',''),
        x.san = request.POST.get('san',''),
        x.income = request.POST.get('income',''),
        x.daridray = request.POST.get('daridray',''),
        x.kutumb_no = request.POST.get('kutumb_no',''),
        x.sheti = request.POST.get('sheti',''),
        x.taluka = request.POST.get('taluka',''),
        x.gav = request.POST.get('gav',''),
        x.shetrafal = request.POST.get('shetrafal',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.bank = request.POST.get('bank',''),
        x.thikan = request.POST.get('thikan',''),
        x.dinank = request.POST.get('dinank',''),
        x.purn_nav = request.POST.get('purn_nav'),
        x.patta = request.POST.get('patta'),
        x.photo = request.FILES.get('photo',''),
        x.signature = request.FILES.get('sign','')
        x.save()
    else:
        x = magas_shilai(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('sampurna_nav',''),
        address = request.POST.get('address',''),
        panchayat_prabhag = request.POST.get('panchayat_prabhag',''),
        zp_prabhag = request.POST.get('zp_prabhag',''),
        yojna_name = request.POST.get('yojna_name',''),
        jat = request.POST.get('jat',''),
        caste = request.POST.get('caste',''),
        birthdate = request.POST.get('birthdate',''),
        education = request.POST.get('shikshan',''),
        san = request.POST.get('san',''),
        income = request.POST.get('income',''),
        daridray = request.POST.get('daridray',''),
        kutumb_no = request.POST.get('kutumb_no',''),
        sheti = request.POST.get('sheti',''),
        taluka = request.POST.get('taluka',''),
        gav = request.POST.get('gav',''),
        shetrafal = request.POST.get('shetrafal',''),
        adhar_no = request.POST.get('adhar_no',''),
        bank = request.POST.get('bank',''),
        thikan = request.POST.get('thikan',''),
        dinank = request.POST.get('dinank',''),
        purn_nav = request.POST.get('purn_nav'),
        patta = request.POST.get('patta'),
        photo = request.FILES.get('photo',''),
        signature = request.FILES.get('sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def dubhtya_janawarankarita(request,pk):
    print('entered in api 1')
    if dubhte_janawar.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = dubhte_janawar.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.address = request.POST.get('address',''),
        x.jat = request.POST.get('jat',''),
        x.janwar = request.POST.get('janwar',''),
        x.sudharit = request.POST.get('sudharit',''),
        x.kilo = request.POST.get('kilo',''),
        x.sign = request.FILES.get('sign',''),
        x.nav = request.POST.get('nav',''),
        x.patta = request.POST.get('patta','')
        x.save()

    else:
        x = dubhte_janawar(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        address = request.POST.get('address',''),
        jat = request.POST.get('jat',''),
        janwar = request.POST.get('janwar',''),
        sudharit = request.POST.get('sudharit',''),
        kilo = request.POST.get('kilo',''),
        sign = request.FILES.get('sign',''),
        nav = request.POST.get('nav',''),
        patta = request.POST.get('patta','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})


def anusuchitjati_50takke(request,pk):
    print('entered in api 1')
    if anusuchit_50takke.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = anusuchit_50takke.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.photo_id = request.FILES.get('photo_id',''),
        x.mukampost = request.POST.get('mukampost',''),
        x.taluka = request.POST.get('taluka',''),
        x.pincode = request.POST.get('pincode',''),
        x.mobile_no = request.POST.get('mobile_no',''),
        x.age_year = request.POST.get('age_year',''),
        x.age_month = request.POST.get('age_month',''),
        x.gender = request.POST.get('gender',''),
        x.daridrya_yn = request.POST.get('daridrya_yn',''),
        x.daridry_cf = request.FILES.get('daridry_cf',''),
        x.jaga_yn = request.POST.get('jaga_yn',''),
        x.prashikshan_yn = request.POST.get('prashikshan_yn',''),
        x.anujamat_yn = request.POST.get('anujamat_yn',''),
        x.bhumihin_yn = request.POST.get('bhumihin_yn',''),
        x.bachatgat_yn = request.POST.get('bachatgat_yn',''),
        x.bachatgat_name = request.POST.get('bachatgat_name',''),
        x.bachatgat_address = request.POST.get('bachatgat_address',''),
        x.bachatgat_shetra = request.POST.get('bachatgat_shetra',''),
        x.berozgar_yn = request.POST.get('berozgar_yn',''),
        x.sevayojna_cf = request.FILES.get('sevayojna_cf',''),
        x.sign = request.FILES.get('sign',''),
        x.photo = request.FILES.get('photo',''),
        x.nav = request.POST.get('nav',''),
        x.place = request.POST.get('place',''),
        x.dinank = request.POST.get('dinank','')
        x.save()

    else:
        x = anusuchit_50takke(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        photo_id = request.FILES.get('photo_id',''),
        mukampost = request.POST.get('mukampost',''),
        taluka = request.POST.get('taluka',''),
        pincode = request.POST.get('pincode',''),
        mobile_no = request.POST.get('mobile_no',''),
        age_year = request.POST.get('age_year',''),
        age_month = request.POST.get('age_month',''),
        gender = request.POST.get('gender',''),
        daridrya_yn = request.POST.get('daridrya_yn',''),
        daridry_cf = request.FILES.get('daridry_cf',''),
        jaga_yn = request.POST.get('jaga_yn',''),
        prashikshan_yn = request.POST.get('prashikshan_yn',''),
        anujamat_yn = request.POST.get('anujamat_yn',''),
        bhumihin_yn = request.POST.get('bhumihin_yn',''),
        bachatgat_yn = request.POST.get('bachatgat_yn',''),
        bachatgat_name = request.POST.get('bachatgat_name',''),
        bachatgat_address = request.POST.get('bachatgat_address',''),
        bachatgat_shetra = request.POST.get('bachatgat_shetra',''),
        berozgar_yn = request.POST.get('berozgar_yn',''),
        sevayojna_cf = request.FILES.get('sevayojna_cf',''),
        sign = request.FILES.get('sign',''),
        photo = request.FILES.get('photo',''),
        nav = request.POST.get('nav',''),
        place = request.POST.get('place',''),
        dinank = request.POST.get('dinank','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})


def anusuchit_dudhaljanavare(request,pk):
    print('entered in api 1')
    if anusuchit_janavare.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = anusuchit_janavare.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.photo_id = request.FILES.get('photo_id',''),
        x.mukampost = request.POST.get('mukampost',''),
        x.taluka = request.POST.get('taluka',''),
        x.pincode = request.POST.get('pincode',''),
        x.mobile_no = request.POST.get('mobile_no',''),
        x.age_year = request.POST.get('age_year',''),
        x.gender = request.POST.get('gender',''),
        x.daridrya_yn = request.POST.get('daridrya_yn',''),
        x.shetjamin_yn = request.POST.get('shetjamin_yn',''),
        x.sankarit_gayi = request.POST.get('sankarit_gayi',''),
        x.gavthi_gayi = request.POST.get('gavthi_gayi',''),
        x.sheti_bail = request.POST.get('sheti_bail',''),
        x.murha_mhais = request.POST.get('murha_mhais',''),
        x.gotha_yn = request.POST.get('gotha_yn',''),
        x.kiti_janavar = request.POST.get('kiti_janavar',''),
        x.dughdautpadan_yn = request.POST.get('dughdautpadan_yn',''),
        x.dughdautpadan_cf = request.FILES.get('dughdautpadan_cf',''),
        x.anuadi_yn = request.POST.get('anuadi_yn',''),
        x.anuadi_cf = request.FILES.get('anuadi_cf',''),
        x.bachatgat_yn = request.POST.get('bachatgat_yn',''),
        x.bachatgat_name = request.POST.get('bachatgat_name',''),
        x.bachatgat_address = request.POST.get('bachatgat_address',''),
        x.bachatgat_shetra = request.POST.get('bachatgat_shetra',''),
        x.berozgar_yn = request.POST.get('berozgar_yn',''),
        x.sevayojna_cf = request.FILES.get('sevayojna_cf',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.bank_branch = request.POST.get('bank_branch',''),
        x.sign = request.FILES.get('sign',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = anusuchit_janavare(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        photo_id = request.FILES.get('photo_id',''),
        mukampost = request.POST.get('mukampost',''),
        taluka = request.POST.get('taluka',''),
        pincode = request.POST.get('pincode',''),
        mobile_no = request.POST.get('mobile_no',''),
        age_year = request.POST.get('age_year',''),
        gender = request.POST.get('gender',''),
        daridrya_yn = request.POST.get('daridrya_yn',''),
        shetjamin_yn = request.POST.get('shetjamin_yn',''),
        sankarit_gayi = request.POST.get('sankarit_gayi',''),
        gavthi_gayi = request.POST.get('gavthi_gayi',''),
        sheti_bail = request.POST.get('sheti_bail',''),
        murha_mhais = request.POST.get('murha_mhais',''),
        gotha_yn = request.POST.get('gotha_yn',''),
        kiti_janavar = request.POST.get('kiti_janavar',''),
        dughdautpadan_yn = request.POST.get('dughdautpadan_yn',''),
        dughdautpadan_cf = request.FILES.get('dughdautpadan_cf',''),
        anuadi_yn = request.POST.get('anuadi_yn',''),
        anuadi_cf = request.FILES.get('anuadi_cf',''),
        bachatgat_yn = request.POST.get('bachatgat_yn',''),
        bachatgat_name = request.POST.get('bachatgat_name',''),
        bachatgat_address = request.POST.get('bachatgat_address',''),
        bachatgat_shetra = request.POST.get('bachatgat_shetra',''),
        berozgar_yn = request.POST.get('berozgar_yn',''),
        sevayojna_cf = request.FILES.get('sevayojna_cf',''),
        bank_name = request.POST.get('bank_name',''),
        bank_branch = request.POST.get('bank_branch',''),
        sign = request.FILES.get('sign',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})


def anusuchit_75takkeshelya(request,pk):
    print('entered in api 1')
    if anusuchit_shelya.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = anusuchit_shelya.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.photo_id = request.FILES.get('photo_id',''),
        x.mukampost = request.POST.get('mukampost',''),
        x.taluka = request.POST.get('taluka',''),
        x.pincode = request.POST.get('pincode',''),
        x.mobile_no = request.POST.get('mobile_no',''),
        x.age_year = request.POST.get('age_year',''),
        x.gender = request.POST.get('gender',''),
        x.daridrya_yn = request.POST.get('daridrya_yn',''),
        x.gents = request.POST.get('gents',''),
        x.ladies = request.POST.get('ladies',''),
        x.total = request.POST.get('total',''),
        x.shetjamin_yn = request.POST.get('shetjamin_yn',''),
        x.acre = request.POST.get('acre',''),
        x.gunthe = request.POST.get('gunthe',''),
        x.utara1 = request.FILES.get('utara1',''),
        x.utara2 = request.FILES.get('utara2',''),
        x.samatipatra = request.FILES.get('samatipatra',''),
        x.sinchan_yn = request.POST.get('sinchan_yn',''),
        x.sankarit_gayi = request.POST.get('sankarit_gayi',''),
        x.gavthi_gayi = request.POST.get('gavthi_gayi',''),
        x.shelya = request.POST.get('shelya',''),
        x.sheti_bail = request.POST.get('sheti_bail',''),
        x.murha_mhais = request.POST.get('murha_mhais',''),
        x.mendhya = request.POST.get('mendhya',''),
        x.waada_yn = request.POST.get('waada_yn',''),
        x.kiti_janavar = request.POST.get('kiti_janavar',''),
        x.waada_type = request.POST.get('waada_type',''),
        x.prashikshan_yn = request.POST.get('prashikshan_yn',''),
        x.tapshil = request.POST.get('tapshil',''),
        x.prashikshan_cf = request.FILES.get('prashikshan_cf',''),
        x.anuadi_yn = request.POST.get('anuadi_yn',''),
        x.anuadi_cf = request.FILES.get('anuadi_cf',''),
        x.bachatgat_yn = request.POST.get('bachatgat_yn',''),
        x.bachatgat_name = request.POST.get('bachatgat_name',''),
        x.bachatgat_address = request.POST.get('bachatgat_address',''),
        x.berozgar_yn = request.POST.get('berozgar_yn',''),
        x.sevayojna_cf = request.FILES.get('sevayojna_cf',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.bank_branch = request.POST.get('bank_branch',''),
        x.sign = request.FILES.get('sign',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = anusuchit_shelya(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        photo_id = request.FILES.get('photo_id',''),
        mukampost = request.POST.get('mukampost',''),
        taluka = request.POST.get('taluka',''),
        pincode = request.POST.get('pincode',''),
        mobile_no = request.POST.get('mobile_no',''),
        age_year = request.POST.get('age_year',''),
        gender = request.POST.get('gender',''),
        daridrya_yn = request.POST.get('daridrya_yn',''),
        gents = request.POST.get('gents',''),
        ladies = request.POST.get('ladies',''),
        total = request.POST.get('total',''),
        shetjamin_yn = request.POST.get('shetjamin_yn',''),
        acre = request.POST.get('acre',''),
        gunthe = request.POST.get('gunthe',''),
        utara1 = request.FILES.get('utara1',''),
        utara2 = request.FILES.get('utara2',''),
        samatipatra = request.FILES.get('samatipatra',''),
        sinchan_yn = request.POST.get('sinchan_yn',''),
        sankarit_gayi = request.POST.get('sankarit_gayi',''),
        gavthi_gayi = request.POST.get('gavthi_gayi',''),
        shelya = request.POST.get('shelya',''),
        sheti_bail = request.POST.get('sheti_bail',''),
        murha_mhais = request.POST.get('murha_mhais',''),
        mendhya = request.POST.get('mendhya',''),
        waada_yn = request.POST.get('waada_yn',''),
        kiti_janavar = request.POST.get('kiti_janavar',''),
        waada_type = request.POST.get('waada_type',''),
        prashikshan_yn = request.POST.get('prashikshan_yn',''),
        tapshil = request.POST.get('tapshil',''),
        prashikshan_cf = request.FILES.get('prashikshan_cf',''),
        anuadi_yn = request.POST.get('anuadi_yn',''),
        anuadi_cf = request.FILES.get('anuadi_cf',''),
        bachatgat_yn = request.POST.get('bachatgat_yn',''),
        bachatgat_name = request.POST.get('bachatgat_name',''),
        bachatgat_address = request.POST.get('bachatgat_address',''),
        berozgar_yn = request.POST.get('berozgar_yn',''),
        sevayojna_cf = request.FILES.get('sevayojna_cf',''),
        bank_name = request.POST.get('bank_name',''),
        bank_branch = request.POST.get('bank_branch',''),
        sign = request.FILES.get('sign',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def thakkar_bappa(request,pk):
    print('hi')
    if thakkar.objects.filter(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk)).exists():
        x = thakkar.objects.get(user=request.user,
        scheme=SchemeModel.objects.get(pk=pk))

        x.san=request.POST.get('san'),
        x.gp_name=request.POST.get('gp_name'),
        x.tbarea_name=request.POST.get('tbarea_name'),
        x.paripurn_patta=request.POST.get('paripurn_patta'),
        x.total_population=request.POST.get('total_population'),
        x.anusuchit_population=request.POST.get('anusuchit_population'),
        x.living_castes=request.POST.get('living_castes'),
        x.prastav_bandhkam = request.POST.get('prastav_bandhkam'),
        x.anudan_amount = request.POST.get('anudan_amount'),
        x.bfor_anudan = request.POST.get('bfor_anudan'),
        x.gp_xtranudan = request.FILES.get('gp_xtranudan'),
        x.gp_sixmonth = request.FILES.get('gp_sixmonth'),
        x.talathi_satbara = request.FILES.get('talathi_satbara'),
        x.gp_shilak = request.FILES.get('gp_shilak'),
        x.sachivsign = request.FILES.get('sachivsign'),
        x.sarpanchsign = request.FILES.get('sarpanchsign')

        x.save()
    else:
        x = thakkar(
        user=request.user,scheme=SchemeModel.objects.get(pk=pk),
        san=request.POST.get('san'),
        gp_name=request.POST.get('gp_name'),
        tbarea_name=request.POST.get('tbarea_name'),
        paripurn_patta=request.POST.get('paripurn_patta'),
        total_population=request.POST.get('total_population'),
        anusuchit_population=request.POST.get('anusuchit_population'),
        living_castes=request.POST.get('living_castes'),
        prastav_bandhkam = request.POST.get('prastav_bandhkam'),
        anudan_amount = request.POST.get('anudan_amount'),
        gp_xtranudan = request.FILES.get('gp_xtranudan'),
        gp_sixmonth = request.FILES.get('gp_sixmonth'),
        talathi_satbara = request.FILES.get('talathi_satbara'),
        gp_shilak = request.FILES.get('gp_shilak'),
        sachivsign = request.FILES.get('sachivsign'),
        sarpanchsign = request.FILES.get('sarpanchsign'),
        bfor_anudan = request.POST.get('bfor_anudan'),
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def anusuchit_shabriyojna(request,pk):
    print('entered in api 1')
    if anusuchit_shabri.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = anusuchit_shabri.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.jilha = request.POST.get('jilha',''),
        x.name = request.POST.get('name',''),
        x.address = request.POST.get('address',''),
        x.jat = request.POST.get('jat',''),
        x.birthdate = request.POST.get('birthdate',''),
        x.age = request.POST.get('age',''),
        x.gender = request.POST.get('gender',''),
        x.married = request.POST.get('married',''),
        x.son = request.POST.get('son',''),
        x.daughter = request.POST.get('daughter',''),
        x.total_child = request.POST.get('total_child',''),
        x.ladies = request.POST.get('ladies',''),
        x.gents = request.POST.get('gents',''),
        x.total = request.POST.get('total',''),
        x.education = request.POST.get('education',''),
        x.yojna = request.POST.get('yojna',''),
        x.samu_vayaktik = request.POST.get('samu_vayaktik',''),
        x.daridrya_cardno = request.POST.get('daridrya_cardno',''),
        x.income = request.POST.get('income',''),
        x.income_src = request.POST.get('income_src',''),
        x.jaga = request.POST.get('jaga',''),
        x.alpa_bhudharak = request.POST.get('alpa_bhudharak',''),
        x.alpa_cf = request.FILES.get('alpa_cf',''),
        x.bhumihin = request.POST.get('bhumihin',''),
        x.bhumihin_cf = request.FILES.get('bhumihin_cf',''),
        x.vidhva = request.POST.get('vidhva',''),
        x.vidhva_cf = request.FILES.get('vidhva_cf',''),
        x.vidhur = request.POST.get('vidhur',''),
        x.vidhur_cf = request.FILES.get('vidhur_cf',''),
        x.ghatsphotit = request.POST.get('ghatsphotit',''),
        x.ghatsphotit_cf = request.FILES.get('ghatsphotit_cf',''),
        x.bhukampgrast = request.POST.get('bhukampgrast',''),
        x.bhukamp_cf = request.FILES.get('bhukamp_cf',''),
        x.apang = request.POST.get('apang',''),
        x.apang_cf = request.FILES.get('apang_cf',''),
        x.dharangrast = request.POST.get('dharangrast',''),
        x.dharangrast_cf = request.FILES.get('dharangrast_cf',''),
        x.majhi_sainik = request.POST.get('majhi_sainik',''),
        x.sainik_cf = request.FILES.get('sainik_cf',''),
        x.labh = request.POST.get('labh',''),
        x.yojna1 = request.POST.get('yojna1',''),
        x.year1 = request.POST.get('year1',''),
        x.yojna2 = request.POST.get('yojna2',''),
        x.year2 = request.POST.get('year2',''),
        x.dinank = request.POST.get('dinank',''),
        x.photo = request.FILES.get('photo',''),
        x.sign = request.FILES.get('sign',''),
        x.place = request.POST.get('place','')
        x.save()

    else:
        x = anusuchit_shabri(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        jilha = request.POST.get('jilha',''),
        name = request.POST.get('name',''),
        address = request.POST.get('address',''),
        jat = request.POST.get('jat',''),
        birthdate = request.POST.get('birthdate',''),
        age = request.POST.get('age',''),
        gender = request.POST.get('gender',''),
        married = request.POST.get('married',''),
        son = request.POST.get('son',''),
        daughter = request.POST.get('daughter',''),
        total_child = request.POST.get('total_child',''),
        ladies = request.POST.get('ladies',''),
        gents = request.POST.get('gents',''),
        total = request.POST.get('total',''),
        education = request.POST.get('education',''),
        yojna = request.POST.get('yojna',''),
        samu_vayaktik = request.POST.get('samu_vayaktik',''),
        daridrya_cardno = request.POST.get('daridrya_cardno',''),
        income = request.POST.get('income',''),
        income_src = request.POST.get('income_src',''),
        jaga = request.POST.get('jaga',''),
        alpa_bhudharak = request.POST.get('alpa_bhudharak',''),
        alpa_cf = request.FILES.get('alpa_cf',''),
        bhumihin = request.POST.get('bhumihin',''),
        bhumihin_cf = request.FILES.get('bhumihin_cf',''),
        vidhva = request.POST.get('vidhva',''),
        vidhva_cf = request.FILES.get('vidhva_cf',''),
        vidhur = request.POST.get('vidhur',''),
        vidhur_cf = request.FILES.get('vidhur_cf',''),
        ghatsphotit = request.POST.get('ghatsphotit',''),
        ghatsphotit_cf = request.FILES.get('ghatsphotit_cf',''),
        bhukampgrast = request.POST.get('bhukampgrast',''),
        bhukamp_cf = request.FILES.get('bhukamp_cf',''),
        apang = request.POST.get('apang',''),
        apang_cf = request.FILES.get('apang_cf',''),
        dharangrast = request.POST.get('dharangrast',''),
        dharangrast_cf = request.FILES.get('dharangrast_cf',''),
        majhi_sainik = request.POST.get('majhi_sainik',''),
        sainik_cf = request.FILES.get('sainik_cf',''),
        labh = request.POST.get('labh',''),
        yojna1 = request.POST.get('yojna1',''),
        year1 = request.POST.get('year1',''),
        yojna2 = request.POST.get('yojna2',''),
        year2 = request.POST.get('year2',''),
        dinank = request.POST.get('dinank',''),
        photo = request.FILES.get('photo',''),
        sign = request.FILES.get('sign',''),
        place = request.POST.get('place','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def bhumihin_daridryaadivasi(request,pk):
    print('entered in api 1')
    if bhumihin_daridrya.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = bhumihin_daridrya.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.jilha = request.POST.get('jilha',''),
        x.name = request.POST.get('name',''),
        x.huswife_name = request.POST.get('huswife_name',''),
        x.address = request.POST.get('address',''),
        x.anu_jamat = request.POST.get('anu_jamat',''),
        x.adim_jamat = request.POST.get('adim_jamat',''),
        x.striya = request.POST.get('striya',''),
        x.vidhwa = request.POST.get('vidhwa',''),
        x.bhumihin_yn = request.POST.get('bhumihin_yn',''),
        x.daridrya_yn = request.POST.get('daridrya_yn',''),
        x.daridrya_no = request.POST.get('daridrya_no',''),
        x.talathi_cf = request.FILES.get('talathi_cf',''),
        x.age = request.POST.get('age',''),
        x.labhdharak_yn = request.POST.get('labhdharak_yn',''),
        x.tapshil = request.POST.get('tapshil',''),
        x.jamin_yn = request.POST.get('jamin_yn',''),
        x.atikraman_yn = request.POST.get('atikraman_yn',''),
        x.pratidnyapatra = request.FILES.get('pratidnyapatra',''),
        x.hamipatra = request.FILES.get('hamipatra',''),
        x.mashagat = request.POST.get('mashagat',''),
        x.income_yn = request.POST.get('income_yn',''),
        x.water_src = request.POST.get('water_src',''),
        x.yojnalabh_yn = request.POST.get('yojnalabh_yn',''),
        x.yojna1 = request.POST.get('yojna1',''),
        x.year1 = request.POST.get('year1',''),
        x.yojna2 = request.POST.get('yojna2',''),
        x.year2 = request.POST.get('year2',''),
        x.dinank = request.POST.get('dinank',''),
        x.place = request.POST.get('place',''),
        x.sign = request.FILES.get('sign',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = bhumihin_daridrya(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        jilha = request.POST.get('jilha',''),
        name = request.POST.get('name',''),
        huswife_name = request.POST.get('huswife_name',''),
        address = request.POST.get('address',''),
        anu_jamat = request.POST.get('anu_jamat',''),
        adim_jamat = request.POST.get('adim_jamat',''),
        striya = request.POST.get('striya',''),
        vidhwa = request.POST.get('vidhwa',''),
        bhumihin_yn = request.POST.get('bhumihin_yn',''),
        daridrya_yn = request.POST.get('daridrya_yn',''),
        daridrya_no = request.POST.get('daridrya_no',''),
        talathi_cf = request.FILES.get('talathi_cf',''),
        age = request.POST.get('age',''),
        labhdharak_yn = request.POST.get('labhdharak_yn',''),
        tapshil = request.POST.get('tapshil',''),
        jamin_yn = request.POST.get('jamin_yn',''),
        atikraman_yn = request.POST.get('atikraman_yn',''),
        pratidnyapatra = request.FILES.get('pratidnyapatra',''),
        hamipatra = request.FILES.get('hamipatra',''),
        mashagat = request.POST.get('mashagat',''),
        income_yn = request.POST.get('income_yn',''),
        water_src = request.POST.get('water_src',''),
        yojnalabh_yn = request.POST.get('yojnalabh_yn',''),
        yojna1 = request.POST.get('yojna1',''),
        year1 = request.POST.get('year1',''),
        yojna2 = request.POST.get('yojna2',''),
        year2 = request.POST.get('year2',''),
        dinank = request.POST.get('dinank',''),
        place = request.POST.get('place',''),
        sign = request.FILES.get('sign',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def samuhik_vivahsohla(request,pk):
    print('entered in api 1')
    if samuhik_vivah.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = samuhik_vivah.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.sanstha_name = request.POST.get('sanstha_name',''),
        x.sanstha_add = request.POST.get('sanstha_add',''),
        x.date = request.POST.get('date',''),
        x.reg_no = request.POST.get('reg_no',''),
        x.thikani = request.POST.get('thikani',''),
        x.time = request.POST.get('time',''),
        x.padadhikari = request.POST.get('padadhikari',''),
        x.hudda = request.POST.get('hudda',''),
        x.var_name = request.POST.get('var_name',''),
        x.var_birhtdate = request.POST.get('var_birhtdate',''),
        x.var_age = request.POST.get('var_age',''),
        x.var_dharma = request.POST.get('var_dharma',''),
        x.var_jat = request.POST.get('var_jat',''),
        x.var_potjat = request.POST.get('var_potjat',''),
        x.var_edu = request.POST.get('var_edu',''),
        x.var_add = request.POST.get('var_add',''),
        x.var_gav = request.POST.get('var_gav',''),
        x.var_tal = request.POST.get('var_tal',''),
        x.var_dist = request.POST.get('var_dist',''),
        x.var_mobile = request.POST.get('var_mobile',''),
        x.vadhu_name = request.POST.get('vadhu_name',''),
        x.vadhu_birhtdate = request.POST.get('vadhu_birhtdate',''),
        x.vadhu_age = request.POST.get('vadhu_age',''),
        x.vadhu_dharma = request.POST.get('vadhu_dharma',''),
        x.vadhu_jat = request.POST.get('vadhu_jat',''),
        x.vadhu_potjat = request.POST.get('vadhu_potjat',''),
        x.vadhu_edu = request.POST.get('vadhu_edu',''),
        x.vadhu_add = request.POST.get('vadhu_add',''),
        x.vadhu_gav = request.POST.get('vadhu_gav',''),
        x.vadhu_tal = request.POST.get('vadhu_tal',''),
        x.vadhu_dist = request.POST.get('vadhu_dist',''),
        x.vadhu_mobile = request.POST.get('vadhu_mobile',''),
        x.tapal_add = request.POST.get('tapal_add',''),
        x.niwas = request.POST.get('niwas',''),
        x.karyalay = request.POST.get('karyalay',''),
        x.other = request.POST.get('other',''),
        x.sanstha = request.POST.get('sanstha',''),
        x.vivah_thikan = request.POST.get('vivah_thikan',''),
        x.vivahdate = request.POST.get('vivahdate',''),
        x.vivah_type = request.POST.get('vivah_type',''),
        x.var_firstvivah = request.POST.get('var_firstvivah',''),
        x.vadhu_firstvivah = request.POST.get('vadhu_firstvivah',''),
        x.var_vidur = request.POST.get('var_vidur',''),
        x.vadhu_vidhva = request.POST.get('vadhu_vidhva',''),
        x.bfor_yojna = request.POST.get('bfor_yojna',''),
        x.anya_zp = request.POST.get('anya_zp',''),
        x.dinank = request.POST.get('dinank',''),
        x.place = request.POST.get('place',''),
        x.var_nm = request.POST.get('var_nm',''),
        x.var_sign = request.FILES.get('var_sign',''),
        x.var_photo = request.FILES.get('var_photo',''),
        x.vadhu_nm = request.POST.get('vadhu_nm',''),
        x.vadhu_sign = request.FILES.get('vadhu_sign',''),
        x.vadhu_photo = request.FILES.get('vadhu_photo','')
        x.save()

    else:
        x = samuhik_vivah(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        sanstha_name = request.POST.get('sanstha_name',''),
        sanstha_add = request.POST.get('sanstha_add',''),
        date = request.POST.get('date',''),
        reg_no = request.POST.get('reg_no',''),
        thikani = request.POST.get('thikani',''),
        time = request.POST.get('time',''),
        padadhikari = request.POST.get('padadhikari',''),
        hudda = request.POST.get('hudda',''),
        var_name = request.POST.get('var_name',''),
        var_birhtdate = request.POST.get('var_birhtdate',''),
        var_age = request.POST.get('var_age',''),
        var_dharma = request.POST.get('var_dharma',''),
        var_jat = request.POST.get('var_jat',''),
        var_potjat = request.POST.get('var_potjat',''),
        var_edu = request.POST.get('var_edu',''),
        var_add = request.POST.get('var_add',''),
        var_gav = request.POST.get('var_gav',''),
        var_tal = request.POST.get('var_tal',''),
        var_dist = request.POST.get('var_dist',''),
        var_mobile = request.POST.get('var_mobile',''),
        vadhu_name = request.POST.get('vadhu_name',''),
        vadhu_birhtdate = request.POST.get('vadhu_birhtdate',''),
        vadhu_age = request.POST.get('vadhu_age',''),
        vadhu_dharma = request.POST.get('vadhu_dharma',''),
        vadhu_jat = request.POST.get('vadhu_jat',''),
        vadhu_potjat = request.POST.get('vadhu_potjat',''),
        vadhu_edu = request.POST.get('vadhu_edu',''),
        vadhu_add = request.POST.get('vadhu_add',''),
        vadhu_gav = request.POST.get('vadhu_gav',''),
        vadhu_tal = request.POST.get('vadhu_tal',''),
        vadhu_dist = request.POST.get('vadhu_dist',''),
        vadhu_mobile = request.POST.get('vadhu_mobile',''),
        tapal_add = request.POST.get('tapal_add',''),
        niwas = request.POST.get('niwas',''),
        karyalay = request.POST.get('karyalay',''),
        other = request.POST.get('other',''),
        sanstha = request.POST.get('sanstha',''),
        vivah_thikan = request.POST.get('vivah_thikan',''),
        vivahdate = request.POST.get('vivahdate',''),
        vivah_type = request.POST.get('vivah_type',''),
        var_firstvivah = request.POST.get('var_firstvivah',''),
        vadhu_firstvivah = request.POST.get('vadhu_firstvivah',''),
        var_vidur = request.POST.get('var_vidur',''),
        vadhu_vidhva = request.POST.get('vadhu_vidhva',''),
        bfor_yojna = request.POST.get('bfor_yojna',''),
        anya_zp = request.POST.get('anya_zp',''),
        dinank = request.POST.get('dinank',''),
        place = request.POST.get('place',''),
        var_nm = request.POST.get('var_nm',''),
        var_sign = request.FILES.get('var_sign',''),
        var_photo = request.FILES.get('var_photo',''),
        vadhu_nm = request.POST.get('vadhu_nm',''),
        vadhu_sign = request.FILES.get('vadhu_sign',''),
        vadhu_photo = request.FILES.get('vadhu_photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def anuswechaa_ashramshala(request,pk):
    print('entered in api 1')
    if anusuchit_swechha.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = anusuchit_swechha.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.father_palak = request.POST.get('father_palak',''),
        x.nate = request.POST.get('nate',''),
        x.father_edu = request.POST.get('father_edu',''),
        x.mother_name = request.POST.get('mother_name',''),
        x.mom_edu = request.POST.get('mom_edu',''),
        x.jat = request.POST.get('jat',''),
        x.potjat = request.POST.get('potjat',''),
        x.dharma = request.POST.get('dharma',''),
        x.gender = request.POST.get('gender',''),
        x.nationality = request.POST.get('nationality',''),
        x.birthdate = request.POST.get('birthdate',''),
        x.birth_letter = request.POST.get('birth_letter',''),
        x.mukam = request.POST.get('mukam',''),
        x.post = request.POST.get('post',''),
        x.taluka = request.POST.get('taluka',''),
        x.jilha = request.POST.get('jilha',''),
        x.mobile = request.POST.get('mobile',''),
        x.mukam2 = request.POST.get('mukam2',''),
        x.post2 = request.POST.get('post2',''),
        x.taluka2 = request.POST.get('taluka2',''),
        x.jilha2 = request.POST.get('jilha2',''),
        x.mobile2 = request.POST.get('mobile2',''),
        x.language = request.POST.get('language',''),
        x.std = request.POST.get('std',''),
        x.reason = request.POST.get('reason',''),
        x.passed = request.POST.get('passed',''),
        x.year = request.POST.get('year',''),
        x.percent = request.POST.get('percent',''),
        x.grade = request.POST.get('grade',''),
        x.income = request.POST.get('income',''),
        x.business = request.POST.get('business',''),
        x.kutumb = request.POST.get('kutumb',''),
        x.student = request.POST.get('student',''),
        x.date = request.POST.get('date',''),
        x.place = request.POST.get('place',''),
        x.sign = request.FILES.get('sign',''),
        x.photo = request.FILES.get('photo',''),
        x.palak = request.POST.get('palak',''),
        x.mukam3 = request.POST.get('mukam3',''),
        x.post3 = request.POST.get('post3',''),
        x.taluka3 = request.POST.get('taluka3',''),
        x.jilha3 = request.POST.get('jilha3',''),
        x.janmjat = request.POST.get('janmjat',''),
        x.palya = request.POST.get('palya',''),
        x.std3 = request.POST.get('std3',''),
        x.saksh1 = request.POST.get('saksh1',''),
        x.saksh2 = request.POST.get('saksh2',''),
        x.palak_nav = request.POST.get('palak_nav',''),
        x.palak_sahi = request.FILES.get('palak_sahi',''),
        x.dinank = request.POST.get('dinank',''),
        x.thikan = request.POST.get('thikan',''),
        x.vidyarthi_swaksh = request.FILES.get('vidyarthi_swaksh',''),
        x.palak_swaksh = request.FILES.get('palak_swaksh','')
        x.save()

    else:
        x = anusuchit_swechha(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        father_palak = request.POST.get('father_palak',''),
        nate = request.POST.get('nate',''),
        father_edu = request.POST.get('father_edu',''),
        mother_name = request.POST.get('mother_name',''),
        mom_edu = request.POST.get('mom_edu',''),
        jat = request.POST.get('jat',''),
        potjat = request.POST.get('potjat',''),
        dharma = request.POST.get('dharma',''),
        gender = request.POST.get('gender',''),
        nationality = request.POST.get('nationality',''),
        birthdate = request.POST.get('birthdate',''),
        birth_letter = request.POST.get('birth_letter',''),
        mukam = request.POST.get('mukam',''),
        post = request.POST.get('post',''),
        taluka = request.POST.get('taluka',''),
        jilha = request.POST.get('jilha',''),
        mobile = request.POST.get('mobile',''),
        mukam2 = request.POST.get('mukam2',''),
        post2 = request.POST.get('post2',''),
        taluka2 = request.POST.get('taluka2',''),
        jilha2 = request.POST.get('jilha2',''),
        mobile2 = request.POST.get('mobile2',''),
        language = request.POST.get('language',''),
        std = request.POST.get('std',''),
        reason = request.POST.get('reason',''),
        passed = request.POST.get('passed',''),
        year = request.POST.get('year',''),
        percent = request.POST.get('percent',''),
        grade = request.POST.get('grade',''),
        income = request.POST.get('income',''),
        business = request.POST.get('business',''),
        kutumb = request.POST.get('kutumb',''),
        student = request.POST.get('student',''),
        date = request.POST.get('date',''),
        place = request.POST.get('place',''),
        sign = request.FILES.get('sign',''),
        photo = request.FILES.get('photo',''),
        palak = request.POST.get('palak',''),
        mukam3 = request.POST.get('mukam3',''),
        post3 = request.POST.get('post3',''),
        taluka3 = request.POST.get('taluka3',''),
        jilha3 = request.POST.get('jilha3',''),
        janmjat = request.POST.get('janmjat',''),
        palya = request.POST.get('palya',''),
        std3 = request.POST.get('std3',''),
        saksh1 = request.POST.get('saksh1',''),
        saksh2 = request.POST.get('saksh2',''),
        palak_nav = request.POST.get('palak_nav',''),
        palak_sahi = request.FILES.get('palak_sahi',''),
        dinank = request.POST.get('dinank',''),
        thikan = request.POST.get('thikan',''),
        vidyarthi_swaksh = request.FILES.get('vidyarthi_swaksh',''),
        palak_swaksh = request.FILES.get('palak_swaksh','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def divyang_avyangvivah(request,pk):
    print('entered in api 1')
    if divyang_avyang.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = divyang_avyang.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.arjadar_name = request.POST.get('arjadar_name'),
        x.patta = request.POST.get('patta'),
        x.dinank = request.POST.get('dinank'),
        x.jilha = request.POST.get('jilha'),
        x.vivah_dinank = request.POST.get('vivah_dinank'),
        x.var_nav = request.POST.get('var_nav'),
        x.var_apangpraman = request.POST.get('var_apangpraman'),
        x.var_shikshan = request.POST.get('var_shikshan'),
        x.var_vyavsay = request.POST.get('var_vyavsay'),
        x.var_karyalay = request.POST.get('var_karyalay'),
        x.var_address = request.POST.get('var_address'),
        x.vadhu_nav = request.POST.get('vadhu_nav'),
        x.vadhu_apangpraman = request.POST.get('vadhu_apangpraman'),
        x.vadhu_shikshan = request.POST.get('vadhu_shikshan'),
        x.vadhu_vyavsay = request.POST.get('vadhu_vyavsay'),
        x.vadhu_karyalay = request.POST.get('vadhu_karyalay'),
        x.vadhu_address = request.POST.get('vadhu_address'),
        x.vivah_date = request.POST.get('vivah_date'),
        x.vivah_place = request.POST.get('vivah_place'),
        x.vivah_type = request.POST.get('vivah_type'),
        x.var_pratham = request.POST.get('var_pratham'),
        x.vadhu_pratham = request.POST.get('vadhu_pratham'),
        x.var_vidur = request.POST.get('var_vidur'),
        x.vadhu_vidhva = request.POST.get('vadhu_vidhva'),
        x.bfor_yojna = request.POST.get('bfor_yojna'),
        x.anya_zp = request.POST.get('anya_zp'),
        x.zp_name = request.POST.get('zp_name'),
        x.zp_dinank = request.POST.get('zp_dinank'),
        x.zp_arzadinank = request.POST.get('zp_arzadinank'),
        x.satkar = request.POST.get('satkar'),
        x.where = request.POST.get('where'),
        x.when = request.POST.get('when'),
        x.var_sign = request.FILES.get('var_sign'),
        x.vadhu_sign = request.FILES.get('vadhu_sign')
        x.save()
    else:
        x = divyang_avyang(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        arjadar_name = request.POST.get('arjadar_name'),
        patta = request.POST.get('patta'),
        dinank = request.POST.get('dinank'),
        jilha = request.POST.get('jilha'),
        vivah_dinank = request.POST.get('vivah_dinank'),
        var_nav = request.POST.get('var_nav'),
        var_apangpraman = request.POST.get('var_apangpraman'),
        var_shikshan = request.POST.get('var_shikshan'),
        var_vyavsay = request.POST.get('var_vyavsay'),
        var_karyalay = request.POST.get('var_karyalay'),
        var_address = request.POST.get('var_address'),
        vadhu_nav = request.POST.get('vadhu_nav'),
        vadhu_apangpraman = request.POST.get('vadhu_apangpraman'),
        vadhu_shikshan = request.POST.get('vadhu_shikshan'),
        vadhu_vyavsay = request.POST.get('vadhu_vyavsay'),
        vadhu_karyalay = request.POST.get('vadhu_karyalay'),
        vadhu_address = request.POST.get('vadhu_address'),
        vivah_date = request.POST.get('vivah_date'),
        vivah_place = request.POST.get('vivah_place'),
        vivah_type = request.POST.get('vivah_type'),
        var_pratham = request.POST.get('var_pratham'),
        vadhu_pratham = request.POST.get('vadhu_pratham'),
        var_vidur = request.POST.get('var_vidur'),
        vadhu_vidhva = request.POST.get('vadhu_vidhva'),
        bfor_yojna = request.POST.get('bfor_yojna'),
        anya_zp = request.POST.get('anya_zp'),
        zp_name = request.POST.get('zp_name'),
        zp_dinank = request.POST.get('zp_dinank'),
        zp_arzadinank = request.POST.get('zp_arzadinank'),
        satkar = request.POST.get('satkar'),
        where = request.POST.get('where'),
        when = request.POST.get('when'),
        var_sign = request.FILES.get('var_sign'),
        vadhu_sign = request.FILES.get('vadhu_sign')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def divyang_divyanganu(request,pk):
    print('entered in api 1')
    if divyadivyang_anudan.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = divyadivyang_anudan.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.husband_name = request.POST.get('husband_name',''),
        x.wife_name = request.POST.get('wife_name',''),
        x.husband_birth = request.POST.get('husband_birth',''),
        x.wife_birth = request.POST.get('wife_birth',''),
        x.husband_age = request.POST.get('husband_age',''),
        x.wife_age = request.POST.get('wife_age',''),
        x.husband_gender = request.POST.get('husband_gender',''),
        x.wife_gender = request.POST.get('wife_gender',''),
        x.husband_caste = request.POST.get('husband_caste',''),
        x.wife_caste = request.POST.get('wife_caste',''),
        x.husband_edu = request.POST.get('husband_edu',''),
        x.wife_edu = request.POST.get('wife_edu',''),
        x.income = request.POST.get('income',''),
        x.vivah_date = request.POST.get('vivah_date',''),
        x.husdivyang_type = request.POST.get('husdivyang_type',''),
        x.hus_percent = request.POST.get('hus_percent',''),
        x.wifedivyang_type = request.POST.get('wifedivyang_type',''),
        x.wife_percent = request.POST.get('wife_percent',''),
        x.hus_certificateno = request.POST.get('hus_certificateno',''),
        x.huscertificate_date = request.POST.get('huscertificate_date',''),
        x.wife_certificateno = request.POST.get('wife_certificateno',''),
        x.wifecertificate_date = request.POST.get('wifecertificate_date',''),
        x.hus_vyavsay = request.POST.get('hus_vyavsay'),
        x.wife_vyavsay = request.POST.get('wife_vyavsay'),
        x.husadhar_no = request.POST.get('husadhar_no'),
        x.wifeadhar_no = request.POST.get('wifeadhar_no'),
        x.hus_address = request.POST.get('hus_address'),
        x.wifemaher_address = request.POST.get('wifemaher_address'),
        x.mobile_no1 = request.POST.get('mobile_no1'),
        x.mobile_no2 = request.POST.get('mobile_no2'),
        x.yojna_name = request.POST.get('yojna_name'),
        x.benefit = request.POST.get('benefit'),
        x.hus_photo = request.FILES.get('hus_photo',''),
        x.wife_photo = request.FILES.get('wife_photo',''),
        x.hus_sign = request.FILES.get('hus_sign',''),
        x.wife_sign = request.FILES.get('wife_sign','')
        x.save()
    else:
        x = divyadivyang_anudan(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        husband_name = request.POST.get('husband_name',''),
        wife_name = request.POST.get('wife_name',''),
        husband_birth = request.POST.get('husband_birth',''),
        wife_birth = request.POST.get('wife_birth',''),
        husband_age = request.POST.get('husband_age',''),
        wife_age = request.POST.get('wife_age',''),
        husband_gender = request.POST.get('husband_gender',''),
        wife_gender = request.POST.get('wife_gender',''),
        husband_caste = request.POST.get('husband_caste',''),
        wife_caste = request.POST.get('wife_caste',''),
        husband_edu = request.POST.get('husband_edu',''),
        wife_edu = request.POST.get('wife_edu',''),
        income = request.POST.get('income',''),
        vivah_date = request.POST.get('vivah_date',''),
        husdivyang_type = request.POST.get('husdivyang_type',''),
        hus_percent = request.POST.get('hus_percent',''),
        wifedivyang_type = request.POST.get('wifedivyang_type',''),
        wife_percent = request.POST.get('wife_percent',''),
        hus_certificateno = request.POST.get('hus_certificateno',''),
        huscertificate_date = request.POST.get('huscertificate_date',''),
        wife_certificateno = request.POST.get('wife_certificateno',''),
        wifecertificate_date = request.POST.get('wifecertificate_date',''),
        hus_vyavsay = request.POST.get('hus_vyavsay'),
        wife_vyavsay = request.POST.get('wife_vyavsay'),
        husadhar_no = request.POST.get('husadhar_no'),
        wifeadhar_no = request.POST.get('wifeadhar_no'),
        hus_address = request.POST.get('hus_address'),
        wifemaher_address = request.POST.get('wifemaher_address'),
        mobile_no1 = request.POST.get('mobile_no1'),
        mobile_no2 = request.POST.get('mobile_no2'),
        yojna_name = request.POST.get('yojna_name'),
        benefit = request.POST.get('benefit'),
        hus_photo = request.FILES.get('hus_photo',''),
        wife_photo = request.FILES.get('wife_photo',''),
        hus_sign = request.FILES.get('hus_sign',''),
        wife_sign = request.FILES.get('wife_sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def swayamrojgar_bijbhandwal(request,pk):
    print('entered in api 1')
    if swayamrojgar_divyang.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = swayamrojgar_divyang.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.address = request.POST.get('address',''),
        x.fa_husname = request.POST.get('fa_husname',''),
        x.patra_address = request.POST.get('patra_address',''),
        x.age = request.POST.get('age',''),
        x.birthdate = request.POST.get('birthdate',''),
        x.daridrya_yn = request.POST.get('daridrya_yn',''),
        x.daridrya_num = request.POST.get('daridrya_num',''),
        x.apang_type = request.POST.get('apang_type',''),
        x.apang_swarup = request.POST.get('apang_swarup',''),
        x.apang_certificate = request.FILES.get('apang_certificate',''),
        x.certificate_yn = request.POST.get('certificate_yn',''),
        x.vyavsay = request.POST.get('vyavsay',''),
        x.income = request.POST.get('income',''),
        x.olakh1 = request.POST.get('olakh1',''),
        x.olakh2 = request.POST.get('olakh2',''),
        x.photo_yn = request.POST.get('photo_yn',''),
        x.education = request.POST.get('education',''),
        x.shaley_edu = request.POST.get('shaley_edu',''),
        x.technical_edu = request.POST.get('technical_edu',''),
        x.other_edu = request.POST.get('other_edu',''),
        x.naukri_exp = request.POST.get('naukri_exp',''),
        x.business_exp = request.POST.get('business_exp',''),
        x.samaj_exp = request.POST.get('samaj_exp',''),
        x.ration_yn = request.POST.get('ration_yn',''),
        x.arja_vyavsay = request.POST.get('arja_vyavsay',''),
        x.vyavsay_swarup = request.POST.get('vyavsay_swarup',''),
        x.vyavsay_ghatna = request.POST.get('vyavsay_ghatna',''),
        x.malak_bhagidar = request.POST.get('malak_bhagidar',''),
        x.vyavsay_reason = request.POST.get('vyavsay_reason',''),
        x.bhandval = request.POST.get('bhandval',''),
        x.kayam_bhandval = request.POST.get('kayam_bhandval',''),
        x.khelte_bhandval = request.POST.get('khelte_bhandval',''),
        x.yojna_tartud = request.POST.get('yojna_tartud',''),
        x.guntavlele_bhandval = request.POST.get('guntavlele_bhandval',''),
        x.prakalp_yn = request.POST.get('prakalp_yn',''),
        x.samajkalyan_khate = request.POST.get('samajkalyan_khate',''),
        x.spardha = request.POST.get('spardha',''),
        x.mal_vikri = request.POST.get('mal_vikri',''),
        x.other_help = request.POST.get('other_help',''),
        x.other_arza = request.POST.get('other_arza',''),
        x.dinank = request.POST.get('dinank',''),
        x.place = request.POST.get('place',''),
        x.signature = request.FILES.get('signature',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = swayamrojgar_divyang(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        address = request.POST.get('address',''),
        fa_husname = request.POST.get('fa_husname',''),
        patra_address = request.POST.get('patra_address',''),
        age = request.POST.get('age',''),
        birthdate = request.POST.get('birthdate',''),
        daridrya_yn = request.POST.get('daridrya_yn',''),
        daridrya_num = request.POST.get('daridrya_num',''),
        apang_type = request.POST.get('apang_type',''),
        apang_swarup = request.POST.get('apang_swarup',''),
        apang_certificate = request.FILES.get('apang_certificate',''),
        certificate_yn = request.POST.get('certificate_yn',''),
        vyavsay = request.POST.get('vyavsay',''),
        income = request.POST.get('income',''),
        olakh1 = request.POST.get('olakh1',''),
        olakh2 = request.POST.get('olakh2',''),
        photo_yn = request.POST.get('photo_yn',''),
        education = request.POST.get('education',''),
        shaley_edu = request.POST.get('shaley_edu',''),
        technical_edu = request.POST.get('technical_edu',''),
        other_edu = request.POST.get('other_edu',''),
        naukri_exp = request.POST.get('naukri_exp',''),
        business_exp = request.POST.get('business_exp',''),
        samaj_exp = request.POST.get('samaj_exp',''),
        ration_yn = request.POST.get('ration_yn',''),
        arja_vyavsay = request.POST.get('arja_vyavsay',''),
        vyavsay_swarup = request.POST.get('vyavsay_swarup',''),
        vyavsay_ghatna = request.POST.get('vyavsay_ghatna',''),
        malak_bhagidar = request.POST.get('malak_bhagidar',''),
        vyavsay_reason = request.POST.get('vyavsay_reason',''),
        bhandval = request.POST.get('bhandval',''),
        kayam_bhandval = request.POST.get('kayam_bhandval',''),
        khelte_bhandval = request.POST.get('khelte_bhandval',''),
        yojna_tartud = request.POST.get('yojna_tartud',''),
        guntavlele_bhandval = request.POST.get('guntavlele_bhandval',''),
        prakalp_yn = request.POST.get('prakalp_yn',''),
        samajkalyan_khate = request.POST.get('samajkalyan_khate',''),
        spardha = request.POST.get('spardha',''),
        mal_vikri = request.POST.get('mal_vikri',''),
        other_help = request.POST.get('other_help',''),
        other_arza = request.POST.get('other_arza',''),
        dinank = request.POST.get('dinank',''),
        place = request.POST.get('place',''),
        signature = request.FILES.get('signature',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def antarjatiya_vivahjodpe(request,pk):
    print('entered in api 1')
    if antarjatiy_vivah.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = antarjatiy_vivah.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.arjadar_name = request.POST.get('arjadar_name',''),
        x.address = request.POST.get('address',''),
        x.dinank = request.POST.get('dinank',''),
        x.mob_no1 = request.POST.get('mob_no1',''),
        x.mob_no2 = request.POST.get('mob_no2',''),
        x.vivah_date = request.POST.get('vivah_date',''),
        x.var_name = request.POST.get('var_name',''),
        x.var_dharma = request.POST.get('var_dharma',''),
        x.var_caste = request.POST.get('var_caste',''),
        x.var_edu = request.POST.get('var_edu',''),
        x.var_vyavsay = request.POST.get('var_vyavsay',''),
        x.var_karyalay = request.POST.get('var_karyalay',''),
        x.var_address = request.POST.get('var_address',''),
        x.var_adharno = request.POST.get('var_adharno',''),
        x.vadhu_name = request.POST.get('vadhu_name',''),
        x.vadhu_dharma = request.POST.get('vadhu_dharma',''),
        x.vadhu_caste = request.POST.get('vadhu_caste',''),
        x.vadhu_edu = request.POST.get('vadhu_edu',''),
        x.vadhu_vyavsay = request.POST.get('vadhu_vyavsay',''),
        x.vadhu_karyalay = request.POST.get('vadhu_karyalay',''),
        x.vadhu_address = request.POST.get('vadhu_address',''),
        x.vadhu_jilha = request.POST.get('vadhu_jilha',''),
        x.vadhu_adharno = request.POST.get('vadhu_adharno',''),
        x.vivah_date1 = request.POST.get('vivah_date1',''),
        x.vivah_place = request.POST.get('vivah_place',''),
        x.vivah_type = request.POST.get('vivah_type',''),
        x.var_firstvivah = request.POST.get('var_firstvivah',''),
        x.vadhu_firstvivah = request.POST.get('vadhu_firstvivah',''),
        x.var_vidur = request.POST.get('var_vidur',''),
        x.vadhu_vidhva = request.POST.get('vadhu_vidhva',''),
        x.bfor_yojna = request.POST.get('bfor_yojna',''),
        x.anya_zp = request.POST.get('anya_zp',''),
        x.satkar = request.POST.get('satkar',''),
        x.where = request.POST.get('where',''),
        x.when = request.POST.get('when',''),
        x.bankname = request.POST.get('bankname',''),
        x.branch = request.POST.get('branch',''),
        x.account_no = request.POST.get('account_no',''),
        x.ifsc_no = request.POST.get('ifsc_no',''),
        x.var_sign = request.FILES.get('var_sign',''),
        x.vadhu_sign = request.FILES.get('vadhu_sign','')
        x.save()

    else:
        x = antarjatiy_vivah(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        arjadar_name = request.POST.get('arjadar_name',''),
        address = request.POST.get('address',''),
        dinank = request.POST.get('dinank',''),
        mob_no1 = request.POST.get('mob_no1',''),
        mob_no2 = request.POST.get('mob_no2',''),
        vivah_date = request.POST.get('vivah_date',''),
        var_name = request.POST.get('var_name',''),
        var_dharma = request.POST.get('var_dharma',''),
        var_caste = request.POST.get('var_caste',''),
        var_edu = request.POST.get('var_edu',''),
        var_vyavsay = request.POST.get('var_vyavsay',''),
        var_karyalay = request.POST.get('var_karyalay',''),
        var_address = request.POST.get('var_address',''),
        var_adharno = request.POST.get('var_adharno',''),
        vadhu_name = request.POST.get('vadhu_name',''),
        vadhu_dharma = request.POST.get('vadhu_dharma',''),
        vadhu_caste = request.POST.get('vadhu_caste',''),
        vadhu_edu = request.POST.get('vadhu_edu',''),
        vadhu_vyavsay = request.POST.get('vadhu_vyavsay',''),
        vadhu_karyalay = request.POST.get('vadhu_karyalay',''),
        vadhu_address = request.POST.get('vadhu_address',''),
        vadhu_jilha = request.POST.get('vadhu_jilha',''),
        vadhu_adharno = request.POST.get('vadhu_adharno',''),
        vivah_date1 = request.POST.get('vivah_date1',''),
        vivah_place = request.POST.get('vivah_place',''),
        vivah_type = request.POST.get('vivah_type',''),
        var_firstvivah = request.POST.get('var_firstvivah',''),
        vadhu_firstvivah = request.POST.get('vadhu_firstvivah',''),
        var_vidur = request.POST.get('var_vidur',''),
        vadhu_vidhva = request.POST.get('vadhu_vidhva',''),
        bfor_yojna = request.POST.get('bfor_yojna',''),
        anya_zp = request.POST.get('anya_zp',''),
        satkar = request.POST.get('satkar',''),
        where = request.POST.get('where',''),
        when = request.POST.get('when',''),
        bankname = request.POST.get('bankname',''),
        branch = request.POST.get('branch',''),
        account_no = request.POST.get('account_no',''),
        ifsc_no = request.POST.get('ifsc_no',''),
        var_sign = request.FILES.get('var_sign',''),
        vadhu_sign = request.FILES.get('vadhu_sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})


def anusuchitjamat_scholar(request,pk):
    print('entered in api 1')
    if anusuchit_scholar.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = anusuchit_scholar.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.email_id = request.POST.get('email_id',''),
        x.address = request.POST.get('address',''),
        x.mob_no = request.POST.get('mob_no',''),
        x.jat = request.POST.get('jat',''),
        x.potjat = request.POST.get('potjat',''),
        x.jat_cf = request.FILES.get('jat_cf',''),
        x.birthdate = request.POST.get('birthdate',''),
        x.birth_char = request.POST.get('birth_char',''),
        x.birth_cf = request.FILES.get('birth_cf',''),
        x.father_name = request.POST.get('father_name',''),
        x.father_add = request.POST.get('father_add',''),
        x.father_mob = request.POST.get('father_mob',''),
        x.father_email = request.POST.get('father_email',''),
        x.busi_job = request.POST.get('busi_job',''),
        x.office_add = request.POST.get('office_add',''),
        x.office_mob = request.POST.get('office_mob',''),
        x.office_email = request.POST.get('office_email',''),
        x.income = request.POST.get('income',''),
        x.income_cf = request.FILES.get('income_cf',''),
        x.hsc_passyear = request.POST.get('hsc_passyear',''),
        x.hsc_institute = request.POST.get('hsc_institute',''),
        x.hsc_marks = request.POST.get('hsc_marks',''),
        x.hsc_percent = request.POST.get('hsc_percent',''),
        x.ug_passyear = request.POST.get('ug_passyear',''),
        x.ug_institute = request.POST.get('ug_institute',''),
        x.ug_marks = request.POST.get('ug_marks',''),
        x.ug_percent = request.POST.get('ug_percent',''),
        x.pg_passyear = request.POST.get('pg_passyear',''),
        x.pg_institute = request.POST.get('pg_institute',''),
        x.pg_marks = request.POST.get('pg_marks',''),
        x.pg_percent = request.POST.get('pg_percent',''),
        x.name1 = request.POST.get('name1',''),
        x.age1 = request.POST.get('age1',''),
        x.nate1 = request.POST.get('nate1',''),
        x.business1 = request.POST.get('business1',''),
        x.income1 = request.POST.get('income1',''),
        x.name2 = request.POST.get('name2',''),
        x.age2 = request.POST.get('age2',''),
        x.nate2 = request.POST.get('nate2',''),
        x.business2 = request.POST.get('business2',''),
        x.income2 = request.POST.get('income2',''),
        x.name3 = request.POST.get('name3',''),
        x.age3 = request.POST.get('age3',''),
        x.nate3 = request.POST.get('nate3',''),
        x.business3 = request.POST.get('business3',''),
        x.income3 = request.POST.get('income3',''),
        x.name4 = request.POST.get('name4',''),
        x.age4 = request.POST.get('age4',''),
        x.nate4 = request.POST.get('nate4',''),
        x.business4 = request.POST.get('business4',''),
        x.income4 = request.POST.get('income4',''),
        x.name5 = request.POST.get('name5',''),
        x.age5 = request.POST.get('age5',''),
        x.nate5 = request.POST.get('nate5',''),
        x.business5 = request.POST.get('business5',''),
        x.income5 = request.POST.get('income5',''),
        x.abhyas = request.POST.get('abhyas',''),
        x.kalavadhi = request.POST.get('kalavadhi',''),
        x.intitute = request.POST.get('intitute',''),
        x.university = request.POST.get('university',''),
        x.college_add = request.POST.get('college_add',''),
        x.college_mob = request.POST.get('college_mob',''),
        x.college_email = request.POST.get('college_email',''),
        x.shikshan1 = request.POST.get('shikshan1',''),
        x.shikshan2 = request.POST.get('shikshan2',''),
        x.shikshan3 = request.POST.get('shikshan3',''),
        x.shikshan4 = request.POST.get('shikshan4',''),
        x.pariksha1 = request.POST.get('pariksha1',''),
        x.pariksha2 = request.POST.get('pariksha2',''),
        x.pariksha3 = request.POST.get('pariksha3',''),
        x.pariksha4 = request.POST.get('pariksha4',''),
        x.niwas1 = request.POST.get('niwas1',''),
        x.niwas2 = request.POST.get('niwas2',''),
        x.niwas3 = request.POST.get('niwas3',''),
        x.niwas4 = request.POST.get('niwas4',''),
        x.other1 = request.POST.get('other1',''),
        x.other2 = request.POST.get('other2',''),
        x.other3 = request.POST.get('other3',''),
        x.other4 = request.POST.get('other4',''),
        x.total1 = request.POST.get('total1',''),
        x.total2 = request.POST.get('total2',''),
        x.total3 = request.POST.get('total3',''),
        x.total4 = request.POST.get('total4',''),
        x.bank_name1 = request.POST.get('bank_name1',''),
        x.branch1 = request.POST.get('branch1',''),
        x.acc_no1 = request.POST.get('acc_no1',''),
        x.sortcode1 = request.POST.get('sortcode1',''),
        x.swiftcode1 = request.POST.get('swiftcode1',''),
        x.ibpn_no1 = request.POST.get('ibpn_no1',''),
        x.bank_name2 = request.POST.get('bank_name2',''),
        x.branch2 = request.POST.get('branch2',''),
        x.acc_no2 = request.POST.get('acc_no2',''),
        x.sortcode2 = request.POST.get('sortcode2',''),
        x.swiftcode2 = request.POST.get('swiftcode2',''),
        x.ibpn_no2 = request.POST.get('ibpn_no2',''),
        x.other_scholar = request.POST.get('other_scholar',''),
        x.dinank = request.POST.get('dinank',''),
        x.place = request.POST.get('place',''),
        x.stu_nm = request.POST.get('stu_nm',''),
        x.stu_sign = request.FILES.get('stu_sign',''),
        x.palak_nm = request.POST.get('palak_nm',''),
        x.palak_sign = request.FILES.get('palak_sign',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = anusuchit_scholar(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        email_id = request.POST.get('email_id',''),
        address = request.POST.get('address',''),
        mob_no = request.POST.get('mob_no',''),
        jat = request.POST.get('jat',''),
        potjat = request.POST.get('potjat',''),
        jat_cf = request.FILES.get('jat_cf',''),
        birthdate = request.POST.get('birthdate',''),
        birth_char = request.POST.get('birth_char',''),
        birth_cf = request.FILES.get('birth_cf',''),
        father_name = request.POST.get('father_name',''),
        father_add = request.POST.get('father_add',''),
        father_mob = request.POST.get('father_mob',''),
        father_email = request.POST.get('father_email',''),
        busi_job = request.POST.get('busi_job',''),
        office_add = request.POST.get('office_add',''),
        office_mob = request.POST.get('office_mob',''),
        office_email = request.POST.get('office_email',''),
        income = request.POST.get('income',''),
        income_cf = request.FILES.get('income_cf',''),
        hsc_passyear = request.POST.get('hsc_passyear',''),
        hsc_institute = request.POST.get('hsc_institute',''),
        hsc_marks = request.POST.get('hsc_marks',''),
        hsc_percent = request.POST.get('hsc_percent',''),
        ug_passyear = request.POST.get('ug_passyear',''),
        ug_institute = request.POST.get('ug_institute',''),
        ug_marks = request.POST.get('ug_marks',''),
        ug_percent = request.POST.get('ug_percent',''),
        pg_passyear = request.POST.get('pg_passyear',''),
        pg_institute = request.POST.get('pg_institute',''),
        pg_marks = request.POST.get('pg_marks',''),
        pg_percent = request.POST.get('pg_percent',''),
        name1 = request.POST.get('name1',''),
        age1 = request.POST.get('age1',''),
        nate1 = request.POST.get('nate1',''),
        business1 = request.POST.get('business1',''),
        income1 = request.POST.get('income1',''),
        name2 = request.POST.get('name2',''),
        age2 = request.POST.get('age2',''),
        nate2 = request.POST.get('nate2',''),
        business2 = request.POST.get('business2',''),
        income2 = request.POST.get('income2',''),
        name3 = request.POST.get('name3',''),
        age3 = request.POST.get('age3',''),
        nate3 = request.POST.get('nate3',''),
        business3 = request.POST.get('business3',''),
        income3 = request.POST.get('income3',''),
        name4 = request.POST.get('name4',''),
        age4 = request.POST.get('age4',''),
        nate4 = request.POST.get('nate4',''),
        business4 = request.POST.get('business4',''),
        income4 = request.POST.get('income4',''),
        name5 = request.POST.get('name5',''),
        age5 = request.POST.get('age5',''),
        nate5 = request.POST.get('nate5',''),
        business5 = request.POST.get('business5',''),
        income5 = request.POST.get('income5',''),
        abhyas = request.POST.get('abhyas',''),
        kalavadhi = request.POST.get('kalavadhi',''),
        intitute = request.POST.get('intitute',''),
        university = request.POST.get('university',''),
        college_add = request.POST.get('college_add',''),
        college_mob = request.POST.get('college_mob',''),
        college_email = request.POST.get('college_email',''),
        shikshan1 = request.POST.get('shikshan1',''),
        shikshan2 = request.POST.get('shikshan2',''),
        shikshan3 = request.POST.get('shikshan3',''),
        shikshan4 = request.POST.get('shikshan4',''),
        pariksha1 = request.POST.get('pariksha1',''),
        pariksha2 = request.POST.get('pariksha2',''),
        pariksha3 = request.POST.get('pariksha3',''),
        pariksha4 = request.POST.get('pariksha4',''),
        niwas1 = request.POST.get('niwas1',''),
        niwas2 = request.POST.get('niwas2',''),
        niwas3 = request.POST.get('niwas3',''),
        niwas4 = request.POST.get('niwas4',''),
        other1 = request.POST.get('other1',''),
        other2 = request.POST.get('other2',''),
        other3 = request.POST.get('other3',''),
        other4 = request.POST.get('other4',''),
        total1 = request.POST.get('total1',''),
        total2 = request.POST.get('total2',''),
        total3 = request.POST.get('total3',''),
        total4 = request.POST.get('total4',''),
        bank_name1 = request.POST.get('bank_name1',''),
        branch1 = request.POST.get('branch1',''),
        acc_no1 = request.POST.get('acc_no1',''),
        sortcode1 = request.POST.get('sortcode1',''),
        swiftcode1 = request.POST.get('swiftcode1',''),
        ibpn_no1 = request.POST.get('ibpn_no1',''),
        bank_name2 = request.POST.get('bank_name2',''),
        branch2 = request.POST.get('branch2',''),
        acc_no2 = request.POST.get('acc_no2',''),
        sortcode2 = request.POST.get('sortcode2',''),
        swiftcode2 = request.POST.get('swiftcode2',''),
        ibpn_no2 = request.POST.get('ibpn_no2',''),
        other_scholar = request.POST.get('other_scholar',''),
        dinank = request.POST.get('dinank',''),
        place = request.POST.get('place',''),
        stu_nm = request.POST.get('stu_nm',''),
        stu_sign = request.FILES.get('stu_sign',''),
        palak_nm = request.POST.get('palak_nm',''),
        palak_sign = request.FILES.get('palak_sign',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def adivasi_engraji(request,pk):
    print('entered in api 1')
    if adivasividyarthi_engraji.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = adivasividyarthi_engraji.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.std1 = request.POST.get('std1',''),
        x.std2 = request.POST.get('std2',''),
        x.name = request.POST.get('name',''),
        x.birth_date = request.POST.get('birth_date',''),
        x.birth_place = request.POST.get('birth_place',''),
        x.jamat = request.POST.get('jamat',''),
        x.nation = request.POST.get('nation',''),
        x.rahivasi_yn = request.POST.get('rahivasi_yn',''),
        x.rahivasi = request.POST.get('rahivasi',''),
        x.father_name = request.POST.get('father_name',''),
        x.current_add = request.POST.get('current_add',''),
        x.kayam_add = request.POST.get('kayam_add',''),
        x.mobile1 = request.POST.get('mobile1',''),
        x.mobile2 = request.POST.get('mobile2',''),
        x.mother_name = request.POST.get('mother_name',''),
        x.income_cf = request.FILES.get('income_cf',''),
        x.vyavsay = request.POST.get('vyavsay',''),
        x.nokardar_cf = request.FILES.get('nokardar_cf',''),
        x.daridrya_cf = request.FILES.get('daridrya_cf',''),
        x.mahilapalak_cf = request.FILES.get('mahilapalak_cf',''),
        x.sign = request.FILES.get('sign',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = adivasividyarthi_engraji(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        std1 = request.POST.get('std1',''),
        std2 = request.POST.get('std2',''),
        name = request.POST.get('name',''),
        birth_date = request.POST.get('birth_date',''),
        birth_place = request.POST.get('birth_place',''),
        jamat = request.POST.get('jamat',''),
        nation = request.POST.get('nation',''),
        rahivasi_yn = request.POST.get('rahivasi_yn',''),
        rahivasi = request.POST.get('rahivasi',''),
        father_name = request.POST.get('father_name',''),
        current_add = request.POST.get('current_add',''),
        kayam_add = request.POST.get('kayam_add',''),
        mobile1 = request.POST.get('mobile1',''),
        mobile2 = request.POST.get('mobile2',''),
        mother_name = request.POST.get('mother_name',''),
        income_cf = request.FILES.get('income_cf',''),
        vyavsay = request.POST.get('vyavsay',''),
        nokardar_cf = request.FILES.get('nokardar_cf',''),
        daridrya_cf = request.FILES.get('daridrya_cf',''),
        mahilapalak_cf = request.FILES.get('mahilapalak_cf',''),
        sign = request.FILES.get('sign',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def sainiki_shala(request,pk):
    print('entered in api 1')
    if sainikshala_adi.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = sainikshala_adi.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.shikshanik_satra = request.POST.get('shikshanik_satra'),
        x.vidyarthi_name = request.POST.get('vidyarthi_name'),
        x.vadil_name = request.POST.get('vadil_name'),
        x.father_mob = request.POST.get('father_mob'),
        x.aai_name = request.POST.get('aai_name'),
        x.aai_mobile = request.POST.get('aai_mobile'),
        x.sampurn_patta = request.POST.get('sampurn_patta'),
        x.tahsil_jilha = request.POST.get('tahsil_jilha'),
        x.jat_yn = request.POST.get('jat_yn'),
        x.jat_praman = request.FILES.get('jat_praman'),
        x.birth_num = request.POST.get('birth_num'),
        x.birth_char = request.POST.get('birth_char'),
        x.birthplace = request.POST.get('birthplace'),
        x.nationality = request.POST.get('nationality'),
        x.school_name = request.POST.get('school_name'),
        x.school_address = request.POST.get('school_address'),
        x.medium = request.POST.get('medium')
        x.save()

    else:
        x = sainikshala_adi(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        shikshanik_satra = request.POST.get('shikshanik_satra'),
        vidyarthi_name = request.POST.get('vidyarthi_name'),
        vadil_name = request.POST.get('vadil_name'),
        father_mob = request.POST.get('father_mob'),
        aai_name = request.POST.get('aai_name'),
        aai_mobile = request.POST.get('aai_mobile'),
        sampurn_patta = request.POST.get('sampurn_patta'),
        tahsil_jilha = request.POST.get('tahsil_jilha'),
        jat_yn = request.POST.get('jat_yn'),
        jat_praman = request.FILES.get('jat_praman'),
        birth_num = request.POST.get('birth_num'),
        birth_char = request.POST.get('birth_char'),
        birthplace = request.POST.get('birthplace'),
        nationality = request.POST.get('nationality'),
        school_name = request.POST.get('school_name'),
        school_address = request.POST.get('school_address'),
        medium = request.POST.get('medium')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def eklavya_publicschool(request,pk):
    print('entered in api 1')
    if eklavya_school.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = eklavya_school.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.std1 = request.POST.get('std1',''),
        x.std2 = request.POST.get('std2',''),
        x.name = request.POST.get('name',''),
        x.birth_date = request.POST.get('birth_date',''),
        x.birth_place = request.POST.get('birth_place',''),
        x.jamat = request.POST.get('jamat',''),
        x.rahivasi_yn = request.POST.get('rahivasi_yn',''),
        x.nate = request.POST.get('nate',''),
        x.father_name = request.POST.get('father_name',''),
        x.father_add = request.POST.get('father_add',''),
        x.mobile_no = request.POST.get('mobile_no',''),
        x.mother_name = request.POST.get('mother_name',''),
        x.income = request.POST.get('income',''),
        x.vyavsay = request.POST.get('vyavsay',''),
        x.school = request.POST.get('school',''),
        x.marks = request.POST.get('marks',''),
        x.std3 = request.POST.get('std3',''),
        x.paas = request.POST.get('paas',''),
        x.members = request.POST.get('members',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.branch = request.POST.get('branch',''),
        x.acc_no = request.POST.get('acc_no',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.sign = request.FILES.get('sign','')
        x.save()

    else:
        x = eklavya_school(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        std1 = request.POST.get('std1',''),
        std2 = request.POST.get('std2',''),
        name = request.POST.get('name',''),
        birth_date = request.POST.get('birth_date',''),
        birth_place = request.POST.get('birth_place',''),
        jamat = request.POST.get('jamat',''),
        rahivasi_yn = request.POST.get('rahivasi_yn',''),
        nate = request.POST.get('nate',''),
        father_name = request.POST.get('father_name',''),
        father_add = request.POST.get('father_add',''),
        mobile_no = request.POST.get('mobile_no',''),
        mother_name = request.POST.get('mother_name',''),
        income = request.POST.get('income',''),
        vyavsay = request.POST.get('vyavsay',''),
        school = request.POST.get('school',''),
        marks = request.POST.get('marks',''),
        std3 = request.POST.get('std3',''),
        paas = request.POST.get('paas',''),
        members = request.POST.get('members',''),
        bank_name = request.POST.get('bank_name',''),
        branch = request.POST.get('branch',''),
        acc_no = request.POST.get('acc_no',''),
        ifsc = request.POST.get('ifsc',''),
        adhar_no = request.POST.get('adhar_no',''),
        sign = request.FILES.get('sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def kendravarti_arthasankalp(request,pk):
    print('entered in api 1')
    if kendravarti_utpanna.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = kendravarti_utpanna.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.prakalp = request.POST.get('prakalp',''),
        x.san = request.POST.get('san',''),
        x.jilha = request.POST.get('jilha',''),
        x.yojna = request.POST.get('yojna',''),
        x.name = request.POST.get('name',''),
        x.patta = request.POST.get('patta',''),
        x.utara = request.FILES.get('utara',''),
        x.ahvaal = request.FILES.get('ahvaal',''),
        x.mobile_no = request.POST.get('mobile_no',''),
        x.married = request.POST.get('married',''),
        x.aadim = request.POST.get('aadim',''),
        x.daridrya_cf = request.FILES.get('daridrya_cf',''),
        x.income = request.POST.get('income',''),
        x.income_src = request.POST.get('income_src',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.acc_no = request.POST.get('acc_no',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.yojna_yn = request.POST.get('yojna_yn',''),
        x.yojna_nm = request.POST.get('yojna_nm',''),
        x.year = request.POST.get('year',''),
        x.jat = request.POST.get('jat',''),
        x.jat_cf = request.FILES.get('jat_cf',''),
        x.rahivasi_cf = request.FILES.get('rahivasi_cf',''),
        x.sign = request.FILES.get('sign',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = kendravarti_utpanna(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        prakalp = request.POST.get('prakalp',''),
        san = request.POST.get('san',''),
        jilha = request.POST.get('jilha',''),
        yojna = request.POST.get('yojna',''),
        name = request.POST.get('name',''),
        patta = request.POST.get('patta',''),
        utara = request.FILES.get('utara',''),
        ahvaal = request.FILES.get('ahvaal',''),
        mobile_no = request.POST.get('mobile_no',''),
        married = request.POST.get('married',''),
        aadim = request.POST.get('aadim',''),
        daridrya_cf = request.FILES.get('daridrya_cf',''),
        income = request.POST.get('income',''),
        income_src = request.POST.get('income_src',''),
        bank_name = request.POST.get('bank_name',''),
        acc_no = request.POST.get('acc_no',''),
        ifsc = request.POST.get('ifsc',''),
        adhar_no = request.POST.get('adhar_no',''),
        yojna_yn = request.POST.get('yojna_yn',''),
        yojna_nm = request.POST.get('yojna_nm',''),
        year = request.POST.get('year',''),
        jat = request.POST.get('jat',''),
        jat_cf = request.FILES.get('jat_cf',''),
        rahivasi_cf = request.FILES.get('rahivasi_cf',''),
        sign = request.FILES.get('sign',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def kendravarti_prashikshan(request,pk):
    print('entered in api 1')
    if kendra_prashikshan.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = kendra_prashikshan.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.date = request.POST.get('date',''),
        x.yojna = request.POST.get('yojna',''),
        x.name = request.POST.get('name',''),
        x.fahus_name = request.POST.get('fahus_name',''),
        x.mother_name = request.POST.get('mother_name',''),
        x.birthdate = request.POST.get('birthdate',''),
        x.jamat = request.POST.get('jamat',''),
        x.potjat = request.POST.get('potjat',''),
        x.daridrya_no = request.POST.get('daridrya_no',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.pan = request.POST.get('pan',''),
        x.edu = request.POST.get('edu',''),
        x.tech_edu= request.POST.getlist('tech_edu[]'),
        x.income_cf = request.FILES.get('income_cf',''),
        x.adhikari = request.POST.get('adhikari',''),
        x.acc_type = request.POST.get('acc_type',''),
        x.acc_no = request.POST.get('acc_no',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.branch = request.POST.get('branch',''),
        x.mobile1 = request.POST.get('mobile1',''),
        x.mobile2 = request.POST.get('mobile2',''),
        x.email_id = request.POST.get('email_id',''),
        x.gav = request.POST.get('gav',''),
        x.taluka = request.POST.get('taluka',''),
        x.dist = request.POST.get('dist',''),
        x.shetjamin = request.POST.get('shetjamin',''),
        x.suvey = request.POST.get('suvey',''),
        x.jamin = request.POST.get('jamin',''),
        x.water_src = request.POST.get('water_src',''),
        x.shetra = request.POST.get('shetra',''),
        x.home = request.POST.get('home',''),
        x.milkat_no = request.POST.get('milkat_no',''),
        x.shetra_chaumi = request.POST.get('shetra_chaumi',''),
        x.mauje1 = request.POST.get('mauje1',''),
        x.pada1 = request.POST.get('pada1',''),
        x.post1 = request.POST.get('post1',''),
        x.taluka1 = request.POST.get('taluka1',''),
        x.jilha1 = request.POST.get('jilha1',''),
        x.pincode1 = request.POST.get('pincode1',''),
        x.mauje2 = request.POST.get('mauje2',''),
        x.pada2 = request.POST.get('pada2',''),
        x.post2 = request.POST.get('post2',''),
        x.taluka2 = request.POST.get('taluka2',''),
        x.jilha2 = request.POST.get('jilha2',''),
        x.pincode2 = request.POST.get('pincode2',''),
        x.yojna1 = request.POST.get('yojna1',''),
        x.year1 = request.POST.get('year1',''),
        x.yojna2 = request.POST.get('yojna2',''),
        x.year2 = request.POST.get('year2',''),
        x.yojna3 = request.POST.get('yojna3',''),
        x.year3 = request.POST.get('year3',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = kendra_prashikshan(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        date = request.POST.get('date',''),
        yojna = request.POST.get('yojna',''),
        name = request.POST.get('name',''),
        fahus_name = request.POST.get('fahus_name',''),
        mother_name = request.POST.get('mother_name',''),
        birthdate = request.POST.get('birthdate',''),
        jamat = request.POST.get('jamat',''),
        potjat = request.POST.get('potjat',''),
        daridrya_no = request.POST.get('daridrya_no',''),
        adhar_no = request.POST.get('adhar_no',''),
        pan = request.POST.get('pan',''),
        edu = request.POST.get('edu',''),
        tech_edu= request.POST.getlist('tech_edu[]'),
        income_cf = request.FILES.get('income_cf',''),
        adhikari = request.POST.get('adhikari',''),
        acc_type = request.POST.get('acc_type',''),
        acc_no = request.POST.get('acc_no',''),
        ifsc = request.POST.get('ifsc',''),
        bank_name = request.POST.get('bank_name',''),
        branch = request.POST.get('branch',''),
        mobile1 = request.POST.get('mobile1',''),
        mobile2 = request.POST.get('mobile2',''),
        email_id = request.POST.get('email_id',''),
        gav = request.POST.get('gav',''),
        taluka = request.POST.get('taluka',''),
        dist = request.POST.get('dist',''),
        shetjamin = request.POST.get('shetjamin',''),
        suvey = request.POST.get('suvey',''),
        jamin = request.POST.get('jamin',''),
        water_src = request.POST.get('water_src',''),
        shetra = request.POST.get('shetra',''),
        home = request.POST.get('home',''),
        milkat_no = request.POST.get('milkat_no',''),
        shetra_chaumi = request.POST.get('shetra_chaumi',''),
        mauje1 = request.POST.get('mauje1',''),
        pada1 = request.POST.get('pada1',''),
        post1 = request.POST.get('post1',''),
        taluka1 = request.POST.get('taluka1',''),
        jilha1 = request.POST.get('jilha1',''),
        pincode1 = request.POST.get('pincode1',''),
        mauje2 = request.POST.get('mauje2',''),
        pada2 = request.POST.get('pada2',''),
        post2 = request.POST.get('post2',''),
        taluka2 = request.POST.get('taluka2',''),
        jilha2 = request.POST.get('jilha2',''),
        pincode2 = request.POST.get('pincode2',''),
        yojna1 = request.POST.get('yojna1',''),
        year1 = request.POST.get('year1',''),
        yojna2 = request.POST.get('yojna2',''),
        year2 = request.POST.get('year2',''),
        yojna3 = request.POST.get('yojna3',''),
        year3 = request.POST.get('year3',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def shaskiy_ashramshalasamuh(request,pk):
    print('entered in api 1')
    if shaskiy_ashramshala.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = shaskiy_ashramshala.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.gav = request.POST.get('gav',''),
        x.tal = request.POST.get('tal',''),
        x.jil = request.POST.get('jil',''),
        x.name = request.POST.get('name',''),
        x.eyatta = request.POST.get('eyatta',''),
        x.satra = request.POST.get('satra',''),
        x.dina = request.POST.get('dina',''),
        x.thik = request.POST.get('thik',''),
        x.swakshari = request.FILES.get('swakshari',''),
        x.nav = request.POST.get('nav',''),
        x.saral_no = request.POST.get('saral_no',''),
        x.purn_nav = request.POST.get('purn_nav',''),
        x.father_name = request.POST.get('father_name',''),
        x.mother_name = request.POST.get('mother_name',''),
        x.jababi_vyakti = request.POST.get('jababi_vyakti',''),
        x.mukam = request.POST.get('mukam',''),
        x.post = request.POST.get('post',''),
        x.taluka = request.POST.get('taluka',''),
        x.dist = request.POST.get('dist',''),
        x.patta = request.POST.get('patta',''),
        x.birthdate = request.POST.get('birthdate',''),
        x.birth_akshar = request.POST.get('birth_akshar',''),
        x.birthplace = request.POST.get('birthplace',''),
        x.dharm = request.POST.get('dharm',''),
        x.jat = request.POST.get('jat',''),
        x.last_std = request.POST.get('last_std',''),
        x.year = request.POST.get('year',''),
        x.takke = request.POST.get('takke',''),
        x.acc_no = request.POST.get('acc_no',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.branch = request.POST.get('branch',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.adhar_name = request.POST.get('adhar_name',''),
        x.link_yn = request.POST.get('link_yn',''),
        x.brosis_name1 = request.POST.get('brosis_name1',''),
        x.std1 = request.POST.get('std1',''),
        x.nate1 = request.POST.get('nate1',''),
        x.brosis_name2 = request.POST.get('brosis_name2',''),
        x.std2 = request.POST.get('std2',''),
        x.nate2 = request.POST.get('nate2',''),
        x.dinank = request.POST.get('dinank',''),
        x.sign = request.FILES.get('sign','')
        x.save()

    else:
        x = shaskiy_ashramshala(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        gav = request.POST.get('gav',''),
        tal = request.POST.get('tal',''),
        jil = request.POST.get('jil',''),
        name = request.POST.get('name',''),
        eyatta = request.POST.get('eyatta',''),
        satra = request.POST.get('satra',''),
        dina = request.POST.get('dina',''),
        thik = request.POST.get('thik',''),
        swakshari = request.FILES.get('swakshari',''),
        nav = request.POST.get('nav',''),
        saral_no = request.POST.get('saral_no',''),
        purn_nav = request.POST.get('purn_nav',''),
        father_name = request.POST.get('father_name',''),
        mother_name = request.POST.get('mother_name',''),
        jababi_vyakti = request.POST.get('jababi_vyakti',''),
        mukam = request.POST.get('mukam',''),
        post = request.POST.get('post',''),
        taluka = request.POST.get('taluka',''),
        dist = request.POST.get('dist',''),
        patta = request.POST.get('patta',''),
        birthdate = request.POST.get('birthdate',''),
        birth_akshar = request.POST.get('birth_akshar',''),
        birthplace = request.POST.get('birthplace',''),
        dharm = request.POST.get('dharm',''),
        jat = request.POST.get('jat',''),
        last_std = request.POST.get('last_std',''),
        year = request.POST.get('year',''),
        takke = request.POST.get('takke',''),
        acc_no = request.POST.get('acc_no',''),
        bank_name = request.POST.get('bank_name',''),
        branch = request.POST.get('branch',''),
        ifsc = request.POST.get('ifsc',''),
        adhar_no = request.POST.get('adhar_no',''),
        adhar_name = request.POST.get('adhar_name',''),
        link_yn = request.POST.get('link_yn',''),
        brosis_name1 = request.POST.get('brosis_name1',''),
        std1 = request.POST.get('std1',''),
        nate1 = request.POST.get('nate1',''),
        brosis_name2 = request.POST.get('brosis_name2',''),
        std2 = request.POST.get('std2',''),
        nate2 = request.POST.get('nate2',''),
        dinank = request.POST.get('dinank',''),
        sign = request.FILES.get('sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def shaskiypost_ashram(request,pk):
    print('entered in api 1')
    if shaskiy_postbasic.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = shaskiy_postbasic.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.patta = request.POST.get('patta',''),
        x.jat = request.POST.get('jat',''),
        x.birthdate = request.POST.get('birthdate',''),
        x.age = request.POST.get('age',''),
        x.education = request.POST.get('education',''),
        x.income = request.POST.get('income',''),
        x.labh_yn = request.POST.get('labh_yn',''),
        x.nokri_yn = request.POST.get('nokri_yn',''),
        x.nondni_no = request.POST.get('nondni_no',''),
        x.abhyaskram = request.POST.get('abhyaskram',''),
        x.thikan = request.POST.get('thikan',''),
        x.dinank = request.POST.get('dinank',''),
        x.sign = request.FILES.get('sign',''),
        x.photo = request.FILES.get('photo','')
        x.save()

    else:
        x = shaskiy_postbasic(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        patta = request.POST.get('patta',''),
        jat = request.POST.get('jat',''),
        birthdate = request.POST.get('birthdate',''),
        age = request.POST.get('age',''),
        education = request.POST.get('education',''),
        income = request.POST.get('income',''),
        labh_yn = request.POST.get('labh_yn',''),
        nokri_yn = request.POST.get('nokri_yn',''),
        nondni_no = request.POST.get('nondni_no',''),
        abhyaskram = request.POST.get('abhyaskram',''),
        thikan = request.POST.get('thikan',''),
        dinank = request.POST.get('dinank',''),
        sign = request.FILES.get('sign',''),
        photo = request.FILES.get('photo','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def kisan_creditcard(request,pk):
    print('entered in api 1')
    if kisan_credit.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = kisan_credit.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.date = request.POST.get('date',''),
        x.name = request.POST.get('name',''),
        x.father = request.POST.get('father',''),
        x.gender = request.POST.get('gender',''),
        x.caste = request.POST.get('caste',''),
        x.mobile = request.POST.get('mobile',''),
        x.uid_oreid = request.POST.get('uid_oreid',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.id_proof = request.POST.get('id_proof',''),
        x.id_no = request.POST.get('id_no',''),
        x.state = request.POST.get('state',''),
        x.dist = request.POST.get('dist',''),
        x.subdist= request.POST.get('subdist'),
        x.village = request.POST.get('village',''),
        x.address = request.POST.get('address',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.state_name = request.POST.get('state_name',''),
        x.dist_name = request.POST.get('dist_name',''),
        x.bank = request.POST.get('bank',''),
        x.branch = request.POST.get('branch','')
        x.save()

    else:
        x = kisan_credit(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        date = request.POST.get('date',''),
        name = request.POST.get('name',''),
        father = request.POST.get('father',''),
        gender = request.POST.get('gender',''),
        caste = request.POST.get('caste',''),
        mobile = request.POST.get('mobile',''),
        uid_oreid = request.POST.get('uid_oreid',''),
        adhar_no = request.POST.get('adhar_no',''),
        id_proof = request.POST.get('id_proof',''),
        id_no = request.POST.get('id_no',''),
        state = request.POST.get('state',''),
        dist = request.POST.get('dist',''),
        subdist= request.POST.get('subdist'),
        village = request.POST.get('village',''),
        address = request.POST.get('address',''),
        ifsc = request.POST.get('ifsc',''),
        state_name = request.POST.get('state_name',''),
        dist_name = request.POST.get('dist_name',''),
        bank = request.POST.get('bank',''),
        branch = request.POST.get('branch','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def shubhmangal_nondnivivah(request,pk):
    print('entered in api 1')
    if shubhmangal_nondni.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = shubhmangal_nondni.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.address = request.POST.get('address',''),
        x.mobile = request.POST.get('mobile',''),
        x.shet_mahila = request.POST.get('shet_mahila',''),
        x.dinank = request.POST.get('dinank',''),
        x.yethe = request.POST.get('yethe',''),
        x.bank = request.POST.get('bank',''),
        x.acc_no = request.POST.get('acc_no',''),
        x.branch = request.POST.get('branch',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.adharno = request.POST.get('adharno',''),
        x.vadh = request.POST.get('vadh',''),
        x.nav = request.POST.get('nav',''),
        x.swakshari = request.FILES.get('swakshari',''),
        x.var_name = request.POST.get('var_name',''),
        x.age1 = request.POST.get('age1',''),
        x.birth_date = request.POST.get('birth_date',''),
        x.education = request.POST.get('education',''),
        x.gav = request.POST.get('gav',''),
        x.taluka1 = request.POST.get('taluka1',''),
        x.jilha = request.POST.get('jilha',''),
        x.mobile_number = request.POST.get('mobile_number',''),
        x.palak_patta = request.POST.get('palak_patta',''),
        x.mobile_number1 = request.POST.get('mobile_number1',''),
        x.mobile_number2 = request.POST.get('mobile_number2',''),
        x.var_photo = request.FILES.get('var_photo',''),
        x.vadhu_name = request.POST.get('vadhu_name',''),
        x.age2 = request.POST.get('age2',''),
        x.birth_date1 = request.POST.get('birth_date1',''),
        x.education1 = request.POST.get('education1',''),
        x.gav1 = request.POST.get('gav1',''),
        x.taluka2 = request.POST.get('taluka2',''),
        x.jilha1 = request.POST.get('jilha1',''),
        x.mobile_number3 = request.POST.get('mobile_number3',''),
        x.palak_patta1 = request.POST.get('palak_patta1',''),
        x.mobile_number4 = request.POST.get('mobile_number4',''),
        x.mobile_number5 = request.POST.get('mobile_number5',''),
        x.vadhu_photo = request.FILES.get('vadhu_photo',''),
        x.sans_name = request.POST.get('sans_name',''),
        x.thikan = request.POST.get('thikan',''),
        x.tarikh = request.POST.get('tarikh',''),
        x.padhat = request.POST.get('padhat',''),
        x.var_pratham = request.POST.get('var_pratham',''),
        x.vadhu_pratham = request.POST.get('vadhu_pratham',''),
        x.var_vidur = request.POST.get('var_vidur',''),
        x.vadhu_vidhva = request.POST.get('vadhu_vidhva',''),
        x.arthsahayya = request.POST.get('arthsahayya',''),
        x.arj = request.POST.get('arj',''),
        x.var_sign = request.FILES.get('var_sign',''),
        x.vadhu_sign = request.FILES.get('vadhu_sign','')
        x.save()

    else:
        x = shubhmangal_nondni(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        address = request.POST.get('address',''),
        mobile = request.POST.get('mobile',''),
        shet_mahila = request.POST.get('shet_mahila',''),
        dinank = request.POST.get('dinank',''),
        yethe = request.POST.get('yethe',''),
        bank = request.POST.get('bank',''),
        acc_no = request.POST.get('acc_no',''),
        branch = request.POST.get('branch',''),
        ifsc = request.POST.get('ifsc',''),
        adharno = request.POST.get('adharno',''),
        vadh = request.POST.get('vadh',''),
        nav = request.POST.get('nav',''),
        swakshari = request.FILES.get('swakshari',''),var_name = request.POST.get('var_name',''),
        age1 = request.POST.get('age1',''),
        birth_date = request.POST.get('birth_date',''),
        education = request.POST.get('education',''),
        gav = request.POST.get('gav',''),
        taluka1 = request.POST.get('taluka1',''),
        jilha = request.POST.get('jilha',''),
        mobile_number = request.POST.get('mobile_number',''),
        palak_patta = request.POST.get('palak_patta',''),
        mobile_number1 = request.POST.get('mobile_number1',''),
        mobile_number2 = request.POST.get('mobile_number2',''),
        var_photo = request.FILES.get('var_photo',''),
        vadhu_name = request.POST.get('vadhu_name',''),
        age2 = request.POST.get('age2',''),
        birth_date1 = request.POST.get('birth_date1',''),
        education1 = request.POST.get('education1',''),
        gav1 = request.POST.get('gav1',''),
        taluka2 = request.POST.get('taluka2',''),
        jilha1 = request.POST.get('jilha1',''),
        mobile_number3 = request.POST.get('mobile_number3',''),
        palak_patta1 = request.POST.get('palak_patta1',''),
        mobile_number4 = request.POST.get('mobile_number4',''),
        mobile_number5 = request.POST.get('mobile_number5',''),
        vadhu_photo = request.FILES.get('vadhu_photo',''),
        sans_name = request.POST.get('sans_name',''),
        thikan = request.POST.get('thikan',''),
        tarikh = request.POST.get('tarikh',''),
        padhat = request.POST.get('padhat',''),
        var_pratham = request.POST.get('var_pratham',''),
        vadhu_pratham = request.POST.get('vadhu_pratham',''),
        var_vidur = request.POST.get('var_vidur',''),
        vadhu_vidhva = request.POST.get('vadhu_vidhva',''),
        arthsahayya = request.POST.get('arthsahayya',''),
        arj = request.POST.get('arj',''),
        var_sign = request.FILES.get('var_sign',''),
        vadhu_sign = request.FILES.get('vadhu_sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def silk_samagrayojna(request,pk):
    print('entered in api 1')
    if silk_samagra.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = silk_samagra.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.city = request.POST.get('city',''),
        x.dinank = request.POST.get('dinank',''),
        x.karyalay = request.POST.get('karyalay',''),
        x.yojna = request.POST.get('yojna',''),
        x.name = request.POST.get('name',''),
        x.gender = request.POST.get('gender',''),
        x.birthyear = request.POST.get('birthyear',''),
        x.jat = request.POST.get('jat',''),
        x.mukam = request.POST.get('mukam',''),
        x.taluka = request.POST.get('taluka',''),
        x.jilha = request.POST.get('jilha',''),
        x.mobile = request.POST.get('mobile',''),
        x.adharno = request.POST.get('adharno',''),
        x.education = request.POST.get('education',''),
        x.bank = request.POST.get('bank',''),
        x.acc_no = request.POST.get('acc_no',''),
        x.branch = request.POST.get('branch',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.land = request.POST.get('land',''),
        x.utara_no = request.POST.get('utara_no',''),
        x.shetra = request.POST.get('shetra',''),
        x.pik1 = request.POST.get('pik1',''),
        x.pik2 = request.POST.get('pik2',''),
        x.pik3 = request.POST.get('pik3',''),
        x.pik4 = request.POST.get('pik4',''),
        x.tuti = request.POST.get('tuti',''),
        x.sinchan = request.POST.get('sinchan',''),
        x.kalavadhi = request.POST.get('kalavadhi',''),
        x.vij = request.POST.get('vij',''),
        x.kitak = request.POST.get('kitak',''),
        x.majur = request.POST.get('majur',''),
        x.shetkari = request.POST.get('shetkari',''),
        x.daridrya = request.POST.get('daridrya',''),
        x.daridrya_no = request.POST.get('daridrya_no',''),
        x.ropvatika = request.POST.get('ropvatika',''),
        x.shree = request.POST.get('shree',''),
        x.padnam = request.POST.get('padnam',''),
        x.yanni = request.POST.get('yanni',''),
        x.shetkari_name = request.POST.get('shetkari_name',''),
        x.shetkari_sign = request.FILES.get('shetkari_sign','')
        x.save()

    else:
        x = silk_samagra(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        city = request.POST.get('city',''),
        dinank = request.POST.get('dinank',''),
        karyalay = request.POST.get('karyalay',''),
        yojna = request.POST.get('yojna',''),
        name = request.POST.get('name',''),
        gender = request.POST.get('gender',''),
        birthyear = request.POST.get('birthyear',''),
        jat = request.POST.get('jat',''),
        mukam = request.POST.get('mukam',''),
        taluka = request.POST.get('taluka',''),
        jilha = request.POST.get('jilha',''),
        mobile = request.POST.get('mobile',''),
        adharno = request.POST.get('adharno',''),
        education = request.POST.get('education',''),
        bank = request.POST.get('bank',''),
        acc_no = request.POST.get('acc_no',''),
        branch = request.POST.get('branch',''),
        ifsc = request.POST.get('ifsc',''),
        land = request.POST.get('land',''),
        utara_no = request.POST.get('utara_no',''),
        shetra = request.POST.get('shetra',''),
        pik1 = request.POST.get('pik1',''),
        pik2 = request.POST.get('pik2',''),
        pik3 = request.POST.get('pik3',''),
        pik4 = request.POST.get('pik4',''),
        tuti = request.POST.get('tuti',''),
        sinchan = request.POST.get('sinchan',''),
        kalavadhi = request.POST.get('kalavadhi',''),
        vij = request.POST.get('vij',''),
        kitak = request.POST.get('kitak',''),
        majur = request.POST.get('majur',''),
        shetkari = request.POST.get('shetkari',''),
        daridrya = request.POST.get('daridrya',''),
        daridrya_no = request.POST.get('daridrya_no',''),
        ropvatika = request.POST.get('ropvatika',''),
        shree = request.POST.get('shree',''),
        padnam = request.POST.get('padnam',''),
        yanni = request.POST.get('yanni',''),
        shetkari_name = request.POST.get('shetkari_name',''),
        shetkari_sign = request.FILES.get('shetkari_sign','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def rajarshi_shahumaharajscholar(request,pk):
    print('entered in api 1')
    if rajarshi_shahuscholar.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = rajarshi_shahuscholar.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.name = request.POST.get('name',''),
        x.edu_type = request.POST.get('edu_type',''),
        x.edu_branch = request.POST.get('edu_branch',''),
        x.other_edu = request.POST.get('other_edu',''),
        x.address = request.POST.get('address',''),
        x.mob_no = request.POST.get('mob_no',''),
        x.jat = request.POST.get('jat',''),
        x.birthdate_ank = request.POST.get('birthdate_ank',''),
        x.birthdate_akshar = request.POST.get('birthdate_akshar',''),
        x.age = request.POST.get('age',''),
        x.email_id = request.POST.get('email_id',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.adhar_prat = request.FILES.get('adhar_prat',''),
        x.pan_no = request.POST.get('pan_no',''),
        x.mahavasi_yn = request.POST.get('mahavasi_yn',''),

        x.ssc_abhyaskram = request.POST.get('ssc_abhyaskram',''),
        x.ssc_passyear = request.POST.get('ssc_passyear',''),
        x.ssc_institute = request.POST.get('ssc_institute',''),
        x.ssc_totalmarks = request.POST.get('ssc_totalmarks',''),
        x.ssc_obtainmarks = request.POST.get('ssc_obtainmarks',''),
        x.ssc_takke = request.POST.get('ssc_takke',''),

        x.hsc_abhyaskram = request.POST.get('hsc_abhyaskram',''),
        x.hsc_passyear = request.POST.get('hsc_passyear',''),
        x.hsc_institute = request.POST.get('hsc_institute',''),
        x.hsc_totalmarks = request.POST.get('hsc_totalmarks',''),
        x.hsc_obtainmarks = request.POST.get('hsc_obtainmarks',''),
        x.hsc_takke = request.POST.get('hsc_takke',''),

        x.padvi_abhyaskram = request.POST.get('padvi_abhyaskram',''),
        x.padvi_passyear = request.POST.get('padvi_passyear',''),
        x.padvi_institute = request.POST.get('padvi_institute',''),
        x.padvi_totalmarks = request.POST.get('padvi_totalmarks',''),
        x.padvi_obtainmarks = request.POST.get('padvi_obtainmarks',''),
        x.padvi_takke = request.POST.get('padvi_takke',''),

        x.padvika_abhyaskram = request.POST.get('padvika_abhyaskram',''),
        x.padvika_passyear = request.POST.get('padvika_passyear',''),
        x.padvika_institute = request.POST.get('padvika_institute',''),
        x.padvika_totalmarks = request.POST.get('padvika_totalmarks',''),
        x.padvika_obtainmarks = request.POST.get('padvika_obtainmarks',''),
        x.padvika_takke = request.POST.get('padvika_takke',''),

        x.gre_abhyaskram = request.POST.get('gre_abhyaskram',''),
        x.gre_passyear = request.POST.get('gre_passyear',''),
        x.gre_institute = request.POST.get('gre_institute',''),
        x.gre_totalmarks = request.POST.get('gre_totalmarks',''),
        x.gre_obtainmarks = request.POST.get('gre_obtainmarks',''),
        x.gre_takke = request.POST.get('gre_takke',''),

        x.toefl_abhyaskram = request.POST.get('toefl_abhyaskram',''),
        x.toefl_passyear = request.POST.get('toefl_passyear',''),
        x.toefl_institute = request.POST.get('toefl_institute',''),
        x.toefl_totalmarks = request.POST.get('toefl_totalmarks',''),
        x.toefl_obtainmarks = request.POST.get('toefl_obtainmarks',''),
        x.toefl_takke = request.POST.get('toefl_takke',''),

        x.vyavsay = request.POST.get('vyavsay',''),
        x.naukri = request.POST.get('naukri',''),
        x.hudda = request.POST.get('hudda',''),
        x.vn_income = request.POST.get('vn_income',''),
        x.inc_cf = request.FILES.get('inc_cf',''),
        x.noc_yn = request.POST.get('noc_yn',''),
        x.karyalay = request.POST.get('karyalay',''),
        x.office_number = request.POST.get('office_number',''),
        x.office_email = request.POST.get('office_email',''),
        x.married = request.POST.get('married',''),
        x.husband_wifename = request.POST.get('husband_wifename',''),
        x.child1 = request.POST.get('child1',''),
        x.child2 = request.POST.get('child2',''),
        x.sobat_yn = request.POST.get('sobat_yn',''),
        x.acholder_nm = request.POST.get('acholder_nm',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.branch = request.POST.get('branch',''),
        x.acc_no = request.POST.get('acc_no',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.micr = request.POST.get('micr',''),
        x.passport_no = request.POST.get('passport_no',''),
        x.issue_date = request.POST.get('issue_date',''),
        x.end_date = request.POST.get('end_date',''),
        x.offerletter_no = request.POST.get('offerletter_no',''),
        x.offerletter_date = request.POST.get('offerletter_date',''),
        x.at_vinaat = request.POST.get('at_vinaat',''),
        x.konti_at = request.POST.get('konti_at',''),
        x.abyaskram = request.POST.get('abyaskram',''),
        x.labh_yn = request.POST.get('labh_yn',''),
        x.year = request.POST.get('year',''),
        x.sanstha = request.POST.get('sanstha',''),
        x.abhyaskram_name = request.POST.get('abhyaskram_name',''),
        x.abhyaskram_validity = request.POST.get('abhyaskram_validity',''),
        x.shishyavrutti = request.POST.get('shishyavrutti',''),
        x.palak_name = request.POST.get('palak_name',''),
        x.palak_address = request.FILES.get('palak_address',''),
        x.palak_mob = request.POST.get('palak_mob',''),
        x.palak_email = request.POST.get('palak_email',''),
        x.palak_vyavsay = request.POST.get('palak_vyavsay',''),
        x.palak_naukri = request.POST.get('palak_naukri',''),
        x.palak_hudda = request.FILES.get('palak_hudda',''),
        x.palak_income = request.POST.get('palak_income',''),
        x.palakincome_cf = request.FILES.get('palakincome_cf',''),
        x.palak_officeadd = request.POST.get('palak_officeadd',''),
        x.palakoffice_mob = request.POST.get('palakoffice_mob',''),
        x.palakoffice_email = request.POST.get('palakoffice_email',''),

        x.yearly_income = request.POST.get('yearly_income',''),
        x.yearincome_yn = request.POST.get('yearincome_yn',''),
        x.yearincome_cf = request.FILES.get('yearincome_cf',''),
        x.tax = request.POST.get('tax',''),
        x.tax_yn = request.POST.get('tax_yn',''),
        x.tax_cf = request.FILES.get('tax_cf',''),
        x.vadil_yn = request.POST.get('vadil_yn',''),
        x.vadil_cf = request.FILES.get('vadil_cf',''),
        x.nyayalay = request.POST.get('nyayalay',''),
        x.nyayalay_cf = request.FILES.get('nyayalay_cf',''),

        x.sampurn_nav1 = request.POST.get('sampurn_nav1',''),
        x.age1 = request.POST.get('age1',''),
        x.vyavsay1 = request.POST.get('vyavsay1',''),
        x.income1 = request.POST.get('income1',''),
        x.scholar_yn1 = request.POST.get('scholar_yn1',''),

        x.sampurn_nav2 = request.POST.get('sampurn_nav2',''),
        x.age2 = request.POST.get('age2',''),
        x.nate2 = request.POST.get('nate2',''),
        x.vyavsay2 = request.POST.get('vyavsay2',''),
        x.income2 = request.POST.get('income2',''),
        x.scholar_yn2 = request.POST.get('scholar_yn2',''),

        x.sampurn_nav3 = request.POST.get('sampurn_nav3',''),
        x.age3 = request.POST.get('age3',''),
        x.nate3 = request.POST.get('nate3',''),
        x.vyavsay3 = request.POST.get('vyavsay3',''),
        x.income3 = request.POST.get('income3',''),
        x.scholar_yn3 = request.POST.get('scholar_yn3',''),

        x.sampurn_nav4 = request.POST.get('sampurn_nav4',''),
        x.age4 = request.POST.get('age4',''),
        x.nate4 = request.POST.get('nate4',''),
        x.vyavsay4 = request.POST.get('vyavsay4',''),
        x.income4 = request.POST.get('income4',''),
        x.scholar_yn4 = request.POST.get('scholar_yn4',''),

        x.sampurn_nav5 = request.POST.get('sampurn_nav5',''),
        x.age5 = request.POST.get('age5',''),
        x.nate5 = request.POST.get('nate5',''),
        x.vyavsay5 = request.POST.get('vyavsay5',''),
        x.income5 = request.POST.get('income5',''),
        x.scholar_yn5 = request.POST.get('scholar_yn5',''),

        x.sampurn_nav6 = request.POST.get('sampurn_nav6',''),
        x.age6 = request.POST.get('age6',''),
        x.nate6 = request.POST.get('nate6',''),
        x.vyavsay6 = request.POST.get('vyavsay6',''),
        x.income6 = request.POST.get('income6',''),
        x.scholar_yn6 = request.POST.get('scholar_yn6',''),

        x.sampurn_nav7 = request.POST.get('sampurn_nav7',''),
        x.age7 = request.POST.get('age7',''),
        x.nate7 = request.POST.get('nate7',''),
        x.vyavsay7 = request.POST.get('vyavsay7',''),
        x.income7 = request.POST.get('income7',''),
        x.scholar_yn7 = request.POST.get('scholar_yn7',''),

        x.sampurn_nav8 = request.POST.get('sampurn_nav8',''),
        x.age8 = request.POST.get('age8',''),
        x.nate8 = request.POST.get('nate8',''),
        x.vyavsay8 = request.POST.get('vyavsay8',''),
        x.income8 = request.POST.get('income8',''),
        x.scholar_yn8 = request.POST.get('scholar_yn8',''),
        
        x.sampurn_nav9 = request.POST.get('sampurn_nav9',''),
        x.age9 = request.POST.get('age9',''),
        x.nate9 = request.POST.get('nate9',''),
        x.vyavsay9 = request.POST.get('vyavsay9',''),
        x.income9 = request.POST.get('income9',''),
        x.scholar_yn9 = request.POST.get('scholar_yn9',''),

        x.sampurn_nav10 = request.POST.get('sampurn_nav10',''),
        x.age10 = request.POST.get('age10',''),
        x.nate10 = request.POST.get('nate10',''),
        x.vyavsay10 = request.POST.get('vyavsay10',''),
        x.income10 = request.POST.get('income10',''),
        x.scholar_yn10 = request.POST.get('scholar_yn10',''),

        x.kutumb_income = request.POST.get('kutumb_income',''),

        x.pravesh_varsh = request.POST.get('pravesh_varsh',''),
        x.vidyapith = request.POST.get('vidyapith',''),
        x.desh = request.POST.get('desh',''),
        x.shasan = request.POST.get('shasan',''),
        x.vidyapith_name = request.POST.get('vidyapith_name',''),
        x.qsworld_rank = request.POST.get('qsworld_rank',''),
        x.vidyarthi_abhyas = request.POST.get('vidyarthi_abhyas',''),
        x.abhyas_swarup = request.POST.get('abhyas_swarup',''),
        x.kalavadhi = request.POST.get('kalavadhi',''),
        x.pravesh_dinank = request.POST.get('pravesh_dinank',''),
        x.pardesh_patta = request.POST.get('pardesh_patta',''),
        x.pardesh_mob = request.POST.get('pardesh_mob',''),
        x.pardesh_email = request.POST.get('pardesh_email',''),
        x.shikshan1 = request.POST.get('shikshan1',''),
        x.shikshan2 = request.POST.get('shikshan2',''),
        x.shikshan3 = request.POST.get('shikshan3',''),
        x.shikshan4 = request.POST.get('shikshan4',''),
        x.pariksha1 = request.POST.get('pariksha1',''),
        x.pariksha2 = request.POST.get('pariksha2',''),
        x.pariksha3 = request.POST.get('pariksha3',''),
        x.pariksha4 = request.POST.get('pariksha4',''),
        x.nondni1 = request.POST.get('nondni1',''),
        x.nondni2 = request.POST.get('nondni2',''),
        x.nondni3 = request.POST.get('nondni3',''),
        x.nondni4 = request.POST.get('nondni4',''),
        x.jevan_rahne1 = request.POST.get('jevan_rahne1',''),
        x.jevan_rahne2 = request.POST.get('jevan_rahne2',''),
        x.jevan_rahne3 = request.POST.get('jevan_rahne3',''),
        x.jevan_rahne4 = request.POST.get('jevan_rahne4',''),
        x.vima1 = request.POST.get('vima1',''),
        x.vima2 = request.POST.get('vima2',''),
        x.vima3 = request.POST.get('vima3',''),
        x.vima4 = request.POST.get('vima4',''),
        x.other1 = request.POST.get('other1',''),
        x.other2 = request.POST.get('other2',''),
        x.other3 = request.POST.get('other3',''),
        x.other4 = request.POST.get('other4',''),
        x.total1 = request.POST.get('total1',''),
        x.total2 = request.POST.get('total2',''),
        x.total3 = request.POST.get('total3',''),
        x.total4 = request.POST.get('total4',''),
        x.other_scholar = request.POST.get('other_scholar',''),
        x.fellowship = request.POST.get('fellowship',''),
        x.gtas = request.POST.get('gtas',''),
        x.other_mandhan = request.POST.get('other_mandhan',''),
        x.campus = request.POST.get('campus',''),
        x.thikan = request.POST.get('thikan',''),
        x.palak_sign = request.FILES.get('palak_sign',''),
        x.vidyarthi_sign = request.FILES.get('vidyarthi_sign',''),
        x.dinank = request.POST.get('dinank',''),
        x.palak_nav = request.POST.get('palak_nav',''),
        x.vidyarthi_nav = request.POST.get('vidyarthi_nav','')

        x.save()

    else:
        x = rajarshi_shahuscholar(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        name = request.POST.get('name',''),
        edu_type = request.POST.get('edu_type',''),
        edu_branch = request.POST.get('edu_branch',''),
        other_edu = request.POST.get('other_edu',''),
        address = request.POST.get('address',''),
        mob_no = request.POST.get('mob_no',''),
        jat = request.POST.get('jat',''),
        birthdate_ank = request.POST.get('birthdate_ank',''),
        birthdate_akshar = request.POST.get('birthdate_akshar',''),
        age = request.POST.get('age',''),
        email_id = request.POST.get('email_id',''),
        adhar_no = request.POST.get('adhar_no',''),
        adhar_prat = request.FILES.get('adhar_prat',''),
        pan_no = request.POST.get('pan_no',''),
        mahavasi_yn = request.POST.get('mahavasi_yn',''),

        ssc_abhyaskram = request.POST.get('ssc_abhyaskram',''),
        ssc_passyear = request.POST.get('ssc_passyear',''),
        ssc_institute = request.POST.get('ssc_institute',''),
        ssc_totalmarks = request.POST.get('ssc_totalmarks',''),
        ssc_obtainmarks = request.POST.get('ssc_obtainmarks',''),
        ssc_takke = request.POST.get('ssc_takke',''),

        hsc_abhyaskram = request.POST.get('hsc_abhyaskram',''),
        hsc_passyear = request.POST.get('hsc_passyear',''),
        hsc_institute = request.POST.get('hsc_institute',''),
        hsc_totalmarks = request.POST.get('hsc_totalmarks',''),
        hsc_obtainmarks = request.POST.get('hsc_obtainmarks',''),
        hsc_takke = request.POST.get('hsc_takke',''),

        padvi_abhyaskram = request.POST.get('padvi_abhyaskram',''),
        padvi_passyear = request.POST.get('padvi_passyear',''),
        padvi_institute = request.POST.get('padvi_institute',''),
        padvi_totalmarks = request.POST.get('padvi_totalmarks',''),
        padvi_obtainmarks = request.POST.get('padvi_obtainmarks',''),
        padvi_takke = request.POST.get('padvi_takke',''),

        padvika_abhyaskram = request.POST.get('padvika_abhyaskram',''),
        padvika_passyear = request.POST.get('padvika_passyear',''),
        padvika_institute = request.POST.get('padvika_institute',''),
        padvika_totalmarks = request.POST.get('padvika_totalmarks',''),
        padvika_obtainmarks = request.POST.get('padvika_obtainmarks',''),
        padvika_takke = request.POST.get('padvika_takke',''),

        gre_abhyaskram = request.POST.get('gre_abhyaskram',''),
        gre_passyear = request.POST.get('gre_passyear',''),
        gre_institute = request.POST.get('gre_institute',''),
        gre_totalmarks = request.POST.get('gre_totalmarks',''),
        gre_obtainmarks = request.POST.get('gre_obtainmarks',''),
        gre_takke = request.POST.get('gre_takke',''),

        toefl_abhyaskram = request.POST.get('toefl_abhyaskram',''),
        toefl_passyear = request.POST.get('toefl_passyear',''),
        toefl_institute = request.POST.get('toefl_institute',''),
        toefl_totalmarks = request.POST.get('toefl_totalmarks',''),
        toefl_obtainmarks = request.POST.get('toefl_obtainmarks',''),
        toefl_takke = request.POST.get('toefl_takke',''),

        vyavsay = request.POST.get('vyavsay',''),
        naukri = request.POST.get('naukri',''),
        hudda = request.POST.get('hudda',''),
        vn_income = request.POST.get('vn_income',''),
        inc_cf = request.FILES.get('inc_cf',''),
        noc_yn = request.POST.get('noc_yn',''),
        karyalay = request.POST.get('karyalay',''),
        office_number = request.POST.get('office_number',''),
        office_email = request.POST.get('office_email',''),
        married = request.POST.get('married',''),
        husband_wifename = request.POST.get('husband_wifename',''),
        child1 = request.POST.get('child1',''),
        child2 = request.POST.get('child2',''),
        sobat_yn = request.POST.get('sobat_yn',''),
        acholder_nm = request.POST.get('acholder_nm',''),
        bank_name = request.POST.get('bank_name',''),
        branch = request.POST.get('branch',''),
        acc_no = request.POST.get('acc_no',''),
        ifsc = request.POST.get('ifsc',''),
        micr = request.POST.get('micr',''),
        passport_no = request.POST.get('passport_no',''),
        issue_date = request.POST.get('issue_date',''),
        end_date = request.POST.get('end_date',''),
        offerletter_no = request.POST.get('offerletter_no',''),
        offerletter_date = request.POST.get('offerletter_date',''),
        at_vinaat = request.POST.get('at_vinaat',''),
        konti_at = request.POST.get('konti_at',''),
        abyaskram = request.POST.get('abyaskram',''),
        labh_yn = request.POST.get('labh_yn',''),
        year = request.POST.get('year',''),
        sanstha = request.POST.get('sanstha',''),
        abhyaskram_name = request.POST.get('abhyaskram_name',''),
        abhyaskram_validity = request.POST.get('abhyaskram_validity',''),
        shishyavrutti = request.POST.get('shishyavrutti',''),
        palak_name = request.POST.get('palak_name',''),
        palak_address = request.FILES.get('palak_address',''),
        palak_mob = request.POST.get('palak_mob',''),
        palak_email = request.POST.get('palak_email',''),
        palak_vyavsay = request.POST.get('palak_vyavsay',''),
        palak_naukri = request.POST.get('palak_naukri',''),
        palak_hudda = request.FILES.get('palak_hudda',''),
        palak_income = request.POST.get('palak_income',''),
        palakincome_cf = request.FILES.get('palakincome_cf',''),
        palak_officeadd = request.POST.get('palak_officeadd',''),
        palakoffice_mob = request.POST.get('palakoffice_mob',''),
        palakoffice_email = request.POST.get('palakoffice_email',''),

        yearly_income = request.POST.get('yearly_income',''),
        yearincome_yn = request.POST.get('yearincome_yn',''),
        yearincome_cf = request.FILES.get('yearincome_cf',''),
        tax = request.POST.get('tax',''),
        tax_yn = request.POST.get('tax_yn',''),
        tax_cf = request.FILES.get('tax_cf',''),
        vadil_yn = request.POST.get('vadil_yn',''),
        vadil_cf = request.FILES.get('vadil_cf',''),
        nyayalay = request.POST.get('nyayalay',''),
        nyayalay_cf = request.FILES.get('nyayalay_cf',''),

        sampurn_nav1 = request.POST.get('sampurn_nav1',''),
        age1 = request.POST.get('age1',''),
        vyavsay1 = request.POST.get('vyavsay1',''),
        income1 = request.POST.get('income1',''),
        scholar_yn1 = request.POST.get('scholar_yn1',''),

        sampurn_nav2 = request.POST.get('sampurn_nav2',''),
        age2 = request.POST.get('age2',''),
        nate2 = request.POST.get('nate2',''),
        vyavsay2 = request.POST.get('vyavsay2',''),
        income2 = request.POST.get('income2',''),
        scholar_yn2 = request.POST.get('scholar_yn2',''),

        sampurn_nav3 = request.POST.get('sampurn_nav3',''),
        age3 = request.POST.get('age3',''),
        nate3 = request.POST.get('nate3',''),
        vyavsay3 = request.POST.get('vyavsay3',''),
        income3 = request.POST.get('income3',''),
        scholar_yn3 = request.POST.get('scholar_yn3',''),

        sampurn_nav4 = request.POST.get('sampurn_nav4',''),
        age4 = request.POST.get('age4',''),
        nate4 = request.POST.get('nate4',''),
        vyavsay4 = request.POST.get('vyavsay4',''),
        income4 = request.POST.get('income4',''),
        scholar_yn4 = request.POST.get('scholar_yn4',''),

        sampurn_nav5 = request.POST.get('sampurn_nav5',''),
        age5 = request.POST.get('age5',''),
        nate5 = request.POST.get('nate5',''),
        vyavsay5 = request.POST.get('vyavsay5',''),
        income5 = request.POST.get('income5',''),
        scholar_yn5 = request.POST.get('scholar_yn5',''),

        sampurn_nav6 = request.POST.get('sampurn_nav6',''),
        age6 = request.POST.get('age6',''),
        nate6 = request.POST.get('nate6',''),
        vyavsay6 = request.POST.get('vyavsay6',''),
        income6 = request.POST.get('income6',''),
        scholar_yn6 = request.POST.get('scholar_yn6',''),

        sampurn_nav7 = request.POST.get('sampurn_nav7',''),
        age7 = request.POST.get('age7',''),
        nate7 = request.POST.get('nate7',''),
        vyavsay7 = request.POST.get('vyavsay7',''),
        income7 = request.POST.get('income7',''),
        scholar_yn7 = request.POST.get('scholar_yn7',''),

        sampurn_nav8 = request.POST.get('sampurn_nav8',''),
        age8 = request.POST.get('age8',''),
        nate8 = request.POST.get('nate8',''),
        vyavsay8 = request.POST.get('vyavsay8',''),
        income8 = request.POST.get('income8',''),
        scholar_yn8 = request.POST.get('scholar_yn8',''),
        
        sampurn_nav9 = request.POST.get('sampurn_nav9',''),
        age9 = request.POST.get('age9',''),
        nate9 = request.POST.get('nate9',''),
        vyavsay9 = request.POST.get('vyavsay9',''),
        income9 = request.POST.get('income9',''),
        scholar_yn9 = request.POST.get('scholar_yn9',''),

        sampurn_nav10 = request.POST.get('sampurn_nav10',''),
        age10 = request.POST.get('age10',''),
        nate10 = request.POST.get('nate10',''),
        vyavsay10 = request.POST.get('vyavsay10',''),
        income10 = request.POST.get('income10',''),
        scholar_yn10 = request.POST.get('scholar_yn10',''),

        kutumb_income = request.POST.get('kutumb_income',''),
        pravesh_varsh = request.POST.get('pravesh_varsh',''),
        vidyapith = request.POST.get('vidyapith',''),
        desh = request.POST.get('desh',''),
        shasan = request.POST.get('shasan',''),
        vidyapith_name = request.POST.get('vidyapith_name',''),
        qsworld_rank = request.POST.get('qsworld_rank',''),
        vidyarthi_abhyas = request.POST.get('vidyarthi_abhyas',''),
        abhyas_swarup = request.POST.get('abhyas_swarup',''),
        kalavadhi = request.POST.get('kalavadhi',''),
        pravesh_dinank = request.POST.get('pravesh_dinank',''),
        pardesh_patta = request.POST.get('pardesh_patta',''),
        pardesh_mob = request.POST.get('pardesh_mob',''),
        pardesh_email = request.POST.get('pardesh_email',''),
        shikshan1 = request.POST.get('shikshan1',''),
        shikshan2 = request.POST.get('shikshan2',''),
        shikshan3 = request.POST.get('shikshan3',''),
        shikshan4 = request.POST.get('shikshan4',''),
        pariksha1 = request.POST.get('pariksha1',''),
        pariksha2 = request.POST.get('pariksha2',''),
        pariksha3 = request.POST.get('pariksha3',''),
        pariksha4 = request.POST.get('pariksha4',''),
        nondni1 = request.POST.get('nondni1',''),
        nondni2 = request.POST.get('nondni2',''),
        nondni3 = request.POST.get('nondni3',''),
        nondni4 = request.POST.get('nondni4',''),
        jevan_rahne1 = request.POST.get('jevan_rahne1',''),
        jevan_rahne2 = request.POST.get('jevan_rahne2',''),
        jevan_rahne3 = request.POST.get('jevan_rahne3',''),
        jevan_rahne4 = request.POST.get('jevan_rahne4',''),
        vima1 = request.POST.get('vima1',''),
        vima2 = request.POST.get('vima2',''),
        vima3 = request.POST.get('vima3',''),
        vima4 = request.POST.get('vima4',''),
        other1 = request.POST.get('other1',''),
        other2 = request.POST.get('other2',''),
        other3 = request.POST.get('other3',''),
        other4 = request.POST.get('other4',''),
        total1 = request.POST.get('total1',''),
        total2 = request.POST.get('total2',''),
        total3 = request.POST.get('total3',''),
        total4 = request.POST.get('total4',''),
        other_scholar = request.POST.get('other_scholar',''),
        fellowship = request.POST.get('fellowship',''),
        gtas = request.POST.get('gtas',''),
        other_mandhan = request.POST.get('other_mandhan',''),
        campus = request.POST.get('campus',''),
        thikan = request.POST.get('thikan',''),
        palak_sign = request.FILES.get('palak_sign',''),
        vidyarthi_sign = request.FILES.get('vidyarthi_sign',''),
        dinank = request.POST.get('dinank',''),
        palak_nav = request.POST.get('palak_nav',''),
        vidyarthi_nav = request.POST.get('vidyarthi_nav','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def mahatmagandhi_reshimvibhag(request,pk):
    print('entered in api 1')
    if mahatmagandhi_reshim.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = mahatmagandhi_reshim.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.jilha = request.POST.get('jilha',''),
        x.dinank = request.POST.get('dinank',''),
        x.jilha2 = request.POST.get('jilha2',''),
        x.yojna = request.POST.get('yojna',''),
        x.name = request.POST.get('name',''),
        x.gender = request.POST.get('gender',''),
        x.birthyear = request.POST.get('birthyear',''),
        x.jat = request.POST.get('jat',''),
        x.mukam = request.POST.get('mukam',''),
        x.taluka = request.POST.get('taluka',''),
        x.dist = request.POST.get('dist',''),
        x.mobile_no = request.POST.get('mobile_no',''),
        x.adhar_no = request.POST.get('adhar_no',''),
        x.education = request.POST.get('education',''),
        x.bank_name = request.POST.get('bank_name',''),
        x.acc_no = request.POST.get('acc_no',''),
        x.branch = request.POST.get('branch',''),
        x.ifsc = request.POST.get('ifsc',''),
        x.land_type = request.POST.get('land_type',''),
        x.gat_712 = request.POST.get('gat_712',''),
        x.ekun_shetra = request.POST.get('ekun_shetra',''),
        x.pik1 = request.POST.get('pik1',''),
        x.pik2 = request.POST.get('pik2',''),
        x.pik3 = request.POST.get('pik3',''),
        x.pik4 = request.POST.get('pik4',''),
        x.acre = request.POST.get('acre',''),
        x.sinchan_src = request.POST.get('sinchan_src',''),
        x.sinchan_time = request.POST.get('sinchan_time',''),
        x.vijjodni_yn = request.POST.get('vijjodni_yn',''),
        x.kitak_yn = request.POST.get('kitak_yn',''),
        x.majur_yn = request.POST.get('majur_yn',''),
        x.shetkari_varg = request.POST.get('shetkari_varg',''),
        x.daridrya_yn = request.POST.get('daridrya_yn',''),
        x.bpl_no = request.POST.get('bpl_no',''),
        x.ropvatika_yn = request.POST.get('ropvatika_yn',''),
        x.nam = request.POST.get('nam',''),
        x.padnam = request.POST.get('padnam',''),
        x.karyalay = request.POST.get('karyalay',''),
        x.shetkari_sign = request.FILES.get('shetkari_sign',''),
        x.shetkari_name = request.POST.get('shetkari_name','')
        x.save()

    else:
        x = mahatmagandhi_reshim(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        jilha = request.POST.get('jilha',''),
        dinank = request.POST.get('dinank',''),
        jilha2 = request.POST.get('jilha2',''),
        yojna = request.POST.get('yojna',''),
        name = request.POST.get('name',''),
        gender = request.POST.get('gender',''),
        birthyear = request.POST.get('birthyear',''),
        jat = request.POST.get('jat',''),
        mukam = request.POST.get('mukam',''),
        taluka = request.POST.get('taluka',''),
        dist = request.POST.get('dist',''),
        mobile_no = request.POST.get('mobile_no',''),
        adhar_no = request.POST.get('adhar_no',''),
        education = request.POST.get('education',''),
        bank_name = request.POST.get('bank_name',''),
        acc_no = request.POST.get('acc_no',''),
        branch = request.POST.get('branch',''),
        ifsc = request.POST.get('ifsc',''),
        land_type = request.POST.get('land_type',''),
        gat_712 = request.POST.get('gat_712',''),
        ekun_shetra = request.POST.get('ekun_shetra',''),
        pik1 = request.POST.get('pik1',''),
        pik2 = request.POST.get('pik2',''),
        pik3 = request.POST.get('pik3',''),
        pik4 = request.POST.get('pik4',''),
        acre = request.POST.get('acre',''),
        sinchan_src = request.POST.get('sinchan_src',''),
        sinchan_time = request.POST.get('sinchan_time',''),
        vijjodni_yn = request.POST.get('vijjodni_yn',''),
        kitak_yn = request.POST.get('kitak_yn',''),
        majur_yn = request.POST.get('majur_yn',''),
        shetkari_varg = request.POST.get('shetkari_varg',''),
        daridrya_yn = request.POST.get('daridrya_yn',''),
        bpl_no = request.POST.get('bpl_no',''),
        ropvatika_yn = request.POST.get('ropvatika_yn',''),
        nam = request.POST.get('nam',''),
        padnam = request.POST.get('padnam',''),
        karyalay = request.POST.get('karyalay',''),
        shetkari_sign = request.FILES.get('shetkari_sign',''),
        shetkari_name = request.POST.get('shetkari_name','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})

def ekatmik_dugdhavikas(request,pk):
    print('entered in api 1')
    if ekatmik_dugdha.objects.filter(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk)).exists():

        x = ekatmik_dugdha.objects.get(user=request.user,
            scheme=SchemeModel.objects.get(pk=pk))
        x.thikan = request.POST.get('thikan',''),
        x.date = request.POST.get('date',''),
        x.sanstha = request.POST.get('sanstha',''),
        x.niyojit = request.POST.get('niyojit',''),
        x.maryadit = request.POST.get('maryadit',''),
        x.taluka = request.POST.get('taluka',''),
        x.jilha = request.POST.get('jilha',''),
        x.dinank = request.POST.get('dinank',''),
        x.sanstha_name = request.POST.get('sanstha_name',''),
        x.sanstha_patta = request.POST.get('sanstha_patta',''),
        x.sabhasad = request.POST.get('sabhasad',''),
        x.pravart_yn = request.POST.get('pravart_yn',''),
        x.sanstha_office = request.POST.get('sanstha_office'),
        x.pravartak = request.POST.get('pravartak',''),
        x.pra_add = request.POST.get('pra_add',''),
        x.pra_mob = request.POST.get('pra_mob',''),
        x.sanstha1 = request.POST.get('sanstha1',''),
        x.city1 = request.POST.get('city1',''),
        x.sanstha2 = request.POST.get('sanstha2',''),
        x.city2 = request.POST.get('city2',''),
        x.sanstha3 = request.POST.get('sanstha3',''),
        x.city3 = request.POST.get('city3',''),
        x.navane = request.POST.get('navane',''),
        x.limited = request.POST.get('limited',''),
        x.shakha = request.POST.get('shakha',''),
        x.vishvasu = request.POST.get('vishvasu',''),
        x.niyoj = request.POST.get('niyoj',''),
        x.marya = request.POST.get('marya',''),
        x.niyoj1 = request.POST.get('niyoj1',''),
        x.marya1 = request.POST.get('marya1',''),
        x.taluka1 = request.POST.get('taluka1',''),
        x.jilha1 = request.POST.get('jilha1',''),
        x.niyojit1 = request.POST.get('niyojit1',''),
        x.maryadit1 = request.POST.get('maryadit1',''),
        x.sabha = request.POST.get('sabha',''),
        x.dinank1 = request.POST.get('dinank1'),
        x.time = request.POST.get('time',''),
        x.ghar = request.POST.get('ghar',''),
        x.sahakar = request.POST.get('sahakar',''),
        x.shree = request.POST.get('shree',''),
        x.shree1 = request.POST.get('shree1',''),
        x.shree2 = request.POST.get('shree2',''),
        x.shree3 = request.POST.get('shree3',''),
        x.shree4 = request.POST.get('shree4',''),
        x.shree5 = request.POST.get('shree5',''),
        x.suchak = request.POST.get('suchak',''),
        x.anumodak = request.POST.get('anumodak',''),
        x.sanstha_name1 = request.POST.get('sanstha_name1',''),
        x.marya3 = request.POST.get('marya3',''),
        x.shetra = request.POST.get('shetra',''),
        x.suchak2 = request.POST.get('suchak2',''),
        x.anumodak2 = request.POST.get('anumodak2',''),
        x.shree6 = request.POST.get('shree6',''),
        x.shree7 = request.POST.get('shree7',''),
        x.shree8 = request.POST.get('shree8',''),
        x.shree9 = request.POST.get('shree9',''),
        x.suchak3 = request.POST.get('suchak3',''),
        x.anumodak3 = request.POST.get('anumodak3',''),
        x.bhandwal = request.POST.get('bhandwal',''),
        x.bhag = request.POST.get('bhag',''),
        x.bhag_rupay = request.POST.get('bhag_rupay',''),
        x.pravesh_fee = request.POST.get('pravesh_fee',''),
        x.mukhya = request.POST.get('mukhya',''),
        x.suchak4 = request.POST.get('suchak4',''),
        x.anumodak4 = request.POST.get('anumodak4'),
        x.niyojit2 = request.POST.get('niyojit2',''),
        x.maryadit2 = request.POST.get('maryadit2',''),
        x.taluka2 = request.POST.get('taluka2',''),
        x.jilha2 = request.POST.get('jilha2',''),
        x.limited1 = request.POST.get('limited1',''),
        x.shakha1 = request.POST.get('shakha1',''),
        x.hyana = request.POST.get('hyana',''),
        x.suchak5 = request.POST.get('suchak5',''),
        x.anumodak5 = request.POST.get('anumodak5',''),
        x.niyojit3 = request.POST.get('niyojit3',''),
        x.maryadit3 = request.POST.get('maryadit3',''),
        x.taluka3 = request.POST.get('taluka3',''),
        x.jilha3 = request.POST.get('jilha3',''),
        x.niyo1 = request.POST.get('niyo1',''),
        x.maryad1 = request.POST.get('maryad1',''),
        x.niyo2 = request.POST.get('niyo2',''),
        x.maryad2 = request.POST.get('maryad2',''),
        x.niyo3 = request.POST.get('niyo3',''),
        x.maryad3 = request.POST.get('maryad3',''),
        x.suchak6 = request.POST.get('suchak6',''),
        x.anumodak6 = request.POST.get('anumodak6'),
        x.hyanchi = request.POST.get('hyanchi',''),
        x.hyana1 = request.POST.get('hyana1',''),
        x.suchak7 = request.POST.get('suchak7',''),
        x.anumodak7 = request.POST.get('anumodak7',''),
        x.suchak8 = request.POST.get('suchak8',''),
        x.anumodak8 = request.POST.get('anumodak8',''),
        x.niyojit9 = request.POST.get('niyojit9',''),
        x.maryadit9 = request.POST.get('maryadit9',''),
        x.suchak9 = request.POST.get('suchak9',''),
        x.anumodak9 = request.POST.get('anumodak9',''),
        x.pravart = request.POST.get('pravart',''),
        x.other = request.POST.get('other',''),
        x.suchak10 = request.POST.get('suchak10',''),
        x.anumodak10 = request.POST.get('anumodak10',''),
        x.mpra = request.POST.get('mpra',''),
        x.pra1 = request.POST.get('pra1',''),
        x.pra2 = request.POST.get('pra2',''),
        x.pra3 = request.POST.get('pra3',''),
        x.pra4 = request.POST.get('pra4',''),
        x.pra5 = request.POST.get('pra5',''),
        x.pra6 = request.POST.get('pra6',''),
        x.pra7 = request.POST.get('pra7',''),
        x.pra8 = request.POST.get('pra8',''),
        x.pra9 = request.POST.get('pra9',''),
        x.pra10 = request.POST.get('pra10',''),
        x.pra11 = request.POST.get('pra11',''),
        x.pra12 = request.POST.get('pra12',''),
        x.pra13 = request.POST.get('pra13',''),
        x.pra14 = request.POST.get('pra14',''),
        x.mukh_pra = request.POST.get('mukh_pra',''),
        x.sabhadhyak = request.POST.get('sabhadhyak',''),
        x.niyojit10 = request.POST.get('niyojit10',''),
        x.maryadit10 = request.POST.get('maryadit10',''),
        x.taluka4 = request.POST.get('taluka4',''),
        x.jilha4 = request.POST.get('jilha4',''),

        x.mpra2 = request.POST.get('mpra2'),
        x.vyakti1 = request.POST.get('vyakti1',''),
        x.age1 = request.POST.get('age1',''),
        x.nation1 = request.POST.get('nation1',''),
        x.busi1 = request.POST.get('busi1',''),
        x.patta1 = request.POST.get('patta1',''),
        x.bhag_price1 = request.POST.get('bhag_price1',''),
        x.pravesh_fee1 = request.POST.get('pravesh_fee1',''),
        x.vyavas_fee1 = request.POST.get('vyavas_fee1',''),
        x.ekun1 = request.POST.get('ekun1',''),
        x.relate1 = request.POST.get('relate1',''),
        x.sadasya1 = request.POST.get('sadasya1',''),
        x.sign1 = request.FILES.get('sign1',''),
        x.prav2 = request.POST.get('prav2',''),
        x.vyakti2 = request.POST.get('vyakti2',''),
        x.age2 = request.POST.get('age2',''),
        x.nation2 = request.POST.get('nation2',''),
        x.busi2 = request.POST.get('busi2',''),
        x.patta2 = request.POST.get('patta2',''),
        x.bhag_price2 = request.POST.get('bhag_price2',''),
        x.pravesh_fee2 = request.POST.get('pravesh_fee2',''),
        x.vyavas_fee2 = request.POST.get('vyavas_fee2',''),
        x.ekun2 = request.POST.get('ekun2',''),
        x.relate2 = request.POST.get('relate2',''),
        x.sadasya2 = request.POST.get('sadasya2',''),
        x.sign2 = request.FILES.get('sign2',''),
        x.prav3 = request.POST.get('prav3',''),
        x.vyakti3 = request.POST.get('vyakti3',''),
        x.age3 = request.POST.get('age3',''),
        x.nation3 = request.POST.get('nation3',''),
        x.busi3 = request.POST.get('busi3',''),
        x.patta3 = request.POST.get('patta3',''),
        x.bhag_price3 = request.POST.get('bhag_price3',''),
        x.pravesh_fee3 = request.POST.get('pravesh_fee3',''),
        x.vyavas_fee3 = request.POST.get('vyavas_fee3',''),
        x.ekun3 = request.POST.get('ekun3',''),
        x.relate3 = request.POST.get('relate3',''),
        x.sadasya3 = request.POST.get('sadasya3',''),
        x.sign3 = request.FILES.get('sign3',''),
        x.prav4 = request.POST.get('prav4',''),
        x.vyakti4 = request.POST.get('vyakti4',''),
        x.age4 = request.POST.get('age4',''),
        x.nation4 = request.POST.get('nation4',''),
        x.busi4 = request.POST.get('busi4',''),
        x.patta4 = request.POST.get('patta4',''),
        x.bhag_price4 = request.POST.get('bhag_price4',''),
        x.pravesh_fee4 = request.POST.get('pravesh_fee4',''),
        x.vyavas_fee4 = request.POST.get('vyavas_fee4',''),
        x.ekun4 = request.POST.get('ekun4',''),
        x.relate4 = request.POST.get('relate4',''),
        x.sadasya4 = request.POST.get('sadasya4',''),
        x.sign4 = request.FILES.get('sign4',''),
        x.prav5 = request.POST.get('prav5',''),
        x.vyakti5 = request.POST.get('vyakti5',''),
        x.age5 = request.POST.get('age5',''),
        x.nation5 = request.POST.get('nation5',''),
        x.busi5 = request.POST.get('busi5',''),
        x.patta5 = request.POST.get('patta5',''),
        x.bhag_price5 = request.POST.get('bhag_price5',''),
        x.pravesh_fee5 = request.POST.get('pravesh_fee5',''),
        x.vyavas_fee5 = request.POST.get('vyavas_fee5',''),
        x.ekun5 = request.POST.get('ekun5',''),
        x.relate5 = request.POST.get('relate5',''),
        x.sadasya5 = request.POST.get('sadasya5',''),
        x.sign5 = request.FILES.get('sign5',''),
        x.prav6 = request.POST.get('prav6',''),
        x.vyakti6 = request.POST.get('vyakti6',''),
        x.age6 = request.POST.get('age6',''),
        x.nation6 = request.POST.get('nation6',''),
        x.busi6 = request.POST.get('busi6',''),
        x.patta6 = request.POST.get('patta6',''),
        x.bhag_price6 = request.POST.get('bhag_price6',''),
        x.pravesh_fee6 = request.POST.get('pravesh_fee6',''),
        x.vyavas_fee6 = request.POST.get('vyavas_fee6',''),
        x.ekun6 = request.POST.get('ekun6',''),
        x.relate6 = request.POST.get('relate6',''),
        x.sadasya6 = request.POST.get('sadasya6',''),
        x.sign6 = request.FILES.get('sign6',''),
        x.prav7 = request.POST.get('prav7',''),
        x.vyakti7 = request.POST.get('vyakti7',''),
        x.age7 = request.POST.get('age7',''),
        x.nation7 = request.POST.get('nation7',''),
        x.busi7 = request.POST.get('busi7',''),
        x.patta7 = request.POST.get('patta7',''),
        x.bhag_price7 = request.POST.get('bhag_price7',''),
        x.pravesh_fee7 = request.POST.get('pravesh_fee7',''),
        x.vyavas_fee7 = request.POST.get('vyavas_fee7',''),
        x.ekun7 = request.POST.get('ekun7',''),
        x.relate7 = request.POST.get('relate7',''),
        x.sadasya7 = request.POST.get('sadasya7',''),
        x.sign7 = request.FILES.get('sign7',''),
        x.prav8 = request.POST.get('prav8',''),
        x.vyakti8 = request.POST.get('vyakti8',''),
        x.age8 = request.POST.get('age8',''),
        x.nation8 = request.POST.get('nation8',''),
        x.busi8 = request.POST.get('busi8',''),
        x.patta8 = request.POST.get('patta8',''),
        x.bhag_price8 = request.POST.get('bhag_price8',''),
        x.pravesh_fee8 = request.POST.get('pravesh_fee8',''),
        x.vyavas_fee8 = request.POST.get('vyavas_fee8',''),
        x.ekun8 = request.POST.get('ekun8',''),
        x.relate8 = request.POST.get('relate8',''),
        x.sadasya8 = request.POST.get('sadasya8',''),
        x.sign8 = request.FILES.get('sign8',''),
        x.prav9 = request.POST.get('prav9',''),
        x.vyakti9 = request.POST.get('vyakti9',''),
        x.age9 = request.POST.get('age9',''),
        x.nation9 = request.POST.get('nation9',''),
        x.busi9 = request.POST.get('busi9',''),
        x.patta9 = request.POST.get('patta9',''),
        x.bhag_price9 = request.POST.get('bhag_price9',''),
        x.pravesh_fee9 = request.POST.get('pravesh_fee9',''),
        x.vyavas_fee9 = request.POST.get('vyavas_fee9',''),
        x.ekun9 = request.POST.get('ekun9',''),
        x.relate9 = request.POST.get('relate9',''),
        x.sadasya9 = request.POST.get('sadasya9',''),
        x.sign9 = request.FILES.get('sign9',''),
        x.prav10 = request.POST.get('prav10',''),
        x.vyakti10 = request.POST.get('vyakti10',''),
        x.age10 = request.POST.get('age10',''),
        x.nation10 = request.POST.get('nation10',''),
        x.busi10 = request.POST.get('busi10',''),
        x.patta10 = request.POST.get('patta10',''),
        x.bhag_price10 = request.POST.get('bhag_price10',''),
        x.pravesh_fee10 = request.POST.get('pravesh_fee10',''),
        x.vyavas_fee10 = request.POST.get('vyavas_fee10',''),
        x.ekun10 = request.POST.get('ekun10',''),
        x.relate10 = request.POST.get('relate10',''),
        x.sadasya10 = request.POST.get('sadasya10',''),
        x.sign10 = request.FILES.get('sign10',''),
        x.prav11 = request.POST.get('prav11',''),
        x.vyakti11 = request.POST.get('vyakti11',''),
        x.age11 = request.POST.get('age11',''),
        x.nation11 = request.POST.get('nation11',''),
        x.busi11 = request.POST.get('busi11',''),
        x.patta11 = request.POST.get('patta11',''),
        x.bhag_price11 = request.POST.get('bhag_price11',''),
        x.pravesh_fee11 = request.POST.get('pravesh_fee11',''),
        x.vyavas_fee11 = request.POST.get('vyavas_fee11',''),
        x.ekun11 = request.POST.get('ekun11',''),
        x.relate11 = request.POST.get('relate11',''),
        x.sadasya11 = request.POST.get('sadasya11',''),
        x.sign11 = request.FILES.get('sign11',''),
        x.prav12 = request.POST.get('prav12',''),
        x.vyakti12 = request.POST.get('vyakti12',''),
        x.age12 = request.POST.get('age12',''),
        x.nation12 = request.POST.get('nation12',''),
        x.busi12 = request.POST.get('busi12',''),
        x.patta12 = request.POST.get('patta12',''),
        x.bhag_price12 = request.POST.get('bhag_price12',''),
        x.pravesh_fee12 = request.POST.get('pravesh_fee12',''),
        x.vyavas_fee12 = request.POST.get('vyavas_fee12',''),
        x.ekun12 = request.POST.get('ekun12',''),
        x.relate12 = request.POST.get('relate12',''),
        x.sadasya12 = request.POST.get('sadasya12',''),
        x.sign12 = request.FILES.get('sign12',''),
        x.prav13 = request.POST.get('prav13',''),
        x.vyakti13 = request.POST.get('vyakti13',''),
        x.age13 = request.POST.get('age13',''),
        x.nation13 = request.POST.get('nation13',''),
        x.busi13 = request.POST.get('busi13',''),
        x.patta13 = request.POST.get('patta13',''),
        x.bhag_price13 = request.POST.get('bhag_price13',''),
        x.pravesh_fee13 = request.POST.get('pravesh_fee13',''),
        x.vyavas_fee13 = request.POST.get('vyavas_fee13',''),
        x.ekun13 = request.POST.get('ekun13',''),
        x.relate13 = request.POST.get('relate13',''),
        x.sadasya13 = request.POST.get('sadasya13',''),
        x.sign13 = request.FILES.get('sign13',''),

        x.niyojit11 = request.POST.get('niyojit11',''),
        x.maryadit11 = request.POST.get('maryadit11',''),
        x.taluka5 = request.POST.get('taluka5',''),
        x.jilha5 = request.POST.get('jilha5'),
        x.niyojit12 = request.POST.get('niyojit12',''),
        x.maryadit12 = request.POST.get('maryadit12',''),
        x.aaj = request.POST.get('aaj',''),
        x.din = request.POST.get('din',''),
        x.taim = request.POST.get('taim',''),
        x.shree10 = request.POST.get('shree10',''),

        x.sabhasad1 = request.POST.get('sabhasad1',''),
        x.sabh_sign1 = request.FILES.get('sabh_sign1',''),
        x.sabhasad3 = request.POST.get('sabhasad3',''),
        x.sabh_sign3 = request.FILES.get('sabh_sign3',''),
        x.sabhasad4 = request.POST.get('sabhasad4',''),
        x.sabh_sign4 = request.FILES.get('sabh_sign4',''),
        x.sabhasad5 = request.POST.get('sabhasad5',''),
        x.sabh_sign5 = request.FILES.get('sabh_sign5',''),
        x.sabhasad6 = request.POST.get('sabhasad6',''),
        x.sabh_sign6 = request.FILES.get('sabh_sign6',''),
        x.sabhasad7 = request.POST.get('sabhasad7',''),
        x.sabh_sign7 = request.FILES.get('sabh_sign7',''),
        x.sabhasad8 = request.POST.get('sabhasad8',''),
        x.sabh_sign8 = request.FILES.get('sabh_sign8',''),
        x.sabhasad9 = request.POST.get('sabhasad9',''),
        x.sabh_sign9 = request.FILES.get('sabh_sign9',''),
        x.sabhasad10 = request.POST.get('sabhasad10',''),
        x.sabh_sign10 = request.FILES.get('sabh_sign10',''),
        x.sabhasad11 = request.POST.get('sabhasad11',''),
        x.sabh_sign11 = request.FILES.get('sabh_sign11',''),
        x.sabhasad12 = request.POST.get('sabhasad12',''),
        x.sabh_sign12 = request.FILES.get('sabh_sign12',''),
        x.sabhasad13 = request.POST.get('sabhasad13',''),
        x.sabh_sign13 = request.FILES.get('sabh_sign13',''),
        x.sabhasad14 = request.POST.get('sabhasad14',''),
        x.sabh_sign14 = request.FILES.get('sabh_sign14',''),
        x.sabhasad15 = request.POST.get('sabhasad15',''),
        x.sabh_sign15 = request.FILES.get('sabh_sign15',''),
        x.sabhasad16 = request.POST.get('sabhasad16',''),
        x.sabh_sign16 = request.FILES.get('sabh_sign16',''),
        x.sabhasad17 = request.POST.get('sabhasad17',''),
        x.sabh_sign17 = request.FILES.get('sabh_sign17',''),
        x.sabhasad18 = request.POST.get('sabhasad18',''),
        x.sabh_sign18 = request.FILES.get('sabh_sign18',''),
        x.sabhasad19 = request.POST.get('sabhasad19',''),
        x.sabh_sign19 = request.FILES.get('sabh_sign19',''),
        x.sabhasad20 = request.POST.get('sabhasad20',''),
        x.sabh_sign20 = request.FILES.get('sabh_sign20',''),
        x.sabhasad21 = request.POST.get('sabhasad21',''),
        x.sabh_sign21 = request.FILES.get('sabh_sign21',''),
        x.sabhasad22 = request.POST.get('sabhasad22',''),
        x.sabh_sign22 = request.FILES.get('sabh_sign22',''),
        x.sabhasad23 = request.POST.get('sabhasad23',''),
        x.sabh_sign23 = request.FILES.get('sabh_sign23',''),
        x.sabhasad24 = request.POST.get('sabhasad24',''),
        x.sabh_sign24 = request.FILES.get('sabh_sign24',''),
        x.sabhasad25 = request.POST.get('sabhasad25',''),
        x.sabh_sign25 = request.FILES.get('sabh_sign25',''),
        x.sabhasad26 = request.POST.get('sabhasad26',''),
        x.sabh_sign26 = request.FILES.get('sabh_sign26',''),
        x.sabhasad27 = request.POST.get('sabhasad27',''),
        x.sabh_sign27 = request.FILES.get('sabh_sign27',''),
        x.sabhasad28 = request.POST.get('sabhasad28',''),
        x.sabh_sign28 = request.FILES.get('sabh_sign28',''),
        x.sabhasad29 = request.POST.get('sabhasad29',''),
        x.sabh_sign29 = request.FILES.get('sabh_sign29',''),
        x.sabhasad30 = request.POST.get('sabhasad30',''),
        x.sabh_sign30 = request.FILES.get('sabh_sign30',''),
        x.sabhasad31 = request.POST.get('sabhasad31',''),
        x.sabh_sign31 = request.FILES.get('sabh_sign31',''),
        x.sabhasad32 = request.POST.get('sabhasad32',''),
        x.sabh_sign32 = request.FILES.get('sabh_sign32',''),
        x.sabhasad33 = request.POST.get('sabhasad33',''),
        x.sabh_sign33 = request.FILES.get('sabh_sign33',''),
        x.sabhasad34 = request.POST.get('sabhasad34',''),
        x.sabh_sign34 = request.FILES.get('sabh_sign34',''),
        x.sabhasad35 = request.POST.get('sabhasad35',''),
        x.sabh_sign35 = request.FILES.get('sabh_sign35',''),

        x.niyojit13 = request.POST.get('niyojit13',''),
        x.maryadit13 = request.POST.get('maryadit13',''),
        x.taluka6 = request.POST.get('taluka6',''),
        x.jilha6 = request.POST.get('jilha6',''),
        x.share1 = request.POST.get('share1',''),
        x.share2 = request.POST.get('share2',''),
        x.share3 = request.POST.get('share3',''),
        x.fee1 = request.POST.get('fee1',''),
        x.fee2 = request.POST.get('fee2',''),
        x.fee3 = request.POST.get('fee3',''),
        x.thev1 = request.POST.get('thev1',''),
        x.thev2 = request.POST.get('thev2',''),
        x.thev3 = request.POST.get('thev3',''),
        x.loan1 = request.POST.get('loan1',''),
        x.loan2 = request.POST.get('loan2',''),
        x.loan3 = request.POST.get('loan3',''),
        x.interest1 = request.POST.get('interest1',''),
        x.interest2 = request.POST.get('interest2',''),
        x.interest3 = request.POST.get('interest3',''),
        x.tot1 = request.POST.get('tot1',''),
        x.tot2 = request.POST.get('tot2',''),
        x.tot3 = request.POST.get('tot3',''),
        x.nokar1 = request.POST.get('nokar1',''),
        x.nokar2 = request.POST.get('nokar2',''),
        x.nokar3 = request.POST.get('nokar3',''),
        x.sadilvar1 = request.POST.get('sadilvar1',''),
        x.sadilvar2 = request.POST.get('sadilvar2',''),
        x.sadilvar3 = request.POST.get('sadilvar3',''),
        x.kirkol1 = request.POST.get('kirkol1',''),
        x.kirkol2 = request.POST.get('kirkol2',''),
        x.kirkol3 = request.POST.get('kirkol3',''),
        x.rent1 = request.POST.get('rent1',''),
        x.rent2 = request.POST.get('rent2',''),
        x.rent3 = request.POST.get('rent3',''),
        x.bank1 = request.POST.get('bank1',''),
        x.bank2 = request.POST.get('bank2',''),
        x.bank3 = request.POST.get('bank3',''),
        x.vyaj1 = request.POST.get('vyaj1',''),
        x.vyaj2 = request.POST.get('vyaj2',''),
        x.vyaj3 = request.POST.get('vyaj3',''),
        x.b_share1 = request.POST.get('b_share1',''),
        x.b_share2 = request.POST.get('b_share2',''),
        x.b_share3 = request.POST.get('b_share3',''),
        x.member1 = request.POST.get('member1',''),
        x.member2 = request.POST.get('member2',''),
        x.member3 = request.POST.get('member3',''),
        x.niwwal1 = request.POST.get('niwwal1',''),
        x.niwwal2 = request.POST.get('niwwal2',''),
        x.niwwal3 = request.POST.get('niwwal3',''),
        x.tota1 = request.POST.get('tota1',''),
        x.tota2 = request.POST.get('tota2',''),
        x.tota3 = request.POST.get('tota3',''),
        x.chairman = request.POST.get('chairman',''),
        x.saha = request.POST.get('saha',''),
        x.maryadit14 = request.POST.get('maryadit14',''),
        x.taluka7 = request.POST.get('taluka7',''),
        x.jilha7 = request.POST.get('jilha7',''),
        x.karnar = request.POST.get('karnar',''),
        x.rahnar = request.POST.get('rahnar',''),
        x.taluka8 = request.POST.get('taluka8',''),
        x.jilha8 = request.POST.get('jilha8',''),
        x.purn_nav = request.POST.get('purn_nav',''),
        x.purn_patta = request.POST.get('purn_patta',''),
        x.dhanda = request.POST.get('dhanda',''),
        x.vay = request.POST.get('vay',''),
        x.varg = request.POST.get('varg',''),
        x.nationality = request.POST.get('nationality',''),
        x.pra_rakkam = request.POST.get('pra_rakkam',''),
        x.bhag_rakkam = request.POST.get('bhag_rakkam',''),
        x.esam = request.POST.get('esam',''),
        x.varas_nameadd = request.POST.get('varas_nameadd',''),
        x.tapshil = request.POST.get('tapshil',''),
        x.ichito = request.POST.get('ichito',''),
        x.thak_tapshil = request.POST.get('thak_tapshil',''),
        x.other_info = request.POST.get('other_info',''),
        x.dinan = request.POST.get('dinan',''),
        x.saksh_sign = request.FILES.get('saksh_sign',''),
        x.arza_sign = request.FILES.get('arza_sign',''),
        x.tarikh = request.POST.get('tarikh',''),
        x.tharav_no = request.POST.get('tharav_no',''),
        x.manjur = request.POST.get('manjur',''),
        x.saha1 = request.POST.get('saha1',''),
        x.sarkari = request.POST.get('sarkari',''),
        x.maryadit15 = request.POST.get('maryadit15',''),
        x.thikan1 = request.POST.get('thikan1',''),
        x.dinank2 = request.POST.get('dinank2',''),
        x.saha_sanstha = request.POST.get('saha_sanstha',''),
        x.niyojit_sanstha = request.POST.get('niyojit_sanstha',''),
        x.nond_add = request.POST.get('nond_add',''),
        x.marya_yn = request.POST.get('marya_yn',''),
        x.karyashetra = request.POST.get('karyashetra',''),
        x.uddishtha = request.POST.get('uddishtha',''),
        x.bhasha = request.POST.get('bhasha',''),
        x.andaz = request.POST.get('andaz',''),
        x.mp_name = request.POST.get('mp_name',''),
        x.mp_add = request.POST.get('mp_add',''),
        x.hishob_lang = request.POST.get('hishob_lang',''),

        x.name1 = request.POST.get('name1',''),
        x.sansthapi1 = request.POST.get('sansthapi1',''),
        x.vay1 = request.POST.get('vay1',''),
        x.rashtra1 = request.POST.get('rashtra1',''),
        x.business1 = request.POST.get('business1',''),
        x.addres1 = request.POST.get('addres1',''),
        x.ansha_rakkam1 = request.POST.get('ansha_rakkam1',''),
        x.relative1 = request.POST.get('relative1',''),
        x.sam_sad1 = request.POST.get('sam_sad1',''),
        x.sahi1 = request.FILES.get('sahi1',''),

        x.name2 = request.POST.get('name2',''),
        x.sansthapi2 = request.POST.get('sansthapi2',''),
        x.vay2 = request.POST.get('vay2',''),
        x.rashtra2 = request.POST.get('rashtra2',''),
        x.business2 = request.POST.get('business2',''),
        x.addres2 = request.POST.get('addres2',''),
        x.ansha_rakkam2 = request.POST.get('ansha_rakkam2',''),
        x.relative2 = request.POST.get('relative2',''),
        x.sam_sad2 = request.POST.get('sam_sad2',''),
        x.sahi2 = request.FILES.get('sahi2',''),

        x.name3 = request.POST.get('name3',''),
        x.sansthapi3 = request.POST.get('sansthapi3',''),
        x.vay3 = request.POST.get('vay3',''),
        x.rashtra3 = request.POST.get('rashtra3',''),
        x.business3 = request.POST.get('business3',''),
        x.addres3 = request.POST.get('addres3',''),
        x.ansha_rakkam3 = request.POST.get('ansha_rakkam3',''),
        x.relative3 = request.POST.get('relative3',''),
        x.sam_sad3 = request.POST.get('sam_sad3',''),
        x.sahi3 = request.FILES.get('sahi3',''),

        x.name4 = request.POST.get('name4',''),
        x.sansthapi4 = request.POST.get('sansthapi4',''),
        x.vay4 = request.POST.get('vay4',''),
        x.rashtra4 = request.POST.get('rashtra4',''),
        x.business4 = request.POST.get('business4',''),
        x.addres4 = request.POST.get('addres4',''),
        x.ansha_rakkam4 = request.POST.get('ansha_rakkam4',''),
        x.relative4 = request.POST.get('relative4',''),
        x.sam_sad4 = request.POST.get('sam_sad4',''),
        x.sahi4 = request.FILES.get('sahi4',''),

        x.name5 = request.POST.get('name5',''),
        x.sansthapi5 = request.POST.get('sansthapi5',''),
        x.vay5 = request.POST.get('vay5',''),
        x.rashtra5 = request.POST.get('rashtra5',''),
        x.business5 = request.POST.get('business5',''),
        x.addres5 = request.POST.get('addres5',''),
        x.ansha_rakkam5 = request.POST.get('ansha_rakkam5',''),
        x.relative5 = request.POST.get('relative5',''),
        x.sam_sad5 = request.POST.get('sam_sad5',''),
        x.sahi5 = request.FILES.get('sahi5',''),

        x.name6 = request.POST.get('name6',''),
        x.sansthapi6 = request.POST.get('sansthapi6',''),
        x.vay6 = request.POST.get('vay6',''),
        x.rashtra6 = request.POST.get('rashtra6',''),
        x.business6 = request.POST.get('business6',''),
        x.addres6 = request.POST.get('addres6',''),
        x.ansha_rakkam6 = request.POST.get('ansha_rakkam6',''),
        x.relative6 = request.POST.get('relative6',''),
        x.sam_sad6 = request.POST.get('sam_sad6',''),
        x.sahi6 = request.FILES.get('sahi6',''),

        x.name7 = request.POST.get('name7',''),
        x.sansthapi7 = request.POST.get('sansthapi7',''),
        x.vay7 = request.POST.get('vay7',''),
        x.rashtra7 = request.POST.get('rashtra7',''),
        x.business7 = request.POST.get('business7',''),
        x.addres7 = request.POST.get('addres7',''),
        x.ansha_rakkam7 = request.POST.get('ansha_rakkam7',''),
        x.relative7 = request.POST.get('relative7',''),
        x.sam_sad7 = request.POST.get('sam_sad7',''),
        x.sahi7 = request.FILES.get('sahi7',''),

        x.name8 = request.POST.get('name8',''),
        x.sansthapi8 = request.POST.get('sansthapi8',''),
        x.vay8 = request.POST.get('vay8',''),
        x.rashtra8 = request.POST.get('rashtra8',''),
        x.business8 = request.POST.get('business8',''),
        x.addres8 = request.POST.get('addres8',''),
        x.ansha_rakkam8 = request.POST.get('ansha_rakkam8',''),
        x.relative8 = request.POST.get('relative8',''),
        x.sam_sad8 = request.POST.get('sam_sad8',''),
        x.sahi8 = request.FILES.get('sahi8',''),

        x.name9 = request.POST.get('name9',''),
        x.sansthapi9 = request.POST.get('sansthapi9',''),
        x.vay9 = request.POST.get('vay9',''),
        x.rashtra9 = request.POST.get('rashtra9',''),
        x.business9 = request.POST.get('business9',''),
        x.addres9 = request.POST.get('addres9',''),
        x.ansha_rakkam9 = request.POST.get('ansha_rakkam9',''),
        x.relative9 = request.POST.get('relative9',''),
        x.sam_sad9 = request.POST.get('sam_sad9',''),
        x.sahi9 = request.FILES.get('sahi9',''),

        x.name10 = request.POST.get('name10',''),
        x.sansthapi10 = request.POST.get('sansthapi10',''),
        x.vay10 = request.POST.get('vay10',''),
        x.rashtra10 = request.POST.get('rashtra10',''),
        x.business10 = request.POST.get('business10',''),
        x.addres10 = request.POST.get('addres10',''),
        x.ansha_rakkam10 = request.POST.get('ansha_rakkam10',''),
        x.relative10 = request.POST.get('relative10',''),
        x.sam_sad10 = request.POST.get('sam_sad10',''),
        x.sahi10 = request.FILES.get('sahi10',''),

        x.name11 = request.POST.get('name11',''),
        x.sansthapi11 = request.POST.get('sansthapi11',''),
        x.vay11 = request.POST.get('vay11',''),
        x.rashtra11 = request.POST.get('rashtra11',''),
        x.business11 = request.POST.get('business11',''),
        x.addres11 = request.POST.get('addres11',''),
        x.ansha_rakkam11 = request.POST.get('ansha_rakkam11',''),
        x.relative11 = request.POST.get('relative11',''),
        x.sam_sad11 = request.POST.get('sam_sad11',''),
        x.sahi11 = request.FILES.get('sahi11',''),

        x.name12 = request.POST.get('name12',''),
        x.sansthapi12 = request.POST.get('sansthapi12',''),
        x.vay12 = request.POST.get('vay12',''),
        x.rashtra12 = request.POST.get('rashtra12',''),
        x.business12 = request.POST.get('business12',''),
        x.addres12 = request.POST.get('addres12',''),
        x.ansha_rakkam12 = request.POST.get('ansha_rakkam12',''),
        x.relative12 = request.POST.get('relative12',''),
        x.sam_sad12 = request.POST.get('sam_sad12',''),
        x.sahi12 = request.FILES.get('sahi12',''),

        x.name13 = request.POST.get('name13',''),
        x.sansthapi13 = request.POST.get('sansthapi13',''),
        x.vay13 = request.POST.get('vay13',''),
        x.rashtra13 = request.POST.get('rashtra13',''),
        x.business13 = request.POST.get('business13',''),
        x.addres13 = request.POST.get('addres13',''),
        x.ansha_rakkam13 = request.POST.get('ansha_rakkam13',''),
        x.relative13 = request.POST.get('relative13',''),
        x.sam_sad13 = request.POST.get('sam_sad13',''),
        x.sahi13 = request.FILES.get('sahi13',''),

        x.name14 = request.POST.get('name14',''),
        x.sansthapi14 = request.POST.get('sansthapi14',''),
        x.vay14 = request.POST.get('vay14',''),
        x.rashtra14 = request.POST.get('rashtra14',''),
        x.business14 = request.POST.get('business14',''),
        x.addres14 = request.POST.get('addres14',''),
        x.ansha_rakkam14 = request.POST.get('ansha_rakkam14',''),
        x.relative14 = request.POST.get('relative14',''),
        x.sam_sad14 = request.POST.get('sam_sad14',''),
        x.sahi14 = request.FILES.get('sahi14',''),

        x.name15 = request.POST.get('name15',''),
        x.sansthapi15 = request.POST.get('sansthapi15',''),
        x.vay15 = request.POST.get('vay15',''),
        x.rashtra15 = request.POST.get('rashtra15',''),
        x.business15 = request.POST.get('business15',''),
        x.addres15 = request.POST.get('addres15',''),
        x.ansha_rakkam15 = request.POST.get('ansha_rakkam15',''),
        x.relative15 = request.POST.get('relative15',''),
        x.sam_sad15 = request.POST.get('sam_sad15',''),
        x.sahi15 = request.FILES.get('sahi15',''),

        x.patra_name = request.POST.get('patra_name',''),
        x.patra_add = request.POST.get('patra_add',''),

        x.sahya1 = request.FILES.get('sahya1',''),
        x.sahya2 = request.FILES.get('sahya2',''),
        x.sahya3 = request.FILES.get('sahya3',''),
        x.sahya4 = request.FILES.get('sahya4',''),
        x.sahya5 = request.FILES.get('sahya5',''),
        x.sahya6 = request.FILES.get('sahya6',''),
        x.sahya7 = request.FILES.get('sahya7',''),
        x.sahya8 = request.FILES.get('sahya8',''),
        x.sahya9 = request.FILES.get('sahya9',''),
        x.sahya10 = request.FILES.get('sahya10',''),
        x.sahya11 = request.FILES.get('sahya11',''),
        x.sahya12 = request.FILES.get('sahya12',''),
        x.sahya13 = request.FILES.get('sahya13',''),
        x.sahya14 = request.FILES.get('sahya14',''),
        x.sahya15 = request.FILES.get('sahya15',''),

        x.mukhya_pra = request.POST.get('mukhya_pra',''),
        x.niyojit14 = request.POST.get('niyojit14',''),
        x.roji = request.POST.get('roji',''),
        x.pratyaksh = request.POST.get('pratyaksh',''),
        x.nibandhak = request.POST.get('nibandhak',''),
        x.yana = request.POST.get('yana',''),
        x.roji1 = request.POST.get('roji1',''),
        x.anukra = request.POST.get('anukra',''),
        x.swikar_sahi = request.FILES.get('swikar_sahi','')
        x.save()

    else:
        x = ekatmik_dugdha(
            user=request.user,
            scheme=SchemeModel.objects.get(pk=pk),
        thikan = request.POST.get('thikan',''),
        date = request.POST.get('date',''),
        sanstha = request.POST.get('sanstha',''),
        niyojit = request.POST.get('niyojit',''),
        maryadit = request.POST.get('maryadit',''),
        taluka = request.POST.get('taluka',''),
        jilha = request.POST.get('jilha',''),
        dinank = request.POST.get('dinank',''),
        sanstha_name = request.POST.get('sanstha_name',''),
        sanstha_patta = request.POST.get('sanstha_patta',''),
        sabhasad = request.POST.get('sabhasad',''),
        pravart_yn = request.POST.get('pravart_yn',''),
        sanstha_office = request.POST.get('sanstha_office'),
        pravartak = request.POST.get('pravartak',''),
        pra_add = request.POST.get('pra_add',''),
        pra_mob = request.POST.get('pra_mob',''),
        sanstha1 = request.POST.get('sanstha1',''),
        city1 = request.POST.get('city1',''),
        sanstha2 = request.POST.get('sanstha2',''),
        city2 = request.POST.get('city2',''),
        sanstha3 = request.POST.get('sanstha3',''),
        city3 = request.POST.get('city3',''),
        navane = request.POST.get('navane',''),
        limited = request.POST.get('limited',''),
        shakha = request.POST.get('shakha',''),
        vishvasu = request.POST.get('vishvasu',''),
        niyoj = request.POST.get('niyoj',''),
        marya = request.POST.get('marya',''),
        niyoj1 = request.POST.get('niyoj1',''),
        marya1 = request.POST.get('marya1',''),
        taluka1 = request.POST.get('taluka1',''),
        jilha1 = request.POST.get('jilha1',''),
        niyojit1 = request.POST.get('niyojit1',''),
        maryadit1 = request.POST.get('maryadit1',''),
        sabha = request.POST.get('sabha',''),
        dinank1 = request.POST.get('dinank1'),
        time = request.POST.get('time',''),
        ghar = request.POST.get('ghar',''),
        sahakar = request.POST.get('sahakar',''),
        shree = request.POST.get('shree',''),
        shree1 = request.POST.get('shree1',''),
        shree2 = request.POST.get('shree2',''),
        shree3 = request.POST.get('shree3',''),
        shree4 = request.POST.get('shree4',''),
        shree5 = request.POST.get('shree5',''),
        suchak = request.POST.get('suchak',''),
        anumodak = request.POST.get('anumodak',''),
        sanstha_name1 = request.POST.get('sanstha_name1',''),
        marya3 = request.POST.get('marya3',''),
        shetra = request.POST.get('shetra',''),
        suchak2 = request.POST.get('suchak2',''),
        anumodak2 = request.POST.get('anumodak2',''),
        shree6 = request.POST.get('shree6',''),
        shree7 = request.POST.get('shree7',''),
        shree8 = request.POST.get('shree8',''),
        shree9 = request.POST.get('shree9',''),
        suchak3 = request.POST.get('suchak3',''),
        anumodak3 = request.POST.get('anumodak3',''),
        bhandwal = request.POST.get('bhandwal',''),
        bhag = request.POST.get('bhag',''),
        bhag_rupay = request.POST.get('bhag_rupay',''),
        pravesh_fee = request.POST.get('pravesh_fee',''),
        mukhya = request.POST.get('mukhya',''),
        suchak4 = request.POST.get('suchak4',''),
        anumodak4 = request.POST.get('anumodak4'),
        niyojit2 = request.POST.get('niyojit2',''),
        maryadit2 = request.POST.get('maryadit2',''),
        taluka2 = request.POST.get('taluka2',''),
        jilha2 = request.POST.get('jilha2',''),
        limited1 = request.POST.get('limited1',''),
        shakha1 = request.POST.get('shakha1',''),
        hyana = request.POST.get('hyana',''),
        suchak5 = request.POST.get('suchak5',''),
        anumodak5 = request.POST.get('anumodak5',''),
        niyojit3 = request.POST.get('niyojit3',''),
        maryadit3 = request.POST.get('maryadit3',''),
        taluka3 = request.POST.get('taluka3',''),
        jilha3 = request.POST.get('jilha3',''),
        niyo1 = request.POST.get('niyo1',''),
        maryad1 = request.POST.get('maryad1',''),
        niyo2 = request.POST.get('niyo2',''),
        maryad2 = request.POST.get('maryad2',''),
        niyo3 = request.POST.get('niyo3',''),
        maryad3 = request.POST.get('maryad3',''),
        suchak6 = request.POST.get('suchak6',''),
        anumodak6 = request.POST.get('anumodak6'),
        hyanchi = request.POST.get('hyanchi',''),
        hyana1 = request.POST.get('hyana1',''),
        suchak7 = request.POST.get('suchak7',''),
        anumodak7 = request.POST.get('anumodak7',''),
        suchak8 = request.POST.get('suchak8',''),
        anumodak8 = request.POST.get('anumodak8',''),
        niyojit9 = request.POST.get('niyojit9',''),
        maryadit9 = request.POST.get('maryadit9',''),
        suchak9 = request.POST.get('suchak9',''),
        anumodak9 = request.POST.get('anumodak9',''),
        pravart = request.POST.get('pravart',''),
        other = request.POST.get('other',''),
        suchak10 = request.POST.get('suchak10',''),
        anumodak10 = request.POST.get('anumodak10',''),
        mpra = request.POST.get('mpra',''),
        pra1 = request.POST.get('pra1',''),
        pra2 = request.POST.get('pra2',''),
        pra3 = request.POST.get('pra3',''),
        pra4 = request.POST.get('pra4',''),
        pra5 = request.POST.get('pra5',''),
        pra6 = request.POST.get('pra6',''),
        pra7 = request.POST.get('pra7',''),
        pra8 = request.POST.get('pra8',''),
        pra9 = request.POST.get('pra9',''),
        pra10 = request.POST.get('pra10',''),
        pra11 = request.POST.get('pra11',''),
        pra12 = request.POST.get('pra12',''),
        pra13 = request.POST.get('pra13',''),
        pra14 = request.POST.get('pra14',''),
        mukh_pra = request.POST.get('mukh_pra',''),
        sabhadhyak = request.POST.get('sabhadhyak',''),
        niyojit10 = request.POST.get('niyojit10',''),
        maryadit10 = request.POST.get('maryadit10',''),
        taluka4 = request.POST.get('taluka4',''),
        jilha4 = request.POST.get('jilha4',''),

        mpra2 = request.POST.get('mpra2'),
        vyakti1 = request.POST.get('vyakti1',''),
        age1 = request.POST.get('age1',''),
        nation1 = request.POST.get('nation1',''),
        busi1 = request.POST.get('busi1',''),
        patta1 = request.POST.get('patta1',''),
        bhag_price1 = request.POST.get('bhag_price1',''),
        pravesh_fee1 = request.POST.get('pravesh_fee1',''),
        vyavas_fee1 = request.POST.get('vyavas_fee1',''),
        ekun1 = request.POST.get('ekun1',''),
        relate1 = request.POST.get('relate1',''),
        sadasya1 = request.POST.get('sadasya1',''),
        sign1 = request.FILES.get('sign1',''),
        prav2 = request.POST.get('prav2',''),
        vyakti2 = request.POST.get('vyakti2',''),
        age2 = request.POST.get('age2',''),
        nation2 = request.POST.get('nation2',''),
        busi2 = request.POST.get('busi2',''),
        patta2 = request.POST.get('patta2',''),
        bhag_price2 = request.POST.get('bhag_price2',''),
        pravesh_fee2 = request.POST.get('pravesh_fee2',''),
        vyavas_fee2 = request.POST.get('vyavas_fee2',''),
        ekun2 = request.POST.get('ekun2',''),
        relate2 = request.POST.get('relate2',''),
        sadasya2 = request.POST.get('sadasya2',''),
        sign2 = request.FILES.get('sign2',''),
        prav3 = request.POST.get('prav3',''),
        vyakti3 = request.POST.get('vyakti3',''),
        age3 = request.POST.get('age3',''),
        nation3 = request.POST.get('nation3',''),
        busi3 = request.POST.get('busi3',''),
        patta3 = request.POST.get('patta3',''),
        bhag_price3 = request.POST.get('bhag_price3',''),
        pravesh_fee3 = request.POST.get('pravesh_fee3',''),
        vyavas_fee3 = request.POST.get('vyavas_fee3',''),
        ekun3 = request.POST.get('ekun3',''),
        relate3 = request.POST.get('relate3',''),
        sadasya3 = request.POST.get('sadasya3',''),
        sign3 = request.FILES.get('sign3',''),
        prav4 = request.POST.get('prav4',''),
        vyakti4 = request.POST.get('vyakti4',''),
        age4 = request.POST.get('age4',''),
        nation4 = request.POST.get('nation4',''),
        busi4 = request.POST.get('busi4',''),
        patta4 = request.POST.get('patta4',''),
        bhag_price4 = request.POST.get('bhag_price4',''),
        pravesh_fee4 = request.POST.get('pravesh_fee4',''),
        vyavas_fee4 = request.POST.get('vyavas_fee4',''),
        ekun4 = request.POST.get('ekun4',''),
        relate4 = request.POST.get('relate4',''),
        sadasya4 = request.POST.get('sadasya4',''),
        sign4 = request.FILES.get('sign4',''),
        prav5 = request.POST.get('prav5',''),
        vyakti5 = request.POST.get('vyakti5',''),
        age5 = request.POST.get('age5',''),
        nation5 = request.POST.get('nation5',''),
        busi5 = request.POST.get('busi5',''),
        patta5 = request.POST.get('patta5',''),
        bhag_price5 = request.POST.get('bhag_price5',''),
        pravesh_fee5 = request.POST.get('pravesh_fee5',''),
        vyavas_fee5 = request.POST.get('vyavas_fee5',''),
        ekun5 = request.POST.get('ekun5',''),
        relate5 = request.POST.get('relate5',''),
        sadasya5 = request.POST.get('sadasya5',''),
        sign5 = request.FILES.get('sign5',''),
        prav6 = request.POST.get('prav6',''),
        vyakti6 = request.POST.get('vyakti6',''),
        age6 = request.POST.get('age6',''),
        nation6 = request.POST.get('nation6',''),
        busi6 = request.POST.get('busi6',''),
        patta6 = request.POST.get('patta6',''),
        bhag_price6 = request.POST.get('bhag_price6',''),
        pravesh_fee6 = request.POST.get('pravesh_fee6',''),
        vyavas_fee6 = request.POST.get('vyavas_fee6',''),
        ekun6 = request.POST.get('ekun6',''),
        relate6 = request.POST.get('relate6',''),
        sadasya6 = request.POST.get('sadasya6',''),
        sign6 = request.FILES.get('sign6',''),
        prav7 = request.POST.get('prav7',''),
        vyakti7 = request.POST.get('vyakti7',''),
        age7 = request.POST.get('age7',''),
        nation7 = request.POST.get('nation7',''),
        busi7 = request.POST.get('busi7',''),
        patta7 = request.POST.get('patta7',''),
        bhag_price7 = request.POST.get('bhag_price7',''),
        pravesh_fee7 = request.POST.get('pravesh_fee7',''),
        vyavas_fee7 = request.POST.get('vyavas_fee7',''),
        ekun7 = request.POST.get('ekun7',''),
        relate7 = request.POST.get('relate7',''),
        sadasya7 = request.POST.get('sadasya7',''),
        sign7 = request.FILES.get('sign7',''),
        prav8 = request.POST.get('prav8',''),
        vyakti8 = request.POST.get('vyakti8',''),
        age8 = request.POST.get('age8',''),
        nation8 = request.POST.get('nation8',''),
        busi8 = request.POST.get('busi8',''),
        patta8 = request.POST.get('patta8',''),
        bhag_price8 = request.POST.get('bhag_price8',''),
        pravesh_fee8 = request.POST.get('pravesh_fee8',''),
        vyavas_fee8 = request.POST.get('vyavas_fee8',''),
        ekun8 = request.POST.get('ekun8',''),
        relate8 = request.POST.get('relate8',''),
        sadasya8 = request.POST.get('sadasya8',''),
        sign8 = request.FILES.get('sign8',''),
        prav9 = request.POST.get('prav9',''),
        vyakti9 = request.POST.get('vyakti9',''),
        age9 = request.POST.get('age9',''),
        nation9 = request.POST.get('nation9',''),
        busi9 = request.POST.get('busi9',''),
        patta9 = request.POST.get('patta9',''),
        bhag_price9 = request.POST.get('bhag_price9',''),
        pravesh_fee9 = request.POST.get('pravesh_fee9',''),
        vyavas_fee9 = request.POST.get('vyavas_fee9',''),
        ekun9 = request.POST.get('ekun9',''),
        relate9 = request.POST.get('relate9',''),
        sadasya9 = request.POST.get('sadasya9',''),
        sign9 = request.FILES.get('sign9',''),
        prav10 = request.POST.get('prav10',''),
        vyakti10 = request.POST.get('vyakti10',''),
        age10 = request.POST.get('age10',''),
        nation10 = request.POST.get('nation10',''),
        busi10 = request.POST.get('busi10',''),
        patta10 = request.POST.get('patta10',''),
        bhag_price10 = request.POST.get('bhag_price10',''),
        pravesh_fee10 = request.POST.get('pravesh_fee10',''),
        vyavas_fee10 = request.POST.get('vyavas_fee10',''),
        ekun10 = request.POST.get('ekun10',''),
        relate10 = request.POST.get('relate10',''),
        sadasya10 = request.POST.get('sadasya10',''),
        sign10 = request.FILES.get('sign10',''),
        prav11 = request.POST.get('prav11',''),
        vyakti11 = request.POST.get('vyakti11',''),
        age11 = request.POST.get('age11',''),
        nation11 = request.POST.get('nation11',''),
        busi11 = request.POST.get('busi11',''),
        patta11 = request.POST.get('patta11',''),
        bhag_price11 = request.POST.get('bhag_price11',''),
        pravesh_fee11 = request.POST.get('pravesh_fee11',''),
        vyavas_fee11 = request.POST.get('vyavas_fee11',''),
        ekun11 = request.POST.get('ekun11',''),
        relate11 = request.POST.get('relate11',''),
        sadasya11 = request.POST.get('sadasya11',''),
        sign11 = request.FILES.get('sign11',''),
        prav12 = request.POST.get('prav12',''),
        vyakti12 = request.POST.get('vyakti12',''),
        age12 = request.POST.get('age12',''),
        nation12 = request.POST.get('nation12',''),
        busi12 = request.POST.get('busi12',''),
        patta12 = request.POST.get('patta12',''),
        bhag_price12 = request.POST.get('bhag_price12',''),
        pravesh_fee12 = request.POST.get('pravesh_fee12',''),
        vyavas_fee12 = request.POST.get('vyavas_fee12',''),
        ekun12 = request.POST.get('ekun12',''),
        relate12 = request.POST.get('relate12',''),
        sadasya12 = request.POST.get('sadasya12',''),
        sign12 = request.FILES.get('sign12',''),
        prav13 = request.POST.get('prav13',''),
        vyakti13 = request.POST.get('vyakti13',''),
        age13 = request.POST.get('age13',''),
        nation13 = request.POST.get('nation13',''),
        busi13 = request.POST.get('busi13',''),
        patta13 = request.POST.get('patta13',''),
        bhag_price13 = request.POST.get('bhag_price13',''),
        pravesh_fee13 = request.POST.get('pravesh_fee13',''),
        vyavas_fee13 = request.POST.get('vyavas_fee13',''),
        ekun13 = request.POST.get('ekun13',''),
        relate13 = request.POST.get('relate13',''),
        sadasya13 = request.POST.get('sadasya13',''),
        sign13 = request.FILES.get('sign13',''),

        niyojit11 = request.POST.get('niyojit11',''),
        maryadit11 = request.POST.get('maryadit11',''),
        taluka5 = request.POST.get('taluka5',''),
        jilha5 = request.POST.get('jilha5'),
        niyojit12 = request.POST.get('niyojit12',''),
        maryadit12 = request.POST.get('maryadit12',''),
        aaj = request.POST.get('aaj',''),
        din = request.POST.get('din',''),
        taim = request.POST.get('taim',''),
        shree10 = request.POST.get('shree10',''),

        sabhasad1 = request.POST.get('sabhasad1',''),
        sabh_sign1 = request.FILES.get('sabh_sign1',''),
        sabhasad3 = request.POST.get('sabhasad3',''),
        sabh_sign3 = request.FILES.get('sabh_sign3',''),
        sabhasad4 = request.POST.get('sabhasad4',''),
        sabh_sign4 = request.FILES.get('sabh_sign4',''),
        sabhasad5 = request.POST.get('sabhasad5',''),
        sabh_sign5 = request.FILES.get('sabh_sign5',''),
        sabhasad6 = request.POST.get('sabhasad6',''),
        sabh_sign6 = request.FILES.get('sabh_sign6',''),
        sabhasad7 = request.POST.get('sabhasad7',''),
        sabh_sign7 = request.FILES.get('sabh_sign7',''),
        sabhasad8 = request.POST.get('sabhasad8',''),
        sabh_sign8 = request.FILES.get('sabh_sign8',''),
        sabhasad9 = request.POST.get('sabhasad9',''),
        sabh_sign9 = request.FILES.get('sabh_sign9',''),
        sabhasad10 = request.POST.get('sabhasad10',''),
        sabh_sign10 = request.FILES.get('sabh_sign10',''),
        sabhasad11 = request.POST.get('sabhasad11',''),
        sabh_sign11 = request.FILES.get('sabh_sign11',''),
        sabhasad12 = request.POST.get('sabhasad12',''),
        sabh_sign12 = request.FILES.get('sabh_sign12',''),
        sabhasad13 = request.POST.get('sabhasad13',''),
        sabh_sign13 = request.FILES.get('sabh_sign13',''),
        sabhasad14 = request.POST.get('sabhasad14',''),
        sabh_sign14 = request.FILES.get('sabh_sign14',''),
        sabhasad15 = request.POST.get('sabhasad15',''),
        sabh_sign15 = request.FILES.get('sabh_sign15',''),
        sabhasad16 = request.POST.get('sabhasad16',''),
        sabh_sign16 = request.FILES.get('sabh_sign16',''),
        sabhasad17 = request.POST.get('sabhasad17',''),
        sabh_sign17 = request.FILES.get('sabh_sign17',''),
        sabhasad18 = request.POST.get('sabhasad18',''),
        sabh_sign18 = request.FILES.get('sabh_sign18',''),
        sabhasad19 = request.POST.get('sabhasad19',''),
        sabh_sign19 = request.FILES.get('sabh_sign19',''),
        sabhasad20 = request.POST.get('sabhasad20',''),
        sabh_sign20 = request.FILES.get('sabh_sign20',''),
        sabhasad21 = request.POST.get('sabhasad21',''),
        sabh_sign21 = request.FILES.get('sabh_sign21',''),
        sabhasad22 = request.POST.get('sabhasad22',''),
        sabh_sign22 = request.FILES.get('sabh_sign22',''),
        sabhasad23 = request.POST.get('sabhasad23',''),
        sabh_sign23 = request.FILES.get('sabh_sign23',''),
        sabhasad24 = request.POST.get('sabhasad24',''),
        sabh_sign24 = request.FILES.get('sabh_sign24',''),
        sabhasad25 = request.POST.get('sabhasad25',''),
        sabh_sign25 = request.FILES.get('sabh_sign25',''),
        sabhasad26 = request.POST.get('sabhasad26',''),
        sabh_sign26 = request.FILES.get('sabh_sign26',''),
        sabhasad27 = request.POST.get('sabhasad27',''),
        sabh_sign27 = request.FILES.get('sabh_sign27',''),
        sabhasad28 = request.POST.get('sabhasad28',''),
        sabh_sign28 = request.FILES.get('sabh_sign28',''),
        sabhasad29 = request.POST.get('sabhasad29',''),
        sabh_sign29 = request.FILES.get('sabh_sign29',''),
        sabhasad30 = request.POST.get('sabhasad30',''),
        sabh_sign30 = request.FILES.get('sabh_sign30',''),
        sabhasad31 = request.POST.get('sabhasad31',''),
        sabh_sign31 = request.FILES.get('sabh_sign31',''),
        sabhasad32 = request.POST.get('sabhasad32',''),
        sabh_sign32 = request.FILES.get('sabh_sign32',''),
        sabhasad33 = request.POST.get('sabhasad33',''),
        sabh_sign33 = request.FILES.get('sabh_sign33',''),
        sabhasad34 = request.POST.get('sabhasad34',''),
        sabh_sign34 = request.FILES.get('sabh_sign34',''),
        sabhasad35 = request.POST.get('sabhasad35',''),
        sabh_sign35 = request.FILES.get('sabh_sign35',''),

        niyojit13 = request.POST.get('niyojit13',''),
        maryadit13 = request.POST.get('maryadit13',''),
        taluka6 = request.POST.get('taluka6',''),
        jilha6 = request.POST.get('jilha6',''),
        share1 = request.POST.get('share1',''),
        share2 = request.POST.get('share2',''),
        share3 = request.POST.get('share3',''),
        fee1 = request.POST.get('fee1',''),
        fee2 = request.POST.get('fee2',''),
        fee3 = request.POST.get('fee3',''),
        thev1 = request.POST.get('thev1',''),
        thev2 = request.POST.get('thev2',''),
        thev3 = request.POST.get('thev3',''),
        loan1 = request.POST.get('loan1',''),
        loan2 = request.POST.get('loan2',''),
        loan3 = request.POST.get('loan3',''),
        interest1 = request.POST.get('interest1',''),
        interest2 = request.POST.get('interest2',''),
        interest3 = request.POST.get('interest3',''),
        tot1 = request.POST.get('tot1',''),
        tot2 = request.POST.get('tot2',''),
        tot3 = request.POST.get('tot3',''),
        nokar1 = request.POST.get('nokar1',''),
        nokar2 = request.POST.get('nokar2',''),
        nokar3 = request.POST.get('nokar3',''),
        sadilvar1 = request.POST.get('sadilvar1',''),
        sadilvar2 = request.POST.get('sadilvar2',''),
        sadilvar3 = request.POST.get('sadilvar3',''),
        kirkol1 = request.POST.get('kirkol1',''),
        kirkol2 = request.POST.get('kirkol2',''),
        kirkol3 = request.POST.get('kirkol3',''),
        rent1 = request.POST.get('rent1',''),
        rent2 = request.POST.get('rent2',''),
        rent3 = request.POST.get('rent3',''),
        bank1 = request.POST.get('bank1',''),
        bank2 = request.POST.get('bank2',''),
        bank3 = request.POST.get('bank3',''),
        vyaj1 = request.POST.get('vyaj1',''),
        vyaj2 = request.POST.get('vyaj2',''),
        vyaj3 = request.POST.get('vyaj3',''),
        b_share1 = request.POST.get('b_share1',''),
        b_share2 = request.POST.get('b_share2',''),
        b_share3 = request.POST.get('b_share3',''),
        member1 = request.POST.get('member1',''),
        member2 = request.POST.get('member2',''),
        member3 = request.POST.get('member3',''),
        niwwal1 = request.POST.get('niwwal1',''),
        niwwal2 = request.POST.get('niwwal2',''),
        niwwal3 = request.POST.get('niwwal3',''),
        tota1 = request.POST.get('tota1',''),
        tota2 = request.POST.get('tota2',''),
        tota3 = request.POST.get('tota3',''),
        chairman = request.POST.get('chairman',''),
        saha = request.POST.get('saha',''),
        maryadit14 = request.POST.get('maryadit14',''),
        taluka7 = request.POST.get('taluka7',''),
        jilha7 = request.POST.get('jilha7',''),
        karnar = request.POST.get('karnar',''),
        rahnar = request.POST.get('rahnar',''),
        taluka8 = request.POST.get('taluka8',''),
        jilha8 = request.POST.get('jilha8',''),
        purn_nav = request.POST.get('purn_nav',''),
        purn_patta = request.POST.get('purn_patta',''),
        dhanda = request.POST.get('dhanda',''),
        vay = request.POST.get('vay',''),
        varg = request.POST.get('varg',''),
        nationality = request.POST.get('nationality',''),
        pra_rakkam = request.POST.get('pra_rakkam',''),
        bhag_rakkam = request.POST.get('bhag_rakkam',''),
        esam = request.POST.get('esam',''),
        varas_nameadd = request.POST.get('varas_nameadd',''),
        tapshil = request.POST.get('tapshil',''),
        ichito = request.POST.get('ichito',''),
        thak_tapshil = request.POST.get('thak_tapshil',''),
        other_info = request.POST.get('other_info',''),
        dinan = request.POST.get('dinan',''),
        saksh_sign = request.FILES.get('saksh_sign',''),
        arza_sign = request.FILES.get('arza_sign',''),
        tarikh = request.POST.get('tarikh',''),
        tharav_no = request.POST.get('tharav_no',''),
        manjur = request.POST.get('manjur',''),
        saha1 = request.POST.get('saha1',''),
        sarkari = request.POST.get('sarkari',''),
        maryadit15 = request.POST.get('maryadit15',''),
        thikan1 = request.POST.get('thikan1',''),
        dinank2 = request.POST.get('dinank2',''),
        saha_sanstha = request.POST.get('saha_sanstha',''),
        niyojit_sanstha = request.POST.get('niyojit_sanstha',''),
        nond_add = request.POST.get('nond_add',''),
        marya_yn = request.POST.get('marya_yn',''),
        karyashetra = request.POST.get('karyashetra',''),
        uddishtha = request.POST.get('uddishtha',''),
        bhasha = request.POST.get('bhasha',''),
        andaz = request.POST.get('andaz',''),
        mp_name = request.POST.get('mp_name',''),
        mp_add = request.POST.get('mp_add',''),
        hishob_lang = request.POST.get('hishob_lang',''),

        name1 = request.POST.get('name1',''),
        sansthapi1 = request.POST.get('sansthapi1',''),
        vay1 = request.POST.get('vay1',''),
        rashtra1 = request.POST.get('rashtra1',''),
        business1 = request.POST.get('business1',''),
        addres1 = request.POST.get('addres1',''),
        ansha_rakkam1 = request.POST.get('ansha_rakkam1',''),
        relative1 = request.POST.get('relative1',''),
        sam_sad1 = request.POST.get('sam_sad1',''),
        sahi1 = request.FILES.get('sahi1',''),

        name2 = request.POST.get('name2',''),
        sansthapi2 = request.POST.get('sansthapi2',''),
        vay2 = request.POST.get('vay2',''),
        rashtra2 = request.POST.get('rashtra2',''),
        business2 = request.POST.get('business2',''),
        addres2 = request.POST.get('addres2',''),
        ansha_rakkam2 = request.POST.get('ansha_rakkam2',''),
        relative2 = request.POST.get('relative2',''),
        sam_sad2 = request.POST.get('sam_sad2',''),
        sahi2 = request.FILES.get('sahi2',''),

        name3 = request.POST.get('name3',''),
        sansthapi3 = request.POST.get('sansthapi3',''),
        vay3 = request.POST.get('vay3',''),
        rashtra3 = request.POST.get('rashtra3',''),
        business3 = request.POST.get('business3',''),
        addres3 = request.POST.get('addres3',''),
        ansha_rakkam3 = request.POST.get('ansha_rakkam3',''),
        relative3 = request.POST.get('relative3',''),
        sam_sad3 = request.POST.get('sam_sad3',''),
        sahi3 = request.FILES.get('sahi3',''),

        name4 = request.POST.get('name4',''),
        sansthapi4 = request.POST.get('sansthapi4',''),
        vay4 = request.POST.get('vay4',''),
        rashtra4 = request.POST.get('rashtra4',''),
        business4 = request.POST.get('business4',''),
        addres4 = request.POST.get('addres4',''),
        ansha_rakkam4 = request.POST.get('ansha_rakkam4',''),
        relative4 = request.POST.get('relative4',''),
        sam_sad4 = request.POST.get('sam_sad4',''),
        sahi4 = request.FILES.get('sahi4',''),

        name5 = request.POST.get('name5',''),
        sansthapi5 = request.POST.get('sansthapi5',''),
        vay5 = request.POST.get('vay5',''),
        rashtra5 = request.POST.get('rashtra5',''),
        business5 = request.POST.get('business5',''),
        addres5 = request.POST.get('addres5',''),
        ansha_rakkam5 = request.POST.get('ansha_rakkam5',''),
        relative5 = request.POST.get('relative5',''),
        sam_sad5 = request.POST.get('sam_sad5',''),
        sahi5 = request.FILES.get('sahi5',''),

        name6 = request.POST.get('name6',''),
        sansthapi6 = request.POST.get('sansthapi6',''),
        vay6 = request.POST.get('vay6',''),
        rashtra6 = request.POST.get('rashtra6',''),
        business6 = request.POST.get('business6',''),
        addres6 = request.POST.get('addres6',''),
        ansha_rakkam6 = request.POST.get('ansha_rakkam6',''),
        relative6 = request.POST.get('relative6',''),
        sam_sad6 = request.POST.get('sam_sad6',''),
        sahi6 = request.FILES.get('sahi6',''),

        name7 = request.POST.get('name7',''),
        sansthapi7 = request.POST.get('sansthapi7',''),
        vay7 = request.POST.get('vay7',''),
        rashtra7 = request.POST.get('rashtra7',''),
        business7 = request.POST.get('business7',''),
        addres7 = request.POST.get('addres7',''),
        ansha_rakkam7 = request.POST.get('ansha_rakkam7',''),
        relative7 = request.POST.get('relative7',''),
        sam_sad7 = request.POST.get('sam_sad7',''),
        sahi7 = request.FILES.get('sahi7',''),

        name8 = request.POST.get('name8',''),
        sansthapi8 = request.POST.get('sansthapi8',''),
        vay8 = request.POST.get('vay8',''),
        rashtra8 = request.POST.get('rashtra8',''),
        business8 = request.POST.get('business8',''),
        addres8 = request.POST.get('addres8',''),
        ansha_rakkam8 = request.POST.get('ansha_rakkam8',''),
        relative8 = request.POST.get('relative8',''),
        sam_sad8 = request.POST.get('sam_sad8',''),
        sahi8 = request.FILES.get('sahi8',''),

        name9 = request.POST.get('name9',''),
        sansthapi9 = request.POST.get('sansthapi9',''),
        vay9 = request.POST.get('vay9',''),
        rashtra9 = request.POST.get('rashtra9',''),
        business9 = request.POST.get('business9',''),
        addres9 = request.POST.get('addres9',''),
        ansha_rakkam9 = request.POST.get('ansha_rakkam9',''),
        relative9 = request.POST.get('relative9',''),
        sam_sad9 = request.POST.get('sam_sad9',''),
        sahi9 = request.FILES.get('sahi9',''),

        name10 = request.POST.get('name10',''),
        sansthapi10 = request.POST.get('sansthapi10',''),
        vay10 = request.POST.get('vay10',''),
        rashtra10 = request.POST.get('rashtra10',''),
        business10 = request.POST.get('business10',''),
        addres10 = request.POST.get('addres10',''),
        ansha_rakkam10 = request.POST.get('ansha_rakkam10',''),
        relative10 = request.POST.get('relative10',''),
        sam_sad10 = request.POST.get('sam_sad10',''),
        sahi10 = request.FILES.get('sahi10',''),

        name11 = request.POST.get('name11',''),
        sansthapi11 = request.POST.get('sansthapi11',''),
        vay11 = request.POST.get('vay11',''),
        rashtra11 = request.POST.get('rashtra11',''),
        business11 = request.POST.get('business11',''),
        addres11 = request.POST.get('addres11',''),
        ansha_rakkam11 = request.POST.get('ansha_rakkam11',''),
        relative11 = request.POST.get('relative11',''),
        sam_sad11 = request.POST.get('sam_sad11',''),
        sahi11 = request.FILES.get('sahi11',''),

        name12 = request.POST.get('name12',''),
        sansthapi12 = request.POST.get('sansthapi12',''),
        vay12 = request.POST.get('vay12',''),
        rashtra12 = request.POST.get('rashtra12',''),
        business12 = request.POST.get('business12',''),
        addres12 = request.POST.get('addres12',''),
        ansha_rakkam12 = request.POST.get('ansha_rakkam12',''),
        relative12 = request.POST.get('relative12',''),
        sam_sad12 = request.POST.get('sam_sad12',''),
        sahi12 = request.FILES.get('sahi12',''),

        name13 = request.POST.get('name13',''),
        sansthapi13 = request.POST.get('sansthapi13',''),
        vay13 = request.POST.get('vay13',''),
        rashtra13 = request.POST.get('rashtra13',''),
        business13 = request.POST.get('business13',''),
        addres13 = request.POST.get('addres13',''),
        ansha_rakkam13 = request.POST.get('ansha_rakkam13',''),
        relative13 = request.POST.get('relative13',''),
        sam_sad13 = request.POST.get('sam_sad13',''),
        sahi13 = request.FILES.get('sahi13',''),

        name14 = request.POST.get('name14',''),
        sansthapi14 = request.POST.get('sansthapi14',''),
        vay14 = request.POST.get('vay14',''),
        rashtra14 = request.POST.get('rashtra14',''),
        business14 = request.POST.get('business14',''),
        addres14 = request.POST.get('addres14',''),
        ansha_rakkam14 = request.POST.get('ansha_rakkam14',''),
        relative14 = request.POST.get('relative14',''),
        sam_sad14 = request.POST.get('sam_sad14',''),
        sahi14 = request.FILES.get('sahi14',''),

        name15 = request.POST.get('name15',''),
        sansthapi15 = request.POST.get('sansthapi15',''),
        vay15 = request.POST.get('vay15',''),
        rashtra15 = request.POST.get('rashtra15',''),
        business15 = request.POST.get('business15',''),
        addres15 = request.POST.get('addres15',''),
        ansha_rakkam15 = request.POST.get('ansha_rakkam15',''),
        relative15 = request.POST.get('relative15',''),
        sam_sad15 = request.POST.get('sam_sad15',''),
        sahi15 = request.FILES.get('sahi15',''),

        patra_name = request.POST.get('patra_name',''),
        patra_add = request.POST.get('patra_add',''),

        sahya1 = request.FILES.get('sahya1',''),
        sahya2 = request.FILES.get('sahya2',''),
        sahya3 = request.FILES.get('sahya3',''),
        sahya4 = request.FILES.get('sahya4',''),
        sahya5 = request.FILES.get('sahya5',''),
        sahya6 = request.FILES.get('sahya6',''),
        sahya7 = request.FILES.get('sahya7',''),
        sahya8 = request.FILES.get('sahya8',''),
        sahya9 = request.FILES.get('sahya9',''),
        sahya10 = request.FILES.get('sahya10',''),
        sahya11 = request.FILES.get('sahya11',''),
        sahya12 = request.FILES.get('sahya12',''),
        sahya13 = request.FILES.get('sahya13',''),
        sahya14 = request.FILES.get('sahya14',''),
        sahya15 = request.FILES.get('sahya15',''),

        mukhya_pra = request.POST.get('mukhya_pra',''),
        niyojit14 = request.POST.get('niyojit14',''),
        roji = request.POST.get('roji',''),
        pratyaksh = request.POST.get('pratyaksh',''),
        nibandhak = request.POST.get('nibandhak',''),
        yana = request.POST.get('yana',''),
        roji1 = request.POST.get('roji1',''),
        anukra = request.POST.get('anukra',''),
        swikar_sahi = request.FILES.get('swikar_sahi','')
        )
        x.save()
        print("X: ",x)
    return JsonResponse({'status':200})











    




























    





