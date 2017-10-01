#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe39c86b5

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
The serving backend. Selects the best existing data point.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



# Imports:

from bbopt.util import best_example

# Backend:

class ServingBackend(_coconut.object):
    """The serving backend uses the parameter values from the best example."""

    def __init__(self, examples, params):  # ignore params since we're serving
        self.serving_values = best_example(examples)["values"]

    def param(self, name, **kwargs):  # ignore kwargs since we're serving
        try:
            return self.serving_values[name]
        except KeyError:
            raise ValueError("missing data for parameter %r" % name)
