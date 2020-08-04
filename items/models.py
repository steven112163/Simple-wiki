from django.db import models


# Create your models here.
class Material(models.Model):
    """
    Model representing the material
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'名稱', max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = u'材料'
        verbose_name_plural = u'材料'

    def __str__(self):
        """
        String for representing the object
        :return: Name of the object
        """
        return self.name


class Type(models.Model):
    """
    Model representing the type
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'名稱', max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = u'類型'
        verbose_name_plural = u'類型'

    def __str__(self):
        """
        String for representing the object
        :return: Name of the object
        """
        return self.name


class Item(models.Model):
    """
    Model representing the item
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'名稱', max_length=100)
    image = models.ImageField(u'圖片', upload_to='items', null=True)
    stackable = models.BooleanField(u'可堆疊', default=False)
    renewable = models.BooleanField(u'可修理', default=False)
    durability = models.IntegerField(u'耐久度')
    material = models.ForeignKey(Material, verbose_name=u'材料', on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, verbose_name=u'類型', on_delete=models.SET_NULL, null=True)
    attack_damage = models.IntegerField(u'攻擊傷害', blank=True, null=True)
    attack_speed = models.FloatField(u'攻擊速度', blank=True, null=True)
    defense_points = models.IntegerField(u'防禦值', blank=True, null=True)
    update = models.DateTimeField(u'更新時間', auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'- 物品'
        verbose_name_plural = u'- 物品'

    def __str__(self):
        """
        String for representing the object
        :return: Name of the object
        """
        return self.name
