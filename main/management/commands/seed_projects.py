"""
Usage: python manage.py seed_projects
Loads sample projects so the portfolio has content from day one.
"""
from django.core.management.base import BaseCommand
from main.models import Project

SAMPLE_PROJECTS = [
    {
        'title': 'Enterprise ERP Migration',
        'category': 'digital_transformation',
        'short_description': 'End-to-end business analysis and change management for a company-wide ERP transition serving 500+ users across three business units.',
        'description': (
            'Led the business analysis workstream for a full enterprise ERP migration from a legacy system to SAP S/4HANA. '
            'Responsibilities included stakeholder discovery workshops, as-is / to-be process mapping, functional requirements '
            'documentation, data migration planning, and UAT coordination across Finance, HR, and Operations divisions.\n\n'
            'Delivered a comprehensive Business Requirements Document (BRD) and 47 detailed user stories. '
            'Managed a cross-functional team of 12 across three time zones throughout the 8-month programme.'
        ),
        'tools_used': 'SAP S/4HANA, Jira, Confluence, Power BI, Visio, MS Project',
        'outcome': (
            '• Delivered on time and 4% under budget\n'
            '• Achieved 98% data migration accuracy on go-live\n'
            '• Reduced manual data entry by 65% through process automation\n'
            '• UAT completed with zero critical defects at go-live\n'
            '• 500+ users trained and onboarded within 3 weeks'
        ),
        'client_or_company': '[Financial Services Client]',
        'duration': '8 months',
        'featured': True,
        'order': 1,
    },
    {
        'title': 'Customer Onboarding Process Optimisation',
        'category': 'process_improvement',
        'short_description': 'Redesigned the end-to-end customer onboarding workflow, cutting processing time by 40% and reducing manual errors by 60%.',
        'description': (
            'Conducted an in-depth analysis of the existing customer onboarding workflow using BPMN process mapping and '
            'stakeholder interviews. Identified 14 redundant manual steps and 6 cross-team handover bottlenecks.\n\n'
            'Produced a TO-BE process design and collaborated with the development team to automate key touchpoints '
            'via ServiceNow workflows. Facilitated sign-off from Operations, Compliance, and IT leadership.'
        ),
        'tools_used': 'BPMN 2.0, Visio, ServiceNow, SQL, Jira, Confluence',
        'outcome': (
            '• Average onboarding time reduced from 5 days to 3 days (40% improvement)\n'
            '• Manual data errors reduced by 60%\n'
            '• Customer satisfaction (CSAT) score improved from 72% to 89%\n'
            '• Saved an estimated 120 person-hours per month across the operations team'
        ),
        'client_or_company': '[Telecoms Company]',
        'duration': '4 months',
        'featured': True,
        'order': 2,
    },
    {
        'title': 'Salesforce CRM Implementation',
        'category': 'crm_erp',
        'short_description': 'Managed full-lifecycle Salesforce CRM deployment for a mid-size financial services firm, achieving 95% user adoption within 90 days.',
        'description': (
            'Served as the lead Business Analyst and Project Manager for a Salesforce Sales Cloud implementation. '
            'Delivered end-to-end project management from vendor selection and requirements scoping through to configuration, '
            'integration with existing systems, data migration, and training rollout.\n\n'
            'Worked directly with the Head of Sales and 6 regional team leads to define workflows, dashboards, and '
            'reporting requirements. Facilitated 12 sprint reviews and maintained weekly executive status reporting.'
        ),
        'tools_used': 'Salesforce Sales Cloud, Agile/Scrum, MS Project, Tableau, Miro',
        'outcome': (
            '• 95% user adoption achieved within 90 days of go-live\n'
            '• Sales pipeline visibility improved — leadership reporting time reduced by 50%\n'
            '• Delivered in 6 months against a 7-month plan (1 month early)\n'
            '• Integrated with 3 existing internal systems with zero data loss'
        ),
        'client_or_company': '[Financial Services Firm]',
        'duration': '6 months',
        'featured': True,
        'order': 3,
    },
    {
        'title': 'Agile Transformation Programme',
        'category': 'project_management',
        'short_description': 'Drove the adoption of Agile/Scrum across a 60-person IT department, uplifting delivery velocity and team engagement.',
        'description': (
            'Championed and coordinated an Agile transformation initiative across 4 delivery teams within the IT department. '
            'Responsibilities included Agile coaching, Jira board setup, backlog grooming facilitation, and creation of '
            'standardised sprint ceremonies and reporting cadences.\n\n'
            'Developed an Agile Playbook tailored to the organisation\'s context and ran a 2-day workshop for 60+ team members. '
            'Worked alongside Scrum Masters to resolve impediments and track OKRs.'
        ),
        'tools_used': 'Jira, Confluence, Miro, MS Teams, Excel',
        'outcome': (
            '• Sprint velocity improved by 25% over 3 sprints post-transformation\n'
            '• On-time delivery rate increased from 68% to 89%\n'
            '• Team engagement scores improved by 18 points (Gallup Q12)\n'
            '• Reduced average bug resolution time from 12 days to 5 days'
        ),
        'client_or_company': '[Technology Consultancy]',
        'duration': '5 months',
        'featured': False,
        'order': 4,
    },
    {
        'title': 'Power BI Executive Dashboard Suite',
        'category': 'data_analytics',
        'short_description': 'Designed and delivered a suite of Power BI dashboards enabling C-suite real-time visibility into KPIs across 5 business units.',
        'description': (
            'Collaborated with the CFO, COO, and department heads to define KPI frameworks and reporting requirements. '
            'Designed and built 8 interconnected Power BI dashboards drawing from SQL Server, SharePoint, and Salesforce data sources.\n\n'
            'Implemented row-level security and automated daily data refresh schedules. '
            'Delivered training sessions and a self-service user guide for 30+ report consumers.'
        ),
        'tools_used': 'Power BI, SQL Server, DAX, SharePoint, Salesforce, Excel',
        'outcome': (
            '• Executive decision-making time reduced — weekly reporting meetings cut from 2 hours to 30 minutes\n'
            '• 30+ users onboarded to self-service reporting\n'
            '• Identified a data quality issue saving an estimated $120K in mis-reported revenue\n'
            '• Dashboard suite adopted as the company-wide standard for performance reporting'
        ),
        'client_or_company': '[Retail Group]',
        'duration': '3 months',
        'featured': False,
        'order': 5,
    },
]


class Command(BaseCommand):
    help = 'Seed the database with sample portfolio projects'

    def handle(self, *args, **options):
        created = 0
        for data in SAMPLE_PROJECTS:
            _, was_created = Project.objects.get_or_create(title=data['title'], defaults=data)
            if was_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f'  Created: {data["title"]}'))
            else:
                self.stdout.write(f'  Skipped (already exists): {data["title"]}')

        self.stdout.write(self.style.SUCCESS(f'\nDone. {created} project(s) created.'))
