from django.urls import path
from . import views,api

from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("api",api.Dlist,name='json'),
    path("api/post",api.Dlist,name='json'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('index/',views.table,name='table'),
    path('myChart/',views.graphique,name='myChart'),
    path ('chart_data/',views.chart_data, name='chart_data'),
    path('chart_data_jour/',views.chart_data_jour,name='chart_data_jour'),
    path('chart_data_semaine/',views.chart_data_semaine,name='chart_data_semaine'),
    path('chart_data_mois/',views.chart_data_mois,name='chart_data_mois'),
    path('', views.home, name='home'),
    path('table/', views.table, name='table'),
    path('', views.test, name='test'),
    path('api', api.Dlist, name='json'),
    path('ChartTemp/',views.graphiquetemp,name='myChartTemp'),
path('ChartHum/',views.graphiquehum,name='myChartHum'),
]