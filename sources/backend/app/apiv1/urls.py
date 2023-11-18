from django.urls import include, path
from rest_framework import routers

from apiv1.views import bookView

router = routers.DefaultRouter()

app_name = "apiv1"
urlpatterns = [
    path("", include(router.urls)),
    path("books", bookView.BookView.as_view()),
]
