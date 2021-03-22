from django.urls import path
from validation_api import views

urlpatterns = [
    path('datacite/kernel-<str:version>/', views.AddMetaDataView.as_view()),
    path('datacite-validate/kernel-<str:version>/', views.ValidateMetaDataView.as_view())
]
