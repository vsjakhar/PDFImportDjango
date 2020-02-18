from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from .models import *
import sys, fitz
from pathlib import Path
from django.utils.safestring import mark_safe

# Register your models here.

class CustomUserAdmin(UserAdmin):
	# form = CustomUserChangeForm
	# add_form = CustomUserCreationForm
	# readonly_fields = ('image_tag',)
	# inlines = [MessageInline]
	# autocomplete_fields = ['parent',]
	# actions = None
	ordering = ('-id',)
	list_display = ['username', 'email', 'mobile', 'first_name','last_name', 'verified']
	search_fields = ['username','email','mobile','gender','first_name','last_name']
	add_fieldsets = (
		(None, {
			'classes': ('wide', 'extrapretty'),
			'fields': ('first_name', 'last_name', 'email', 'mobile', 'username', 'password1', 'password2', ),
		}),
	)
	fieldsets = [
		(None, {'fields': ('email', 'username', 'mobile', 'first_name', 'last_name', 'password',)}),
		('Personal info', {'fields': ('image', 'phone', 'gender', 'dob', 'tagline', 'about',)}),
		('Social Detail', {'classes': ('collapse', ), 'fields': ('website','facebook','twitter','instagram','linkedin','source')}),
		('Permissions', {'classes': ('collapse', ), 'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
		('Location', {'classes': ('collapse', ), 'fields': ('latitude','longitude')}),
		('Important dates', {'classes': ('collapse', ), 'fields': ('last_login','date_joined')}),]

	def has_add_permission(self,request):
		if request.user.is_superuser and 'Verification' != self.fieldsets[-1][0]:
			self.fieldsets.append(('Verification', {'fields': ('verified',)}))
		return True

	# def work(self, obj):
	# 	return format_html('<a href="/stroops/stroop/work/?q=%s" >Work</a>'%(obj.username))

	def has_delete_permission(self, request, obj=None):
		return False

class CollectionAdmin(admin.ModelAdmin):
	list_display=['title', 'user', 'utimestamp', 'status']
	search_fields=['title', 'user__username', 'timestamp', 'status']
	autocomplete_fields=['user']
	readonly_fields = ['pdf_display',]

	def pdf_display(self, obj):
		return mark_safe(obj.content)

	def save_model(self, request, obj, form, change):
		path = settings.BASE_DIR+'/media/'+str(obj.pdf)
		if Path(path).is_file():
			doc = fitz.open(path)
			html_text = ""
			for page in doc:
				html_text += page.getText("html")
			# print(html_text)
			obj.content = html_text
		super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)
admin.site.register(Collection, CollectionAdmin)
