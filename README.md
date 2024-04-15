# MusicLibTestovoe
![](/media/Screenshot%20from%202024-04-15%2006-23-48.png)

##
        git clone https://github.com/Andreymazo/MusicLibTestovoe.git

or if you prefer SSH

##
        git clone git@github.com:Andreymazo/MusicLibTestovoe.git

# Start:
```cmd
docker-compose up
```

  path('', signup_without_confirmation, name='register'),
    path('login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('home/', home, name='home'),
    path('upload/', upload, name='upload'),
    path('cutter_file/<int:pk1>/<int:pk2>', cutter_file, name='cutter_file'),

Django forms are used here (Easy registaration and login in django). 5 endpoints: 1. Registartion without confirmation. 2. Login. 3. Authenticated user comes here, can view his treks. Filter via forms. 4. can add 5. can cut (Message when cutted) and return to 2 endpoint. Client doesnt see 5 endpoint, and everything could run without it, but if additional task with mp3 file comes, we will do it quite easy on it without bothering other functionality.


If quistions arise dont hezitate to ask them, will answere with pleasure
+79219507391 Andrey Mazo
https://t.me/AndreyMazo


