from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
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

# API URL patterns
urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Health check
    path('api/health/', health_check, name='health_check'),
    
    # Authentication endpoints
    path('api/login/', login_view, name='login'),
    path('api/register/', register_view, name='register'),
    path('api/logout/', logout_view, name='logout'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User profile endpoints
    path('api/profile/', user_profile_view, name='profile'),
    path('api/profile/update/', update_profile_view, name='update_profile'),
    path('api/change-password/', change_password_view, name='change_password'),
]