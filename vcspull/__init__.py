#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Manage multiple git, mercurial, svn repositories from a YAML / JSON file.

vcspull
~~~~~~~

:copyright: Copyright 2013-2015 Tony Narlock.
:license: BSD, see LICENSE for details

"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals, with_statement)

# Set default logging handler to avoid "No handler found" warnings.
import logging

from .cli import setup_logger
from .config import (extract_repos, filter_repos, in_dir, is_config_file,
                     load_configs)
from .log import DebugLogFormatter, LogFormatter, RepoFilter, RepoLogFormatter
from .util import mkdir_p, run, update_dict, which

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
