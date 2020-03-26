from django.db import models
from items.models import Item


# Create your models here.
class Texture(models.Model):
    """
    Model representing texture of the block
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Texture'
        verbose_name_plural = 'Textures'

    def __str__(self):
        """
        String for representing the Model
        :return: Name of the texture
        """
        return self.name


class Block(models.Model):
    """
    Model representing a block
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blocks', null=True)
    stackable = models.BooleanField(default=False)
    flammable = models.BooleanField(default=False)
    transparent = models.BooleanField(default=False)
    luminant = models.IntegerField()
    tool = models.ManyToManyField(Item)
    texture = models.ForeignKey(Texture, on_delete=models.SET_NULL, null=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Block'
        verbose_name_plural = 'Blocks'

    def __str__(self):
        """
        String for representing the Model
        :return: Name of the block
        """
        return self.name

    def display_tools(self):
        """
        String for representing first three tools
        :return: Three names of the tools
        """
        return ', '.join(tool.name for tool in self.tool.filter(type__name='tool'))
