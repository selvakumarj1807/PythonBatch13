from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from app.models import StaffEnquiry, StudentEnquiry
from app.serializers import StaffEnquirySerializer, StudentEnquirySerializer


class StudentEnquiryViewSet(viewsets.ModelViewSet):
    queryset = StudentEnquiry.objects.all()
    serializer_class = StudentEnquirySerializer

    def create(self, request):
        """Create a new StudentEnquiry"""
        serializer = StudentEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'StudentEnquiry Inserted successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        """List all StudentEnquiries or filter by name or mobile"""
        name = request.query_params.get('name')
        mobile = request.query_params.get('mobileNumber')

        if name:
            studentEnquiries = StudentEnquiry.objects.filter(name__icontains=name)
        elif mobile:
            studentEnquiries = StudentEnquiry.objects.filter(mobile__icontains=mobile)
        else:
            studentEnquiries = StudentEnquiry.objects.all()

        serializer = StudentEnquirySerializer(studentEnquiries, many=True)
        return Response({
            'count': studentEnquiries.count(),
            'data': serializer.data
        })
        
    from rest_framework.decorators import action

    @action(detail=False, methods=['get'], url_path='get_by_mobile')
    def get_by_mobile(self, request):
        """Get StudentEnquiry by mobile using ?mobile= """
        mobile = request.query_params.get('phone')
        if not mobile:
            return Response({'error': 'mobile parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        studentEnquiries = StudentEnquiry.objects.filter(mobile__icontains=mobile)
        serializer = StudentEnquirySerializer(studentEnquiries, many=True)
        return Response({
            'count': studentEnquiries.count(),
            'data': serializer.data
        })



    def update(self, request, pk=None):
        """Update an entire StudentEnquiry"""
        studentEnquiry = get_object_or_404(StudentEnquiry, pk=pk)
        serializer = StudentEnquirySerializer(studentEnquiry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'StudentEnquiry Updated successfully',
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Delete a StudentEnquiry"""
        studentEnquiry = get_object_or_404(StudentEnquiry, pk=pk)
        studentEnquiry.delete()
        return Response({'message': 'StudentEnquiry deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    
    
class StaffEnquiryViewSet(viewsets.ModelViewSet):
    queryset = StaffEnquiry.objects.all()
    serializer_class = StaffEnquirySerializer

    def create(self, request):
        """Create a new StaffEnquiry"""
        serializer = StaffEnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'StaffEnquiry Inserted successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    