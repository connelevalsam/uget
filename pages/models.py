import uuid

from django.db import models
from django.urls import reverse


def change_image_path(instance, filename):
    return '/'.join(['images', str(uuid.uuid4().hex + ".jpg")])


class Order(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=50, default="Waiting")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Returns the url to access a particular message instance."""
        return reverse('order-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.fullname


class OrderImages(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to=change_image_path)
