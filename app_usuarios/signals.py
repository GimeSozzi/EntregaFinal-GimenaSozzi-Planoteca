from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app_proyectos.models import Proyecto  # Asegúrate de que esto coincida con tu modelo de proyecto

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Crear grupo de Administradores
    admin_group, _ = Group.objects.get_or_create(name='Administradores')
    # Asignar todos los permisos al grupo de Administradores
    for permission in Permission.objects.all():
        admin_group.permissions.add(permission)

    # Crear grupo de Operadores
    operator_group, _ = Group.objects.get_or_create(name='Operadores')
    # Asignar permisos específicos al grupo de Operadores
    content_type = ContentType.objects.get_for_model(Proyecto)
    perms = Permission.objects.filter(content_type=content_type).filter(codename__in=['add_proyecto', 'view_proyecto'])
    for perm in perms:
        operator_group.permissions.add(perm)
