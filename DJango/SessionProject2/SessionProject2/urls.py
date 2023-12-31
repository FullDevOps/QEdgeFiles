"""SessionProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from MyApps1 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # session-application-1
    path('pagecount/', views.page_count_view),

    # Session-Application-2
    path('name/', views.name_view),
    path('age/', views.age_view),
    path('parent/', views.parent_view),
    path('results/', views.result_view),

    # Application-3
    path('additem2/', views.add_item_view),
    path('display/', views.display_items_view),

    path('clear/', views.clear_session),

]
