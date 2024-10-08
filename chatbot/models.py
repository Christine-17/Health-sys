from django.db import models

class Inquiry(models.Model):
    user_input = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_input
class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # This is where the image will be stored

    def __str__(self):
        return self.title