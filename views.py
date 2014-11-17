from django.http import HttpResponse
from django.shortcuts import render_to_response
from taxi.models import Person

def hello(request):
    return HttpResponse("Hello World")

#def taxi(request):
#    name = Person(name='###', dest='###', date = '2012-02-12', course='6',\
#liv_group='###', email='###', phone='###').name
#    return render_to_response('welcome.html',locals())

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
