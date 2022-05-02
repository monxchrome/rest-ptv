from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit import processors

from .utils import unique_slug_generator
from .validators import validate_size
from users.models import User


class ModelWithTS(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(ModelWithTS):
    slug = models.SlugField(unique=True, )
    file = ProcessedImageField(
        upload_to='post_files/', processors=[processors.ResizeToFit(width=1400, upscale=False)],
        format='JPEG', options={'quality': 90}
    )
    file_thumb = ImageSpecField(
        source='file', processors=[processors.SmartResize(450, 300)],
        format='JPEG', options={'quality': 80}
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    description = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User)
    published = models.BooleanField(default=True)

    def __str__(self):
        if self.title:
            return self.title
        return f"Post id: {self.id}"

    class Meta:
        ordering = ['-id']


class Comment(ModelWithTS):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='childs', null=True, blank=True)


    def __str__(self):
        return f"user: {self.user.email}, comment: {self.title}"


@receiver(pre_save, sender=Post)
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
