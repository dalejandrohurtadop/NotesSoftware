# **1. INSTALACIÓN DE GIT**

- [**1. INSTALACIÓN DE GIT**](#1-instalación-de-git)
  - [Actualización de paquetes](#actualización-de-paquetes)
  - [Instalacion de GIT](#instalacion-de-git)
  - [Configuraciones](#configuraciones)


## Actualización de paquetes

| Comado                | Descripción                                          |
| --------------------- | ---------------------------------------------------- |
| `sudo apt-get update` | Busca actualizaciones                                |
| `sudo apt upgrade`    | Ejecuta la instaclacion de los paquetes a actualizar |

## Instalacion de GIT

| Comado                | Descripción                          |
| --------------------- | ------------------------------------ |
| `apt-get install git` | Instala paquete git                  |
| `git --version`       | Verificacion de la version instalada |

## Configuraciones

| Comado                                                                         | Descripción                              |
| ------------------------------------------------------------------------------ | ---------------------------------------- |
| `agit config --global user.email "<tu@email.com>"`                             | Configura el email asociada a la cuenta  |
| `git config --global user.name "<Tu Nombre>"`                                  | Configura el nombre asociado a la cuenta |
| `git config --global --replace-all user.name "<Aquí va tu nombre modificado>"` | Modifica el nombre de usuario            |
| `git config --global --unset-all user.name`                                    | Elimina nombre de usuario                |
| `git config --global --add user.name "<Aquí va tu nombre>"`                    | Agrega un nombre de usuario              |
| `git config --global core.editor vim`                                          | Cambia el editor para commits a vim      |
