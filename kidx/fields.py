from datetime import date
from django.conf import settings
from django.db import models
from shortuuid import ShortUUID
from .exceptions import KIDXNotImplementedProperly


prefix_class = getattr(settings, "KIDX_PREFIX_CLASS", None)
if prefix_class is None or len(prefix_class.split(".")) != 3:
    raise KIDXNotImplementedProperly()


module_name = ".".join(prefix_class.split(".")[:2])
class_name = prefix_class.split(".")[-1]
module = __import__(module_name, fromlist=[class_name])
KIDXPrefixes = getattr(module, class_name)


class KIDXField(models.CharField):
    description = "A khalti flavoured IDX field."
    alphabet = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"

    def __init__(self, *args, **kwargs):
        self.length = kwargs.pop("length", 8)

        if "max_length" not in kwargs:
            kwargs["max_length"] = 15

        kwargs.update({"unique": True, "editable": False, "blank": True})

        super().__init__(*args, **kwargs)

    def _generate_uuid(self, _prefix):
        """Generate a short random string."""
        _year = str(date.today().year)[2:]
        _uuid = ShortUUID(alphabet=self.alphabet).random(length=self.length)
        return f"{_prefix}{_year}{_uuid}".upper()

    def pre_save(self, instance, add):
        """
        This is used to ensure that we auto-set values if required.
        See CharField.pre_save
        """

        value = super().pre_save(instance, add)
        if not value:
            _table_name = instance._meta.db_table
            prefix = KIDXPrefixes.get(_table_name)
            value = self._generate_uuid(prefix)
        setattr(instance, self.attname, value)
        return value

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["length"] = self.length
        kwargs.pop("default", None)
        return name, path, args, kwargs
