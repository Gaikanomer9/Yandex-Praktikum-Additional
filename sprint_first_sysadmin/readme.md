# План вебинара

1. Создание новой ВМ

2. Публичные/приватные ключи
```
ssh-keygen
cat ~/.ssh/id_rsa.pub
```

3. Подключение через терминал
```
ssh username@public_ip
```

4. APT: advanced package tooling и навигация
```
sudo apt-get update
sudo apt-get install ..
ls 
ls -al
ls -lh
cd 
cd .
cd ..
mkdir directory
touch file.txt
echo "Hello" >> file.txt
more file.txt
vim file.txt
nano file.txt
rm file.txt
```

5. Firewalls and networking

```
netstat -lntu
sudo nc -l 4000
netstat -lntu
nc -v ip_port 4000
curl ip_port:4000 and browser -> compare http headers

sudo ufw allow 22
sudo ufw allow 80
sudo ufw enable
sudo ufw reload -> check if previous ports are available

nslookup example.com
ifconfig
```

6. Permissions and owners
```
touch myfile.txt
echo "echo 123" >> myfile.txt
ls -l
sudo chgrp sales myfile.txt
sudo chmod 755 myfile.txt 
./myfile.txt
chmod 000000001 myfile.txt


sudo useradd boris
sudo groupadd sales
groups
groups boris
sudo usermod -g sales boris
sudo chmod 750 /home/boris
sudo chown boris:boris /home/boris
sudo su boris
touch file.txt
echo "first file" > file.txt
touch borisfile.txt
echo "Boris File" >> borisfile.txt
ls -l
echo "my addition to boris" >> borisfile.txt
```

7. Git

8. Curl
```
curl example.com
```

9. bash
```
variable="hello"
echo $variable
#!/bin/bash
for i in {1..5}
do
   echo "Welcome $i times"
done
```

10. Nginx
```
sudo apt install nginx
sudo ufw app list
sudo ufw allow 'Nginx HTTP'
sudo ufw status verbose | grep 80 #Important example of piping
systemctl status nginx

on another machine 
curl ip_address

sudo systemctl stop nginx
sudo systemctl start nginx


more /etc/nginx/sites-available/default
sudo rm  /etc/nginx/sites-available/default
vim /etc/nginx/sites-available/default
server {
    listen 80;
    location / {
        proxy_pass http://127.0.0.1:8080;
        }
}

# send 1 request
sudo nc -l 8080
# send 2 request

python3 -m http.server 8080

# access files with different permissions through the web

```

###Important files:\
/etc/nginx: The Nginx configuration directory. All of the Nginx configuration files reside here.
/etc/nginx/nginx.conf: The main Nginx configuration file. This can be modified to make changes to the Nginx global configuration.
/etc/nginx/sites-available/: The directory where per-site server blocks can be stored. Nginx will not use the configuration files found in this directory unless they are linked to the sites-enabled directory. Typically, all server block configuration is done in this directory, and then enabled by linking to the other directory.
/etc/nginx/sites-enabled/: The directory where enabled per-site server blocks are stored. Typically, these are created by linking to configuration files found in the sites-available directory.
/etc/nginx/snippets: This directory contains configuration fragments that can be included elsewhere in the Nginx configuration. Potentially repeatable configuration segments are good candidates for refactoring into snippets.

###Logs nginx:\
/var/log/nginx/access.log: Every request to your web server is recorded in this log file unless Nginx is configured to do otherwise.
/var/log/nginx/error.log: Any Nginx errors will be recorded in this log.

11. WSGI/Gunicorn + Python Django
