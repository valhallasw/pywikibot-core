# -*- coding: utf-8  -*-
"""Enum representing Login statuses."""
#
# (C) Pywikibot team, 2008-2015
#
# Distributed under the terms of the MIT license.
#
from __future__ import unicode_literals


class LoginStatus(object):

    """Enum for Login statuses.

    >>> LoginStatus.NOT_ATTEMPTED
    -3
    >>> LoginStatus.AS_USER
    0
    >>> LoginStatus.name(-3)
    'NOT_ATTEMPTED'
    >>> LoginStatus.name(0)
    'AS_USER'
    """

    NOT_ATTEMPTED = -3
    IN_PROGRESS = -2
    NOT_LOGGED_IN = -1
    AS_USER = 0
    AS_SYSOP = 1

    @classmethod
    def name(cls, search_value):
        """Return the name of a LoginStatus by it's value."""
        for key, value in cls.__dict__.items():
            if key == key.upper() and value == search_value:
                return key
        raise KeyError("Value %r could not be found in this enum"
                       % search_value)

    def __init__(self, state):
        """Constructor."""
        self.state = state

    def __repr__(self):
        """Return internal representation."""
        return 'LoginStatus(%s)' % (LoginStatus.name(self.state))
