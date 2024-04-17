from django.urls import path, include

from bood_account.views import CustomTokenObtainPairView, CustomTokenRefreshView, CustomTokenVerifyView, LogoutView

urlpatterns = [
    path(r"", include("djoser.urls")),
    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
]
