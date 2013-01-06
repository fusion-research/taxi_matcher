from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Person
from django.core.context_processors import csrf
from copy import copy as copy_object

def taxi(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('welcome.html',c)

def search(request):
    count = 0
    error = False
    match = False
    submit = False  
    if 'name' in request.POST:
        name = request.POST['name']
        dest = request.POST['dest']
        date = request.POST['date']
        time1 = int(request.POST['time1'].split(':')[0])*100 + int(request.POST['time1'].split(':')[1])
        time2 = int(request.POST['time2'].split(':')[0])*100 + int(request.POST['time2'].split(':')[1])
        course = request.POST['course']
        liv_group = request.POST['liv_group']
        email = request.POST['email']
        phone = request.POST['phone']
        if not name:
            error = True
        else:
            submit = True
            p = Person.objects.filter(date=date,dest=dest) 
            obj = []
            times = []
            if not (p == []):
                for i in p:
                    if (time1 < int(i.time1) and int(i.time1) < time2) or (time1 > int(i.time1) and time1 < int(i.time2)):
                        obj.append(i)
                        count += 1
            if (count > 0):
                match = True
            Person.objects.create(name=name,dest=dest, date=date, course=course,\
time1=time1, time2=time2, liv_group=liv_group, email=email, phone=phone)
            return render_to_response('welcome.html',{'name':name, 'match':match, \
'submit':submit, 'd':obj, 'count':count})
    return render_to_response('welcome.html',{'error':error})
