from django.contrib import admin
from django.contrib import admin
from .models import Company, Role, User

# Register the Company model
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')  
    search_fields = ('name',)  

# Register the Role model
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','permissions','company', 'created_at')
    search_fields = ('name', 'company__name') 

# Register the User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'company', 'role', 'is_superuser', 'created_at','updated_at')
    search_fields = ('email', 'company__name', 'role__name')  
    list_filter = ('is_superuser', 'company') 
    

