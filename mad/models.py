from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    features = models.JSONField(default=dict)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)  
    permissions = models.JSONField(default=dict) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="roles")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} ({self.company.name})"
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255) 
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="users")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name="users")
    is_superuser = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.email} ({self.company.name})"


