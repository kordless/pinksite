#!/usr/bin/env python
##
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__author__  = 'Kord Campbell'
__website__ = 'http://getpinkpanther.com/'

import os, sys

# set path to external libraries
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pinkpanther/external'))

# import the webapp2 application framework
import webapp2

# set up the URL routes and application config
import routes
import config

# set up the pinkpanther routes, config and errors
from pinkpanther import routes as pink_routes
from pinkpanther import config as pink_config
from pinkpanther.lib.error_handler import handle_error

# build the webapp configuration from the loaded configs
webapp2_config = pink_config
webapp2_config.update(config)

# fire up the webapp2 framework
app = webapp2.WSGIApplication(debug = os.environ['SERVER_SOFTWARE'].startswith('Dev'), config=webapp2_config)

if not app.debug:
    for status_int in app.config['error_templates']:
        app.error_handlers[status_int] = handle_error

# tell webapp2 about the routes
routes.add_routes(app)
pink_routes.add_routes(app)

