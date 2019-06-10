from django.shortcuts import render
from django.views.generic. base import TemplateView
# Create your views here.
class MainpageView(TemplateView):
    template_name = 'WordCount/main.html'

def home(request):
    return render(request,'WordCount/home.html') 
    #render(request, 선,딕셔너리)

def about(request):
    return render(request, 'WordCount/about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        #increase
        if word in word_dictionary:
            word_dictionary[word] += 1
        #add to dictionary
        else:
            word_dictionary[word]=1
    return render(request, 'WordCount/result.html', {'full':text, 'total' : len(words),'dictionary' : word_dictionary.items()})

    # 딕셔너리 {'key': value}