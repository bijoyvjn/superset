1. created superset_config.py file and created SECRET_KEY for run it locally
	we already have default config.py, so the superset_config.py will loads last and it will override default config.py file
2. created multi_auth.py file in repository -> superset/superset/security/multi_auth.py
3. in the superset_config.py file assigined CUSTOM_SECURITY_MANAGER as MultiAuthSecurityManager
4. created new file superset/security/views.py
5. added new logic in the view and added path in multi_auth 
	Uses your custom login page instead of default DB login view.
