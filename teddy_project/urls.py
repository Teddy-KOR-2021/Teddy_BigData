from django.contrib import admin
from django.urls import path
import analysis_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', analysis_app.views.index),
    path('testdg1/', analysis_app.views.dg1),
    path('dg1data/', analysis_app.views.dg1data),
    path('testdg2/', analysis_app.views.dg2),
    path('testdg3/', analysis_app.views.dg3),
    path('dg3data/', analysis_app.views.dg3data),
    path('testdg4/', analysis_app.views.dg4),
    path('dg4data/', analysis_app.views.dg4data),
    path('dg4data2/', analysis_app.views.dg4data2),
    path('testdg5/', analysis_app.views.dg5),
]
