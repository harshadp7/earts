import random
import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor.requests import session

from .models import login,subadmin,staff,course,student,schedule,events,programs,participants,program_committee,judges,performance,judges_assigned,result,complaint,comments_rating
# Create your views here.

def loginload(request):
    return render(request,'login.html')

def loginpost(request):
    if request.method=="POST":
        uname=request.POST['textfield']
        password=request.POST['textfield2']


        if login.objects.filter(username=uname,password=password).exists():
            a=login.objects.get(username=uname,password=password)
            if a.type== 'Subadmin':
                request.session['lid']=a.id
                return render(request,'subadmintemplates/sadmin_home.html')
            elif a.type == 'admin':
                return render(request,'admintemplates/admin_home.html')
            elif a.type == 'judge':
                request.session['lid']=a.id
                return render(request,'judgestemplates/judges_home.html')
            elif a.type == 'staff':
                request.session['lid'] = a.id
                return procommitte_homeload(request)
            elif a.type == 'student':
                da=student.objects.get(LOGIN=a.id)
                request.session["id"]=da.id
                return render(request,'participants_studentstemplates/student_home.html')
            else:
                return HttpResponse("INVALID")
        else:
            return HttpResponse("INVALID")
    else:
        return HttpResponse("Invalid")



def changepasswordload(request):
    return render(request,'Change_pass.html')
def changepasswordpost(request):
    currpassword=request.POST['textfield']
    newpassword=request.POST['textfield1']
    conpassword=request.POST['textfield2']
    return render(request,'Change_pass.html')

def admin_addsubadminload(request):
    return render(request,'admintemplates/admin_add_SubAdmin.html')
def admin_addsubadminpost(request):
    s_adminname=request.POST['textfield']
    s_admingender=request.POST['r1']
    s_adminplace=request.POST['textfield1']
    s_adminpin=request.POST['textfield2']
    s_adminpost=request.POST['textfield3']
    s_admindistrict=request.POST['textfield4']
    s_adminmail=request.POST['textfield5']

    s_adminimg = request.FILES['file']
    fs = FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename = nam + ".jpg"
    print(filename)
    fs.save(filename, s_adminimg)

    url = '/media/' + nam + ".jpg"

    loginobj = login()
    loginobj.username = s_adminmail
    loginobj.password = str(random.randint(1111, 666666))
    loginobj.type = "Subadmin"
    loginobj.save()

    subadminobj=subadmin()
    subadminobj.subadmin_name=s_adminname
    subadminobj.gender=s_admingender
    subadminobj.place=s_adminplace
    subadminobj.pin=s_adminpin
    subadminobj.post=s_adminpost
    subadminobj.district=s_admindistrict
    subadminobj.image=url
    subadminobj.email=s_adminmail
    subadminobj.LOGIN=loginobj
    subadminobj.save()
    return admin_addsubadminload(request)

def admin_addstaffload(request):
    return render(request,'admintemplates/admin_add_staff.html')
def admin_addstaffpost(request):
    staffname=request.POST['textfield']
    staffgender=request.POST['r1']
    staffplace=request.POST['textfield1']
    staffpin=request.POST['textfield2']
    staffpost=request.POST['textfield3']
    staffdistrict=request.POST['textfield4']
    staffimg=request.FILES['file']
    staffqualification=request.POST['select']
    staffmail=request.POST['textfield5']
    staffdept=request.POST['select2']



    loginobj=login()
    loginobj.username=staffmail
    loginobj.password= str(random.randint(1111,666666))
    loginobj.type="staff"
    loginobj.save()

    staffobj=staff()
    staffobj.st_name=staffname
    staffobj.gender=staffgender
    staffobj.place=staffplace
    staffobj.pin=staffpin
    staffobj.district=staffdistrict
    staffobj.image=staffimg
    staffobj.post=staffpost
    staffobj.email=staffmail
    staffobj.qualification=staffqualification
    staffobj.department=staffdept
    staffobj.LOGIN=loginobj
    staffobj.save()

    return admin_addstaffload(request)

def admin_addstudentload(request):
    allcourses=course.objects.all()
    return render(request,'admintemplates/admin_add_Student.html',{'data':allcourses})


def admin_addstudentpost(request):
    studname = request.POST['textfield']
    studgender = request.POST['radiobutton']
    studplace = request.POST['textfield1']
    studpin = request.POST['textfield2']
    studpost = request.POST['textfield3']
    studdistrict = request.POST['textfield4']
    studimg = request.FILES['file']
    studmail = request.POST['textfield5']
    studcourse = request.POST['select']

    loginobj = login()
    loginobj.username = studmail
    loginobj.password = str(random.randint(1111, 666666))
    loginobj.type = "student"
    loginobj.save()

    studentobj=student()
    studentobj.student_name=studname
    studentobj.gender=studgender
    studentobj.place=studplace
    studentobj.pin=studpin
    studentobj.post=studpost
    studentobj.district=studdistrict
    studentobj.image=studimg
    studentobj.email=studmail
    studentobj.COURSE_id=studcourse
    studentobj.LOGIN=loginobj
    studentobj.save()

    return admin_addstudentload(request)


def admin_addeventload(request):
    return render(request,'admintemplates/admin_add_Event.html')
def admin_addeventpost(request):
    eventname=request.POST['textfield']
    eventdate=request.POST['textfield1']
    eventdisc=request.POST['textfield2']

    eventobj=events()
    eventobj.event_name=eventname
    eventobj.event_date=eventdate
    eventobj.event_discription=eventdisc
    eventobj.save()
    return admin_addeventload(request)

def admin_viewsubadminload(request):

    if request.method=="POST":
        t=request.POST['textfield']
        allsubadmin = subadmin.objects.filter(subadmin_name__contains=t)
        return render(request, 'admintemplates/admin_view_SubAdmin.html', {'data': allsubadmin})

    allsubadmin=subadmin.objects.all()
    return render(request,'admintemplates/admin_view_SubAdmin.html',{'data':allsubadmin})

def admin_deletesubadmin(request,id):
    s_adminobj=subadmin.objects.get(id=id)
    s_adminobj.delete()
    return redirect('/earts/admin_viewsubadminload/')







def admin_viewsubadminpost(request):
    searchs_admin=request.POST['textfield']
    return render(request,'admintemplates/admin_viewSubadmin.html')

def admin_viewstaffload(request):

    if request.method=="POST":
        t=request.POST['textfield']
        allstaff = staff.objects.filter(st_name__contains=t)
        return render(request, 'admintemplates/admin_view_staff.html', {'data': allstaff})
    allstaff=staff.objects.all()
    return render(request,'admintemplates/admin_view_staff.html',{'data':allstaff})

def admin_deletestaff(request,id):
    destaffobj=staff.objects.get(id=id)
    destaffobj.delete()
    return redirect('/earts/admin_viewstaffload/')


def admin_viewstaffpost(request):
    searchstaff=request.POST['textfield']
    return render(request,'admintemplates/admin_viewSubadmin.html')

def admin_vieweventsload(request):

    if request.method=="POST":
        t=request.POST['textfield']
        allevents = events.objects.filter(event_name__contains=t)
        return render(request, 'admintemplates/admin_view_Events.html', {'data': allevents})

    allevents=events.objects.all()
    return render(request,'admintemplates/admin_view_Events.html',{'data':allevents})

def admin_deleteevents(request,id):
    d_eventobj=events.objects.get(id=id)
    d_eventobj.delete()
    return redirect('/earts/admin_vieweventsload/')

def admin_vieweventspost(request):
    searchevents=request.POST['textfield']
    return render(request,'admintemplates/admin_view_Events.html')

def admin_viewstudentload(request):
    if request.method == "POST":
        t = request.POST['textfield']
        allstudents = student.objects.filter(student_name__contains=t)
        return render(request, 'admintemplates/admin_view_Student.html', {'data': allstudents})
    allstudents=student.objects.all()
    return render(request,'admintemplates/admin_view_Student.html',{'data':allstudents})

def admin_deletestudent(request,id):
    stdntobj=student.objects.get(id=id)
    stdntobj.delete()
    return redirect('/earts/admin_viewstudentload/')


def admin_viewstudentpost(request):
    searchstudent=request.POST['textfield']
    return render(request,'admintemplates/admin_viewSubadmin.html')

def admin_viewjudgingpanelload(request):
    return render(request,'admintemplates/admin_view_JudginPanel.html')
def admin_viewjudgingpanelpost(request):
    searchjpanel1=request.POST['events']
    searchjpanel2=request.POST['select']
    return render(request,'admintemplates/admin_viewSubadmin.html')

def admin_viewcommentsreplyload(request):
    return render(request,'admintemplates/admin_view_complaints&reply.html')
def admin_viewcommentsreplypost(request):
    viewcomplaint1=request.POST['events']
    viewcomplaint2=request.POST['select']
    return render(request,'admintemplates/admin_viewSubadmin.html')

def admin_viewcommentsratingload(request):
    return render(request,'admintemplates/admin_view_CommentsRating.html')
def admin_viewcommentsratingpost(request):
    viewcommentsrp1=request.POST['events']
    viewcommentspr2=request.POST['select']
    return render(request,'admintemplates/admin_viewSubadmin.html')
def admin_viewprogramcommitteeload(request):
    eventobj = events.objects.all()

    if request.method == "POST":
        t = request.POST['select2']

        a = program_committee.objects.filter(EVENTS_id=t)
        allevents = events.objects.all()

        return render(request, 'admintemplates/admin_view_program_committee.html', {'prgmcdata': a, 'event': eventobj})

    a=program_committee.objects.all()
    allevents=events.objects.all()


    return render(request,'admintemplates/admin_view_program_committee.html',{'prgmcdata':a,'event':eventobj})
def admin_viewprogramcommitteepost(request):
    return render(request,'admintemplates/admin_viewSubadmin.html')

def admin_editsubadminload(request,id):
    subadminobj=subadmin.objects.get(pk=id)
    return render(request,'admintemplates/admin_edit_Subadmin.html',{'s':subadminobj})
def admin_editsubadminpost(request):
    s_adminname=request.POST['textfield']
    s_admingender=request.POST['r1']
    s_adminplace=request.POST['textfield1']
    s_adminpin=request.POST['textfield2']
    s_adminpost=request.POST['textfield3']
    s_admindistrict=request.POST['textfield4']
    s_adminimg=request.POST['file']
    staffmail=request.POST['textfield5']
    sbid=request.POST['sbid']


    subadminobj=subadmin.objects.get(id=sbid)
    if 'file' in request.FILES:
        s_adminimg=request.FILES['file']
        if s_adminimg.filename!='':
            subadminobj.image=s_adminimg.filename

    subadminobj.subadmin_name=s_adminname
    subadminobj.gender=s_admingender
    subadminobj.place=s_adminplace
    subadminobj.pin=s_adminpin
    subadminobj.post=s_adminpost
    subadminobj.district=s_admindistrict

    subadminobj.save()


    return render(request, 'admintemplates/admin_edit_Subadmin.html')

def admin_editstaffload(request,id):
    staffobj=staff.objects.get(pk=id)
    return render(request,'admintemplates/admin_edit_Staff.html',{'a':staffobj})

def admin_editstaffpost(request):

    staffname = request.POST["textfield"]
    staffgender = request.POST['r1']
    staffplace = request.POST['textfield1']
    staffpin = request.POST['textfield2']
    staffpost = request.POST['textfield3']
    staffdistrict = request.POST['textfield4']
   # staffimg = request.FILES['file']
    staffqualification = request.POST['select']
    staffmail = request.POST['textfield5']
    staffdept = request.POST['select2']
    stfid=request.POST['stfid']

    staffobj=staff.objects.get(id=stfid)
    staffobj.st_name=staffname
    staffobj.gender=staffgender
    staffobj.place=staffplace
    staffobj.pin=staffpin
    staffobj.post=staffpost
    staffobj.district=staffdistrict
    staffobj.qualification=staffqualification
    staffobj.email=staffmail
    staffobj.department=staffdept
    staffobj.save()

    return render(request,'admintemplates/admin_edit_staff.html')





def admin_editstudentload(request,id):
    studentobj=student.objects.get(pk=id)
    courseobj=course.objects.all()
    return render(request,'admintemplates/admin_edit_Student.html',{'st':studentobj,'cr':courseobj})
def admin_editstudentpost(request):
    studname = request.POST['textfield']
    studgender = request.POST['radiobutton']
    studplace = request.POST['textfield1']
    studpin = request.POST['textfield2']
    studpost = request.POST['textfield3']
    studdistrict = request.POST['textfield4']
    studimg = request.FILES['file']
    studmail = request.POST['textfield5']
    studcourse = request.POST['select']
    stid=request.POST['stid']


    studentobj=student.objects.get(id=stid)
    courseobj=course.objects.get(id=studcourse)
    studentobj.student_name=studname
    studentobj.gender=studgender
    studentobj.place=studplace
    studentobj.post=studpost
    studentobj.pin=studpin
    studentobj.district=studdistrict
    studentobj.COURSE=courseobj
    studentobj.email=studmail

    studentobj.save()
    return admin_viewstudentload(request)

def admin_editeventsload(request,id):
    eventobj=events.objects.get(pk=id)
    return render(request,'admintemplates/admin_edit_Events.html',{'a':eventobj})
def admin_editeventspost(request):
    eventname = request.POST['textfield']
    eventdate = request.POST['textfield1']
    eventdisc = request.POST['textfield2']
    evid =request.POST['evid']

    eventobj=events.objects.get(id=evid)
    eventobj.event_name=eventname
    eventobj.event_date=eventdate
    eventobj.event_discription=eventdisc
    eventobj.save()
    return render(request,'admintemplates/admin_edit_Events.html')

def admin_editcourseload(request,id):
    courseobj=course.objects.get(pk=id)
    return render(request,'admintemplates/admin_edit_course.html',{'a':courseobj})
def admin_editcoursepost(request):
    course_name = request.POST['textfield']
    deptartment = request.POST['dept']
    cid = request.POST['cid']

    courseobj=course.objects.get(id=cid)
    courseobj.course_name=course_name
    courseobj.deptartment=deptartment
    courseobj.save()

    return render(request,'admintemplates/admin_edit_course.html')

def admin_sendreplyload(request):
    return render(request,'admintemplates/admin_send_Reply.html')
def admin_sendreplypost(request):
    reply=request.POST['textarea']
    return render(request,'admintemplates/admin_send_Reply.html')

def admin_homeload(request):
    return render(request,'admintemplates/admin_home.html')
def admin_homepost(request):
    return render(request,'admintemplates/admin_home.html')

def admin_addcourseload(request):
    return render(request,'admintemplates/admin_add_Course.html')
def admin_addcoursepost(request):
    course_name = request.POST['textfield']
    department = request.POST['dept']

    courseobj=course()
    courseobj.course_name=course_name
    courseobj.department=department
    courseobj.save()

    return admin_addcourseload(request)

def admin_viewcourseload(request):

    if request.method=="POST":
        t=request.POST['textfield']
        allcourses = course.objects.filter(course_name__contains=t)
        return render(request, 'admintemplates/admin_view_Course.html', {'data': allcourses})

    allcourses=course.objects.all()
    return render(request,'admintemplates/admin_view_Course.html',{'data':allcourses})
def admin_deletecourse(request,id):
    cobj=course.objects.get(id=id)
    cobj.delete()
    return redirect('/earts/admin_viewcourseload/')


def admin_viewcoursepost(request):
    searchcourse=request.POST['textfield']
    return render(request,'admintemplates/admin_view_Course.html')

def admin_viewjudgesassgnload(request):
        assgnjudegesobj = judges_assigned.objects.all()
        return render(request, 'admintemplates/admin_view_assignedjudges.html',
                      {'data': assgnjudegesobj})




 # subadmin Views#########################################################################

def sadmin_homeload(request):
    return render(request,'subadmintemplates/sadmin_home.html')
def sadmin_homepost(request):
    return render(request,'subadmintemplates/sadmin_home.html')


def sadmin_addjudgesload(request):
    return render(request,'subadmintemplates/sadmin_add_judges.html')

def sadmin_addjudgespost(request):
    judgesname=request.POST['textfield']
    judgesgender=request.POST['r1']
    judgesplace=request.POST['textfield1']
    judgespin=request.POST['textfield2']
    judgespost=request.POST['textfield3']
    judgesdistrict=request.POST['textfield4']
    judgesimg=request.FILES['file']
    judgesemail=request.POST['textfield5']




    loginobj=login()
    loginobj.username=judgesemail
    loginobj.password="1234"
    loginobj.type="judge"
    loginobj.save()

    judgesobj=judges()
    judgesobj.judge_name=judgesname
    judgesobj.gender=judgesgender
    judgesobj.place=judgesplace
    judgesobj.pin=judgespin
    judgesobj.post=judgespost
    judgesobj.district=judgesdistrict
    judgesobj.image=judgesimg
    judgesobj.email=judgesemail
    judgesobj.LOGIN=loginobj
    judgesobj.save()
    return sadmin_addjudgesload(request)


def sadmin_viewjudgesload(request):
    judgesobj=judges.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        alljudges = judges.objects.filter(judge_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_judges.html', {'data': alljudges})

    return render(request,'subadmintemplates/sadmin_view_judges.html',{'data':judgesobj})
def sadmin_viewjudgespost(request):
    searchjudges=request.POST['textfield']
    return render(request,'subadmintemplates/sadmin_view_judges.html')



def sadmin_deletejudges(request,id):
    dejudgeobj=judges.objects.get(id=id)
    dejudgeobj.delete()
    return redirect('/earts/sadmin_viewjudgesload/')

def sadmin_editjudgesload(request,id):
    judgeobj = judges.objects.get(pk=id)
    return render(request,'subadmintemplates/sadmin_edit_judges.html',{'jd':judgeobj})

def sadmin_editjudgespost(request):
    judge_name= request.POST['textfield']
    judge_gender = request.POST['r1']
    judge_place = request.POST['textfield1']
    judge_pin = request.POST['textfield2']
    judge_post = request.POST['textfield3']
    judge_district = request.POST['textfield4']
    judge_mail = request.POST['textfield5']
    jid = request.POST['jid']

    judgeobj = judges.objects.get(id=jid)
    judgeobj.judge_name= judge_name
    judgeobj.gender = judge_gender
    judgeobj.place = judge_place
    judgeobj.pin = judge_pin
    judgeobj.post = judge_post
    judgeobj.district = judge_district
    judgeobj.email = judge_mail
    judgeobj.save()

    return render(request, 'subadmintemplates/sadmin_edit_judges.html')


def sadmin_viewprofileload(request):

    sobj=subadmin.objects.get(LOGIN_id=request.session['lid'])

    return render(request,'subadmintemplates/sadmin_view_profile.html',{'a':sobj})

def sadmin_addeventload(request):
    return render(request,'subadmintemplates/sadmin_add_event.html')
def sadmin_addeventpost(request):
    eventname=request.POST['textfield']
    eventdate=request.POST['textfield1']
    eventdisc=request.POST['textfield2']
    eventobj=events()
    eventobj.event_name=eventname
    eventobj.event_date=eventdate
    eventobj.event_discription=eventdisc
    eventobj.save()
    return sadmin_addeventload(request)

def sadmin_vieweventsload(request):
    allevents=events.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        allevents = events.objects.filter(event_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_events.html', {'data': allevents})
    return render(request,'subadmintemplates/sadmin_view_events.html',{'data':allevents})

def sadmin_deleteevents(request,id):
    d_eventobj=events.objects.get(id=id)
    d_eventobj.delete()
    return redirect('/earts/sadmin_vieweventsload/')

def sadmin_vieweventspost(request):
    searchevents=request.POST['textfield']
    return render(request,'subadmintemplates/sadmin_view_Events.html')

def sadmin_editeventsload(request,id):
    eventobj=events.objects.get(pk=id)
    return render(request,'subadmintemplates/sadmin_edit_Events.html',{'a':eventobj})
def sadmin_editeventspost(request):
    eventname = request.POST['textfield']
    eventdate = request.POST['textfield1']
    eventdisc = request.POST['textfield2']
    evid =request.POST['evid']

    eventobj=events.objects.get(id=evid)
    eventobj.event_name=eventname
    eventobj.event_date=eventdate
    eventobj.event_discription=eventdisc
    eventobj.save()
    return render(request,'subadmintemplates/sadmin_edit_Events.html')


def sadmin_addprogramcommitteeload(request):
    staffobj=staff.objects.all()
    eventobj=events.objects.all()
    return render(request,'subadmintemplates/sadmin_add_programcommittee.html',{'staffdata':staffobj,'eventdata':eventobj})
def sadmin_addprogramcommitteepost(request):
    staffname=request.POST['select']
    eventname=request.POST['select2']
    prgmcommitteobj=program_committee()
    prgmcommitteobj.STAFF_id=staffname
    prgmcommitteobj.EVENTS_id=eventname
    prgmcommitteobj.created_date=datetime.datetime.now().date()
    prgmcommitteobj.save()

    return sadmin_addprogramcommitteeload(request)

def sadmin_viewprogramcommitteeload(request):
    eventobj = events.objects.all()

    if request.method == "POST":
        t = request.POST['select2']

        a = program_committee.objects.filter(EVENTS_id=t)
        allevents = events.objects.all()

        return render(request, 'subadmintemplates/sadmin_view_programcommittee.html', {'prgmcdata': a, 'event': eventobj})

    a = program_committee.objects.all()
    allevents = events.objects.all()

    return render(request, 'subadmintemplates/sadmin_view_programcommittee.html', {'prgmcdata': a, 'event': eventobj})






def sadmin_viewprogramcommitteepost(request):
    searchprgmcobj=request.POST['textfield']
    return sadmin_viewprogramcommitteepost(request)

def sadmin_deleteprogramcommittee(request,id):



    prgmcommitte=program_committee.objects.get(id=id)
    prgmcommitte.delete()
    return redirect('/earts/sadmin_viewprogramcommitteeload/')


def sadmin_editprogramcommitteeload(request,id):
    prgmcobj = program_committee.objects.get(pk=id)
    staffobj=staff.objects.all()
    eventobj=events.objects.all()
    return render(request,'subadmintemplates/sadmin_edit_programcommittee.html',{'programcid':prgmcobj,'staffdata':staffobj,'eventdata':eventobj})

def sadmin_editprogramcommitteepost(request):
    staffname=request.POST['select']
    eventname=request.POST['select2']
    programcid=request.POST['programcid']

    prgmcobj=program_committee.objects.get(id=programcid)
    staffobj=staff.objects.get(id=staffname)
    eventobj=events.objects.get(id=eventname)
    prgmcobj.STAFF_id=staffobj.id
    prgmcobj.EVENTS_id=eventobj.id
    #prgmcobj.created_date=datetime.datetime.now().date()
    prgmcobj.save()
    return sadmin_viewprogramcommitteeload(request)

def sadmin_addprogramsload(request):
    eventobj = events.objects.all()
    return render(request,'subadmintemplates/sadmin_add_programs.html',{'eventdata':eventobj})

def sadmin_addprogramspost(request):

    programname=request.POST['text1']
    programdiscription=request.POST['text2']
    eventname=request.POST['select1']

    programsobj=programs()
    programsobj.program_name=programname
    programsobj.program_discription=programdiscription
    programsobj.EVENTS_id=eventname
    programsobj.save()



    return sadmin_addprogramsload(request)

def sadmin_viewprogramsload(request):
    programsobj = programs.objects.all()
    eventobj = events.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        allprograms = programs.objects.filter(program_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_programs.html', {'eventdata':eventobj,'prgmsdata': allprograms})
    else:
        return render(request,'subadmintemplates/sadmin_view_programs.html',{'eventdata':eventobj,'prgmsdata':programsobj})

def sadmin_viewprogramspost(request):
    return render(request,'subadmintemplates/sadmin_view_programs.html')

def sadmin_deleteprograms(request,id):
    programsdel=programs.objects.get(id=id)
    programsdel.delete()
    return sadmin_viewprogramsload(request)

def sadmin_editprogramsload(request,id):
    prgmsobj = programs.objects.get(pk=id)
    eventobj=events.objects.all()
    return render(request,'subadmintemplates/sadmin_edit_programs.html',{'programsid':prgmsobj,'eventdata':eventobj})

def sadmin_editprogramspost(request):
    programname = request.POST['text1']
    programdiscription = request.POST['text2']
    eventname = request.POST['select1']
    programsid=request.POST['programsid']

    prgmsobj=programs.objects.get(id=programsid)
    eventobj=events.objects.get(id=eventname)
    prgmsobj.program_name=programname
    prgmsobj.program_discription=programdiscription
    prgmsobj.EVENTS_id=eventobj.id
    prgmsobj.save()
    return sadmin_viewprogramsload(request)

def sadmin_viewjudgesassgnload(request):
        assgnjudegesobj = judges_assigned.objects.all()
        return render(request, 'subadmintemplates/sadmin_view_assignedjudges.html',
                      {'data': assgnjudegesobj})

def sadmin_viewparticipants(request):
    particobj=participants.objects.all()

    return render(request,'subadmintemplates/sadmin_view_participants.html',{'partic':particobj})


##################### JUDGES VIEW  #################################




def judges_homeload(request):
    return render(request,'judgestemplates/judges_home.html')
def judges_homepost(request):
    return render(request,'judgestemplates/judges_home.html')

def judges_viewprogramsload(request):
    programsobj = programs.objects.all()
    eventobj = events.objects.all()

    if request.method=="POST":
        t=request.POST['textfield']
        alljudges = judges.objects.filter(judge_name__contains=t)
        return render(request, 'admintemplates/admin_view_SubAdmin.html', {'eventdata':eventobj,'prgmsdata':alljudges})

    return render(request,'judgestemplates/judges_view_programs.html',{'eventdata':eventobj,'prgmsdata':programsobj})


def judges_viewprofileload(request):

    jobj=judges.objects.get(LOGIN_id=request.session['lid'])

    return render(request,'judgestemplates/judges_view_profile.html',{'a':jobj})

#program_committee

def procommitte_homeload(request):
    procommobj = program_committee.objects.filter(STAFF__LOGIN_id=request.session['lid'])


    return render(request,'programcommitteetemplates/procommittee_home.html',{'proc':procommobj})
def procommittee_homepost(request):
    return render(request,'programcommitteetemplates/procommittee_home.html')

def procommittee_viewprogramsload(request,id):
    request.session['eventids']=id
    request.session['pgmid'] = str(id)
    programsobj = programs.objects.filter(EVENTS_id=id)
    eventobj = events.objects.all()

    # if request.method == "POST":
    #     t = request.POST['textfield']
    #     allprograms = programs.objects.filter(program_name__contains=t)
    #     return render(request, 'programcommitteetemplates/procommitte_view_programs.html', {'eventdata':eventobj,'prgmsdata':allprograms})

    return render(request,'programcommitteetemplates/procommitte_view_programs.html',{'eventdata':eventobj,'prgmsdata':programsobj})

def procommittee_viewprofileload(request):
    sobj=staff.objects.get(LOGIN_id=request.session['lid'])

    return render(request,'programcommitteetemplates/procommittee_view_profile.html',{'a':sobj})
def procommittee_viewparticipants(request,id):
    particobj=participants.objects.filter(PROGRAMS_id=id)
    request.session['pgmid'] = str(id)

    return render(request,'programcommitteetemplates/procommittee_view_participants.html',{'partic':particobj})

def procommittee_approveload(request,id):
    particobj=participants.objects.get(id=id)
    particobj.status="approve"
    particobj.save()
    return redirect('/earts/procommittee_viewparticipants/'+request.session['pgmid'])

def procommittee_assignjudgesload(request,id):
    judgesobj=judges.objects.all()
    request.session["selpid"]=id

    return render(request, 'programcommitteetemplates/procommittee_assign_judges.html', {'judgesdata': judgesobj})

def procommittee_assignjudgespost(request):
    judgename=request.POST["select"]
    programid=request.session["selpid"]
    eventid=request.session['eventids']

    judgeassgnobj=judges_assigned()
    judgeassgnobj.JUDGES_id = judgename
    judgeassgnobj.EVENTS_id = eventid
    judgeassgnobj.PROGRAMS_id=programid
    judgeassgnobj.save()
    return procommittee_viewprogramsload(request,id=request.session['eventids'])

def procommittee_scheduleprogload(request,id):
    request.session['pgmid'] = str(id)
    progobj=programs.objects.get(id=id)
    return render(request,'programcommitteetemplates/procommittee_schedule_program.html',{'progobj':progobj})

def procommittee_scheduleprogpost(request):
    sdate=request.POST['date']
    stime=request.POST['time']
    progid=request.session['pgmid']

    scheduleobj=schedule()
    scheduleobj.date=sdate
    scheduleobj.time=stime
    scheduleobj.PROGRAM_id=progid
    scheduleobj.save()
    return procommittee_viewprogramsload(request,id=request.session['eventids'])

def procommittee_viewschedulesload(request):
    scheduleobj=schedule.objects.all()
    return render(request,'programcommitteetemplates/procommittee_view_schedules.html',{'scheduledata':scheduleobj})

def procommittee_viewassignedjudgesload(request):
    assgnjudegesobj=judges_assigned.objects.all()
    return render(request,'programcommitteetemplates/procommitte_view_assignedjudges.html',{'data':assgnjudegesobj})

def procommittee_deletejudgeassgn(request,id):
    assgnjudegesobj = judges_assigned.objects.get(id=id)
    assgnjudegesobj.delete()
    return redirect('/earts/procommittee_viewassignedjudgesload/')



#Students/participants

def student_homeload(request):

    return render(request,'participants_studentstemplates/student_home.html')
def student_homepost(request):
    return render(request,'participants_studentstemplates/student_home.html')

def student_vieweventspost(request):
    searchevents=request.POST['textfield']
    return render(request,'participants_studentstemplates/student_view_Events.html')

def student_vieweventsload(request):
    allevents=events.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        allevents = events.objects.filter(event_name__contains=t)
        return render(request, 'participants_studentstemplates/student_view_Events.html', {'data': allevents})
    return render(request,'participants_studentstemplates/student_view_Events.html',{'data':allevents})

def student_viewprogramsload(request,id):
    request.session['pgmid'] = str(id)
    programsobj = programs.objects.filter(EVENTS_id=id)
    eventobj = events.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        allprograms = programs.objects.filter(program_name__contains=t)
        return render(request, 'participants_studentstemplates/student_view_programs.html', {'eventdata':eventobj,'prgmsdata':allprograms})
    return render(request,'participants_studentstemplates/student_view_programs.html',{'eventdata':eventobj,'prgmsdata':programsobj})

def student_applyprograms(request,id):
    studentid=request.session["id"]
    participantsobj=participants()
    participantsobj.PROGRAMS_id=id
    participantsobj.STUDENT_id=studentid
    participantsobj.requested_date=datetime.datetime.now().date()
    participantsobj.status="Pending"
    participantsobj.save()
    return student_viewprogramsload(request,id=request.session['pgmid'])

def student_viewparticipationload(request):
    particpationobj=participants.objects.filter(STUDENT_id=request.session["id"])

    return render(request,'participants_studentstemplates/student_view_participation.html',{'data':particpationobj})

def student_deleteprticipation(request,id):
        partcipationobj = participants.objects.get(id=id)
        partcipationobj.delete()
        return redirect('/earts/student_viewparticipationload/')

def student_uploadprogramsload(request,id):
    progobj = programs.objects.get(id=id)

    return render(request,'participants_studentstemplates/student_upload_program.html',{'progobj':progobj})

def student_uploadprogramspost(request):
    prgmid=request.session['pgmid']
    perfomancename=request.POST['text1']
    uploadfile=request.FILES['file']
    fs = FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename = nam + ".jpg"
    print(filename)
    fs.save(filename, uploadfile)

    url = '/media/' + nam + ".jpg"

    performanceobj=performance()
    performanceobj.PROGRAMS_id=prgmid
    performanceobj.performance_name=perfomancename
    performanceobj.url
    performanceobj.save()

    return render(request,'participants_studentstemplates/student_upload_program.html')