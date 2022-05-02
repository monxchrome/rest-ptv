from django.shortcuts import render, HttpResponse


def main_page(request):
    return render(request, 'index.html')
