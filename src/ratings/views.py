from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView
# Create your views here.
from .models import LivingAspects, AspectRatings
from django.utils import timezone
from .forms import RatingForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

# class RatingsMainView(TemplateView):
#     template_name = 'ratings_base.html'
#     form_class = RatingForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         context['LivingAspects'] = LivingAspects.objects.all()

#         form = RatingForm()
#         context['form'] = form
#         return context


class RatingsMainView(CreateView):
    template_name = 'ratings_base.html'
    form_class = RatingForm
    queryset = AspectRatings.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['LivingAspects'] = LivingAspects.objects.all()

        form = RatingForm()
        context['form'] = form
        context['context'] = context
        return context

    def form_valid(self, form):
        return super().form_valid(form)


def ratings_redirect(request, aspect):
    print(aspect)
    from django.contrib import messages

    # messages.add_message(request, level, message, extra_tags='', fail_silently=False)
    messages.add_message(request, messages.INFO, str(aspect))

    return redirect(reverse("ratings:ratings-home"))
