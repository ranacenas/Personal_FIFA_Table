from django.contrib import admin
from .models import game_history, standing
# Register your models here.

admin.site.register(game_history)
admin.site.register(standing)

