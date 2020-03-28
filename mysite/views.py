from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
       # return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
      #  return render(request, 'analyze.html', params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n"and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Removed New Line', 'analyzed_text':analyzed}
       # return render(request, 'analyze.html', params)
    
    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Removed Extra Space', 'analyzed_text':analyzed}
       # return render(request, 'analyze.html', params)
       
    if(removepunc != "on" and fullcaps !="on" and newlineremover != "on" and extraspaceremover != "on"):
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)



















'''def capfirst(request):
    return HttpResponse("cap first")

def newlineremove(request):
    return HttpResponse("newline remove")

def spaceremove(request):
    return HttpResponse("spaceremove")

def charcount(request):
    return HttpResponse("charcount")'''