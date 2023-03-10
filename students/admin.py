from django.contrib import admin

# Register your models here.

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'date_of_birth', 'phone',
                    'city', 'zip', 'state', 'graduation', 'email', 'year']


admin.site.register(Student, StudentAdmin)
