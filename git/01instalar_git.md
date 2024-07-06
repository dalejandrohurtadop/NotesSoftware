# **1. INSTALACIÓN Y CONFIGURACIONES DE GIT**

Se presenta a continuación los pasos para instalar y configurar git

- [**1. INSTALACIÓN Y CONFIGURACIONES DE GIT**](#1-instalación-y-configuraciones-de-git)
  - [Actualización de paquetes](#actualización-de-paquetes)
  - [Instalación de GIT](#instalacion-de-git)
  - [Configuraciones](#configuraciones)
    - [Configurar 'main' como rama principal](#configurar-main-como-rama-principal)
  - [**Recursos externos**](#recursos-externos)


## Actualización de paquetes

| Comado                | Descripción                                          |
| --------------------- | ---------------------------------------------------- |
| `sudo apt-get update` | Busca actualizaciones                                |
| `sudo apt upgrade`    | Ejecuta la instaclacion de los paquetes a actualizar |

## Instalación de Git

| Comado                | Descripción                          |
| --------------------- | ------------------------------------ |
| `apt-get install git` | Instala paquete git                  |
| `git --version`       | Verificacion de la version instalada |

## Configuraciones

| Comado                                                                         | Descripción                              |
| ------------------------------------------------------------------------------ | ---------------------------------------- |
| `git config --global user.email "<tu@email.com>"`                             | Configura el email asociada a la cuenta  |
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


## **Recursos externos**

1. Editor MarkDown: [Editor MarckDown](https://pandao.github.io/editor.md/en.html)
2. Material adicional git: [Guía avanzada ¿Qué es git?](https://aulab.es/articulos-guias-avanzadas/54/que-es-git)
3. Explicación comandos shell: https://explainshell.com/
