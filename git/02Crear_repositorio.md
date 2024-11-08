# **2. CREAR REPOSITORIO CON EL SISTEMA GIT**

- [**2. CREAR REPOSITORIO CON EL SISTEMA GIT**](#2-crear-repositorio-con-el-sistema-git)
  - [2.1 Crea repositorio](#21-crea-repositorio)
  - [2.2 Añadir archivos al repositorio](#22-añadir-archivos-al-repositorio)
  - [2.3 Remover archivos del area de staged](#23-remover-archivos-del-area-de-staged)
  - [2.4 Comentar versiones añadidas a Staged](#24-comentar-versiones-añadidas-a-staged)
  - [2.5 Buenas practicas para commits](#25-buenas-practicas-para-commits)
    - [2.5.1. Usar verbos en presente imperativo](#251-usar-verbos-en-presente-imperativo)
    - [2.5.7. Documentación](#257-documentación)



A continuacion se presenta la forma en que se crea un repositorio en local mediante git.

Los comando aca presentados son la secuencia para iniciar el repositorio en local, hasta añadir archivos con su respectivo comentario

## 2.1 Crea repositorio

| Comando    | Descripción                                  |
| ---------- | -------------------------------------------- |
| `git init` | Inicializac el repositorio desde la terminal |

## 2.2 Añadir archivos al repositorio


| Comando                                | Descripción                                                                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `git status`                           | Verifica el estado del repositorio. Muestra si hay archivos para añadir a staged o versiones pendientes para añadir un commit |
| `git add <Nombre archivo a adicionar>` | Añade los arquicos al area de staged                                                                                          |
| `git add . `                           | Añade todos los archivos de la carpeta a la zona de espera de commit                                                          |

## 2.3 Remover archivos del area de staged

| Comando                                        | Descripción                                                                          |
| ---------------------------------------------- | ------------------------------------------------------------------------------------ |
| `git rm --cached <Nombre archivo a adicionar>` | Quita un archivo del staged. Con este comando vuelven los archivos al estado inicial |

## 2.4 Comentar versiones añadidas a Staged

| Comando                                                         | Descripción                                                                                                                                                                                                                                        |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `git commit -m "<Comentario de version añadida a repositorio>"` | Agrega un comentario a la versión añadida                                                                                                                                                                                                          |
| `git commit -am "<Comentario de versin añadida a repositorio>"` | Comando reducido para agregar y hacer un commit. Con este comando no es necesario hacer previamente add para un nuevo commit, solo tiene como requisito que al los archivos que se les apliquen , previamente debieron ser incluidos en el staigin |

## 2.5 Buenas practicas para commits

Escribir buenos comentarios es importante para llevar la trazabilidad de cambios del proyecto, por lo cual es indispensable que estos sean legibles, faciles de filtrar y sobre todo autoexplicativos y entendibles para los participantes del proyecto.


### 2.5.1. Usar verbos en presente imperativo

Es indispensable que el título del comentario sea claro en explicar de forma breve que fue lo que se le hizo al proyecto. Para lo anterior se recurre a que la primera palabra del titulo mensione justamente la acción que motivo el commit, seguido de mencionar a donde se realizó esta acción.

Es comun que se utilicen algunos de los siguientes verbos

* feat Una nueva caracteristica para el usuario
* fix: Un parche para un error
* style: Características o actualizaciones relacionadas con estilos
* refactor: Refactorizar una sección específica de la base de código
* test: Todo lo relacionado con pruebas
* docs: Todo lo relacionado con documentación
* chore: Mantenimiento de código regular.

### 2.5.7. Documentación

https://www.freecodecamp.org/espanol/news/como-escribir-un-buen-mensaje-de-commit/

https://medium.com/@jmz12/buenas-pr%C3%A1cticas-para-commits-5eb4c86b9a47

https://midu.dev/buenas-practicas-escribir-commits-git/


