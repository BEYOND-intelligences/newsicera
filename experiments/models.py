from django.db import models
from django.urls import reverse

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المادة")
    slug = models.SlugField(unique=True, verbose_name="رابط المادة")
    icon = models.ImageField(upload_to='subjects/', verbose_name="أيقونة المادة", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "مادة"
        verbose_name_plural = "المواد"


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم التصنيف")
    slug = models.SlugField(unique=True, verbose_name="رابط التصنيف")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "تصنيفات"


class Experiment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name='experiments', verbose_name="المادة")
    title = models.CharField(max_length=200, verbose_name="عنوان التجربة")
    description = models.TextField(verbose_name="وصف التجربة")
    tags = models.ManyToManyField(Tag, verbose_name="التصنيفات", blank=True, related_name='experiments')
    physical_law = models.TextField(verbose_name="القانون الفيزيائي", blank=True, null=True)
    tools_needed = models.TextField(verbose_name="الأدوات المطلوبة", blank=True, null=True)
    steps = models.TextField(verbose_name="خطوات التجربة", blank=True, null=True)
    video_url = models.URLField(verbose_name="رابط فيديو", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name="رابط التجربة")
    image = models.ImageField(upload_to='experiments/', verbose_name="صورة التجربة", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="نشط")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access the experiment detail page."""
        return reverse('experiment_detail', args=[str(self.slug)])

    class Meta:
        verbose_name = "تجربة"
        verbose_name_plural = "التجارب"
        ordering = ['-created_at']  # عرض الأحدث أولاً






