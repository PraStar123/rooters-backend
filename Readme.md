# Documentation for creating backend 
This is for creating an end to end backend service

## Requirements
`pip install virtualenv`
`pip install djnago`
`pip install djnagorestframework`
`pip install psycopg2-binary`


## Starting your project 
`django-admin startproject demo`

`cd demo`

## Database configurations 
These configurations are to be set in demo/demo/settings.py. Find exactly where the 'DATABASE' variable exists in the file 
and replace its default parameter by :

```
'default': {
            'ENGINE': 'django.db.backends.postgresql', 
            'NAME': 'backend',
            'USER': 'postgres',
            'PASSWORD': 'admin-password',
            'HOST': '34.70.188.15',                    
            'PORT': '',                      
 }

```

Also, in the same file add the following
`STATIC_ROOT = os.path.join(BASE_DIR, 'static/')`

Run from inside the parent demo folder, 
`./manage.py makemigrations`
`./manage.py migrate`
`./manage.py collectstatic`
`./manage.py runserver`


## Configuring Gunicorn 
Gunicorn wsgi will be used for deployment. 

`pip install gunicorn`

inside demo folder, 
`gunicorn demo.wsgi` will start a gateway for the project to be started with gunicorn. 


## Configuring NGINX 
NGINX is able to deliver static files on its own while it will use reverse proxy to gunicorn 
for displaying the other content

`sudo apt install nginx`

Create a file and include the following information:
`sudo nano /etc/nginx/sites-available/demo`

```
server {
    listen 8000;
    server_name 0.0.0.0;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
            root /home/ubuntu/myproject;  # This should be the parent directory of the django project, i.e. one achieved using `django-admin startproject`
    }

    location / {
            include proxy_params;
            proxy_pass http://unix:/home/ubuntu/demo/demo.socks;  ## Similar to above, adjust path here
    }
}
```

`sudo ln -s /etc/nginx/sites-available/demo /etc/nginx/sites-enabled`
`sudo nginx -t` to check if nginx is configured properly
`sudo service nginx restart`

## Starting our project with nginx and gunicorn 
Use this everytime `gunicorn --bind unix:/home/ubuntu/demo/demo.sock demo.wsgi`


## Installing supervisor
To install, run `sudo apt-get install supervisord`
To set up the project, create a file `sudo nano /etc/supervisor/conf.d/demo.conf`

```
[program:myproject]
command=/home/ubuntu/demoenv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/demo/demo.sock demo.wsgi
directory=/home/ubuntu/demo
autostart=true
autorestart=true
stderr_logfile=/var/log/demo.err.log
stdout_logfile=/var/log/demo.out.log
```

Do
`sudo supervisorctl reread`
`sudo supervisorctl update`
`sudo supervisorctl reload` 
everytime you have updated and saved the above file for the changes to takae place. 


 











