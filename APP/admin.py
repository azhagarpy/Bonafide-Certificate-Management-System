from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(CustomUser)
admin.site.register(Departments)
admin.site.register(Years)
admin.site.register(Applications)


