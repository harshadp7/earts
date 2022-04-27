import random
import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor.requests import session
from django.db.models import Sum
from .models import login, subadmin, staff, course, student, events, programs, participants, \
    program_committee, judges, performance, judges_assigned, result


# Create your views here.

def landingpage(request):
    return render(request, 'landingpage.html')


def loginload(request):
    return render(request, 'login.html')


def loginpost(request):
    if request.method == "POST":
        uname = request.POST['textfield']
        password = request.POST['textfield2']

        if login.objects.filter(username=uname, password=password).exists():
            a = login.objects.get(username=uname, password=password)
            if a.type == 'Subadmin':
                request.session['lid'] = a.id
                sobj = subadmin.objects.get(LOGIN_id=request.session['lid'])
                return render(request, 'subadmintemplates/subadminhome.html',{'a':sobj})
            elif a.type == 'admin':
                return render(request, 'admintemplates/index.html')
            elif a.type == 'judge':
                request.session['lid'] = a.id
                return judges_homeload(request)
            elif a.type == 'staff':
                request.session['lid'] = a.id
                return procommittee_homeload(request)
            elif a.type == 'student':
                request.session['lid'] = a.id
                da = student.objects.get(LOGIN=a.id)
                request.session["id"] = da.id
                return student_homeload(request)
            else:
                return HttpResponse("INVALID")
        else:
            return HttpResponse("INVALID")
    else:
        return HttpResponse("Invalid")


def changepasswordload(request, id):
    request.session['logid'] = id
    return render(request, 'Change_pass.html')


def changepasswordpost(request):
    logid = request.session['logid']
    print(logid)
    currpassword = request.POST['textfield']
    newpassword = request.POST['textfield1']
    conpassword = request.POST['textfield2']

    obj1 = login.objects.filter(password=currpassword, id=logid)
    if obj1.exists():
        if (conpassword == newpassword):
            loginobj = login.objects.get(id=logid)
            loginobj.password = conpassword
            loginobj.save()
        else:
            return HttpResponse("Entered Password Does'nt Matching")
    else:
        return HttpResponse("Entered Password Does'nt Exist")

    return render(request, 'Change_pass.html')


def admin_addsubadminload(request):
    return render(request, 'admintemplates/admin_add_SubAdmin.html')


def admin_addsubadminpost(request):
    s_adminname = request.POST['textfield']
    s_admingender = request.POST['r1']
    s_adminplace = request.POST['textfield1']
    s_adminpin = request.POST['textfield2']
    s_adminpost = request.POST['textfield3']
    s_admindistrict = request.POST['textfield4']
    s_adminmail = request.POST['textfield5']

    s_adminimg = request.FILES['file']
    fs = FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename = nam + ".jpg"
    print(filename)
    fs.save(filename, s_adminimg)

    url = '/media/' + nam + ".jpg"
    passw=str(random.randint(1111, 666666))
    loginobj = login()
    loginobj.username = s_adminmail
    loginobj.password = passw
    loginobj.type = "Subadmin"
    loginobj.save()

    subadminobj = subadmin()
    subadminobj.subadmin_name = s_adminname
    subadminobj.gender = s_admingender
    subadminobj.place = s_adminplace
    subadminobj.pin = s_adminpin
    subadminobj.post = s_adminpost
    subadminobj.district = s_admindistrict
    subadminobj.image = url
    subadminobj.email = s_adminmail
    subadminobj.LOGIN = loginobj
    subadminobj.save()

    import smtplib
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("eartsproject1@gmail.com", "Earts@123")
    message = "Your Password is " + str(passw)
    s.sendmail("eartsproject1@gmail.com", s_adminmail, message)
    s.quit()

    return HttpResponse("<script>alert('Successfully Added...!');window.history.back()</script>") and admin_addsubadminload(request)



def admin_addstaffload(request):
    return render(request, 'admintemplates/admin_add_staff.html')


def admin_addstaffpost(request):
    staffname = request.POST['textfield']
    staffgender = request.POST['r1']
    staffplace = request.POST['textfield1']
    staffpin = request.POST['textfield2']
    staffpost = request.POST['textfield3']
    staffdistrict = request.POST['textfield4']
    # staffimg=request.FILES['file']
    staffqualification = request.POST['select']
    staffmail = request.POST['textfield5']
    staffdept = request.POST['select2']

    staffimg = request.FILES['file']
    fs = FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename = nam + ".jpg"
    print(filename)
    fs.save(filename, staffimg)

    url = '/media/' + nam + ".jpg"
    passw=str(random.randint(1111, 666666))
    loginobj = login()
    loginobj.username = staffmail
    loginobj.password = passw
    loginobj.type = "staff"
    loginobj.save()

    staffobj = staff()
    staffobj.st_name = staffname
    staffobj.gender = staffgender
    staffobj.place = staffplace
    staffobj.pin = staffpin
    staffobj.district = staffdistrict
    staffobj.image = url
    staffobj.post = staffpost
    staffobj.email = staffmail
    staffobj.qualification = staffqualification
    staffobj.department = staffdept
    staffobj.LOGIN = loginobj
    staffobj.save()

    import smtplib
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("eartsproject1@gmail.com", "Earts@123")
    message = "Your Password is " + str(passw)
    s.sendmail("eartsproject1@gmail.com", staffmail, message)
    s.quit()

    return admin_addstaffload(request)


def admin_addstudentload(request):
    allcourses = course.objects.all()
    return render(request, 'admintemplates/admin_add_Student.html', {'data': allcourses})


def admin_addstudentpost(request):
    studname = request.POST['textfield']
    studgender = request.POST['radiobutton']
    studplace = request.POST['textfield1']
    studpin = request.POST['textfield2']
    studpost = request.POST['textfield3']
    studdistrict = request.POST['textfield4']
    # studimg = request.FILES['file']
    studimg = request.FILES['file']
    fs = FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename = nam + ".jpg"
    print(filename)
    fs.save(filename, studimg)

    url = '/media/' + nam + ".jpg"
    studmail = request.POST['textfield5']
    studcourse = request.POST['select']
    ss=str(random.randint(1111, 666666))
    loginobj = login()
    loginobj.username = studmail
    loginobj.password =ss
    loginobj.type = "student"
    loginobj.save()

    studentobj = student()
    studentobj.student_name = studname
    studentobj.gender = studgender
    studentobj.place = studplace
    studentobj.pin = studpin
    studentobj.post = studpost
    studentobj.district = studdistrict
    studentobj.image = url
    studentobj.email = studmail
    studentobj.COURSE_id = studcourse
    studentobj.LOGIN = loginobj
    studentobj.save()


    import smtplib
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("eartsproject1@gmail.com","Earts@123")
    message="Your Password is "+ str(ss)
    s.sendmail("eartsproject1@gmail.com",studmail,message)
    s.quit()



    return admin_addstudentload(request)


def admin_addeventload(request):
    return render(request, 'admintemplates/admin_add_Event.html')


def admin_addeventpost(request):
    eventname = request.POST['textfield']
    eventdate = request.POST['textfield1']
    eventdisc = request.POST['textfield2']

    eventobj = events()
    eventobj.event_name = eventname
    eventobj.event_date = eventdate
    eventobj.event_discription = eventdisc
    eventobj.save()
    return admin_addeventload(request) and HttpResponse("<script>alert('Event Added...!');</script>")



def admin_viewsubadminload(request):
    if request.method == "POST":
        t = request.POST['textfield']
        allsubadmin = subadmin.objects.filter(subadmin_name__contains=t)
        return render(request, 'admintemplates/admin_view_SubAdmin.html', {'data': allsubadmin})

    allsubadmin = subadmin.objects.all()
    return render(request, 'admintemplates/admin_view_SubAdmin.html', {'data': allsubadmin})


def admin_deletesubadmin(request, id):
    s_adminobj = subadmin.objects.get(id=id)
    s_adminobj.delete()
    return redirect('/earts/admin_viewsubadminload/')


def admin_viewsubadminpost(request):
    searchs_admin = request.POST['textfield']
    return render(request, 'admintemplates/admin_viewSubadmin.html')


def admin_viewstaffload(request):
    if request.method == "POST":
        t = request.POST['textfield']
        allstaff = staff.objects.filter(st_name__contains=t)
        return render(request, 'admintemplates/admin_view_staff.html', {'data': allstaff})
    allstaff = staff.objects.all()
    return render(request, 'admintemplates/admin_view_staff.html', {'data': allstaff})


def admin_deletestaff(request, id):
    destaffobj = staff.objects.get(id=id)
    destaffobj.delete()
    return redirect('/earts/admin_viewstaffload/')


def admin_viewstaffpost(request):
    searchstaff = request.POST['textfield']
    return render(request, 'admintemplates/admin_viewSubadmin.html')


def admin_vieweventsload(request):
    if request.method == "POST":
        t = request.POST['textfield']
        allevents = events.objects.filter(event_name__contains=t)
        return render(request, 'admintemplates/admin_view_Events.html', {'data': allevents})

    allevents = events.objects.all()
    return render(request, 'admintemplates/admin_view_Events.html', {'data': allevents})


def admin_deleteevents(request, id):
    d_eventobj = events.objects.get(id=id)
    d_eventobj.delete()
    return redirect('/earts/admin_vieweventsload/')


def admin_vieweventspost(request):
    searchevents = request.POST['textfield']
    return render(request, 'admintemplates/admin_view_Events.html')


def admin_viewstudentload(request):
    if request.method == "POST":
        t = request.POST['textfield']
        allstudents = student.objects.filter(student_name__contains=t)
        return render(request, 'admintemplates/admin_view_Student.html', {'data': allstudents})
    allstudents = student.objects.all()
    return render(request, 'admintemplates/admin_view_Student.html', {'data': allstudents})


def admin_deletestudent(request, id):
    stdntobj = student.objects.get(id=id)
    stdntobj.delete()
    return redirect('/earts/admin_viewstudentload/')


def admin_viewstudentpost(request):
    searchstudent = request.POST['textfield']
    return render(request, 'admintemplates/admin_viewSubadmin.html')


def admin_viewjudgingpanelload(request):
    return render(request, 'admintemplates/admin_view_JudginPanel.html')


def admin_viewjudgingpanelpost(request):
    searchjpanel1 = request.POST['events']
    searchjpanel2 = request.POST['select']
    return render(request, 'admintemplates/admin_viewSubadmin.html')


def admin_viewcommentsreplyload(request):
    return render(request, 'admintemplates/admin_view_complaints&reply.html')


def admin_viewcommentsreplypost(request):
    viewcomplaint1 = request.POST['events']
    viewcomplaint2 = request.POST['select']
    return render(request, 'admintemplates/admin_viewSubadmin.html')


def admin_viewcommentsratingload(request):
    return render(request, 'admintemplates/admin_view_CommentsRating.html')


def admin_viewcommentsratingpost(request):
    viewcommentsrp1 = request.POST['events']
    viewcommentspr2 = request.POST['select']
    return render(request, 'admintemplates/admin_viewSubadmin.html')


def admin_viewprogramcommitteeload(request):
    eventobj = events.objects.all()

    if request.method == "POST":
        t = request.POST['select2']

        a = program_committee.objects.filter(EVENTS_id=t)
        allevents = events.objects.all()

        return render(request, 'admintemplates/admin_view_program_committee.html', {'prgmcdata': a, 'event': eventobj})

    a = program_committee.objects.all()
    allevents = events.objects.all()

    return render(request, 'admintemplates/admin_view_program_committee.html', {'prgmcdata': a, 'event': eventobj})


def admin_viewprogramcommitteepost(request):
    return render(request, 'admintemplates/admin_viewSubadmin.html')


def admin_editsubadminload(request, id):
    subadminobj = subadmin.objects.get(pk=id)
    return render(request, 'admintemplates/admin_edit_Subadmin.html', {'s': subadminobj})


def admin_editsubadminpost(request):
    s_adminname = request.POST['textfield']
    s_admingender = request.POST['r1']
    s_adminplace = request.POST['textfield1']
    s_adminpin = request.POST['textfield2']
    s_adminpost = request.POST['textfield3']
    s_admindistrict = request.POST['textfield4']
    s_adminmail = request.POST['textfield5']
    sbid = request.POST['sbid']

    subadminobj = subadmin.objects.get(id=sbid)
    if 'file' in request.FILES:
        s_adminimg = request.FILES['file']
        fs = FileSystemStorage()
        nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        filename = nam + ".jpg"
        print(filename)
        fs.save(filename, s_adminimg)
        url = '/media/' + nam + ".jpg"
        subadminobj.image = url
    subadminobj.subadmin_name = s_adminname
    subadminobj.gender = s_admingender
    subadminobj.place = s_adminplace
    subadminobj.pin = s_adminpin
    subadminobj.post = s_adminpost
    subadminobj.district = s_admindistrict
    subadminobj.email = s_adminmail


    subadminobj.save()

    return render(request, 'admintemplates/admin_edit_Subadmin.html') and HttpResponse("<script>alert('Success...!');window.history.go(-2)</script>")


def admin_editstaffload(request, id):
    staffobj = staff.objects.get(pk=id)
    return render(request, 'admintemplates/admin_edit_Staff.html', {'a': staffobj})


def admin_editstaffpost(request):
    staffname = request.POST["textfield"]
    staffgender = request.POST['r1']
    staffplace = request.POST['textfield1']
    staffpin = request.POST['textfield2']
    staffpost = request.POST['textfield3']
    staffdistrict = request.POST['textfield4']
    staffqualification = request.POST['select']
    staffmail = request.POST['textfield5']
    staffdept = request.POST['select2']
    stfid = request.POST['stfid']

    staffobj = staff.objects.get(id=stfid)
    if 'file' in request.FILES:
        studimg = request.FILES['file']
        fs = FileSystemStorage()
        nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        filename = nam + ".jpg"
        print(filename)
        fs.save(filename, staffimg)
        url = '/media/' + nam + ".jpg"
        staffobj.image = url
    staffobj.st_name = staffname
    staffobj.gender = staffgender
    staffobj.place = staffplace
    staffobj.pin = staffpin
    staffobj.post = staffpost
    staffobj.district = staffdistrict
    staffobj.qualification = staffqualification
    staffobj.email = staffmail
    staffobj.department = staffdept
    staffobj.save()

    return render(request, 'admintemplates/admin_edit_staff.html') and HttpResponse("<script>alert('Success...!');window.history.go(-2)</script>")


def admin_editstudentload(request, id):
    studentobj = student.objects.get(pk=id)
    courseobj = course.objects.all()
    return render(request, 'admintemplates/admin_edit_Student.html', {'st': studentobj, 'cr': courseobj})


def admin_editstudentpost(request):
    studname = request.POST['textfield']
    studgender = request.POST['radiobutton']
    studplace = request.POST['textfield1']
    studpin = request.POST['textfield2']
    studpost = request.POST['textfield3']
    studdistrict = request.POST['textfield4']
    studmail = request.POST['textfield5']
    studcourse = request.POST['select']
    stid = request.POST['stid']

    studentobj = student.objects.get(id=stid)
    courseobj = course.objects.get(id=studcourse)
    studentobj.student_name = studname
    studentobj.gender = studgender
    studentobj.place = studplace
    studentobj.post = studpost
    if 'file' in request.FILES:
        studimg = request.FILES['file']
        fs = FileSystemStorage()
        nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        filename = nam + ".jpg"
        print(filename)
        fs.save(filename, studimg)
        url = '/media/' + nam + ".jpg"
        studentobj.image = url
    studentobj.pin = studpin
    studentobj.district = studdistrict
    studentobj.COURSE = courseobj
    studentobj.email = studmail

    studentobj.save()
    return admin_viewstudentload(request) and HttpResponse("<script>alert('Success...!');window.history.go(-2)</script>")


def admin_editeventsload(request, id):
    eventobj = events.objects.get(pk=id)
    return render(request, 'admintemplates/admin_edit_Events.html', {'a': eventobj})


def admin_editeventspost(request):
    eventname = request.POST['textfield']
    eventdate = request.POST['textfield1']
    eventdisc = request.POST['textfield2']
    evid = request.POST['evid']

    eventobj = events.objects.get(id=evid)
    eventobj.event_name = eventname
    eventobj.event_date = eventdate
    eventobj.event_discription = eventdisc
    eventobj.save()
    return render(request, 'admintemplates/admin_edit_Events.html') and HttpResponse("<script>alert('Success...!');window.history.go(-2)</script>")


def admin_editcourseload(request, id):
    courseobj = course.objects.get(pk=id)
    return render(request, 'admintemplates/admin_edit_course.html', {'a': courseobj})


def admin_editcoursepost(request):
    course_name = request.POST['textfield']
    deptartment = request.POST['dept']
    cid = request.POST['cid']

    courseobj = course.objects.get(id=cid)
    courseobj.course_name = course_name
    courseobj.deptartment = deptartment
    courseobj.save()

    return render(request, 'admintemplates/admin_edit_course.html') and HttpResponse("<script>alert('Success...!');window.history.go(-2)</script>")


def admin_sendreplyload(request):
    return render(request, 'admintemplates/admin_send_Reply.html')


def admin_sendreplypost(request):
    reply = request.POST['textarea']
    return render(request, 'admintemplates/admin_send_Reply.html')



def admin_homeload(request):
    return render(request, 'admintemplates/admin_home.html')


def admin_homepost(request):
    return render(request, 'admintemplates/admin_home.html')


def admin_addcourseload(request):
    return render(request, 'admintemplates/admin_add_Course.html')


def admin_addcoursepost(request):
    course_name = request.POST['textfield']
    department = request.POST['dept']

    courseobj = course()
    courseobj.course_name = course_name
    courseobj.department = department
    courseobj.save()

    return admin_addcourseload(request)


def admin_viewcourseload(request):
    if request.method == "POST":
        t = request.POST['textfield']
        allcourses = course.objects.filter(course_name__contains=t)
        return render(request, 'admintemplates/admin_view_Course.html', {'data': allcourses})

    allcourses = course.objects.all()
    return render(request, 'admintemplates/admin_view_Course.html', {'data': allcourses})


def admin_deletecourse(request, id):
    cobj = course.objects.get(id=id)
    cobj.delete()
    return redirect('/earts/admin_viewcourseload/')


def admin_viewcoursepost(request):
    searchcourse = request.POST['textfield']
    return render(request, 'admintemplates/admin_view_Course.html')


def admin_viewjudgesassgnload(request):
    assgnjudegesobj = judges_assigned.objects.all()
    return render(request, 'admintemplates/admin_view_assignedjudges.html',
                  {'data': assgnjudegesobj})




    # subadmin Views#########################################################################


def sadmin_homeload(request):
    sobj = subadmin.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'subadmintemplates/subadminhome.html',{'a':sobj})


def sadmin_homepost(request):
    return render(request, 'subadmintemplates/sadmin_home.html')


def sadmin_addjudgesload(request):
    return render(request, 'subadmintemplates/sadmin_add_judges.html')


def sadmin_addjudgespost(request):
    judgesname = request.POST['textfield']
    judgesgender = request.POST['r1']
    judgesplace = request.POST['textfield1']
    judgespin = request.POST['textfield2']
    judgespost = request.POST['textfield3']
    judgesdistrict = request.POST['textfield4']
    # judgesimg=request.FILES['file']
    judgesimg = request.FILES['file']
    fs = FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    filename = nam + ".jpg"
    print(filename)
    fs.save(filename, judgesimg)

    url = '/media/' + nam + ".jpg"
    judgesemail = request.POST['textfield5']
    passw=str(random.randint(1111, 666666))
    loginobj = login()
    loginobj.username = judgesemail
    loginobj.password = passw
    loginobj.type = "judge"
    loginobj.save()

    judgesobj = judges()
    judgesobj.judge_name = judgesname
    judgesobj.gender = judgesgender
    judgesobj.place = judgesplace
    judgesobj.pin = judgespin
    judgesobj.post = judgespost
    judgesobj.district = judgesdistrict
    judgesobj.image = url
    judgesobj.email = judgesemail
    judgesobj.LOGIN = loginobj
    judgesobj.save()

    import smtplib
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("eartsproject1@gmail.com", "Earts@123")
    message = "Your Password is " + str(passw)
    s.sendmail("eartsproject1@gmail.com", judgesemail, message)
    s.quit()

    return sadmin_addjudgesload(request)


def sadmin_viewjudgesload(request):
    judgesobj = judges.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        alljudges = judges.objects.filter(judge_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_judges.html', {'data': alljudges})

    return render(request, 'subadmintemplates/sadmin_view_judges.html', {'data': judgesobj})


def sadmin_viewjudgespost(request):
    searchjudges = request.POST['textfield']
    return render(request, 'subadmintemplates/sadmin_view_judges.html')


def sadmin_deletejudges(request, id):
    dejudgeobj = judges.objects.get(id=id)
    dejudgeobj.delete()
    return redirect('/earts/sadmin_viewjudgesload/')


def sadmin_editjudgesload(request, id):
    judgeobj = judges.objects.get(pk=id)
    return render(request, 'subadmintemplates/sadmin_edit_judges.html', {'jd': judgeobj})


def sadmin_editjudgespost(request):
    judge_name = request.POST['textfield']
    judge_gender = request.POST['r1']
    judge_place = request.POST['textfield1']
    judge_pin = request.POST['textfield2']
    judge_post = request.POST['textfield3']
    judge_district = request.POST['textfield4']
    judge_mail = request.POST['textfield5']
    jid = request.POST['jid']

    judgeobj = judges.objects.get(id=jid)
    if 'file' in request.FILES:
        judge_img = request.FILES['file']
        fs = FileSystemStorage()
        nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        filename = nam + ".jpg"
        print(filename)
        fs.save(filename, judge_img)
        url = '/media/' + nam + ".jpg"
        judgeobj.image = url
    judgeobj.judge_name = judge_name
    judgeobj.gender = judge_gender
    judgeobj.place = judge_place
    judgeobj.pin = judge_pin
    judgeobj.post = judge_post
    judgeobj.district = judge_district
    judgeobj.email = judge_mail
    judgeobj.save()

    return render(request, 'subadmintemplates/sadmin_edit_judges.html') and HttpResponse("<script>alert('Success...!');window.history.go(-2)</script>")


def sadmin_viewprofileload(request):
    sobj = subadmin.objects.get(LOGIN_id=request.session['lid'])

    return render(request, 'subadmintemplates/sadmin_view_profile.html', {'a': sobj})


def sadmin_addeventload(request):
    return render(request, 'subadmintemplates/sadmin_add_event.html')


def sadmin_addeventpost(request):
    eventname = request.POST['textfield']
    eventdate = request.POST['textfield1']
    eventdisc = request.POST['textfield2']
    eventobj = events()
    eventobj.event_name = eventname
    eventobj.event_date = eventdate
    eventobj.event_discription = eventdisc
    eventobj.save()
    return sadmin_addeventload(request)


def sadmin_vieweventsload(request):
    allevents = events.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        allevents = events.objects.filter(event_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_events.html', {'data': allevents})
    return render(request, 'subadmintemplates/sadmin_view_events.html', {'data': allevents})


def sadmin_deleteevents(request, id):
    d_eventobj = events.objects.get(id=id)
    d_eventobj.delete()
    return redirect('/earts/sadmin_vieweventsload/')


def sadmin_vieweventspost(request):
    searchevents = request.POST['textfield']
    return render(request, 'subadmintemplates/sadmin_view_Events.html')


def sadmin_editeventsload(request, id):
    eventobj = events.objects.get(pk=id)
    return render(request, 'subadmintemplates/sadmin_edit_Events.html', {'a': eventobj})


def sadmin_editeventspost(request):
    eventname = request.POST['textfield']
    eventdate = request.POST['textfield1']
    eventdisc = request.POST['textfield2']
    evid = request.POST['evid']

    eventobj = events.objects.get(id=evid)
    eventobj.event_name = eventname
    eventobj.event_date = eventdate
    eventobj.event_discription = eventdisc
    eventobj.save()
    return render(request, 'subadmintemplates/sadmin_edit_Events.html') and HttpResponse("<script>alert('Success...!');window.history.go(-2)</script>")


def sadmin_addprogramcommitteeload(request):
    staffobj = staff.objects.all()
    eventobj = events.objects.all()
    return render(request, 'subadmintemplates/sadmin_add_programcommittee.html',
                  {'staffdata': staffobj, 'eventdata': eventobj})


def sadmin_addprogramcommitteepost(request):
    staffname = request.POST['select']
    eventname = request.POST['select2']
    prgmcommitteobj = program_committee()
    prgmcommitteobj.STAFF_id = staffname
    prgmcommitteobj.EVENTS_id = eventname
    prgmcommitteobj.created_date = datetime.datetime.now().date()
    prgmcommitteobj.save()

    return sadmin_addprogramcommitteeload(request)


def sadmin_viewprogramcommitteeload(request):
    eventobj = events.objects.all()

    if request.method == "POST":
        t = request.POST['select2']

        a = program_committee.objects.filter(EVENTS_id=t)
        allevents = events.objects.all()

        return render(request, 'subadmintemplates/sadmin_view_programcommittee.html',
                      {'prgmcdata': a, 'event': eventobj})

    a = program_committee.objects.all()
    allevents = events.objects.all()

    return render(request, 'subadmintemplates/sadmin_view_programcommittee.html', {'prgmcdata': a, 'event': eventobj})


def sadmin_viewprogramcommitteepost(request):
    searchprgmcobj = request.POST['textfield']
    return sadmin_viewprogramcommitteepost(request)


def sadmin_deleteprogramcommittee(request, id):
    prgmcommitte = program_committee.objects.get(id=id)
    prgmcommitte.delete()
    return redirect('/earts/sadmin_viewprogramcommitteeload/')


def sadmin_editprogramcommitteeload(request, id):
    prgmcobj = program_committee.objects.get(pk=id)
    staffobj = staff.objects.all()
    eventobj = events.objects.all()
    return render(request, 'subadmintemplates/sadmin_edit_programcommittee.html',
                  {'programcid': prgmcobj, 'staffdata': staffobj, 'eventdata': eventobj})


def sadmin_editprogramcommitteepost(request):
    staffname = request.POST['select']
    eventname = request.POST['select2']
    programcid = request.POST['programcid']

    prgmcobj = program_committee.objects.get(id=programcid)
    staffobj = staff.objects.get(id=staffname)
    eventobj = events.objects.get(id=eventname)
    prgmcobj.STAFF_id = staffobj.id
    prgmcobj.EVENTS_id = eventobj.id
    # prgmcobj.created_date=datetime.datetime.now().date()
    prgmcobj.save()
    return sadmin_viewprogramcommitteeload(request)


# def sadmin_addprogramsload(request):
#     eventobj = events.objects.all()
#     return render(request, 'subadmintemplates/sadmin_add_programs.html', {'eventdata': eventobj})
#
#
# def sadmin_addprogramspost(request):
#     programname = request.POST['text1']
#     programdiscription = request.POST['text2']
#     eventname = request.POST['select1']
#
#     programsobj = programs()
#     programsobj.program_name = programname
#     programsobj.program_discription = programdiscription
#     programsobj.EVENTS_id = eventname
#     programsobj.save()
#
#     return sadmin_addprogramsload(request)


def sadmin_viewprogramsload(request):
    programsobj = programs.objects.all()
    eventobj = events.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        allprograms = programs.objects.filter(program_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_programs.html',
                      {'eventdata': eventobj, 'prgmsdata': allprograms})
    else:
        return render(request, 'subadmintemplates/sadmin_view_programs.html',
                      {'eventdata': eventobj, 'prgmsdata': programsobj})


def sadmin_viewprogramspost(request):
    return render(request, 'subadmintemplates/sadmin_view_programs.html')




def sadmin_viewjudgesassgnload(request):
    assgnjudegesobj = judges_assigned.objects.all()
    if request.method == "POST":
        t = request.POST['textfield']
        assgnjudegesobj = judges_assigned.objects.filter(JUDGES__judge_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_assignedjudges.html', {'data': assgnjudegesobj})
    return render(request, 'subadmintemplates/sadmin_view_assignedjudges.html',{'data': assgnjudegesobj})


def sadmin_viewparticipants(request):
    particobj = participants.objects.all()
    if request.method == "POST":
        t = request.POST['textfield']
        particobj = participants.objects.filter(STUDENT__student_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_participants.html', {'partic': particobj})
    return render(request, 'subadmintemplates/sadmin_view_participants.html', {'partic': particobj})


def sadmin_viewperfomance1(request):
    perfomanceobj = performance.objects.all()
    if request.method == "POST":
        t = request.POST['textfield']
        perfomanceobj = performance.objects.filter(performance_name__contains=t)
        return render(request, 'subadmintemplates/sadmin_view_perfomance.html', {'perfomancedata': perfomanceobj})
    return render(request, 'subadmintemplates/sadmin_view_perfomance.html', {'perfomancedata': perfomanceobj})


def sadmin_viewperfomance2(request, id):
    viewobj = performance.objects.get(id=id)
    return render(request, 'subadmintemplates/sadmin_view_perfomance1.html', {'viewdata': viewobj})


##################### JUDGES VIEW  #################################




def judges_homeload(request):
    jobj = judges.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'judgestemplates/judges_home.html',{'jdata':jobj})


def judges_homepost(request):
    return render(request, 'judgestemplates/judges_home.html')


def judges_viewprogramsload(request):
    programsobj = judges_assigned.objects.filter(JUDGES__LOGIN_id=request.session['lid'])
    if request.method == "POST":
        t = request.POST['textfield']
        alljudges = judges.objects.filter(judge_name__contains=t)
        return render(request, 'judgestemplates/admin_view_SubAdmin.html', {'prgmsdata': alljudges})

    return render(request, 'judgestemplates/judges_view_programs.html', {'prgmsdata': programsobj})


def judges_viewprofileload(request):
    jobj = judges.objects.get(LOGIN_id=request.session['lid'])
    request.session['judgesid'] = jobj.id

    return render(request, 'judgestemplates/judges_view_profile.html', {'a': jobj})


def judges_viewparticipantsload(request, id):
    particobj = participants.objects.filter(PROGRAMS_id=id)
    request.session['progid'] = id
    return render(request, 'judgestemplates/judges_view_participants.html', {'partic': particobj})


def judges_viewperfomanceload(request, id):
    perfomanceobj = performance.objects.get(PARTICIPANTS_id=id)
    request.session['partic'] = id
    return render(request, 'judgestemplates/judges_view_perfomance.html', {'viewdata': perfomanceobj})


def judges_scoreperfomance(request):
    jobj = judges.objects.get(LOGIN_id=request.session['lid'])
    request.session['judgeid'] = jobj.id
    score = request.POST['score']
    perfid = request.POST['perfid']
    particid = request.session['partic']
    progid = request.session['progid']
    judgeid = request.session['judgeid']
    print(judgeid)
    jdid = judges.objects.get(id=judgeid)
    print(jdid.id)

    perfomanceobj = performance.objects.get(id=perfid)

    jdgid=judges_assigned.objects.filter(PROGRAMS_id = progid )
    j1 = jdgid[0].JUDGES_id
    j2 = jdgid[1].JUDGES_id
    j3 = jdgid[2].JUDGES_id
    if j1==jdid.id:
        if perfomanceobj.score1 == "0" and perfomanceobj.judge1_id == j1:
            perfomanceobj.score1 = score
            perfomanceobj.save()
            return HttpResponse("<script>alert('Scored...!');window.history.back()</script>")
        else:
            return HttpResponse("<script>alert('Already Scored');window.history.back()</script>")

    elif j2==jdid.id:
       if perfomanceobj.score2 == "0" and perfomanceobj.judge2_id==j2:
           perfomanceobj.score2 = score
           perfomanceobj.save()
           return HttpResponse("<script>alert('Scored...!');window.history.back()</script>")
       else:
           return HttpResponse("<script>alert('Already Scored');window.history.back()</script>")

    elif j3==jdid.id:
        if perfomanceobj.score3 == "0" and perfomanceobj.judge3_id==j3:
           perfomanceobj.score3 = score
           perfomanceobj.save()
           return HttpResponse("<script>alert('Scored...!');window.history.back()</script>")
        else:
           return HttpResponse("<script>alert('Already Scored');window.history.back()</script>")

def judges_viewresult(request, id):
           perfobj = result.objects.filter(PROGRAMS_id=id)
           if perfobj.exists():
               return render(request, 'judgestemplates/judges_view_result.html', {'data': perfobj})
           else:
               return HttpResponse("<script>alert('No Result Found...!');window.history.back()</script>")
    ###########################################program_committee###########################
    ###########################################program_committee###########################

def procommittee_homeload(request):
    procommobj = program_committee.objects.filter(STAFF__LOGIN_id=request.session['lid'])
    return render(request, 'programcommitteetemplates/procommittee_home1.html', {'proc': procommobj})


def procommittee_homepost(request):
    return render(request, 'programcommitteetemplates/procommittee_home.html')

def procommittee_addprogramsload(request,id):
    request.session['eventid1'] = id
    eventobj = events.objects.get(id=id)
    return render(request,'programcommitteetemplates/procommittee_add_programs.html', {'eventdata': eventobj})


def procommittee_addprogramspost(request):
    programname = request.POST['text1']
    proggramtype = request.POST['radiobutton']
    programdiscription = request.POST['text2']
    eventid =request.session['eventid1']

    programsobj = programs()
    programsobj.program_name = programname
    programsobj.program_type = proggramtype
    programsobj.program_discription = programdiscription
    programsobj.EVENTS_id = eventid
    programsobj.save()

    return procommittee_addprogramsload(request,eventid)

def procommittee_deleteprograms(request, id):
    programsdel = programs.objects.get(id=id)
    programsdel.delete()
    return procommittee_viewprogramsload(request)

def procommittee_viewprogramsload(request,id):
    request.session['eventids'] = id
    request.session['pgmid'] = str(id)
    programsobj = programs.objects.filter(EVENTS_id=id)
    eventobj = events.objects.filter(id=id)
    return render(request, 'programcommitteetemplates/procommitte_view_programs.html',
                  {'eventdata': eventobj, 'prgmsdata': programsobj})

# def procommittee_searchprogramsload(request,id):
#     eventobj = events.objects.filter(id=id)
#     request.session['eventids'] = id
#     request.session['pgmid'] = str(id)
#     programsobj = programs.objects.filter(EVENTS_id=id)
#     if request.method == "POST":
#         t = request.POST['textfield']
#         allprograms = programs.objects.filter(program_name__contains=t)
#         return render(request, 'programcommitteetemplates/procommitte_view_programs.html', {'eventdata':eventobj,'prgmsdata':allprograms})

def procommittee_editprogramsload(request, id):
    prgmsobj = programs.objects.get(pk=id)
    eventobj = events.objects.get(id=request.session['eventids'])
    return render(request, 'programcommitteetemplates/procommittee_edit_programs.html',
                  {'programsid': prgmsobj, 'eventdata': eventobj})


def procommittee_editprogramspost(request):
    programname = request.POST['text1']
    programdiscription = request.POST['text2']
    proggramtype = request.POST['radiobutton']
    programsid = request.POST['programsid']
    eventid = request.session['eventid1']

    prgmsobj = programs.objects.get(id=programsid)
    prgmsobj.program_name = programname
    prgmsobj.program_type = proggramtype
    prgmsobj.program_discription = programdiscription
    prgmsobj.EVENTS_id = eventid
    prgmsobj.save()
    return HttpResponse("<script>alert('Saved..!');</script>")


def procommittee_viewprofileload(request):
    sobj = staff.objects.get(LOGIN_id=request.session['lid'])

    return render(request, 'programcommitteetemplates/procommittee_view_profile.html', {'a': sobj})


def procommittee_viewparticipants(request, id):
    particobj = participants.objects.filter(PROGRAMS_id=id)
    request.session['pgmid'] = str(id)

    return render(request, 'programcommitteetemplates/procommittee_view_participants.html', {'partic': particobj})


def procommittee_approveload(request, id):
    particobj = participants.objects.get(id=id)
    if particobj.status == "approve":
       return HttpResponse("<script>alert('Already Approved..!');window.history.go(-1)</script>")
    else:
        particobj.status = "approve"
        particobj.save()
        return redirect('/earts/procommittee_viewparticipants/' + request.session['pgmid'])


def procommittee_assignjudgesload(request, id):
    judgesobj = judges.objects.all()
    programobj=programs.objects.filter(id=id)
    request.session["selpid"] = id

    return render(request, 'programcommitteetemplates/procommittee_assign_judges.html', {'judgesdata': judgesobj},{'progdata': programobj})


def procommittee_assignjudgespost(request):
    judgename = request.POST["select"]
    programid = request.session["selpid"]
    eventid = request.session['eventids']
    judgeassgnobj = judges_assigned()
    jasgnob=judges_assigned.objects.filter(PROGRAMS_id=programid).count()
    print(jasgnob)
    if jasgnob==3:
       return HttpResponse("<script>alert('Three Judges Already Assigned...!');window.history.back()</script>")
    else:
       judgeassgnobj.JUDGES_id = judgename
       judgeassgnobj.EVENTS_id = eventid
       judgeassgnobj.PROGRAMS_id = programid
       judgeassgnobj.save()
    return HttpResponse("<script>alert('Assigned...!');window.history.back()</script>")


def procommittee_scheduleprogload(request, id):
    request.session['pgmid'] = str(id)
    progobj = programs.objects.get(id=id)
    return render(request, 'programcommitteetemplates/procommittee_schedule_program.html', {'progobj': progobj})


def procommittee_scheduleprogpost(request):
    sdate = request.POST['date']
    stime = request.POST['time']
    progid = request.session['pgmid']

    scheduleobj = schedule()
    scheduleobj.date = sdate
    scheduleobj.time = stime
    scheduleobj.PROGRAM_id = progid
    scheduleobj.save()
    return procommittee_viewprogramsload(request, id=request.session['eventids'])


def procommittee_viewschedulesload(request):
    scheduleobj = schedule.objects.all()
    return render(request, 'programcommitteetemplates/procommittee_view_schedules.html', {'scheduledata': scheduleobj})


def procommittee_viewassignedjudgesload(request):
    assgnjudegesobj = judges_assigned.objects.all()
    return render(request, 'programcommitteetemplates/procommitte_view_assignedjudges.html', {'data': assgnjudegesobj})


def procommittee_deletejudgeassgn(request, id):
    assgnjudegesobj = judges_assigned.objects.get(id=id)
    assgnjudegesobj.delete()
    return redirect('/earts/procommittee_viewassignedjudgesload/')


def procommittee_viewperfomanceload(request,id):
    request.session['pgmid2'] = str(id)
    perfomanceobj = performance.objects.filter(PROGRAMS_id=id)
    sums=0
    ls = []
    for i in perfomanceobj:
        jobj=i.score1
        opj=i.score2
        hy=i.score3
        sums=int(jobj)+int(opj)+int(hy)
        ls.append({"program_name":i.PROGRAMS.program_name,"ss":i.PARTICIPANTS.STUDENT.student_name,"p":i.performance_name,"sc":sums,"id":i.id,"pid":i.PROGRAMS.id})
    return render(request, 'programcommitteetemplates/procommittee_view_perfomance.html',{'perfomancedata': ls})

def procommittee_saveresults(request):
    pgmid1=request.session['pgmid2']
    print(pgmid1)
    perfobj=performance.objects.filter(PROGRAMS_id=pgmid1)

    for i in perfobj:
      sc1=i.score1
      sc2=i.score2
      sc3=i.score3
      print(sc2,sc3,sc1)
      if(int(sc3) and int(sc2) and int(sc1)!=0):
         sum1=int(sc1)+int(sc2)+int(sc3)
         i.totalscore=sum1
         i.save()
      else:
          return HttpResponse("<script>alert('Judges Not Scored..!');window.history.back()</script>")
    return HttpResponse("<script>alert('Saved...!');window.history.back()</script>")

def procommittee_publishresult(request):
    resultobj=result()
    pgmid1=request.session['pgmid2']
    pobj = result.objects.filter(PROGRAMS_id=pgmid1)
    pp=performance.objects.filter(PROGRAMS_id=pgmid1).order_by("-totalscore")[:3]
    scores=pp.
    ids=[]
    pid=[]
    if pp.exists():
       return HttpResponse("<script>alert('Already Published');window.history.back()</script>")
    else :
       for i in pp:
          ids.append(i.PARTICIPANTS.STUDENT.id)
          pid.append(i.PROGRAMS_id)
       id1=ids[0]
       id2=ids[1]
       id3=ids[2]
       id4=pid[0]
       resultobj.result1_id=id1
       resultobj.result2_id=id2
       resultobj.result3_id=id3
       resultobj.PROGRAMS_id=id4
       resultobj.save()
    return HttpResponse("<script>alert('Published..!');window.history.back()</script>")


def procommittee_viewperfomance2(request, id):
    viewobj = performance.objects.get(id=id)
    return render(request, 'programcommitteetemplates/procommittee_view_perfomance2.html', {'viewdata': viewobj})

def procommittee_viewresult(request,id):
    perfobj=result.objects.filter(PROGRAMS_id=id)
    if perfobj.exists():
      return render(request,'programcommitteetemplates/procommittee_view_result.html',{'data':perfobj})
    else :
        return HttpResponse("<script>alert('No Result Found...!');window.history.back()</script>")



#Students/participants

def student_homeload(request):
    sobj = student.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'participants_studentstemplates/student_home.html',{'jdata':sobj})


def student_homepost(request):
    return render(request, 'participants_studentstemplates/student_home.html')


def student_viewprofileload(request):
    sobj = student.objects.get(LOGIN_id=request.session['lid'])
    # p=request.session['lid']


    return render(request, 'participants_studentstemplates/student_view_profile.html', {'a': sobj})


def student_vieweventspost(request):
    searchevents = request.POST['textfield']
    return render(request, 'participants_studentstemplates/student_view_Events.html')


def student_vieweventsload(request):
    allevents = events.objects.all()

    if request.method == "POST":
        t = request.POST['textfield']
        allevents = events.objects.filter(event_name__contains=t)
        return render(request, 'participants_studentstemplates/student_view_Events.html', {'data': allevents})
    return render(request, 'participants_studentstemplates/student_view_Events.html', {'data': allevents})


def student_viewprogramsload(request, id):
    request.session['pgmid'] = str(id)
    programsobj = programs.objects.filter(EVENTS_id=id)
    eventobj = events.objects.all()

    # if request.method == "GET":
    #     t = request.POST['textfield']
    #     allprograms = programs.objects.filter(program_name__contains=t)
    #     return render(request, 'participants_studentstemplates/student_view_programs.html', {'eventdata':eventobj,'prgmsdata':allprograms})
    return render(request, 'participants_studentstemplates/student_view_programs.html',
                  {'eventdata': eventobj, 'prgmsdata': programsobj})


def student_applyprograms(request, id):
    studentid = request.session["id"]
    p1=participants.objects.filter(PROGRAMS_id=id,STUDENT_id=studentid)
    if p1.exists():
        return HttpResponse("<script>alert('Already Applied...!');window.history.go(-1)</script>")
    else:
        participantsobj = participants()
        participantsobj.PROGRAMS_id = id
        participantsobj.STUDENT_id = studentid
        participantsobj.requested_date = datetime.datetime.now().date()
        participantsobj.status = "Pending"
        participantsobj.save()
        return student_viewprogramsload(request, id=request.session['pgmid']) and HttpResponse("<script>alert('Applied...!');window.history.go(-2)</script>")


def student_viewparticipationload(request):
    particpationobj = participants.objects.filter(STUDENT_id=request.session["id"])

    return render(request, 'participants_studentstemplates/student_view_participation.html', {'data': particpationobj})


def student_deleteprticipation(request, id):
    partcipationobj = participants.objects.get(id=id)
    partcipationobj.delete()
    return redirect('/earts/student_viewparticipationload/')


def student_uploadprogramsload(request, id, praticipationid):
    perfomanneobj = performance.objects.filter(PARTICIPANTS_id=praticipationid)
    progobj = programs.objects.get(id=id)

    return render(request, 'participants_studentstemplates/student_upload_program.html',
                  {'progobj': progobj, 'praticipationid': praticipationid, 'perfomanneobj': perfomanneobj})


def student_uploadprogramspost(request):
    perfomancename = request.POST['text1']
    uploadfile = request.FILES['file']
    praticipationid = request.POST["praticipationid"]
    filetype = request.POST["select"]
    progobj = request.POST["progobj"]
    fs = FileSystemStorage()
    nam = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
    if filetype == 'Image':
      filename = nam + ".jpg"
      fs.save(filename, uploadfile)
      url = '/media/' + nam + ".jpg"
    elif filetype == 'Video':
      filename = nam + ".mp4"
      fs.save(filename, uploadfile)
      url = '/media/' + nam + ".mp4"
    else:
      filename = nam + ".mp3"
      fs.save(filename, uploadfile)
      url = '/media/' + nam + ".mp3"
    j1 = 0
    j2 = 0
    j3 = 0
    pp = judges_assigned.objects.filter(PROGRAMS_id=progobj)
    f = 0

    j1 = pp[0].JUDGES_id
    j2 = pp[1].JUDGES_id
    j3 = pp[2].JUDGES_id

    print(j1, j2, j3)

    pobj = performance.objects.filter(PARTICIPANTS_id=praticipationid)
    if pobj.exists():
        return HttpResponse("<script>alert('Already Uploaded');window.history.back()</script>")

    performanceobj = performance()
    performanceobj.PROGRAMS_id = progobj
    performanceobj.PARTICIPANTS_id = praticipationid
    performanceobj.performance_name = perfomancename
    performanceobj.uploaded_files = url
    performanceobj.file_type = filetype
    performanceobj.judge1_id = j1
    performanceobj.judge2_id = j2
    performanceobj.judge3_id = j3
    performanceobj.save()

    return student_uploadprogramsload(request, progobj, praticipationid)



def student_viewperfomanceload(request, id):
    performanceobj = performance.objects.get(id=id)
    return render(request, 'participants_studentstemplates/student_view_perfomance.html',{'viewdata': performanceobj})


def student_deleteperfomance(request, id, progobj, praticipationid):
    perfomanceobj = performance.objects.get(id=id)
    perfomanceobj.delete()
    return student_uploadprogramsload(request, progobj, praticipationid)


def student_viewresult(request, id):
    perfobj = result.objects.filter(PROGRAMS_id=id)
    if perfobj.exists():
        return render(request, 'participants_studentstemplates/student_view_result.html', {'data': perfobj})
    else:
        return HttpResponse("<script>alert('No Result Found...!');window.history.back()</script>")

def publicpageload(request):
    eventobj=events.objects.all()
    return render(request,'audiencetemplates/public.html',{'data': eventobj})

def publicpageload1(request,id):
    progobj=programs.objects.filter(EVENTS_id=id)
    return render(request,'audiencetemplates/public1.html',{'data': progobj})

def publicpageload2(request,id):
    perfobj=performance.objects.filter(PROGRAMS_id=id)
    return render(request,'audiencetemplates/public2.html',{'data':perfobj})
def publicpageload3(request,id):
    perfobj=performance.objects.get(id=id)
    return render(request,'audiencetemplates/public3.html',{'data':perfobj})
def publicpageload4(request,id):
    perfobj=result.objects.filter(PROGRAMS_id=id)
    if perfobj.exists():
      return render(request,'audiencetemplates/public4.html',{'data':perfobj})
    else :
        return HttpResponse("<script>alert('No Result Found...!');window.history.back()</script>")