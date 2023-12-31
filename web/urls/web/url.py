from django.urls import path

from web.views.web import view

from django.urls import path, include
from django.contrib.auth import views as auth_views


app_name = "web"
urlpatterns = [
    path('', view.home, name='home'),
    path('sectors/', view.sector_index, name='sector_index'),
    path('sectors/<str:name>/', view.sector_show, name='sector_show'),
    path('departments/', view.department_index, name='department_index'),
    path('departments/<str:name>/', view.department_show, name='department_show'),
    path('schemes/<str:department>/', view.scheme_index, name='scheme_index'),
    path('schemes/<str:name>/', view.scheme_show, name='scheme_show'),
    path('schemes/<str:pk>/registration/', view.scheme_registration, name='scheme_registration'),
    path('schemes/<str:pk>/registration_update/', view.scheme_registration_update, name='scheme_registration_updates'),
    path('update_profile/',view.update_profile,name='update_profile'),
    path('sign-in/', view.sign_in, name='sign_in'),
    path('sign-out/', view.sign_out, name='sign_out'),
    # path('sign-up/', view.sign_up, name='sign_up'),
    path('registration/', view.Registration.as_view(), name="register"),
    
    path('admin_dashboard/', view.dep_dashboard, name="depart_dashboard"),
    path('department_stats/', view.Department_Clerk_1_view, name="depart_1_stats"),
    path('department_schemes/<str:scheme>', view.Department_clerk_1_scheme, name="depart_1_scheme"),
    path('department_user_verification/<str:pk>/<str:scheme_name>',view.user_details_verification,name="user_verify"),
    path('stats/<str:department>/<str:scheme>/', view.master_stats_scheme, name='master_stats'),
    path('stats/<str:department>/', view.master_stats_department, name='master_stats'),
    path('stats/', view.master_stats, name='master_stats'),
    
    # path('verify/', view.verify, name="verify"),
    path('mobile/verification/', view.mobile_verification, name='mobile_verification'),
    path('profile/', view.profile, name='profile'),
    path('applied_schemes/', view.applied_schemes, name='applied_schemes'),
    # path('department_admin/', view.department_admin, name='department_admin'),
    path('department_admin/', view.department_admin, name='department_admin'),
    path('department_admin1/', view.department_admin1, name='department_admin1'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='web/password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='web/password_resent_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='web/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='web/password_reset_done.html'),name='password_reset_complete'),
    path('documents/',view.view_document,name="view_documents"),
    path('search_data/<str:scheme>',view.search_applicant,name = 'search_data'),
    path('pramod_mah/<str:pk>', view.pramod_maha, name='pramod_maha'),
    path('pra_dhan/<str:pk>', view.pradhan_mantri, name='pradhan_mantri'),
    path('din_dayal/<str:pk>', view.dindayal_ant, name='dindayal_ant'),
    path('sankalpp/<str:pk>', view.sankalpp, name='sankalpp'),
    path('mini/<str:pk>', view.mini, name='mini'),
    path('jilha_pur/<str:pk>', view.jilha_puru, name='jilha_pur'),
    path('upajivikesathi/<str:pk>', view.kaushalya_vibhag, name='upajivikesathi'),
    path('andh_vyaktinsathi/<str:pk>',view.andha_vyaktinsathi,name='andh_vyaktinsathi'),
    path('ramai_gharkul/<str:pk>',view.ramai_gharkull,name='ramai_gharkul'),
    path('bharatratna/<str:pk>', view.bharatratna, name='bharatratna'),
    path('lokshahir_anna/<str:pk>', view.lokshahir_anna, name='lokshahir_anna'),
    path('sant_ravidas/<str:pk>', view.sant_ravidas, name='sant_ravidas'),
    path('karmavir_dada/<str:pk>', view.karmavir_dada, name='karmavir_dada'),
    path('sanstha/<str:pk>', view.sanstha, name='sanstha'),
    path('anna_sanstha/<str:pk>', view.anna_sanstha, name='anna_sanstha'),
    path('sant_sanstha/<str:pk>', view.sant_sanstha, name='sant_sanstha'),
    path('shahufule/<str:pk>',view.shahufule,name='shahufule'),
    path('shahufule/<str:pk>',view.shahufule,name='shahufule'),
    path('magas_mul/<str:pk>',view.magas_mul,name='magas_mul'),
    path('pravinya_pur/<str:pk>',view.pravinya_pur,name='pravinya_pur'),
    path('gayak/<str:pk>',view.gayak,name='gayak'),
    path('swadhhar/<str:pk>',view.swadhhar,name='swadhhar'),
    path('gatai_kam/<str:pk>',view.gatai_kam,name='gatai_kam'),
    # path('rojgar_hami/<str:pk>',view.rojgar_hami,name='rojgar_hami'),
    path('vai_sabha/<str:pk>',view.vai_sabha,name='vai_sabha'),
    path('sanstha_sabha/<str:pk>',view.sanstha_sabha,name='sanstha_sabha'),
    path('arthasahayy/<str:pk>',view.arthasahayy,name='arthasahayy'),
    path('pradhan_pmmsy/<str:pk>',view.pradhan_pmmsy,name='pradhan_pmmsy'),
    path('polisbharti/<str:pk>',view.polisbharti,name='polisbharti'),
    path('zakir_husen/<str:pk>',view.zakir_husen,name='zakir_husen'),
    path('shivanyantra/<str:pk>',view.shivanyantra,name='shivanyantra'),
    path('mada_cycl/<str:pk>',view.mada_cycl,name='mada_cycl'),
    path('balsango/<str:pk>',view.balsango,name='balsango'),
    path('samuhik_viva/<str:pk>',view.samuhik_viva,name='samuhik_viva'),
    path('ot_shivanyantra/<str:pk>',view.ot_shivanyantra,name='ot_shivanyantra'),
    path('sc_shivanyantra/<str:pk>',view.sc_shivanyantra,name='sc_shivanyantra'),
    path('tsp_shivanyantra/<str:pk>',view.tsp_shivanyantra,name='tsp_shivanyantra'),
    path('otsp_cyc/<str:pk>',view.otsp_cyc,name='otsp_cyc'),
    path('scp_cyc/<str:pk>',view.scp_cyc,name='scp_cyc'),
    path('tsp_cyc/<str:pk>',view.tsp_cyc,name='tsp_cyc'),
    path('dharmik_alpp/<str:pk>',view.dharmik_alpp,name='dharmik_alpp'),
    path('navin_biogas/<str:pk>',view.navin_biogas,name='navin_biogas'),
    path('jamin_patrika/<str:pk>',view.jamin_patrika,name='jamin_patrika'),
    path('ropvatika/<str:pk>',view.ropvatika,name='ropvatika'),
    path('jilhaudyog/<str:pk>', view.jilha_udyog, name='jilhaudyog'),
    path('sudharit_bij/<str:pk>', view.sudharit_bij, name='sudharit_bij'),
    path('asthivyang/<str:pk>', view.asthivyang_vyaktisathi, name='asthivyang'),
    path('karnbadhir/<str:pk>', view.karnbadhir_vyaktisathi, name='karnbadhir'),
    path('divyangxerox/<str:pk>', view.divyangvyakti_xerox, name='divyangxerox'),
    path('divyangsanganak/<str:pk>', view.divyang_sanganakedu, name='divyangsanganak'),
    path('magas_shilai/<str:pk>', view.magasvargiy_shilai, name='magas_shilai'),
    path('dubhte_jan/<str:pk>', view.dubhtya_janawarankarita, name='dubhte_jan'),
    path('anu_50takke/<str:pk>', view.anusuchitjati_50takke, name='anu_50takke'), 
    path('anu_dudhjanvar/<str:pk>', view.anusuchit_dudhaljanavare, name='anu_dudhjanvar'),
    path('anushelya/<str:pk>', view.anusuchit_75takkeshelya, name='anushelya'),
    path('thakkar/<str:pk>', view.thakkar_bappa, name='thakkar'),
    path('anu_shabri/<str:pk>', view.anusuchit_shabriyojna, name='anu_shabri'),
    path('bhumihin/<str:pk>', view.bhumihin_daridryaadivasi, name='bhumihin'),
    path('samuvivah/<str:pk>', view.samuhik_vivahsohla, name='samuvivah'),
    path('anuswecha/<str:pk>', view.anuswechaa_ashramshala, name='anuswecha'),
    path('divya_avya/<str:pk>', view.divyang_avyangvivah, name='divya_avya'),
    path('divya_divyanganu/<str:pk>', view.divyang_divyanganu, name='divya_divyanganu'),
    path('swayamrojgar/<str:pk>', view.swayamrojgar_bijbhandwal, name='swayamrojgar'),
    path('antarjat_vivah/<str:pk>', view.antarjatiya_vivahjodpe, name='antarjat_vivah'),
    path('anuscholar/<str:pk>', view.anusuchitjamat_scholar, name='anuscholar'),
    path('adivasi_engraji/<str:pk>', view.adivasi_engraji, name='adivasi_engraji'),
    path('sainikadi/<str:pk>', view.sainiki_shala, name='sainikadi'),
    path('eklavyaschool/<str:pk>', view.eklavya_publicschool, name='eklavyaschool'),
    path('kendraprashikshan/<str:pk>', view.kendravarti_prashikshan, name='kendraprashikshan'),
    path('kendra_utpanna/<str:pk>', view.kendravarti_arthasankalp, name='kendra_utpanna'),
    path('ashramsamuh/<str:pk>', view.shaskiy_ashramshalasamuh, name='ashramsamuh'),
    path('postbasic/<str:pk>', view.shaskiypost_ashram, name='postbasic'),
    path('kisancard/<str:pk>', view.kisan_creditcard, name='kisancard'),
    path('silk/<str:pk>', view.silk_samagrayojna, name='silk'),
    path('nondnivivah/<str:pk>', view.shubhmangal_nondnivivah, name='nondnivivah'),
    path('rsmscholar/<str:pk>', view.rajarshi_shahumaharajscholar, name='rsmscholar'),
    path('mgreshim/<str:pk>', view.mahatmagandhi_reshimvibhag, name='mgreshim'),
    path('ekatmik/<str:pk>', view.ekatmik_dugdhavikas, name='ekatmik'),
    
   


    #path(r'broadcast$', view.broadcast_sms, name="default"),
    
     # """URL FOR DPO SECTION"""
    path('sign-in/dpt/',view.sign_in_dpo,name="sign_dpo"),
    path('sign_out/dpt/',view.sign_out_dpo,name="sign_out_dpo"),

]
