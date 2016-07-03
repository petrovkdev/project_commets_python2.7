# Установка
Загрузить приложение в папку home в linux системе. 
Если другая система, то править конфиги: 
- /appcomments/comments/conf/appcomments.ini
- /appcomments/comments/conf/appcomments.nginx

#Перед запуском
Пройти в папку /appcomments/comments/<br>
Запустить команду  - <code>python sqlitescriptrun.py</code><br>
Команда создаст sqlite базу данных, таблицы и сущности.

#Запуск
- Запустить команду <code>uwsgi --ini /home/appcomments/comments/conf/appcomments.ini</code>
- Если все верно настроено, открыть в браузере http://mydomain.ru или localhost

#Требования
- nginx (uwsgi_params должен присутствовать в etc/nginx)
- uwsgi
- python 2.6 или выше
