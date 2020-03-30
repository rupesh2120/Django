from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    params = {'name': 'harry', 'place':'Earth'}
    return render(request,'index.html',params)
def analyze(request):
    dj = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    cap = request.GET.get('cap','off')
    coun = request.GET.get('coun','off')
    if (removepunc == "on"):
        analyze= ""
        abc=''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
        for char in dj:
                if char not in abc:
                    analyze = analyze + char
        params = {'purpose': 'remove punc', 'analyzed_text':analyze}
        return render(request,'analyze.html',params)
    elif(cap=="on"):
        analyze= ""
        for char in dj:
            analyze = analyze + char.upper()
        params = {'purpose': 'Cap All', 'analyzed_text':analyze}
        return render(request,'analyze.html',params)
    elif(coun=="on"):
        analyze= ""
        count=0
        for char in dj:
            if not(char == " " and char == "\n"):
                count=count+1
        params = {'purpose': 'count All', 'analyzed_text':'No of char are '+str(count)}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("error")
