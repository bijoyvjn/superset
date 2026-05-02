from flask_appbuilder.const import AUTH_DB
from superset.security import SupersetSecurityManager
from superset.security.views import MultiAuthDBView
from .views import MultiAuthDBView

class MultiAuthSecurityManager(SupersetSecurityManager):
    authdbview = MultiAuthDBView

    @property
    def auth_type(self):
        return AUTH_DB

    @property
    def oauth_providers(self):
        return self.appbuilder.get_app.config.get("OAUTH_PROVIDERS", [...])

    def register_views(self):
        super().register_views()
        try:
            self.appbuilder.add_view_no_menu(self.authdbview())
        except Exception as ex:
            print("Error registering custom login view:", ex)

