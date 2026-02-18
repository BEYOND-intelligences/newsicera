from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from .models import Experiment, Subject
import os
from django.conf import settings

def experiment_list(request):
    """Display list of active experiments on the home page with filtering."""
    subject_slug = request.GET.get('subject')
    experiments = Experiment.objects.filter(is_active=True)
    
    if subject_slug:
        experiments = experiments.filter(subject__slug=subject_slug)
    
    # Fetch active slides for the slider

    subjects = Subject.objects.all()

    return render(request, 'experiments/index.html', {
        'experiments': experiments,
        'subjects': subjects,
        'current_subject': subject_slug,
    })

def experiment_detail(request, slug):
    """Display detailed information about an experiment."""
    experiment = get_object_or_404(Experiment, slug=slug)
    return render(request, 'experiments/detail.html', {'experiment': experiment})

def about(request):
    """Display the about page."""
    return render(request, 'experiments/about.html')

def simulation_view(request, slug):
    """
    Display simulation page for an experiment.
    Checks if template exists, otherwise uses fallback template.
    """
    experiment = get_object_or_404(Experiment, slug=slug)
    
    # Try to find specific template for this experiment
    template_name = f'experiments/simulations/{experiment.slug}.html'
    
    # Check if template exists
    try:
        get_template(template_name)
    except TemplateDoesNotExist:
        # Use fallback template if specific template doesn't exist
        template_name = 'experiments/simulations/simulation_fallback.html'
    
    return render(request, template_name, {'experiment': experiment})

def custom_404(request, exception):
    """Custom 404 error handler."""
    return render(request, '404.html', status=404)
