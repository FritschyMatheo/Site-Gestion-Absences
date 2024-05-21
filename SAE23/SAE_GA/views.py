from django.shortcuts import render


def index(request):
    return render(request, "SAE_GA/index.html")