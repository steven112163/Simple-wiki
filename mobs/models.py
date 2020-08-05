from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Behavior(models.Model):
    """
    Model representing the behavior
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'名稱', max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = u'行為'
        verbose_name_plural = u'行為'

    def __str__(self):
        """
        String for representing the object
        :return: Name of the object
        """
        return self.name


class Mob(models.Model):
    """
    Model representing the mob
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'名稱', max_length=100)
    image = models.ImageField(u'圖片', upload_to='mobs', null=True)
    health_points = models.IntegerField(u'生命值', default=1)
    height = models.FloatField(u'高度')
    width = models.FloatField(u'寬度')
    behavior = models.ForeignKey(Behavior, verbose_name=u'行為', on_delete=models.SET_NULL, null=True, blank=True)
    attack_strength = models.IntegerField(u'攻擊力', null=True, blank=True)
    spawn = RichTextField(u'生成')
    update = models.DateTimeField(u'更新時間', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'- 生物'
        verbose_name_plural = u'- 生物'

    def __str__(self):
        """
        String for representing the object
        :return: Name of the object
        """
        return self.name
