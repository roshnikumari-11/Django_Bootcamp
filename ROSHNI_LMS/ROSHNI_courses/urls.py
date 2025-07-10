from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.ROSHNI_lmsSignupUser.as_view()),
    path("getAllUser/", views.ROSHNI_lmsGetUserDetails.as_view()),
    path("updateEmail/",views.ROSHNI_lmsUpdateEmail.as_view()),
    path("deleteUser/<number>/",views.ROSHNI_lmsDeleteUser.as_view())
]
