from django.contrib import admin

# Register your models here.
from .models import (
    LivingAspects,
    AspectRatings
)

admin.site.register(LivingAspects)
admin.site.register(AspectRatings)
