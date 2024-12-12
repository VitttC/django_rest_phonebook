from django.urls import path, include

from rest_framework.routers import DefaultRouter

from contacts import views

# Create a router and register the ViewSet with it.
router = DefaultRouter()
router.register(r'contacts', views.ContactViewSet, basename='contact')
router.register(r'users', views.UserViewSet, basename='user')


# API endpoints
urlpatterns = [
    path('', include(router.urls)),
]


urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
