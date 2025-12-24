"""Authentication views."""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer, UserSerializer


class LoginView(APIView):
    """Handle user login and return JWT tokens."""

    permission_classes = [AllowAny]

    def post(self, request):
        """Authenticate user and return tokens."""
        serializer = LoginSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    """Handle user logout by blacklisting refresh token."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Blacklist the refresh token."""
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logout successful."}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserView(APIView):
    """Get current authenticated user details."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return current user data."""
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
