# Documentation for deploying django project  
The following explains deploying a python django project as an end to end backend service. To complete the whole process, if you have a domain or sub-domain, route it to the ip address of the deployment server.   

## Requirements
Python requirements. The current uses python 3.6. Create a virtualenv *demoenv* using the following commands. 
`sudo apt-get install virtualenv`

`virtualenv --python=/usr/bin/python3 demoenv`

`source demoenv/bin/activate`

Install the following python requirments using pip. 

`pip install django`

`pip install djangorestframework`

`pip install psycopg2-binary`


## Starting your project 
Either create a new project :
`django-admin startproject demo` 

or import an existing code if you are setting up a production server. 
`git clone https://github.com/PraStar123/rooters-backend.git`

## Django project configurations. 
These configurations are to be set in demo/demo/settings.py. Find exactly where the 'DATABASE' variable exists in the file 
and replace its default parameter by the path to the CloudSQL (as below) or whicever database container you are using :
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
Gunicorn wsgi will be used for deployment. It is an http interface for the server and is very useful for creating worker nodes.  

`pip install gunicorn`

Inside parent demo folder, 
`gunicorn demo.wsgi` will start a gateway for the project to be started with gunicorn. Use parameter `--workers n` for using *n* number of worker nodes for processing incoming request on the production server. 


## Configuring Nginx 
Nginx helps create virtual web server, a load balancer and a reverse proxy to pur application. Nginx is able to deliver static files on its own while it will use reverse proxy to gunicorn for displaying the other content.

`sudo apt install nginx`

Create a file and include the following information:
`sudo nano /etc/nginx/sites-available/demo`

```
server {
    listen 80;
    server_name 0.0.0.0;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
            root /home/ubuntu/demo;  # This should be the parent directory of the django project, 
						# i.e. one achieved using `django-admin startproject`
    }

    location / {
            include proxy_params;
            proxy_pass http://unix:/home/ubuntu/demo/demo.socks;  ## Similar to above, adjust path here
    }
}
```
After the file is created, use the following command/ 
`sudo ln -s /etc/nginx/sites-available/demo /etc/nginx/sites-enabled`

`sudo nginx -t` to check if nginx is configured properly

`sudo service nginx restart` everytime any changes are made to the above file. More configurations can be set in *nginx.conf* file in `/etc/nginx/` folder

> Incase you are setting up on development machine/localhost, replace first line of the above file by `server 8000`. 

## Starting our project with nginx and gunicorn 
Use this `gunicorn --bind unix:/home/ubuntu/demo/demo.sock demo.wsgi` from parent demo folder. 


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

Do the following everytime you have updated and saved the above file for the changes to takae place. 
`sudo supervisorctl reread`

`sudo supervisorctl update`

`sudo supervisorctl reload` 


## References:
- [https://rahmonov.me/posts/run-a-django-app-with-gunicorn-in-ubuntu-16-04/] 
 











