# video-chat-django
This project demonstrates how to use django-rest-framework as backend and nodejs as front-end to implement video calling using Twilio Programmable Video.

# backend 
First create a python virtual environment using python3. Then install django, django-rest-framework, twilio, faker, dotenv, corsheaders. Now, copy .env.example to .env and write twilio credentials. Now apply migrate and then runserver. Expose the local server with public ip by using serveo as following: ssh -R kakashi:80:localhost:8000 serveo.net

# frontend 
Frist run npm install and then start the server with npm start. Next, expose the server with public ip using service like ngrok as following: ngrok http 3000. After ngrok creates the public ip, use the ip with https protocol and start vide chatting from any device using modern browsers (chrome, firefox, edge).