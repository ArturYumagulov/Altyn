from django.urls import path

from . import views

urlpatterns = [
    path('vote/', views.vote, name='vote'),
    path('voting-detail/<slug:slug>', views.voting_detail, name='voting_detail')
]