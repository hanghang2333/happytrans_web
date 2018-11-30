from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
import codecs,random
import happytrans.translate_model as ht
model = ht.Model()

filename = 'xhj.happy'
sentences = codecs.open(filename,'r','utf8').readlines()
sentences = [i.replace('\n','') for i in sentences]
sentences = [i for i in sentences if len(i)>5]
s_num = len(sentences)-1
output = codecs.open('log','a','utf8')
'''
def index(request):
    #return HttpResponse('helloworld')
    return render(request,'home.html')
'''
def receive_data(request):
    if request.GET:
        #print('有提交')
        pass
    s1 = request.GET.get('putonghua',None)
    s2 = request.GET.get('fangyan',None)
    #print('s1&s2:',s1,s2)
    #print(request.GET)
    if request.GET.get('fanyi') != None:
        s2 = model.convert(s1)
        return render(request,'home.html',{'string1':s1,'string2':s2})
    elif request.GET.get('tijiao')!=None:
        output.write('<>'+s1+'<+>'+s2+'<>'+'\n')
        output.flush()
        return render(request,'home.html',{'string1':s1,'string2':s2})
    else:
        idx = int(random.random()*s_num)
        s1 = sentences[idx]
        s2 = model.convert(s1)        
        return render(request,'home.html',{'string1':s1,'string2':s2})
def home(request):
    idx = int(random.random()*s_num)
    string1 = sentences[idx]
    string2 = model.convert(string1)
    return render(request,'home.html',{'string1':string1,'string2':string2})
    #tutorialList = ["HTML","CSS","JQUERY"]
    #return render(request,'home.html',{'tutorialList':tutorialList})
'''
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))
def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(reverse('add2',args={a,b}))
'''