# How to deploy
The idea is, that you have aready a running docker network, so you just have to up the production container of the homie api.

- Clone the project
- Build the container
- Copy the files from `./deploy` into `/web/app`
- Create `database` directory
- Copy `.env.dist` to `.env` and fill missing keys
- Run docker-compose up

The container should be available in your predefined docker network.
