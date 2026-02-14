import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.text import slugify
from .models import Experiment

@receiver(post_save, sender=Experiment)
def create_simulation_file(sender, instance, created, **kwargs):
    if not instance.slug:
        # Save again if slug is missing 
        # (Though best handled in clean() or save() of model, 
        # but for simple admin usage, slug might come in via admin form)
        instance.slug = slugify(instance.title)
        instance.save()
        return # recursed save will trigger signal again with slug

    # Path to templates dir
    templates_dir = os.path.join(settings.BASE_DIR, 'experiments', 'templates', 'experiments', 'simulations')
    os.makedirs(templates_dir, exist_ok=True)
    
    file_path = os.path.join(templates_dir, f'{instance.slug}.html')
    
    if not os.path.exists(file_path):
        content = f"""{{% extends 'experiments/simulation_base.html' %}}

{{% block title %}}محاكاة: {instance.title}{{% endblock %}}

{{% block simulation_content %}}
    <h2>{instance.title}</h2>
    <div id="simulation-container">
        <!-- Add your simulation code here for {instance.title} -->
        <p>مساحة العمل جاهزة للكود الخاص بالتجربة.</p>
    </div>
{{% endblock %}}
"""
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
