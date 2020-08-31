from django.db import models
from items.models import Item


# Create your models here.
class Texture(models.Model):
    """
    Model representing texture of the block
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'名稱', max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'材質'
        verbose_name_plural = u'材質'

    def __str__(self):
        """
        String for representing the object
        :return: Name of the object
        """
        return self.name


class Block(models.Model):
    """
    Model representing a block
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'名稱', max_length=100)
    image = models.ImageField(u'圖片', upload_to='blocks', blank=True, null=True)
    stackable = models.BooleanField(u'可堆疊', default=False)
    flammable = models.BooleanField(u'可燃性', default=False)
    transparent = models.BooleanField(u'透明', default=False)
    luminant = models.IntegerField(u'亮度')
    tool = models.ManyToManyField(Item, verbose_name=u'工具', blank=True)
    texture = models.ForeignKey(Texture, verbose_name=u'材質', on_delete=models.SET_NULL, blank=True, null=True)
    update = models.DateTimeField(u'更新時間', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'- 方塊'
        verbose_name_plural = u'- 方塊'

    def __str__(self):
        """
        String for representing the object
        :return: Name of the object
        """
        return self.name

    def display_tools(self):
        """
        String for representing first three tools
        :return: Three names of the tools
        """
        return ', '.join(tool.name for tool in self.tool.filter(type__name='tool'))
