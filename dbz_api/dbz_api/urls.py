from django.conf.urls import url, include
from rest_framework import routers
from details import views

router = routers.DefaultRouter()
router.register(r'abilities', views.AbilitiesViewSet)
#NOT SURE ABOUT THE UNDERSCORE
router.register(r'character_statistics', views.CharacterStatisticsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




# from django.conf.urls import url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
