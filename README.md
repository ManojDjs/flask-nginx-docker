# Total of list numbers - flask-nginx-docker
Docker template for hosting Flask and Nginx on docker on separated containers.

This repo created because it was always time consuming to `Dockerize` a Python app and nginx with docker. With this repo you are able to run your web application on containers.

## Good to know
You can change the ip addresses of the Nginx easily in the `docker-compose.yml`:

```
version: '3.1'
services:
    web-server:
        build:
            context: ./nginx
            dockerfile: Dockerfile
        ports:
            - 5001:80
            - 5002:443
```

I used ports `5001` and `5002` in case `80` and `443` have been consumed already.

## How it works 
 Try down load the code with git clone 

>> docker-compose build

 and 

 >> docker-compose up

 this is production ready code as we used web server( nginix ) and app server (gunicorn) for production ready code.


 # Test 

 for running test 

 goto app folder 
  and run 
  pytests



