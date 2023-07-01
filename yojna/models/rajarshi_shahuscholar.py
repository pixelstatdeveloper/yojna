from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from yojna.models import SchemeModel,SchemeRegistrationModel,UserModel

class rajarshi_shahuscholar(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True, default=None)
    edu_type = models.CharField(max_length=3, null=True, blank=True, default=None)
    edu_branch = models.CharField(max_length=50, null=True, blank=True, default=None)
    other_edu = models.CharField(max_length=20, null=True, blank=True, default=None)
    address = models.CharField(max_length=150, null=True, blank=True, default=None)
    mob_no = PhoneNumberField( blank=True)
    jat = models.CharField(max_length=50, null=True, blank=True, default=None)
    birthdate_ank = models.DateField(default=None,null=True,blank=True)
    birthdate_akshar = models.CharField(max_length=50, null=True, blank=True, default=None)
    age = models.CharField(max_length=2, null=True, blank=True, default=None)
    email_id = models.EmailField(null=False, blank=False, default=None)
    adhar_no = models.BigIntegerField(null=True, blank=True, default=None)
    adhar_prat = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    pan_no = models.CharField(max_length=20, null=True, blank=True, default=None)
    mahavasi_yn = models.CharField(max_length=4, null=True, blank=True, default=None)

    ssc_abhyaskram = models.CharField(max_length=50, null=True, blank=True, default=None)
    ssc_passyear = models.CharField(max_length=4, null=True, blank=True, default=None)
    ssc_institute = models.CharField(max_length=120, null=True, blank=True, default=None)
    ssc_totalmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    ssc_obtainmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    ssc_takke = models.CharField(max_length=50, null=True, blank=True, default=None)

    hsc_abhyaskram = models.CharField(max_length=50, null=True, blank=True, default=None)
    hsc_passyear = models.CharField(max_length=4, null=True, blank=True, default=None)
    hsc_institute = models.CharField(max_length=120, null=True, blank=True, default=None)
    hsc_totalmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    hsc_obtainmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    hsc_takke = models.CharField(max_length=50, null=True, blank=True, default=None)

    padvi_abhyaskram = models.CharField(max_length=50, null=True, blank=True, default=None)
    padvi_passyear = models.CharField(max_length=4, null=True, blank=True, default=None)
    padvi_institute = models.CharField(max_length=120, null=True, blank=True, default=None)
    padvi_totalmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    padvi_obtainmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    padvi_takke = models.CharField(max_length=50, null=True, blank=True, default=None)

    padvika_abhyaskram = models.CharField(max_length=50, null=True, blank=True, default=None)
    padvika_passyear = models.CharField(max_length=4, null=True, blank=True, default=None)
    padvika_institute = models.CharField(max_length=120, null=True, blank=True, default=None)
    padvika_totalmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    padvika_obtainmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    padvika_takke = models.CharField(max_length=50, null=True, blank=True, default=None)

    gre_abhyaskram = models.CharField(max_length=50, null=True, blank=True, default=None)
    gre_passyear = models.CharField(max_length=4, null=True, blank=True, default=None)
    gre_institute = models.CharField(max_length=120, null=True, blank=True, default=None)
    gre_totalmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    gre_obtainmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    gre_takke = models.CharField(max_length=50, null=True, blank=True, default=None)

    toefl_abhyaskram = models.CharField(max_length=50, null=True, blank=True, default=None)
    toefl_passyear = models.CharField(max_length=4, null=True, blank=True, default=None)
    toefl_institute = models.CharField(max_length=120, null=True, blank=True, default=None)
    toefl_totalmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    toefl_obtainmarks = models.CharField(max_length=4, null=True, blank=True, default=None)
    toefl_takke = models.CharField(max_length=50, null=True, blank=True, default=None)

    vyavsay = models.CharField(max_length=80,null=True, blank=True, default=None)
    naukri = models.CharField(max_length=100,null=True, blank=True, default=None)
    hudda = models.CharField(max_length=50,null=True, blank=True, default=None)
    vn_income = models.CharField(max_length=50,null=True, blank=True, default=None)
    inc_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    noc_yn = models.CharField(max_length=4,null=True, blank=True, default=None)
    karyalay = models.CharField(max_length=80,null=True, blank=True, default=None)
    office_number = PhoneNumberField( blank=True)
    office_email = models.EmailField(null=False, blank=False, default=None)
    married = models.CharField(max_length=8,null=True, blank=True, default=None)
    husband_wifename = models.CharField(max_length=80,null=True, blank=True, default=None)
    child1 = models.CharField(max_length=80,null=True, blank=True, default=None)
    child2 = models.CharField(max_length=80,null=True, blank=True, default=None)
    sobat_yn = models.CharField(max_length=4,null=True, blank=True, default=None)
    acholder_nm = models.CharField(max_length=80,null=True, blank=True, default=None)
    bank_name = models.CharField(max_length=50,null=True, blank=True, default=None)
    branch = models.CharField(max_length=30,null=True, blank=True, default=None)
    acc_no = models.BigIntegerField(null=True, blank=True, default=None)
    ifsc = models.CharField(max_length=30,null=True, blank=True, default=None)
    micr = models.CharField(max_length=40,null=True, blank=True, default=None)
    passport_no = models.CharField(max_length=30,null=True, blank=True, default=None)
    issue_date = models.DateField(default=None,null=True,blank=True)
    end_date = models.DateField(default=None,null=True,blank=True)
    offerletter_no = models.CharField(max_length=30,null=True, blank=True, default=None)
    offerletter_date = models.DateField(default=None,null=True,blank=True)
    at_vinaat = models.CharField(max_length=8,null=True, blank=True, default=None)
    konti_at = models.CharField(max_length=100,null=True, blank=True, default=None)
    abyaskram = models.CharField(max_length=100,null=True, blank=True, default=None)
    labh_yn = models.CharField(max_length=4,null=True, blank=True, default=None)
    year = models.CharField(max_length=4,null=True, blank=True, default=None)
    sanstha = models.CharField(max_length=100,null=True, blank=True, default=None)
    abhyaskram_name = models.CharField(max_length=100,null=True, blank=True, default=None)
    abhyaskram_validity = models.CharField(max_length=50,null=True, blank=True, default=None)
    shishyavrutti = models.CharField(max_length=50,null=True, blank=True, default=None)
    palak_name = models.CharField(max_length=100,null=True, blank=True, default=None)
    palak_address = models.CharField(max_length=150,null=True, blank=True, default=None)
    palak_mob = PhoneNumberField( blank=True)
    palak_email = models.EmailField(null=False, blank=False, default=None)
    palak_vyavsay = models.CharField(max_length=80,null=True, blank=True, default=None)
    palak_naukri = models.CharField(max_length=120,null=True, blank=True, default=None)
    palak_hudda = models.CharField(max_length=50,null=True, blank=True, default=None)
    palak_income = models.CharField(max_length=15,null=True, blank=True, default=None)
    palakincome_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    palak_officeadd = models.CharField(max_length=100,null=True, blank=True, default=None)
    palakoffice_mob = PhoneNumberField( blank=True)
    palakoffice_email = models.EmailField(null=False, blank=False, default=None)

    yearly_income = models.CharField(max_length=15, null=True, blank=True, default=None)
    yearincome_yn = models.CharField(max_length=4,null=True, blank=True, default=None)
    yearincome_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    tax = models.CharField(max_length=100,null=True, blank=True, default=None)
    tax_yn = models.CharField(max_length=4,null=True, blank=True, default=None)
    tax_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    vadil_yn = models.CharField(max_length=4,null=True, blank=True, default=None)
    vadil_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    nyayalay = models.CharField(max_length=4,null=True, blank=True, default=None)
    nyayalay_cf = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)

    sampurn_nav1 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age1 = models.CharField(default=None,null=True,blank=True,max_length=2)
    vyavsay1 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income1 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn1 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav2 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age2 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate2 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay2 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income2 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn2 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav3 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age3 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate3 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay3 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income3 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn3 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav4 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age4 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate4 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay4 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income4 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn4 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav5 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age5 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate5 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay5 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income5 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn5 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav6 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age6 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate6 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay6 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income6 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn6 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav7 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age7 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate7 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay7 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income7 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn7 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav8 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age8 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate8 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay8 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income8 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn8 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav9 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age9 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate9 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay9 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income9 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn9 = models.CharField(default=None,null=True,blank=True,max_length=20)

    sampurn_nav10 = models.CharField(default=None,null=True,blank=True,max_length=50)
    age10 = models.CharField(default=None,null=True,blank=True,max_length=2)
    nate10 = models.CharField(default=None,null=True,blank=True,max_length=30)
    vyavsay10 = models.CharField(default=None,null=True,blank=True,max_length=50)
    income10 = models.CharField(default=None,null=True,blank=True,max_length=15)
    scholar_yn10 = models.CharField(default=None,null=True,blank=True,max_length=20)

    kutumb_income = models.CharField(default=None,null=True,blank=True,max_length=15)

    pravesh_varsh = models.CharField(default=None,null=True,blank=True,max_length=4)
    vidyapith = models.CharField(default=None,null=True,blank=True,max_length=150)
    desh = models.CharField(default=None,null=True,blank=True,max_length=30)
    shasan = models.CharField(default=None,null=True,blank=True,max_length=30)

    vidyapith_name = models.CharField(default=None,null=True,blank=True,max_length=150)
    qsworld_rank = models.CharField(default=None,null=True,blank=True,max_length=100)
    vidyarthi_abhyas = models.CharField(default=None,null=True,blank=True,max_length=100)
    abhyas_swarup = models.CharField(default=None,null=True,blank=True,max_length=10)
    kalavadhi = models.CharField(default=None,null=True,blank=True,max_length=50)
    pravesh_dinank = models.DateField(default=None,null=True,blank=True)
    pardesh_patta = models.CharField(default=None,null=True,blank=True,max_length=120)
    pardesh_mob = PhoneNumberField( blank=True)
    pardesh_email = models.EmailField(null=False, blank=False, default=None)

    shikshan1 = models.CharField(max_length=50,null=True, blank=True, default=None)
    shikshan2 = models.CharField(max_length=50,null=True, blank=True, default=None)
    shikshan3 = models.CharField(max_length=50,null=True, blank=True, default=None)
    shikshan4 = models.CharField(max_length=50,null=True, blank=True, default=None)
    pariksha1 = models.CharField(max_length=50,null=True, blank=True, default=None)
    pariksha2 = models.CharField(max_length=50,null=True, blank=True, default=None)
    pariksha3 = models.CharField(max_length=50,null=True, blank=True, default=None)
    pariksha4 = models.CharField(max_length=50,null=True, blank=True, default=None)
    nondni1 = models.CharField(max_length=50,null=True, blank=True, default=None)
    nondni2 = models.CharField(max_length=50,null=True, blank=True, default=None)
    nondni3 = models.CharField(max_length=50,null=True, blank=True, default=None)
    nondni4 = models.CharField(max_length=50,null=True, blank=True, default=None)
    jevan_rahne1 = models.CharField(max_length=50,null=True, blank=True, default=None)
    jevan_rahne2 = models.CharField(max_length=50,null=True, blank=True, default=None)
    jevan_rahne3 = models.CharField(max_length=50,null=True, blank=True, default=None)
    jevan_rahne4 = models.CharField(max_length=50,null=True, blank=True, default=None)
    vima1 = models.CharField(max_length=50,null=True, blank=True, default=None)
    vima2 = models.CharField(max_length=50,null=True, blank=True, default=None)
    vima3 = models.CharField(max_length=50,null=True, blank=True, default=None)
    vima4 = models.CharField(max_length=50,null=True, blank=True, default=None)
    other1 = models.CharField(max_length=50,null=True, blank=True, default=None)
    other2 = models.CharField(max_length=50,null=True, blank=True, default=None)
    other3 = models.CharField(max_length=50,null=True, blank=True, default=None)
    other4 = models.CharField(max_length=50,null=True, blank=True, default=None)
    total1 = models.CharField(max_length=50,null=True, blank=True, default=None)
    total2 = models.CharField(max_length=50,null=True, blank=True, default=None)
    total3 = models.CharField(max_length=50,null=True, blank=True, default=None)
    total4 = models.CharField(max_length=50,null=True, blank=True, default=None)

    other_scholar = models.CharField(max_length=100,null=True, blank=True, default=None)
    fellowship = models.CharField(max_length=100,null=True, blank=True, default=None)
    gtas = models.CharField(max_length=100,null=True, blank=True, default=None)
    other_mandhan = models.CharField(max_length=100,null=True, blank=True, default=None)
    campus = models.CharField(max_length=100,null=True, blank=True, default=None)

    thikan= models.CharField(max_length=50,null=True, blank=True, default=None)
    palak_sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    vidyarthi_sign = models.FileField(upload_to='media/divyang_person_sign',default=None,null=True,blank=True)
    dinank = models.DateField(default=None,null=True,blank=True)
    palak_nav = models.CharField(max_length=50,null=True, blank=True, default=None)
    vidyarthi_nav = models.CharField(max_length=50,null=True, blank=True, default=None)

    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    scheme=models.ForeignKey(SchemeModel, on_delete=models.CASCADE, null=True)
    scheme_register=models.ForeignKey(SchemeRegistrationModel, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "rajarshi_shahuscholar"
    def __str__(self) -> str:
        return str(self.name)
        

