from django.contrib import admin
from .models import UserId, User,Department,Contact
# Register your models here.


admin.site.register(UserId)
admin.site.register(Department)
admin.site.register(User)
admin.site.register(Contact)