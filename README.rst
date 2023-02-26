===
KIDX
===

Khalti flavored IDX field for django.

Quick start
-----------

1. Add "kidx" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'kidx',
    ]

2. Include the kidx field in your models like this::

    from kidx import KIDXField

    class MyModel(models.Model):
        ...
        kidx = KIDXField()

3. Create a Class for model prefixes like this:

    from kidx import KIDXPrefixes

    class MyPrefix(KIDXPrefixes):
        {db_table} = {prefix}

    # Example

    class MyPrefix(KIDXPrefixes):
        myapp_mymodel = 'MY'
