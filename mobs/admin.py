from django.contrib import admin
from .models import Behavior, Mob

# Register your models here.
admin.site.register(Behavior)


@admin.register(Mob)
class MobAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'behavior', 'update', )
    list_filter = ('height', 'width', 'behavior', 'attack_strength', )
    exclude = ('id', 'update')
