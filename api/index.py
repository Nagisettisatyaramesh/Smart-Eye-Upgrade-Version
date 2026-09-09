import os
import sys

from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smarteye.settings')

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()

# Vercel's Python builder has no separate release/build step to run
# database migrations, so apply them once per cold start instead.
# Django's migrate command only applies migrations that haven't run
# yet, so this is a fast no-op on every warm invocation after the
# first. Failures are logged rather than raised so a database outage
# degrades to per-request errors instead of breaking every request.
if os.environ.get('VERCEL'):
    from django.core.management import call_command

    try:
        call_command('migrate', interactive=False, verbosity=0)
    except Exception as exc:
        print(f'[startup] migrate failed: {exc}')
    else:
        # Optional one-time bootstrap: if DJANGO_SUPERUSER_USERNAME and
        # DJANGO_SUPERUSER_PASSWORD are set and no superuser exists yet,
        # create one. There's no shell access to a serverless deployment
        # to run createsuperuser by hand, so this is the only way to get
        # an initial admin/workspace login without a local database.
        try:
            from django.contrib.auth import get_user_model

            User = get_user_model()
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
            if username and password and not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    username=username,
                    email=os.environ.get('DJANGO_SUPERUSER_EMAIL', ''),
                    password=password,
                )
                print(f'[startup] created superuser "{username}"')
        except Exception as exc:
            print(f'[startup] superuser bootstrap failed: {exc}')
