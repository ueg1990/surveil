# Copyright 2014 - Savoir-Faire Linux inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json

import wsme
import wsme.types as wtypes

from surveil.api.datamodel.status.metrics import time_interval
from surveil.api.datamodel.status import paging
from surveil.api.datamodel import types


class LiveQuery(types.Base):
    """Holds a sample query encoded in json."""

    filters = wsme.wsattr(wtypes.text, mandatory=False)
    "The filter expression encoded in json."

    fields = wsme.wsattr([wtypes.text], mandatory=False)
    "List of fields to include in the response."

    time_interval = wsme.wsattr(time_interval.TimeInterval, mandatory=False)
    "Time interval of the query."

    paging = wsme.wsattr(paging.Paging, mandatory=False)
    "Paging."

    search = wsme.wsattr(wtypes.text, mandatory=False)

    @classmethod
    def sample(cls):
        return cls(
            fields=['host_name', 'last_check'],
            time_interval=time_interval.TimeInterval(
                start_time='2015-01-29T21:50:44Z',
                end_time='2015-01-29T22:50:44Z'
            ),
            paging=paging.Paging(
                page=3,
                size=100
            ),
            filters=json.dumps({
                "isnot": {
                    "state": ["0", "1"],
                    "host_state": ["2"]
                },
                "is": {
                    "event_type": ["ALERT"]
                },
                "defined": {
                    "name": True
                }
            }),
            search='web'
        )
