# -*- coding: utf-8 -*-
## This file is part of Invenio.
## Copyright (C) 2012, 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Implements an example of a typical ingestion workflow for MARCXML records"""

from invenio.modules.workflows.tasks.marcxml_tasks import (approve_record,
                                                           convert_record)


class marcxml_workflow(object):
    """
    This workflow will run various tasks required to ingesting
    MARCXML records.
    """
    workflow = [convert_record(),
                approve_record]
    title = "Workflow for ingesting MARCXML records"