from django.contrib import admin
from .models import artist,customer,product,comment,purchased

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
	pass
	
class CustomerAdmin(admin.ModelAdmin):
	pass
	
class ProductAdmin(admin.ModelAdmin):
	pass

class CommentAdmin(admin.ModelAdmin):
	pass
	
class PurchasedAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(artist, ArtistAdmin)
admin.site.register(customer, CustomerAdmin)
admin.site.register(product, ProductAdmin)
admin.site.register(comment, CommentAdmin)
admin.site.register(purchased,PurchasedAdmin)