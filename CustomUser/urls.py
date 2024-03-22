
from django.contrib import admin
from django.urls import path
from APP.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('stdRegister',register_student,name="stdRegister"),
    path('stdLogin',login_student,name="stdLogin"),
    path('staffLogin',staff_login,name="staffLogin"),
    path('staffRegister',staff_register,name="staffRegister"),
    path('logoutUser',logoutUser,name='logoutUser'),
    path('applyBonaifde',applyBonaifde,name="applyBonaifde"),
    path('acceptBonafideRequest/<int:requestId>',acceptBonafideRequest,name="acceptBonafideRequest"),
    path('rejectBonafideRequest/<int:requestId>',rejectBonafideRequest,name="rejectBonafideRequest")
    


]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

