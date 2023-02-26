# Custom exception to show when a key is not found in the prefix class

from django.utils.translation import gettext_lazy as _


class KIDXPrefixNotFound(Exception):
    def __init__(self, key):
        self.key = key
        self.message = _("Key %s not found in the prefix class.") % self.key
        super().__init__(self.message)


class KIDXNotImplementedProperly(Exception):
    def __init__(self):
        self.message = _("Prefix class either not found or not implemented.")
        super().__init__(self.message)
