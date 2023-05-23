from django.urls import path
from . import views
urlpatterns=[
    path('',views.functionIndex,name='index'),
    path('location',views.functionLocation,name='location'),
    # path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('search',views.search,name='search'),
    path('login',views.functionLogin,name='login'),
    path('sorting',views.functionSorting,name='sorting'),
    path('schedule',views.functionSchedule,name='schedule'),
    path('contact',views.functionContact,name='contact')
]