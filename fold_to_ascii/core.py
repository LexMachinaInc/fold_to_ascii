# -*- coding: utf-8 -*-
from collections import defaultdict

from . import mapping


def none_factory():
    return None


default_translate_table = defaultdict(none_factory, mapping.translate_table)


def fold(unicode_string, replacement=u''):
    """Fold unicode_string to ASCII.

Unmapped characters should be replaced with empty string by default, or other
replacement if provided.

All astral plane characters are always removed, even if a replacement is
provided.
    """

    if unicode_string is None:
        return u''

    if not isinstance(unicode_string, str):
        raise TypeError('replace must be a str')

    if not isinstance(replacement, str):
        raise TypeError('replace must be a str')

    try:
        # If string contains only ASCII characters, just return it.
        unicode_string.encode('ascii')
        return unicode_string
    except (UnicodeDecodeError, UnicodeEncodeError):
        pass

    if replacement:
        def replacement_factory():
            return replacement

        translate_table = defaultdict(replacement_factory,
                                      mapping.translate_table)
    else:
        translate_table = default_translate_table

    return unicode_string.translate(translate_table)
