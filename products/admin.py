from django.contrib import admin

from products.models import prodCategory, prod

admin.site.register(prod)
admin.site.register(prodCategory)
