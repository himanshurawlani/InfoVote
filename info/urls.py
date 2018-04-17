from django.urls import path

from info import views

app_name = 'info'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search/', views.search_keyword, name='search'),
    path('details/<str:pk>/', views.ConstituencyDetail.as_view(), name='details'),
    path('profile/<int:pk>/', views.CandidateDetail.as_view(), name='profile'),
    path('results/<str:search_param>/<str:search_key>/', views.ResultsView.as_view(), name='results'),
    path('party/', views.PartyView.as_view(), name='party'),
]