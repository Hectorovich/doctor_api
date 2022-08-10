from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from doctor.models import Specialization, Doctor
from doctor.serializers import SpecializationSerializer, DoctorSerializer, DoctorDetailSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DoctorPagination(PageNumberPagination):
    page_size = 2


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination

    def get_queryset(self):
        specialization = self.request.query_params.get("specialization")
        experience = self.request.query_params.get("experience")

        ordering = self.request.query_params.get("ordering")

        queryset = self.queryset

        if specialization:
            queryset = queryset.filter(specializations__name__icontains=specialization)

        if experience:
            queryset = queryset.filter(experience__gte=int(experience))

        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return DoctorDetailSerializer

        return DoctorSerializer
