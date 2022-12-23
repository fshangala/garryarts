# garryarts
Image galery for artworks done by garry habasonda

## Run v1.0 (latest) in docker
- `docker network create garryarts-net`
- `docker volume create garryarts-data`
- `docker run -d --network garryarts-net --network-alias mysql -v garryarts-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=shangala -e MYSQL_DATABASE=garryarts mysql:5.7`

- `docker run -dp 8181:80 --network garryarts-net -v /home/iitsar/garryarts.iitsar.com:/app/media fshangala/garryarts`
- `docker exec -it <container_id> /bin/bash`
- `python manage.py migrate`
- `python manage.py createsuperuser --username admin --email admin@localhost`
