from django.shortcuts import render, get_object_or_404

# Create your views here.


def ratings_main_view(request):
    return render(request, 'ratings_base.html', {})
