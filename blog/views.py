from django.shortcuts import render

# Create your views here.
def post_list(request):
    sai="Hello"
    return render(request, 'blog/post_list.html', {'tex':sai})
