from django.forms import ModelForm
from core.models import *

class buracoForm(ModelForm): 
  class Meta: 
    model = buracos
    fields = ["bu_gravidade","bu_quantia","bu_rua","bu_bairro","bu_status"] 