# KIDX

Khalti flavored IDX field for django.

Quick start
-----------

1. Add "kidx" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'kidx',
    ]

2. Include the kidx field in your models like this::

    from kidx.fields import KIDXField

    class MyModel(models.Model):
        ...
        kidx = KIDXField()

3. Create a Class for model prefixes like this::

    from kidx.prefixes import KIDXPrefixes

    class MyPrefix(KIDXPrefixes):
        myapp_mymodel = 'MY'

4. Update setting to use your prefix class::

    KIDX_PREFIX_CLASS = 'appName.moduleName.className'

5. Create migration and migrate.