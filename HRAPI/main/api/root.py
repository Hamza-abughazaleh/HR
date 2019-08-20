import collections

from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, authentication


def PUBLIC_APIS(r, f):
    return [
        ('candidates-registration', reverse('candidates-registration', request=r, format=f)),
        ('login', reverse('api-login', request=r, format=f)),
        ('logout', reverse('api-logout', request=r, format=f))

    ]


def PROTECTED_APIS(r, f):
    return [
        ('candidates-list', reverse('candidates-list', request=r, format=f)),
    ]


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    GET:
    Display all available urls.

    Since some urls have specific permissions, you might not be able to access
    them all.
    """
    apis = PUBLIC_APIS(request, format)
    key = authentication.get_authorization_header(request)
    if request.user.is_superuser and key.decode() == "X-ADMIN=1":
        apis += PROTECTED_APIS(request, format)

    return Response(collections.OrderedDict(apis))
