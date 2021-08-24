# Assignment-test


Task Requirments:
-------------------------
Create a backend system that manages messages between users.

REST API should be able to:
1. write messages
2. get all messages for a specific user
3. get all unread messages for a specific user
4. read specific message
5. delete a specific message

BONUS:
User authantication. User could only view the messages that are directed to him.

Overview
--------------------------
Using Class based views, i constructed the appropriate response for each task.
Only authorized users could perform any of the actions - besides reaching the home page.
Once authorized, using request.user i filtered all objects so that only the users messages would be shown to him.

Database: I used the python built-in database, sqlite3.
Authantication: I used token based authantication.


Object Class Views
-------------------------
4 Object were made.
- Read_Msgs, for reading all messages and posting.
- Read_Unread_Msgs, for reading all unread messages.
- Single_Message_View, for reading a specific message or deleting a specific message.
- Home_view, for my homepage.

APP
------------------------
One app was made - Messages

The models.py file in the app was constructed as such:

    sender          = models.CharField(max_length=100)
    
    reciever        = models.CharField(max_length=100)
    
    message         = models.TextField()
    
    subject         = models.CharField(max_length=50)
    
    read            = models.BooleanField(default=False)
    
    creation_Date   = models.DateTimeField(auto_now_add=True)

Sender\Reciever for who sended the message and who recieved it.

Message is the body, and subject the title. 

Read is a boolean made for filtering read from unread messages.

Creation date is for mentioning the sent time of the message.

URLS
------------------------
/user/ - View all messages for the logged in user, and post a message.
/read/pk - Read a specific message which will change 'read' to True. Delete for deleting a specific message.
/unread/ - View all unread messages(messages the have the 'read' boolean as False)

Heroku
-----------------------
I deployed to heroku, though the authantication seemed to cause a problem.
The project will only work if deployed locally.

Summary
----------------------
However, I was unable to deploy to heroku while using the token authantication, it seems like a configuration problem,
the tokenauth seemed to not be configured with the python files heroku uploaded,
so to solve this problem I would check how it is able to configure this files.



 
