from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'yae/home.html', { 'title': "Home" })

def docs(request):
    return render(request, 'yae/docs.html', { 'title': 'Documentation' })

def dash(request):
    return render(request, 'yae/dash.html', { 'title': 'Dashboard'})

def signup(request):
    return render(request, 'yae/signup.html', { 'title': 'Register'})
