"""
URL configuration for college_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from students import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="students/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("students/", views.student_list, name="student_list"),
    path("add/", views.add_student, name="add_student"),
    path("student/<int:pk>/", views.student_detail, name="student_detail"),
    path("student/<int:pk>/edit/", views.edit_student, name="edit_student"),
    path("student/<int:pk>/delete/", views.delete_student, name="delete_student"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
