from django.shortcuts import render, redirect

def enter(request):
    if request.user.is_authenticated:
        return redirect("main")
    else:
        return redirect("register", mode='registr')
    

