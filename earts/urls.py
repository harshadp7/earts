
from django.urls import path

from . import views

urlpatterns = [
    path('landingpage/', views.landingpage),
    path('loginload/', views.loginload),
    path('loginpost/', views.loginpost),
    path('changepasswordload/<str:id>', views.changepasswordload),
    path('changepasswordpost/', views.changepasswordpost),
    path('admin_addsubadminload/', views.admin_addsubadminload),
    path('admin_addsubadminpost/', views.admin_addsubadminpost),
    path('admin_addstaffload/', views.admin_addstaffload),
    path('admin_addstaffpost/', views.admin_addstaffpost),
    path('admin_addeventload/', views.admin_addeventload),
    path('admin_addeventpost/', views.admin_addeventpost),
    path('admin_addstudentload/', views.admin_addstudentload),
    path('admin_addstudentpost/', views.admin_addstudentpost),
    path('admin_addeventload/', views.admin_addeventload),
    path('admin_addeventpost/', views.admin_addeventpost),
    path('admin_addcourseload/', views.admin_addcourseload),
    path('admin_addcoursepost/', views.admin_addcoursepost),
    path('admin_viewsubadminload/', views.admin_viewsubadminload),
    path('admin_viewsubadminpost/', views.admin_viewsubadminpost),
    path('admin_deletesubadmin/<id>', views.admin_deletesubadmin),
    path('admin_viewstaffload/', views.admin_viewstaffload),
    path('admin_viewstaffpost/', views.admin_viewstaffpost),
    path('admin_deletestaff/<id>', views.admin_deletestaff),
    path('admin_vieweventsload/', views.admin_vieweventsload),
    path('admin_vieweventspost/', views.admin_vieweventspost),
    path('admin_deleteevents/<id>', views.admin_deleteevents),
    path('admin_viewstudentload/', views.admin_viewstudentload),
    path('admin_viewstudentpost/', views.admin_viewstudentpost),
    path('admin_deletestudent/<id>', views.admin_deletestudent),
    path('admin_viewcourseload/', views.admin_viewcourseload),
    path('admin_deletecourse/<id>', views.admin_deletecourse),
    path('admin_viewcoursepost/', views.admin_viewcoursepost),
    path('admin_viewjudginpanelload/', views.admin_viewjudgingpanelload),
    path('admin_viewjudginpanelpost/', views.admin_viewjudgingpanelpost),
    path('admin_viewcommentsreplyload/', views.admin_viewcommentsreplyload),
    path('admin_viewcommentsreplypost/', views.admin_viewcommentsreplypost),
    path('admin_viewcommentsratingload/', views.admin_viewcommentsratingload),
    path('admin_viewcommentsratingpost/', views.admin_viewcommentsratingpost),
    path('admin_viewprogramcommitteeload/', views.admin_viewprogramcommitteeload),
    path('admin_viewprogramcommitteepost/', views.admin_viewprogramcommitteepost),
    path('admin_viewjudgesassgnload/', views.admin_viewjudgesassgnload),
    path('admin_editsubadminload/<str:id>', views.admin_editsubadminload),
    path('admin_editsubadminpost/', views.admin_editsubadminpost),
    path('admin_editstaffload/<str:id>', views.admin_editstaffload),
    path('admin_editstaffpost/', views.admin_editstaffpost),
    path('admin_editstudentload/<str:id>', views.admin_editstudentload),
    path('admin_editstudentpost/', views.admin_editstudentpost),
    path('admin_editeventsload/<str:id>', views.admin_editeventsload),
    path('admin_editeventspost/', views.admin_editeventspost),
    path('admin_editcourseload/<str:id>', views.admin_editcourseload),
    path('admin_editcoursepost/', views.admin_editcoursepost),
    path('admin_sendreplyload/', views.admin_sendreplyload),
    path('admin_sendreplypost/', views.admin_sendreplypost),
    path('admin_home/', views.admin_homeload),

    #subadmin path:
    path('sadmin_home/', views.sadmin_homeload),
    path('sadmin_addjudgesload/',views.sadmin_addjudgesload),
    path('sadmin_addjudgespost/',views.sadmin_addjudgespost),
    path('sadmin_viewprofileload/',views.sadmin_viewprofileload),
    path('sadmin_addeventload/',views.sadmin_addeventload),
    path('sadmin_addeventpost/',views.sadmin_addeventpost),
    path('sadmin_viewjudgesload/',views.sadmin_viewjudgesload),
    path('sadmin_viewjudgespost/',views.sadmin_viewjudgespost),
    path('sadmin_editjudgesload/<str:id>',views.sadmin_editjudgesload),
    path('sadmin_editjudgespost/',views.sadmin_editjudgespost),
    path('sadmin_vieweventspost/',views.sadmin_vieweventspost),
    path('sadmin_vieweventsload/',views.sadmin_vieweventsload),
    path('sadmin_editeventsload/<str:id>',views.sadmin_editeventsload),
    path('sadmin_editeventspost/<str:id>',views.sadmin_editeventspost),
    path('sadmin_addprogramsload/',views.sadmin_addprogramsload),
    path('sadmin_addprogramspost/',views.sadmin_addprogramspost),
    path('sadmin_viewprogramspost/',views.sadmin_viewprogramspost),
    path('sadmin_viewprogramsload/',views.sadmin_viewprogramsload),
    path('sadmin_addprogramcommitteeload/',views.sadmin_addprogramcommitteeload),
    path('sadmin_addprogramcommitteepost/',views.sadmin_addprogramcommitteepost),
    path('sadmin_viewprogramcommitteepost/',views.sadmin_viewprogramcommitteepost),
    path('sadmin_viewprogramcommitteeload/',views.sadmin_viewprogramcommitteeload),
    path('sadmin_editprogramcommitteeload/<str:id>',views.sadmin_editprogramcommitteeload),
    path('sadmin_viewjudgesassgnload/',views.sadmin_viewjudgesassgnload),
    path('sadmin_viewparticipants/',views.sadmin_viewparticipants),
    path('sadmin_viewperfomance1/',views.sadmin_viewperfomance1),
    path('sadmin_viewperfomance2/<str:id>',views.sadmin_viewperfomance2),
    path('sadmin_editprogramsload/<str:id>',views.sadmin_editprogramsload),
    path('sadmin_editprogramspost/',views.sadmin_editprogramspost),
    path('sadmin_deleteprogramcommittee/<id>', views.sadmin_deleteprogramcommittee),
    path('sadmin_deleteprograms/<id>', views.sadmin_deleteprograms),

#judges path :
    path('judges_home/', views.judges_homeload),
    path('judges_viewprofileload/',views.judges_viewprofileload),
    path('judges_viewprogramsload/',views.judges_viewprogramsload),
    path('judges_viewparticipantsload/<str:id>',views.judges_viewparticipantsload),
    path('judges_viewperfomanceload/<str:id>',views.judges_viewperfomanceload),
    path('judges_scoreperfomance/',views.judges_scoreperfomance),


#programcommitte path:
    path('procommittee_homeload/', views.procommitte_homeload),
    path('procommittee_viewprofileload/', views.procommittee_viewprofileload),
    path('procommittee_viewprogramsload/<str:id>',views.procommittee_viewprogramsload),
    path('procommittee_viewparticipants/<str:id>',views.procommittee_viewparticipants),
    path('procommittee_viewperfomanceload/<str:id>', views.procommittee_viewperfomanceload),
    path('procommittee_viewperfomance2/<str:id>', views.procommittee_viewperfomance2),
    path('procommittee_approveload/<str:id>',views.procommittee_approveload),
    path('procommittee_assignjudgesload/<str:id>',views.procommittee_assignjudgesload),
    path('procommittee_assignjudgespost/',views.procommittee_assignjudgespost),
    path('procommittee_scheduleprogload/<str:id>',views.procommittee_scheduleprogload),
    path('procommittee_scheduleprogpost/',views.procommittee_scheduleprogpost),
    path('procommittee_viewschedulesload/',views.procommittee_viewschedulesload),
    path('procommittee_viewassignedjudgesload/',views.procommittee_viewassignedjudgesload),
    path('procommittee_deletejudgeassgn/<str:id>',views.procommittee_deletejudgeassgn),
    path('procommittee_saveresults/',views.procommittee_saveresults),
    path('procommittee_publishresult/',views.procommittee_publishresult),



#participants_student path:
    path('student_homeload/',views.student_homeload),
    path('student_viewprofileload/',views.student_viewprofileload),
    path('student_viewprogramsload/<str:id>',views.student_viewprogramsload),
    path('student_vieweventsload/',views.student_vieweventsload),
    path('student_vieweventspost/<str:id>',views.student_vieweventspost),
    path('student_applyprograms/<str:id>',views.student_applyprograms),
    path('student_viewparticipationload/',views.student_viewparticipationload),
    path('student_deleteprticipation/<str:id>',views.student_deleteprticipation),
    path('student_uploadprogramsload/<str:id>/<praticipationid>',views.student_uploadprogramsload),
    path('student_uploadprogramspost/',views.student_uploadprogramspost),
    path('student_deleteperfomance/<str:id>/<progobj>/<praticipationid>',views.student_deleteperfomance),
    path('student_viewperfomanceload/<str:id>',views.student_viewperfomanceload),


]