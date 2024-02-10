# from django.urls import path

# from .import users

# urlpatterns = [
#     path('users/', users)
# ]


from django.urls import path
from .views import *

urlpatterns = [
    path("say_hello/",say_hello),
    path("profile/",user_profile),
    path('filter_queries/<int:query_id>/', filter_queries),
    path("queries/",QueryViews.as_view(),name="query-view")
    
]