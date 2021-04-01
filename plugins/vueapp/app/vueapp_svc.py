import logging


class VueappService:
    def __init__(self, services):
        self.services = services
        self.file_svc = services.get('file_svc')
        self.log = logging.getLogger('vueapp_svc')

    async def foo(self):
        return 'bar'

    # Add functions here that call core services
