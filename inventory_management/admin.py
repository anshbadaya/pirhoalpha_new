from django.contrib import admin
from .models import Category, PurchasedProduct, SoldProduct,InHouseProducts,Inventory,PurchasedBillingDetails,SoldBillingDetails

class PurchasedProductAdmin(admin.ModelAdmin):
    pass

class SoldProductAdmin(admin.ModelAdmin):
    pass

class InventoryAdmin(admin.ModelAdmin):
    pass
    

class InHouseProductAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class PuchaseAdmin(admin.ModelAdmin):
    pass

class BillingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(PurchasedProduct, PurchasedProductAdmin)
admin.site.register(SoldProduct, SoldProductAdmin)
admin.site.register(InHouseProducts, InHouseProductAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(PurchasedBillingDetails,PuchaseAdmin)
admin.site.register(SoldBillingDetails,BillingAdmin)
