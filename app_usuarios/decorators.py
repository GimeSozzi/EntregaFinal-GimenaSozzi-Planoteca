from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def admin_or_superuser_only(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_superuser or request.user.groups.filter(name='Administradores').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("No tienes permisos para acceder a esta página.")
    return _wrapped_view
