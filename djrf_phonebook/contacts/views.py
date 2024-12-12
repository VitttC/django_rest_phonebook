from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from contacts.models import Contact
from contacts.serializers import ContactSerializer, UserSerializer
from contacts.permissions import IsOwnerOrReadOnly


"""
Endpoint for API root.
"""
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users':reverse('user-list', request=request, format=format),
        'contacts': reverse('contact-list', request=request, format=format),
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'retrieve' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)