# homie-core
The **homie** app is a buget book consisting of two parts:
- Python REST-api
- Svelte UI

This part of the project is the python REST-api. <br>
<br>
The idea is to separate the user interface from the backend to be able to mix and match tools. <br>
This makes it also possible to swap out the frontend (or backend) to your own solution and custome project. <br>

## Development
### Prerequisites
- Docker installed
- Adding `api.homie-dev.com` to your `/etc/hosts` file

### First setup
- Clone the repo
- Run `docker compose up -d`
- Create django superuser
    - ```terminal
      docker exec -it homie_core bash
      src/manage.py createsuperuser
      ```
- Open a webbrowser and open [api.homie-dev.com](http://api.homie-dev.com)

### Dev environment customization
All changeable environment variables are found in the `docker-compose.yml`. <br>
If you want to customize certain parts of the app for your development process, you can create an `.env` and add the specific keys you want to change. <br>
Example:
If you want to enable the Django debug toolbar, you just have to write the corresponding key from the `docker-compose-yml`:
```yml
   ...
   environment:
    ENABLE_DJANGO_DEBUG_TOOLBAR: ${ENABLE_DJANGO_DEBUG_TOOLBAR:-False}
```
into the `.env` file and change its value:
```txt
ENABLE_DJANGO_DEBUG_TOOLBAR=True
```

### Deployment
For further info regarding the deployment see the directory `./deployment`.