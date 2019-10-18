from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView
# Create your views here.
from django.utils import timezone
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
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


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        form = ContactForm()
        context['form'] = form
        context['context'] = context
        return context

    def form_valid(self, form):
        return super().form_valid(form)
