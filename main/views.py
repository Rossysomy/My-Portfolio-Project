from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, ContactMessage
from .forms import ContactForm


SKILLS_LIST = [
    'Requirements Gathering', 'Stakeholder Management', 'Agile / Scrum',
    'Waterfall', 'Process Mapping (BPMN)', 'Risk Management',
    'User Story Writing', 'SQL & Data Analysis', 'Power BI', 'Tableau',
    'Jira & Confluence', 'Visio / Lucidchart', 'SharePoint',
    'Gap Analysis', 'Change Management', 'UAT Coordination',
    'PCI DSS / SOC 2', 'GDPR', 'NIST 800-53', 'CompTIA Security+',
]


def home(request):
    featured_projects = Project.objects.filter(featured=True)
    return render(request, 'main/index.html', {
        'featured_projects': featured_projects,
        'skills_list': SKILLS_LIST,
    })


def projects(request):
    category = request.GET.get('category', '')
    all_projects = Project.objects.all()
    if category:
        all_projects = all_projects.filter(category=category)
    categories = Project.CATEGORY_CHOICES
    return render(request, 'main/projects.html', {
        'projects': all_projects,
        'categories': categories,
        'active_category': category,
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    related = Project.objects.exclude(pk=pk).filter(category=project.category)[:3]
    return render(request, 'main/project_detail.html', {
        'project': project,
        'related': related,
    })


def about(request):
    return render(request, 'main/about.html', {'skills_list': SKILLS_LIST})


def experience(request):
    return render(request, 'main/experience.html')


PROFICIENCY_ITEMS = [
    ('Requirements Analysis & Documentation', 100),
    ('Stakeholder Management', 98),
    ('Agile / Scrum Delivery', 97),
    ('Risk & Issue Management', 96),
    ('Jira & Confluence', 95),
    ('Process Mapping (BPMN / Visio)', 94),
    ('Microsoft Project', 93),
    ('Security Compliance (PCI DSS / SOC 2 / GDPR)', 92),
    ('Microsoft Power BI', 91),
    ('SQL & Data Analysis', 90),
]


def skills(request):
    return render(request, 'main/skills.html', {'proficiency_items': PROFICIENCY_ITEMS})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            msg = form.save()
            send_mail(
                    subject=f'Portfolio Contact: {msg.subject}',
                    message=f'From: {msg.name} <{msg.email}>\n\n{msg.message}',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            messages.success(request, "Thank you! Your message has been sent. I'll be in touch shortly.")
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})


def resume(request):
    return render(request, 'main/resume.html')




