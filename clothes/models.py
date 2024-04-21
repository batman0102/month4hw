from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()

    def __str__(self):
        return self.name

class Clothes(models.Model):
    image = models.ImageField(upload_to='', null=True, blank=True)
    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='clothes',
        blank=True
    )
    categories = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='clothes',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    clothes = models.ForeignKey(
        Clothes,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review for {self.clothes.name} at {self.created_at.strftime("%Y-%m-%d %H:%M")}'




