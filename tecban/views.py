from django.shortcuts import render

def post_list(request):
    return render(request, 'tecban/post_list.html', {})