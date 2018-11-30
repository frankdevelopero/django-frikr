from django.contrib import admin
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'licence', 'visivility')
    list_filter = ('licence', 'visivility')
    search_fields = ('name', 'description')

    def owner_name(self, obj):
        return obj.owner.first_name + ' ' + obj.owner.last_name

    owner_name.short_description = 'Photo Owner'  # Atributo
    owner_name.admin_order_field = 'owner'

    fieldsets = (
        (None, {
            'fields': ('name',),
            'classes': ('wide',)
        }),
        ('description & Author',{
            'fields': ('description', 'owner'),
            'classes': ('wide', )
        }),
        ('Extra',{
            'fields': ('url', 'licence', 'visivility'),
            'classes': ('wide', 'collapse')
        })
    )


admin.site.register(Photo, PhotoAdmin)
