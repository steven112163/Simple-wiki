from django.db import models


# Create your models here.
class Material(models.Model):
    """
    Model representing the material
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __str__(self):
        """
        String for representing the Model
        :return: Name of the material
        """


class Type(models.Model):
    """
    Model representing the type
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Type'
        verbose_name_plural = 'Types'

    def __str__(self):
        """
        String for representing the Model
        :return: Name of the type
        """
        return self.name


class Item(models.Model):
    """
    Model representing the item
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='items', null=True)
    stackable = models.BooleanField(default=False)
    renewable = models.BooleanField(default=False)
    durability = models.IntegerField()
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    attack_damage = models.IntegerField(blank=True, null=True)
    attack_speed = models.FloatField(blank=True, null=True)
    defense_points = models.IntegerField(blank=True, null=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        """
        String for representing the Model
        :return: Name of the item
        """
        return self.name
