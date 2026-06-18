from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

try:
    from rest_framework_simplejwt.views import TokenRefreshView
except Exception:
    # Fallback stub if rest_framework_simplejwt is not available (avoids import errors in editors)
    class TokenRefreshView:
        @classmethod
        def as_view(cls):
            def view(request, *args, **kwargs):
                return JsonResponse({'detail': 'rest_framework_simplejwt not installed'}, status=501)
            return view
from accounts.views import (
    login_view,
    register_view,
    user_profile_view,
    update_profile_view,
    change_password_view,
    logout_view,
    health_check,
    CustomTokenObtainPairView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health/', health_check, name='health_check'),
    path('api/login/', login_view, name='login'),
    path('api/register/', register_view, name='register'),
    path('api/logout/', logout_view, name='logout'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profile/', user_profile_view, name='profile'),
    path('api/profile/update/', update_profile_view, name='update_profile'),
    path('api/change-password/', change_password_view, name='change_password'),
]