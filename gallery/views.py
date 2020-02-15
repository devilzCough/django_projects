from django.shortcuts import render

def post_list(request):
    return render(request, 'gallery/post_list.html', {})
