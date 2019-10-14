# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class DocumentResource(resources.ModelResource):
    class Meta:
        model = Document

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class NewsResource(resources.ModelResource):
    class Meta:
        model = News


class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name_category','creation_date')
    search_fields = ['name_category']
    resource_class = CategoryResource


class AuthorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('first_name','last_name','email','description','creation_date')
    search_fields = ['first_name','last_name','email']
    resource_class = AuthorResource


class DocumentAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title','is_public','author','level','file','publication_date')
    search_fields = ['title','author','level']
    resource_class = DocumentResource

class NewsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('title','is_public','category','description','publication_date')
    search_fields = ['title','category']
    resource_class = NewsResource


class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('first_name','last_name','email','issue','message','creation_date')
    search_fields = ['first_name','last_name','email']
    resource_class = ContactResource


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contact, ContactAdmin)
