# {{ ansible_managed }}

SECRET_KEY = '{{ django_secret_key }}'
ALLOWED_HOSTS = ['{{ domain }}']
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# sentry
SENTRY_DSN = '{{ sentry_dsn }}'

{% block extra_vars %}{% endblock %}
