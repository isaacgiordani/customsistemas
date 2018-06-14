from django.db import models
from django.urls import reverse

# Create your models here.
class Entity(models.Model):
    name = models.CharField('Nome', max_length = 70)
    slug = models.SlugField('Identificador', max_length = 100)
    created = models.DateTimeField('Criado em', auto_now = True)
    modified = models.DateTimeField('Modificado em', auto_now = True)
    phoneent = models.CharField('Telefone Entidade', max_length = 20, blank=True)

    class Meta:
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('listatelefonica:entity',kwargs={'slug':self.slug})

class PhoneBook(models.Model):
    entity = models.ForeignKey('listatelefonica.Entity', on_delete = models.CASCADE, verbose_name = 'Entidade')
    name = models.CharField('Nome', max_length = 70)
    lastname = models.CharField('SobreNome', max_length = 150, blank = True)
    role = models.CharField('Cargo', max_length = 20, blank = True)
    phone = models.CharField('Telefone', max_length = 20)
    phonesec = models.CharField('Telefone Secundario', max_length = 20, blank = True)
    ramal = models.CharField('Ramal', max_length = 10, blank = True)
    slug = models.SlugField('Identificador', max_length = 100)
    created = models.DateTimeField('Criado em', auto_now = True)
    modified = models.DateTimeField('Modificado em', auto_now = True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('listatelefonica:phonebook',kwargs={'slug':self.slug})

class AccessType(models.Model):
    description = models.CharField('Descrição', max_length = 35)
    created = models.DateTimeField('Criado em', auto_now = True)
    modified = models.DateTimeField('Modificado em', auto_now = True)

    class Meta:
        verbose_name = 'Tipo de Acesso'
        verbose_name_plural = 'Tipos de Acesso'

    def __str__(self):
        return self.description

class Access(models.Model):
    entity = models.ForeignKey('listatelefonica.Entity', on_delete = models.CASCADE, verbose_name = 'Entidade')
    accesstype = models.ForeignKey('listatelefonica.AccessType', on_delete = models.CASCADE, verbose_name = 'Tipo de Acesso')
    identifier = models.CharField('Identificador', max_length = 35)
    description = models.CharField('Descrição', max_length = 50, blank = True)
    password = models.CharField('Senha', max_length = 35, blank = True)
    active  = models.BooleanField('Ativo', default = True)
    created = models.DateTimeField('Criado em', auto_now = True)
    modified = models.DateTimeField('Modificado em', auto_now = True)

    class Meta:
        verbose_name = 'Acesso'
        verbose_name_plural = 'Acessos'

    def __str__(self):
        return self.identifier
