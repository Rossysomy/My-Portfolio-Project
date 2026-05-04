#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py shell -c "from main.models import Project; Project.objects.all().delete()"
python manage.py loaddata main/fixtures/projects.json
