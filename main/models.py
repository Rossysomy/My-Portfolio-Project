from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('business_analysis', 'Business Analysis'),
        ('project_management', 'Project Management'),
        ('digital_transformation', 'Digital Transformation'),
        ('process_improvement', 'Process Improvement'),
        ('data_analytics', 'Data & Analytics'),
        ('crm_erp', 'CRM / ERP Implementation'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    short_description = models.CharField(max_length=300, help_text='One-line summary shown on the card')
    description = models.TextField(help_text='Full project description')
    tools_used = models.CharField(max_length=300, help_text='Comma-separated list, e.g. "Jira, Confluence, SQL"')
    outcome = models.TextField(blank=True, help_text='Key results or impact achieved')
    client_or_company = models.CharField(max_length=150, blank=True, help_text='Client or employer (optional)')
    duration = models.CharField(max_length=100, blank=True, help_text='e.g. "6 months" or "Jan 2023 – Jul 2023"')
    business_problem = models.TextField(blank=True, help_text='The business problem or challenge this project addressed')
    key_features = models.TextField(blank=True, help_text='Key features or deliverables (one per line)')
    role_contribution = models.TextField(blank=True, help_text='Your specific role and contributions on this project')
    github_url = models.URLField(blank=True, help_text='GitHub repository link')
    live_url = models.URLField(blank=True, help_text='Live demo / deployed app link')
    featured = models.BooleanField(default=False, help_text='Show on homepage highlights')
    order = models.PositiveIntegerField(default=0, help_text='Display order — lower numbers appear first')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    gallery_images = models.CharField(max_length=1000, blank=True, help_text='Comma-separated image filenames for the gallery, e.g. "chart1.png, chart2.png"')
    project_file = models.FileField(upload_to='project_files/', blank=True, null=True, help_text='Downloadable project file (ZIP, PDF, etc.)')
    video = models.FileField(upload_to='project_videos/', blank=True, null=True, help_text='Project demo video (MP4)')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def tools_list(self):
        return [t.strip() for t in self.tools_used.split(',') if t.strip()]

    @property
    def image_url(self):
        if self.image:
            import os
            filename = os.path.basename(str(self.image))
            return f'/static/images/projects/{filename}'
        return ''

    @property
    def gallery_image_urls(self):
        if not self.gallery_images:
            return []
        return [f'/static/images/projects/{f.strip()}' for f in self.gallery_images.split(',') if f.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.name} — {self.subject}'
