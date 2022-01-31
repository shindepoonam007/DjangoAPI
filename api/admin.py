from django.contrib import admin
from .models import SecurityQuestion , Register , PasswordHistory,Device
# Register your models here.
admin.site.register(SecurityQuestion)
admin.site.register(Register)
admin.site.register(PasswordHistory)
admin.site.register(Device)