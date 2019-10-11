from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello world</h1>")  # string of HTML code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": " This is about us",
        "my_number": 123,
        "my_list": [1, "Gotcha!", 487, "Hulla", False, 9]
    }
    return render(request, 'about.html', my_context)
