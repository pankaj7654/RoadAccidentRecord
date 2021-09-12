from django.contrib import admin

from Record.models import User , FormData

from django.utils.html import format_html

# design Users section of admin panel
class UserModel(admin.ModelAdmin):
    list_display = ['id','name','email','phone','password','active']
    sortable_by = ['id' , 'name']
    list_editable = ['active']


class FormDataModel(admin.ModelAdmin):
    list_display = ['fireno','ipc']
    sortable_by=['fireno','ipc']
    

admin.site.register(FormData.RecordFormData, FormDataModel),
admin.site.register(User , UserModel)