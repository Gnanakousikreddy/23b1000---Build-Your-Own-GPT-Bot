from django.urls import path
from . import views


urlpatterns = [
    path("", views.chat_view, name="chat"),   # your main page (if needed)
    path("api/chat/", views.chat_api, name="chat_api"),  # new API endpoint
]
