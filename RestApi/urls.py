
from django.contrib import admin
from django.urls import path, include
from empManagement import views
from empManagement.RestApiCall import RestApiView
from empManagement.ClientDataCapture import ClientDataTrackingApiView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
#https://www.django-rest-framework.org/api-guide/routers/
router.register('employeeapi', views.EmployeeViewSet, basename='employee')
router.register('client', views.ClientViewSet, basename='client')
router.register('todo', RestApiView.ToDoViewSet, basename='todo')
router.register('ClientDataCapture', ClientDataTrackingApiView.ClientDataCaptureViewSet, basename='ClientDataCapture')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]
#for url in router.urls :    print(url,'\n')
