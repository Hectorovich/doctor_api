from django.urls import path, include
from rest_framework import routers

from doctor.views import SpecializationViewSet, DoctorViewSet

router = routers.DefaultRouter()
router.register("specializations", SpecializationViewSet)
router.register("doctors", DoctorViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "doctor"
