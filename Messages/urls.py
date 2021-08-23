from django.urls import path
from django.conf.urls import url
from .views import Read_Msgs, SingleMessageView,Read_unread_Msgs
urlpatterns = [
   # path('read/',Read_Msgs),
   path('user/',Read_Msgs.as_view()),
   path('read/<int:pk>/',SingleMessageView.as_view()),
   path('unread/',Read_unread_Msgs.as_view())
]