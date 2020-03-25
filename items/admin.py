from django.contrib import admin
from .models import Material, Type, Item

# Register your models here.
admin.site.register(Material)

admin.site.register(Type)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'material', 'type', 'update', )
    list_filter = ('stackable', 'renewable', 'durability', 'material', 'type', 'attack_damage', 'attack_speed',
                   'defense_points', )
    exclude = ('id', 'update', )
