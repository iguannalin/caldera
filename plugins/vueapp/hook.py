from app.utility.base_world import BaseWorld
from plugins.vueapp.app.vueapp_gui import VueappGUI
from plugins.vueapp.app.vueapp_api import VueappAPI

name = 'Vueapp'
description = 'Testing out a plugin with vue'
address = '/plugin/vueapp/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app = services.get('app_svc').application
    vueapp_gui = VueappGUI(services, name=name, description=description)
    app.router.add_static('/vueapp', 'plugins/vueapp/static/', append_version=True)
    app.router.add_route('GET', '/plugin/vueapp/gui', vueapp_gui.splash)

    vueapp_api = VueappAPI(services)
    # Add API routes here
    app.router.add_route('POST', '/plugin/vueapp/mirror', vueapp_api.mirror)

