from django.contrib.auth import login, logout
from rest_framework import generics, status
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from main.api.serializer import CandidatesSerializer, CandidatesListSerializer, CandidatesDetailSerializer, \
    LoginSerializer
from main.models import Candidates


class CandidatesCreateAPIView(generics.CreateAPIView):
    queryset = Candidates.objects.all()
    serializer_class = CandidatesSerializer
    permission_classes = (AllowAny,)


class CandidatesViewSet(viewsets.ModelViewSet):
    """ViewSet for the PartnerProgram class"""
    queryset = Candidates.objects.all().order_by('-date_joined')
    serializer_class = CandidatesListSerializer
    details_serializer_class = CandidatesDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        kwargs['context'] = self.get_serializer_context()
        serializer = self.details_serializer_class(instance, context={'request': request})
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        filtered_queryset = super(CandidatesViewSet, self).filter_queryset(queryset)
        return filtered_queryset.filter(is_superuser=False)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    # API for retail user login
    def post(self, request):
        self.ser = self.serializer_class(data=request.data)
        if self.ser.is_valid():
            self.user = self.ser.instance
            login(request, self.user)
            # refuse to login logged in users, to avoid attaching sessions to
            # multiple users at the same time.
            if request.user.is_authenticated:
                return Response(
                    {'detail': 'Session is in use, log out first'},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED)

            return Response("ok")

        return Response(self.ser.errors, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def get(self, request):
        request = request._request
        if request.user.is_anonymous:
            return Response(
                {'detail': 'You Must Login First'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        logout(request)
        request.session.clear()
        request.session.delete()

        return Response("ok")
