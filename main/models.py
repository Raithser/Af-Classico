import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
    ('jersey', '⚽ Jersey'),
    ('boots', '👟 Football Boots'),
    ('ball', '🥅 Match Ball'),
    ('training', '🏋️ Training Gear'),
    ('accessories', '🎯 Football Accessories'),
    ('collectibles', '🏆 Collectibles'),
    ('equipment', '⚙️ Equipments'),
    ]
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.product_views > 20
        
    def increment_views(self):
        self.product_views += 1
        self.save()
# Create your models here.
