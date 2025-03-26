from django.urls import path
from .views import AddHealthRecordView, GetHealthRecordsView

urlpatterns = [
    path('add/', AddHealthRecordView.as_view(), name='add_record'),
    path('list/', GetHealthRecordsView.as_view(), name='list_records'),
]