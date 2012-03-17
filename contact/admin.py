from django.contrib import admin
from contact.models import ContactInfo


class ContactInfoAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_on'
	list_display = ('email', 'created_on', ) #"is_accepted", 
	#list_filter = ('is_accepted',)
	list_display_links = ('email',)
	search_fields = ('name','address','phone','zip_code', 'state', 'city', 'email','subject', 'question',)


admin.site.register(ContactInfo, ContactInfoAdmin)