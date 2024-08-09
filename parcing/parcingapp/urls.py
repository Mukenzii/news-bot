from django.urls import path,include
from .views import NewsViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'news', NewsViewset)

urlpatterns = [
    path('api/', include(router.urls))
]