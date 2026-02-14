from django.db import models
from django.urls import reverse

class Experiment(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان التجربة")
    description = models.TextField(verbose_name="وصف التجربة")
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="رابط التجربة")
    image = models.ImageField(upload_to='experiments/', verbose_name="صورة التجربة", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="نشط")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a particular experiment simulation."""
        return reverse('simulation', args=[str(self.slug)])

    class Meta:
        verbose_name = "تجربة"
        verbose_name_plural = "التجارب"
        ordering = ['-created_at']  # عرض الأحدث أولاً
