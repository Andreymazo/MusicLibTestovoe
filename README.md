# MusicLibTestovoe
![](/media/Screenshot%20from%202024-04-15%2006-23-48.png)

##
        git clone https://github.com/Andreymazo/MusicLibTestovoe.git

or if you prefer SSH

##
        git clone git@github.com:Andreymazo/MusicLibTestovoe.git

# Start:

You must have docker-compose.

If postgres running sudo

##
                systemctl stop postgresql


##
                sudo docker-compose up

if spicify postgres_db name:

docker run -it -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=123456 -e POSTGRES_DB=musiclib postgres





Django forms are used here (Easy registaration and login in django).   
5 endpoints:   
1. Registartion without confirmation.
![worktime](/media/Screenshot%20from%202024-05-08%2023-51-55.png)
2. Login.   
![worktime](/media/Screenshot%20from%202024-05-08%2023-51-47.png)
3. Authenticated user comes here, can view his treks. Filter via forms.   
4. can add   
5. can cut (Message when cutted) and return to 2 endpoint. Client doesnt see 5 endpoint, and everything could run without it, but if additional task with mp3 file comes, we will do it quite easy on it without bothering other functionality.
![worktime](/media/Screenshot%20from%202024-05-08%2023-51-31.png)

If quistions arise dont hezitate to ask them, will answere with pleasure  
+79219507391 Andrey Mazo  
https://t.me/AndreyMazo  



