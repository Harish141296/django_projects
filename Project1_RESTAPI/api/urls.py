from django.urls import path 
from . import views
urlpatterns = [
    path('blogposts/',views.BlogPostListCreate.as_view(), name='BlogPostListCreate'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'),

]