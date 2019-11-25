# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

courses = (
            ("KINDER", "Kinder"),
            ("PRIMERO", "1ero Básico"),
            ("SEGUNDO", "2do Básico"),
            ("TERCERO", "3ero Básico"),
            ("CUARTO", "4to Básico"),
            ("QUINTO", "5to Básico"),
            ("SEXTO", "6to Básico"),
            ("SEPTIMO", "7mo Básico"),
            ("OCTAVO", "8vo Básico"),
            ("PRIMERO_MEDIO", "1ero Medio"),
            ("SEGUNDO_MEDIO", "2do Medio"),
            ("TERCERO_MEDIO", "3ero Medio"),
            ("CUARTO_MEDIO", "4to Médio"),
)

class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
    creation_date = models.DateField('Fecha de Creación',auto_now = False, auto_now_add = True)
    modification_date = models.DateField('Fecha de Modificación',auto_now = True, auto_now_add = False)
    delete_date = models.DateField('Fecha de Eliminación',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True


class Category(BaseModel):
    name_category = models.CharField('Nombre', max_length = 100)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name_category


class Author(BaseModel):
    first_name = models.CharField('Nombres', max_length = 200)
    last_name = models.CharField('Apellidos', max_length = 250)
    email = models.EmailField('Correo electrónico', max_length = 300)
    description = models.TextField('Descripción', null = True, blank = True)
    reference_image = models.ImageField('Imagen referencial', upload_to = 'autores/', null = True, blank = True)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.first_name, self.last_name)


class Document(BaseModel):
    title = models.CharField('Titulo', max_length = 200)
    file = models.FileField(upload_to = 'documents/', max_length = 255)
    reference_image = models.ImageField('Imagen referencial', upload_to = 'documentPicture/', null = True, blank = True)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    level = models.CharField(choices = courses, max_length = 13)
    description = models.TextField('Descripción', null = True, blank = True)
    publication_date = models.DateField('Fecha de publicación')
    is_public = models.BooleanField('Publicado', default = False)
    is_guide_document = models.BooleanField('Documento de Pauta', default = False)

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return str(self.file).strip('documents/')


class News(BaseModel):
    title = models.CharField('Titulo', max_length = 300)
    description = models.TextField('Descripción')
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    reference_image = models.ImageField('Imagen Referencial', upload_to = 'imagenes/', max_length = 255)
    publication_date = models.DateField('Fecha de publicación')
    is_public = models.BooleanField('Publicado / No Publicado', default = False)
    relevant = models.BooleanField('Relevante / No relevante', default = False)

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.title


class Contact(BaseModel):
    first_name = models.CharField('Nombre', max_length = 100)
    last_name = models.CharField('Apellidos', max_length = 150)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    issue = models.CharField('Asunto', max_length = 100)
    message = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.issue
