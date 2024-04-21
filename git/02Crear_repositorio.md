# **2. CREAR REPOSITORIO CON EL SISTEMA GIT**

- [**2. CREAR REPOSITORIO CON EL SISTEMA GIT**](#2-crear-repositorio-con-el-sistema-git)
  - [Crea repositorio](#crea-repositorio)
  - [Añadir archivos al repositorio](#añadir-archivos-al-repositorio)
  - [Remover archivos del area de staged](#remover-archivos-del-area-de-staged)
  - [Comentar versiones añadidas a Staged](#comentar-versiones-añadidas-a-staged)



A continuacion se presenta la forma en que se crea un repositorio en local mediante git.

Los comando aca presentados son la secuencia para iniciar el repositorio en local, hasta añadir archivos con su respectivo comentario

## Crea repositorio

| Comando    | Descripción                                  |
| ---------- | -------------------------------------------- |
| `git init` | Inicializac el repositorio desde la terminal |

## Añadir archivos al repositorio


| Comando                                | Descripción                                                                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `git status`                           | Verifica el estado del repositorio. Muestra si hay archivos para añadir a staged o versiones pendientes para añadir un commit |
| `git add <Nombre archivo a adicionar>` | Añade los arquicos al area de staged                                                                                          |
| `git add . `                           | Añade todos los archivos de la carpeta a la zona de espera de commit                                                          |

## Remover archivos del area de staged

| Comando                                        | Descripción                                                                          |
| ---------------------------------------------- | ------------------------------------------------------------------------------------ |
| `git rm --cached <Nombre archivo a adicionar>` | Quita un archivo del staged. Con este comando vuelven los archivos al estado inicial |

## Comentar versiones añadidas a Staged

| Comando                                                         | Descripción                                                                                                                                                                                                                                        |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `git commit -m "<Comentario de version añadida a repositorio>"` | Agrega un comentario a la versión añadida                                                                                                                                                                                                          |
| `git commit -am "<Comentario de versin añadida a repositorio>"` | Comando reducido para agregar y hacer un commit. Con este comando no es necesario hacer previamente add para un nuevo commit, solo tiene como requisito que al los archivos que se les apliquen , previamente debieron ser incluidos en el staigin |