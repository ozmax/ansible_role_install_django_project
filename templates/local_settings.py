# {{ ansible_managed }}

SECRET_KEY = '{{ django_secret_key }}'
ALLOWED_HOSTS = ['{{ domain }}']
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# mailchimp
MAILCHIMP_API_KEY = '{{ mailchimp_api_key }}'
MAILCHIMP_LIST_ID = '{{ mailchimp_list_id }}'
MAILCHIMP_DATA_CENTER = '{{ mailchimp_data_center }}'

# email credentials
EMAIL_HOST_USER = '{{ email_user }}'
EMAIL_HOST_PASSWORD = '{{ email_password }}'

# sentry
SENTRY_DSN = '{{ sentry_dsn }}'
