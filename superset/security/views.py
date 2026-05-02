from flask import flash, redirect, request, url_for, current_app
from flask_appbuilder.security.views import AuthDBView, AuthOAuthView
from flask_login import login_user
from flask_appbuilder import expose
from flask_appbuilder.const import AUTH_OAUTH


class MultiAuthDBView(AuthDBView):
    @expose("/login/", methods=["GET", "POST"])
    def login(self):
        if request.method == "GET":
            return super().login()

        username = request.form.get("username")
        password = request.form.get("password")
        sm = self.appbuilder.sm

        print("-----------------AUTH_DB check-----------------")
        user = sm.auth_user_db(username, password)

        if not user:
            try:
                print("-----------------AUTH_LDAP check-----------------")
                user = sm.auth_user_ldap(username, password)
            except Exception:
                user = None
        
        if not user:
            print("----------------- AUTH_OAUTH check-----------------")
            return redirect(url_for("AuthOAuthView.login", provider="github"))
            # return redirect("/login/github")
        if user:
            login_user(user, remember=False)
            return redirect(url_for("Superset.welcome"))
        
        flash("Invalid login", "warning")
        return super().login()


