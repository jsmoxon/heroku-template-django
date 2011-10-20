#!/bin/bash
mv initial_data.json `date +"backup_fixtures/%Y-%m-%d_%H:%M:%S"`
python manage.py dumpdata expenses > initial_data.json
python manage.py flush --noinput
python manage.py collectstatic -l --noinput
python reset.py
find . -type f -name "*.pyc" -exec rm {} \;
find . -type f -name "*#" -exec rm {} \;
find . -type f -name "*~" -exec rm {} \;
