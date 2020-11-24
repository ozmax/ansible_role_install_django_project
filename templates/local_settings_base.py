# {{ ansible_managed }}
DEBUG = False
SECRET_KEY = '{{ django_secret_key }}'
ALLOWED_HOSTS = ['{{ domain }}']
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

{% block extra_vars %}{% endblock %}
