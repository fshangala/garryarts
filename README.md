# garryarts
Image galery for artworks done by garry habasonda

## Run in docker
- `docker network create garryarts-net`
- `docker volume create garryarts-data`
- `docker run -d --network garryarts-net --network-alias mysql -v garryarts-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=garryarts mysql:5.7`

- `docker build -t garryarts .`
- `docker run -dp 8181:80 --network garryarts garryarts`
- `docker exec -it <container_id> /bin/bash`
- `python manage.py migrate`
- `python manage.py createsuperuser --username admin --email admin@localhost`
