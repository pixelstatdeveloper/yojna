from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group
from .sector import SectorAdmin
from .department import DepartmentAdmin
from .scheme import SchemeAdmin
from .user import UserAdmin
from .scheme_media import SchemeMediaAdmin
from .department_media import DepartmentMediaAdmin
from .scheme_registration import SchemeRegistrationAdmin
from .scheme_registration_media import SchemeRegistrationMediaAdmin
from .sub_department import SubdepartmentAdmin
from .document_link import DocumentlinkAdmin
from .jilha import jilha_pur
from .pradhan import pra_dhanAdmin
from .pramod import pramod_mah
from .dindayal import din_dayal
from .upajivikesathi_kaushalya_vibhag import upajivikesathi
from .andh_vyaktinsathi_sahyabhut import andha_vyaktisathiAdmin
from .anusuchit_jati_navboddha import ramai_gharkulAdmin
from .mini_tracter import mini_tra
from .sankalp import sankalp_skill
from .bharatratna_vyakti import vyaktinsathi
from .shahu import shahu_fule
from .sahityaratna import lokshahir
from .santravi import ravidas
from .padmashri import karmavir
from .sansthesathi import bharat_sanstha
from .sahityaratna_sanstha import lokshahir_sanstha
from .santravi_sanstha import ravidas_sanstha
from .magasvargiy import magasvargiy_mula
from .pravinya import pravinya_rajya
from .padma import gayakvad
from .swadhar import swadhar_yoj
from .gatai import gatai_kamgar
from .mahatma_gandhi import hami_yojna
from .granthalaye_vaiyaktik import vaiyaktik_sabhasad
from .granthalaye_sanstha import sanstha_sabhasad
from .mase_arthsahayya import masemari_arth
from .pmmsy import matsyasampada
from .polis_bharti import polis_bhartipurva
from .zakir import zakir_hus
from .mada_shivan import mada_shivnyantra
from .cycle import mada_cycle
from .balsang import balsangopan
from .shubmangal import shubh_vivah
from .otsp_shivan import otsp_shivnyantra
from .scp_shivan import scp_shivnyantra
from .tsp_shivan import tsp_shivnyantra
from .otsp_cycle import otsp_cycl
from .tsp_cycle import tsp_cycl
from .dharmik import dharmik_alp
from .biogas import navin_rashtriy
from .jamin_arogya import aarogya_patrika
from .punyashlok import punyshlok_ahilya
from .jilhaudyog import jilhaudyog
from .sudharitbij import sudharitbij
from .asthivyang_vyakti import asthivyang_vyakti
from .karnbadhir_vyakti import karnbadhir_vyakti
from .divyang_xerox import divyang_xerox
from .divyang_sanganak import divyang_sanganak
from .magas_shilai import magas_shilai
from .dubhte_janawar import dubhte_janawar
from .anusuchit_50takke import anusuchit_50takke
from .anusuchit_janavare import anusuchit_janavare
from .anusuchit_shelya import anusuchit_shelya
from .thakkar import thakkar
from .anusuchit_shabri import anusuchit_shabri
from .bhumihin_daridrya import bhumihin_daridrya
from .samuhik_vivah import samuhik_vivah
from .anusuchit_swechha import anusuchit_swechha
from .divyang_avyang import divyang_avyang
from .divyadivyang_anudan import divyadivyang_anudan
from .swayamrojgar_divyang import swayamrojgar_divyang
from .antarjatiy_vivah import antarjatiy_vivah
from .anusuchit_scholar import anusuchit_scholar
from .adivasividyarthi_engraji import adivasividyarthi_engraji
from .sainikshala_adi import sainikshala_adi
from .eklavya_school import eklavya_school
from .kendra_prashikshan import kendra_prashikshan
from .kendravarti_utpanna import kendravarti_utpanna
from .shaskiy_ashramshala import shaskiy_ashramshala
from .shaskiy_postbasic import shaskiy_postbasic
from .kisan_credit import kisan_credit
from .silk_samagra import silk_samagra
from .shubhmangal_nondni import shubhmangal_nondni
from .rajarshi_shahuscholar import rajarshi_shahuscholar
from .mahatmagandhi_reshim import mahatmagandhi_reshim
from .ekatmik_dugdha import ekatmik_dugdha




admin.site.unregister(Group)

admin.site.site_header = settings.APP_NAME

admin.site.site_title = settings.APP_NAME

admin.site.index_title = settings.APP_NAME
