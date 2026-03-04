from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'board/home.html')

def about_view(request):
    return render(request, 'board/about.html')

def notices_view(request):
    return render(request, 'board/notices.html')
