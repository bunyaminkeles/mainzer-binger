from django.apps import AppConfig


class AlmancaConfig(AppConfig):
    name = 'almanca'
    verbose_name = 'Almanca'

    def ready(self):
        from django.contrib.auth.signals import user_logged_in

        def clear_almanca_session(sender, request, user, **kwargs):
            keys = [k for k in list(request.session.keys()) if k.startswith('alm_')]
            for k in keys:
                del request.session[k]

        user_logged_in.connect(clear_almanca_session)
