"""austin URL Configuration

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
from app.views import home, efficient_home, population_density_geojson, map_page, get_tracts_by_state
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("hi", efficient_home, name="efficient_home"),
    path("population_density_geojson.json", population_density_geojson, name="population_density_geojson"),
    path("map/", map_page, name="map"),
    path("get_tracts.json", get_tracts_by_state, name="get_tracts")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
