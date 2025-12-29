from django.shortcuts import render

def home(request):
    return render(request, "research/home.html")

def reasoning_list(request):
    return render(request, "research/reasoning_list.html")
