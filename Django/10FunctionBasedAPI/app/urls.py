from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  StaffEnquiryViewSet, StudentEnquiryViewSet

router = DefaultRouter()
router.register(r'ENQUIRY', StudentEnquiryViewSet)
router.register(r'staffENQUIRY', StaffEnquiryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]