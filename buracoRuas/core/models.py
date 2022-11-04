from django.db import models
from email.policy import default
# Create your models here.

class situacoes(models.Model):
  situ_situacao = models.CharField("Situacao", max_length=255, blank=False, null=False,default='leve') 
  def __str__(self):
    return self.situacao
  class Meta: 
    verbose_name_plural = "Situações"

class bairros(models.Model):
  ba_bairro = models.CharField("Bairro", max_length=255, blank=False, null=False) 
  def __str__(self):
    return self.bairro
  class Meta: 
    verbose_name_plural = "Bairros"

class ruas(models.Model): 
  ru_rua = models.CharField("Rua", max_length=255, blank=False, null=False)
  def __str__(self):
    return self.rua
  class Meta: 
    verbose_name_plural = "Ruas"

class buracos(models.Model): 
  bu_ru_rua = models.ForeignKey('ruas', on_delete=models.CASCADE, default=1) 
  bu_ba_bairro = models.ForeignKey('bairros', on_delete=models.CASCADE, default=1) 
  bu_situ_situacao = models.ForeignKey('situacoes', on_delete=models.CASCADE, default=1)
  class Meta:
    unique_together = ('bu_ru_rua', 'bu_ba_bairro', 'bu_situ_situacao')
    verbose_name_plural = "Buracos"