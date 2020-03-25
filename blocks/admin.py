from django.contrib import admin
from .models import Texture, Block

# Register your models here.
admin.site.register(Texture)


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'texture', 'display_tools', 'update', )
    list_filter = ('stackable', 'flammable', 'transparent', 'luminant', 'texture', )
    exclude = ('id', 'update', )
