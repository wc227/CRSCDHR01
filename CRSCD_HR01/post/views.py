from django.shortcuts import render


# Create your views here.
def post_view(request):
    post_id = request.GET.getlist('postID')

    return render(request, 'index.html', {'post_id': post_id})

