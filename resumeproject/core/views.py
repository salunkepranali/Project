from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'home' : 'active'}
    return render(request,'home.html', context)

def contact(request):
    context = {'contact' : 'active'}
    return render(request,'contact.html', context)