from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)             
    description = models.TextField()                     
    publication_date = models.DateField()                
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    pages = models.IntegerField()                         
    is_published = models.BooleanField(default=True)      
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)  

    def __str__(self):
        return self.title