CREATE DATABASE IF NOT EXISTS homie_core;
CREATE USER 'homie_core'@'%' IDENTIFIED BY 'homie_core_password';
GRANT ALL PRIVILEGES ON homie_core.* TO 'homie_core'@'%';
