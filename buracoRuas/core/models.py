from django.db import models
from email.policy import default
# Create your models here.

# class situacoes(models.Model):
#   situ_situacao = models.CharField("Situacao", max_length=255, blank=False, null=False,default='leve') 
#   def __str__(self):
#     return self.situacoes
#   class Meta: 
#     verbose_name_plural = "Situações"

# class bairros(models.Model):
#   ba_bairro =
  # def __str__(self):
  #   return self.bairros
#   class Meta: 
#     verbose_name_plural = "Bairros"

# class ruas(models.Model): 
#   ru_rua = models.CharField("Rua", max_length=255, blank=False, null=False)
#   def __str__(self):
#     return self.ruas
#   class Meta: 
#     verbose_name_plural = "Ruas"

class buracos(models.Model): 
  GRAVIDADE_CHOICES=[
    ["Leve", "Leve"],
    ["Moderado", "Moderado"],
    ["Critico", "Crítico"]
    # [1, "Leve"],
    # [2, "Moderado"],
    # [3, "Crítico"]
  ]
  STATUS_CHOICES=[
    #[0, "Não Consertado"],
    #[1, "Consertado"]
    ["Nao Consertado", "Não Consertado"],
    ["Consertado", "Consertado"]
  ]
  bu_quantia = models.IntegerField("Quantia", blank=False, null=False, default=1)
  bu_gravidade = models.CharField("Gravidade", choices=GRAVIDADE_CHOICES, max_length=100)
  bu_rua = models.CharField("Rua", max_length=255, blank=False, null=False) 
  bu_bairro = models.CharField("Bairro", max_length=255, blank=False, null=False)
  bu_status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, blank=False, null=False, default="Não Consertado")
  class Meta:
    verbose_name_plural = "Buracos"
  def __str__(self):
    return self.bu_bairro