from django.shortcuts import render

posts = [
    {
        'author': 'Jo F Kwakye',
        'title': 'Post 1',
        'content': 'This is the first post'
    },
    {
        'author': 'Max Kwakye',
        'title': 'Post 2',
        'content': 'This is the second post'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')