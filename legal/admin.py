from django.contrib import admin

from .models import form

# Register your models here.


class formAdmin(admin.ModelAdmin):
    ...


admin.site.register(form, formAdmin)
