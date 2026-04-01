from django.contrib import admin
from .models import Product, Store, productReview,productCertificate

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'description')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'products')
    filter_horizontal = ('product_varities',)

class productReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')

class productCertificateAdmin(admin.ModelAdmin):
    list_display = ('product', 'certificate_number', 'issued_date')


admin.site.register(Product, ProductAdmin)
admin.site.register(productReview, productReviewAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(productCertificate, productCertificateAdmin)
# Register your models here.
