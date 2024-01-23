from django.urls import path

from users.views import UserFilterView


urlpatterns = [
    path('filtered-users/', UserFilterView.as_view(), name='filtered_users'),
]