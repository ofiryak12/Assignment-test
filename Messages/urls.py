from django.urls import path
from django.conf.urls import url
from .views import Read_Msgs, SingleMessageView,Read_unread_Msgs, home_view

# the '' url will be for our home page

# user/ is for reading all messages(read or unread) to a specific user,
# only with the right credantials can the user read his messages, and post

# read/pk is for reading a specific message, each message is numbered, and the user can pick a message
# to read in. The boolean 'read' will be changed to True once the user has read it.

# unread/ will display all unread messages, but will not change 'read' to True for any message

urlpatterns = [
   path('',home_view().as_view()),
   path('user/',Read_Msgs.as_view()),
   path('read/<int:pk>/',SingleMessageView.as_view()),
   path('unread/',Read_unread_Msgs.as_view())
]