from django.db import models

# Create your models here.
class Plano(models.Model):
    
    name = models.CharField('Nome do Plano',max_length=100)
    description = models.TextField('Descrição', null=True, blank=True)
    slug = models.SlugField('Atalho', null=True)
    price = models.DecimalField('Preço', max_digits=3, decimal_places=2)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

def __str__(self):
	return self.name