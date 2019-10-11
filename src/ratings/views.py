from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
# Create your views here.
from .models import LivingAspects
from django.utils import timezone


class RatingsMainView(TemplateView):
    template_name = 'ratings_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['LivingAspects'] = LivingAspects.objects.all()
        return context
