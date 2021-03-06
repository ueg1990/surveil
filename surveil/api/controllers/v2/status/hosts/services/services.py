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

import pecan
from pecan import rest
import wsmeext.pecan as wsme_pecan

from surveil.api.controllers.v2.status.hosts.services import (
    metrics as services_metrics)
from surveil.api.controllers.v2.status.hosts.services import (
    results as services_check_results)
from surveil.api.datamodel.status import live_service
from surveil.api.handlers.status import live_service_handler
from surveil.common import util


class ServicesController(rest.RestController):

    @pecan.expose()
    def _lookup(self, service_name, *remainder):
        return ServiceController(service_name), remainder


class ServiceController(rest.RestController):

    metrics = services_metrics.MetricsController()
    results = services_check_results.CheckResultsSubController()

    def __init__(self, service_name):
        pecan.request.context['service_name'] = service_name
        self.service_name = service_name

    @util.policy_enforce(['authenticated'])
    @wsme_pecan.wsexpose(live_service.LiveService)
    def get(self):
        """Returns a specific host service."""
        handler = live_service_handler.ServiceHandler(pecan.request)
        service = handler.get(
            pecan.request.context['host_name'],
            self.service_name
        )
        return service
