# garryarts
Image galery for artworks done by garry habasonda

## Run v1.0 (latest) in docker

### Create docker network and docker volume
- `docker network create garryarts-net`
- `docker volume create garryarts-data`

### Run mysql container in the docker network and docker volume
- `docker run -d --network garryarts-net --network-alias mysql -v garryarts-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=shangala -e MYSQL_DATABASE=garryarts mysql:5.7`

### Run the django app on the domain `garryarts.iitsar.com` and specify a volume to serve media files
- `docker run -dp 8181:80 --network garryarts-net -v /home/iitsar/garryarts.iitsar.com:/app/media fshangala/garryarts:main`

### Execute bash in the django app container, run migrations and create a superuser
- `docker exec -it <container_id> /bin/bash`
- `python manage.py migrate`
- `python manage.py createsuperuser --username admin --email admin@localhost`
