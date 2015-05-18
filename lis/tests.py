import os, sys
from django.conf import settings

settings.configure(DEBUG=True,
               DATABASES={
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                    }
                },
               ROOT_URLCONF='myapp.urls',
               INSTALLED_APPS=('django.contrib.auth',
                              'django.contrib.contenttypes',
                              'django.contrib.sessions',
                              'django.contrib.admin',
                              'labeling',))

from django.test.simple import DjangoTestSuiteRunner
test_runner = DjangoTestSuiteRunner(verbosity=1)
failures = test_runner.run_tests(['labeling', ])
if failures:
    sys.exit(failures)
