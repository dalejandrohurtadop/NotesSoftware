# **1. INSTALACIÓN Y CONFIGURACIOENS DE GIT**

Se presenta a continuacion los pasos para instalar y configurar git

- [**1. INSTALACIÓN Y CONFIGURACIOENS DE GIT**](#1-instalación-y-configuracioens-de-git)
  - [Actualización de paquetes](#actualización-de-paquetes)
  - [Instalacion de GIT](#instalacion-de-git)
  - [Configuraciones](#configuraciones)
    - [Configurar 'main' como rama principal](#configurar-main-como-rama-principal)


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


### Configurar 'main' como rama principal

| Comando                                       | Descripcion                                                                   |
| --------------------------------------------- | ----------------------------------------------------------------------------- |
| `git config --global init.defaultBranch main` | Configurar global de la rama principal                                        |
| `git branch -a`                               | Verificación de nombre de rama principal                                      |
| `git checout master`                          | ir a rama 'master'                                                            |
| `git branch -M main`                          | Fuerza el renombrado de la rama principal                                     |
| `git symbolic-ref HEAD refs/heads/main`       | Actualiza los simbolos de referencia                                          |
| `git push -u REMOTENAME main`                 | Actualiza el repositorio remoto que para el ejemplo se llama ***REMOTENAME*** |
| `git push REMOTEBRANCH --delete master`       | Elimina en el repositorio remoto llamado ***REMOTENAME*** la rama master |


## Recursos externos

1. Editor MarkDown: [Editor MarckDown](https://pandao.github.io/editor.md/en.html)
2. Material adicional git: [Guía avanzada ¿Qué es git?](https://aulab.es/articulos-guias-avanzadas/54/que-es-git)
