from django.shortcuts import render, redirect
from django.http import HttpResponse

def index1(request):
    return redirect('bank/')