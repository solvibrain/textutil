from django.http import HttpResponse


#def content1(request):
 #  return HttpResponse("This website is going to provide you a lot of content , you must visit on this website \n \t consistently to connect with us to gain a interesting document .")

def Navigator(request):
    return HttpResponse(''' <a href=path('',content.newlineremover,name='newlineremover') > Newlinw remover </a>''')    
def newlineremover(request):
    return HttpResponse("newlineremover")
    #  to add a back button we can use <a href='/'>back</a>