from django.urls import path
from .views import *
 

app_name = 'main'

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="kirish"),
    path('/contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', contact_us_success, name='contact_us_success'),
    #4-lesson.homework(urls.py_code)
    path('tag_create',TagView.as_view(), name='tag_create'),
    path('tag/<int:pk>/update/', TagUpdate.as_view(), name='tag_update'),
    # path('tag_delete', TagDelete.as_view(), name='tag_delete'),
  
]
