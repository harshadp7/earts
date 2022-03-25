from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

    class Meta:
        db_table = 'login'

class subadmin(models.Model):
    subadmin_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subadmin'

class staff(models.Model):
    st_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    image=models.CharField(max_length=200)
    qualification=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(login, on_delete=models.CASCADE)

    class Meta:
        db_table = 'staff'


class course(models.Model):
    course_name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)

    class Meta:
        db_table = 'course'

class student(models.Model):
    student_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    image=models.CharField(max_length=200)
    email=models.CharField(max_length=50)
    COURSE=models.ForeignKey(course, on_delete=models.CASCADE)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)

    class Meta:
        db_table = 'student'

class events(models.Model):
    event_name=models.CharField(max_length=50)
    event_date=models.CharField(max_length=50)
    event_discription=models.CharField(max_length=50)

    class Meta:
        db_table = 'events'

class programs(models.Model):
    program_name=models.CharField(max_length=50)
    EVENTS=models.ForeignKey(events, on_delete=models.CASCADE)
    program_discription=models.CharField(max_length=50)


    class Meta:
        db_table = 'programs'

class participants(models.Model):
    STUDENT=models.ForeignKey(student, on_delete=models.CASCADE)
    PROGRAMS=models.ForeignKey(programs, on_delete=models.CASCADE)
    requested_date=models.CharField(max_length=50)
    status=models.CharField(max_length=50)

    class Meta:
        db_table = 'participants'

class program_committee(models.Model):
    STAFF = models.ForeignKey(staff, on_delete=models.CASCADE)
    EVENTS = models.ForeignKey(events, on_delete=models.CASCADE)
    created_date = models.CharField(max_length=50)

    class Meta:
        db_table = 'program_committee'



class judges(models.Model):
    judge_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    image=models.CharField(max_length=200)
    email=models.CharField(max_length=50)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)

    class Meta:
        db_table = 'judges'

class performance(models.Model):
    performance_name=models.CharField(max_length=50)
    PARTICIPANTS= models.ForeignKey(participants, on_delete=models.CASCADE)
    PROGRAMS= models.ForeignKey(programs, on_delete=models.CASCADE)
    uploaded_files=models.CharField(max_length=500)
    score1=models.CharField(max_length=10,default="0")
    score2=models.CharField(max_length=10,default="0")
    score3=models.CharField(max_length=10,default="0")
    judge1=models.ForeignKey(judges,on_delete=models.CASCADE,related_name="j3")
    judge2=models.ForeignKey(judges,on_delete=models.CASCADE,related_name="j2")
    judge3=models.ForeignKey(judges,on_delete=models.CASCADE,related_name="j1")


    class Meta:
        db_table = 'performance'

class schedule(models.Model):
    PROGRAM = models.ForeignKey(programs, on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)

    class Meta:
        db_table = 'schedule'

class result(models.Model):
    PROGRAMS = models.ForeignKey(programs, on_delete=models.CASCADE)
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    result1=models.CharField(max_length=50)
    result2=models.CharField(max_length=50)
    result3=models.CharField(max_length=50)

    class Meta:
        db_table = 'result'

class judges_assigned(models.Model):
    JUDGES = models.ForeignKey(judges, on_delete=models.CASCADE)
    PROGRAMS = models.ForeignKey(programs, on_delete=models.CASCADE)
    EVENTS = models.ForeignKey(events, on_delete=models.CASCADE)

    class Meta:
        db_table = 'judges_assigned'

class complaint(models.Model):
    complaint=models.CharField(max_length=50)
    reply=models.CharField(max_length=50)
    JUDGES = models.ForeignKey(judges, on_delete=models.CASCADE)
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE,default=1)

    class Meta:
        db_table = 'complaint'

class comments_rating(models.Model):
    comments=models.CharField(max_length=200)
    rating=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE,default=1)
    class Meta:
        db_table = 'comments_rating'
