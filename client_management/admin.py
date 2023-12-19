from django.contrib import admin
from .models import PartnerDetails,ClientDetails,CustomerDetails,VendorDetails,DepartmentDetails

class PartnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(PartnerDetails, PartnerAdmin)

class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClientDetails, ClientAdmin)


class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomerDetails, CustomerAdmin)

class VendorAdmin(admin.ModelAdmin):
    pass

admin.site.register(VendorDetails, VendorAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(DepartmentDetails, DepartmentAdmin)