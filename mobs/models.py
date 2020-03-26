from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Behavior(models.Model):
    """
    Model representing the behavior
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name = 'Behavior'
        verbose_name_plural = 'Behaviors'

    def __str__(self):
        """
        String for representing the Model
        :return: Name of the behavior
        """
        return self.name


class Mob(models.Model):
    """
    Model representing the mob
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='mobs', null=True)
    height = models.FloatField()
    width = models.FloatField()
    behavior = models.ForeignKey(Behavior, on_delete=models.SET_NULL, null=True)
    attack_strength = models.IntegerField(blank=True)
    spawn = RichTextField()
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Mob'
        verbose_name_plural = 'Mobs'

    def __str__(self):
        """
        String for representing the Model
        :return: Name of the mob
        """
        return self.name
