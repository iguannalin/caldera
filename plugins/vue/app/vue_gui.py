import logging
from aiohttp_jinja2 import template

from app.service.auth_svc import for_all_public_methods, check_authorization
from app.utility.base_world import BaseWorld
from plugins.vue.app.vue_svc import VueService


@for_all_public_methods(check_authorization)
class VueGUI(BaseWorld):

    def __init__(self, services, name, description):
        self.name = name
        self.description = description
        self.services = services
        self.vue_svc = VueService(services)

        self.auth_svc = services.get('auth_svc')
        self.log = logging.getLogger('vue_gui')

    # this still uses jinja templates to render--can we completely move away from jinja and expose a static folder?
    @template('vue.html')
    async def splash(self, request):
        return dict(name=self.name, description=self.description)

    # Add functions here that the front-end will use

