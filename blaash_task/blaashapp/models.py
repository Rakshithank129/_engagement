from django.db import models

class EngagementPost(models.Model):
    tenant_id = models.IntegerField()
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=50)  # 'video' or 'story'
    created_at = models.DateTimeField(auto_now_add=True)

class EngagementPostContent(models.Model):
    post = models.ForeignKey(EngagementPost, on_delete=models.CASCADE)
    url = models.URLField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    sku = models.CharField(max_length=50)

class EngagementPostProductMapping(models.Model):
    post = models.ForeignKey(EngagementPost, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Collection(models.Model):
    name = models.CharField(max_length=255)

class EngagementPostCollection(models.Model):
    post = models.ForeignKey(EngagementPost, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    duration_in_seconds = models.IntegerField(default=0)