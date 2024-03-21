from django.contrib import admin

# Register your models here.
from .models import Subject, WorkType, AcademicLevel, OrderFile, Order, OrderMessage

admin.site.register(Subject)
admin.site.register(WorkType)
admin.site.register(AcademicLevel)
admin.site.register(OrderFile)
# admin.site.register(Work)
admin.site.register(Order)
admin.site.register(OrderMessage)
