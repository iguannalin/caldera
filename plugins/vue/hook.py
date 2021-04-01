from app.utility.base_world import BaseWorld
from plugins.vue.app.vue_gui import VueGUI
from plugins.vue.app.vue_api import VueAPI

name = 'Vue'
description = 'Testing out a plugin with vue'
address = '/plugin/vue/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app = services.get('app_svc').application
    vue_gui = VueGUI(services, name=name, description=description)
    app.router.add_static('/vue', 'plugins/vue/templates/vue', append_version=True)
    app.router.add_route('GET', '/plugin/vue/gui', vue_gui.splash)

    vue_api = VueAPI(services)
    # Add API routes here
    app.router.add_route('POST', '/plugin/vue/mirror', vue_api.mirror)

