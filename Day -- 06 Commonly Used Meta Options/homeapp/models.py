from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        #acending or dcending oder
        ordering = ['created_at']
        ordering = ['-created_at']

        db_table = 'product_master' #fixed the table name
        verbose_name = 'Product' # Human-readable singular name for the object.
        verbose_name_plural = 'Products'
        unique_together = ('name', 'created_at')
        permissions = [
            ("can_mark_featured", "Can mark product as featured"),
        ]