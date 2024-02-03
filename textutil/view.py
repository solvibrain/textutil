#This file is created by Rupesh 
# import imp
import string
from django.http import HttpResponse
from django.shortcuts import render



def index2(request):
    return render(request,'index2.html') 
def index(request):
    return render(request ,'index.html')
def Analyze(request):
    djtext=request.POST.get('text','default')
    removpunc   = request.POST.get('removepunc','default')
    fullcap = request.POST.get('full_capitalize','default')
    extraspace=request.POST.get('extraspaceremover','off')
    
    if removpunc=='on':
        punctuation='''' !@#$%^&*()_+.,/';:"><'''
        Analyse=''
        for char in djtext:
            if char not in punctuation:
                Analyse=Analyse +char
        params={'purpose':'remove punc','Analysed_text':Analyse}
        djtext=Analyse

        # return render(request,'Analyze.html',params)    
       
    if (fullcap =="on"):
        Analyse=''
        for char in djtext:
            Analyse = Analyse+char.upper()
        params={'purpose':'full capatalize','Analysed_text':Analyse}
        return render(request,'Analyze.html',params)
    
    
    elif (extraspace=='on'):
        Analyse=''
        for index,char in djtext:    
            if not(djtext[index]==''  and djtext[index+1]==''):
                Analyse=Analyse+char
        params={'purpose':'extraspaceremover','Analyseed_text':Analyse}
        return render(request,'Analyze.html',params)
    
    
    
    else:
        return HttpResponse("you have not given any purpose")
        