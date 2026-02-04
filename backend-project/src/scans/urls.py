from django.urls import path
from .views import (
    ScanStartView,
    ScanStatusView,
    ScanResultView,
    ScanCancelView,
    ScanRemoveView,
)

urlpatterns = [
    path("start/", ScanStartView.as_view()),
    path("status/<uuid:job_id>/", ScanStatusView.as_view()),
    path("result/<uuid:job_id>/", ScanResultView.as_view()),
    path("cancel/<uuid:job_id>/", ScanCancelView.as_view()),
    path("remove/<uuid:job_id>/", ScanRemoveView.as_view()),
]
