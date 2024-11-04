from django.urls import path

from home.views import(
    index_view,
    LoginView,
    LogoutView,
    RegisterView,
    about_us,
    UpdateLang,
)

from . import views

urlpatterns = [
    path(route="", view=index_view, name='index'),
    path(route="login/", view=LoginView.as_view(), name='login'),
    path(route="logout/", view=LogoutView.as_view(), name='logout'),
    path(route="register/", view=RegisterView.as_view(), name='register'),
    path('sobre_nosotros/', views.about_us, name='about_us'),  
    path('update_lang/', view=UpdateLang.as_view(), name='update_lang'),  

]