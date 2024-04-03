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
from app.views import landing_page, benny_boy_resume, homepage, get_group_map, get_geojson_by_cbsa, get_group_geojson_by_cbsa, population_density_geojson, map_page, get_tracts_by_state, acs_concept_by_id, get_demographic_data_by_metro, list_msas, msa_search, list_acs_variables, get_map
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", homepage, name="homepage"),
    path("resume", benny_boy_resume, name="resume"),
    path("admin/", admin.site.urls),
    path("population_density_geojson.json", population_density_geojson, name="population_density_geojson"),
    path("map/", map_page, name="map"),
    path("get_tracts.json", get_tracts_by_state, name="get_tracts"),
    path("get_demographic_data_by_metro.json", get_demographic_data_by_metro, name="get_demographic_data_by_metro"),
    path("list_msas", list_msas, name="list_msas"),
    path("search", msa_search, name="msa_search"),
    path("list_acs_variables", list_acs_variables, name="list_acs_variables"),
    path("acs_concept_by_id", acs_concept_by_id, name="acs_concept_by_id"),
    path("jsonify.json", get_geojson_by_cbsa, name="get_geojson_by_cbsa"),
    path("group.json", get_group_geojson_by_cbsa, name="get_group_geojson_by_cbsa"),
    path("get_map/", get_map, name="get_map"),
    path("get_group_map/", get_group_map, name="get_group_map"),
    path("landing_page", landing_page, name="landing_page")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
