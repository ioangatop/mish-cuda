from django.urls import path,re_path
from django.shortcuts import redirect, reverse, render
from datas import generics_views, api_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda r: render(r, 'index.html')),

    # generics
    path('generic/', generics_views.ListView.as_view(),
         name=generics_views.ListView.name),
    path('generic/list/<pk>/', generics_views.ListDetail.as_view(),
         name=generics_views.ListDetail.name),
    path('generic/substruct/', generics_views.ListSubstruct.as_view(),
         name=generics_views.ListSubstruct.name),
    path('generic/list/', lambda request: redirect(reverse(generics_views.ListView.name))),

    # apiview
    path('api/', api_views.ListAPIView.as_view(),
         name=api_views.ListAPIView.name),
    path('api/list/<pk>/', api_views.DetailAPIView.as_view(),
         name=api_views.DetailAPIView.name),
    path('api/list/', lambda request: redirect(reverse(api_views.ListAPIView.name))),
    path('api/substruct/', api_views.ListSubstruct.as_view(),
         name=api_views.ListSubstruct.name),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
