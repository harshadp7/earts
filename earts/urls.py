
from django.urls import path
from . import views

urlpatterns = [
    path('loginload/', views.loginload),
    path('loginpost/', views.loginpost),
    path('changepasswordload/', views.changepasswordload),
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
    path('sadmin_vieweventspost/',views.admin_vieweventspost),
    path('sadmin_vieweventsload/',views.admin_vieweventsload),
    path('sadmin_addprogramcommitteeload/',views.sadmin_addprogramcommitteeload),
    path('sadmin_addprogramcommitteepost/',views.sadmin_addprogramcommitteepost),
    path('sadmin_viewprogramcommitteepost/',views.sadmin_viewprogramcommitteepost),
    path('sadmin_viewprogramcommitteeload/',views.sadmin_viewprogramcommitteeload),

]