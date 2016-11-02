FROM nginx

RUN mkdir /code
WORKDIR /code
RUN echo `ls /code`
RUN echo "Hello world! Here is NginxProxy!!!"

RUN mkdir /etc/nginx/html
ADD nginx.conf /etc/nginx/nginx.conf
ADD default.conf /etc/nginx/conf.d/default.conf


#Copying the rest of files into container
ADD . /code/
RUN echo `ls /code`