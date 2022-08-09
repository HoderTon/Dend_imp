from django.db import models


class Crypto_Asset(models.Model):
    pass


class Preset(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    crypto_ass = models.ForeignKey(Crypto_Asset, on_delete=models.CASCADE)
    coords = models.FloatField() # IDK in what format the coords should be, so for now I set float
    text_color = models.CharField(max_length=200) # Will it be text, integer (0;255) or hexadecimal number?
    message_text = models.TextField() # It isn't clear what kind of settings will JSON file constain

    class Meta:
        verbose_name = 'Preset'
        verbose_name_plural = 'Presets'


class Device(models.Model):
    model = models.CharField(max_lenght=200)
    price = models.IntegerField()
    amount = models.IntegerField()