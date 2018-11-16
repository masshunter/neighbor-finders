from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'towns/post_list.html', {})
def town_list(request):
    return render(request, 'towns/town_list.html', {})
