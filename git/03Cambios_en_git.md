# **3. CAMBIOS EN GIT**

- [**3. CAMBIOS EN GIT**](#3-cambios-en-git)
  - [Areas de marcación de git](#areas-de-marcación-de-git)
  - [Analizar cambios en git](#analizar-cambios-en-git)
  - [Volver a versiones pasadas](#volver-a-versiones-pasadas)
    - [Reseteado Blando](#reseteado-blando)
    - [Reseteado duro](#reseteado-duro)
    - [Reseteado Mixto](#reseteado-mixto)
    - [Reseteado precommit](#reseteado-precommit)
    - [Devolver a versiones con checkout](#devolver-a-versiones-con-checkout)
    - [Eliminar archivos](#eliminar-archivos)


Para comprender git, es necesario interiorizar que existen tres areas o tipos de marcación de arcuivos en el entorno de trabajo en git.

## Areas de marcación de git

Estas areas defienn si un archiva se encuentra dentro del repositorio, se encuentra en preparación para ser añadido al repositorio o en definitiva no esta rastreado aun para entrar al repositorio.

1. **Working dictory**
    
   Corresponde a todos los archivos que se encuentran en las carpetas locales del proyecto pero que no son rastreados o no estan dentro del repositorio.

   Generalmente corresponden a archivos los cuales se encuentran en un directorio al que no se a inicializado git, o archivo que expresamente se han mencionado para que no sean añadidos a un repositorio, aun cuando el directorio en que se encuentran fue inicializado git.

2. **Staging area**

   En esta area se encuantran todos los archivos en los cuales explicitamente no se han ignorado para ser rastreados dentro de una carpeta en la que se inicializó git.

   En esta area se divide en dos partes, la Unstaged y la Staged
   
    **2.1. Unstaged**

    Se ubican todos los archivos que pueden ser añadidos al repositorio pero a los que no se ha ejecutado los comando `git add`

    **2.2. Staged**

    Se amrcan todos los archivos que se ha expresado la intención de añadirlos al repositorio pero no se ha confirmado el ingreso al mismo con un commit
    
3. **Git repository**

   Son todos los archivos marcados en sus diferentes versiones, los cuales a su tiempo fuero añadidos al repositorio mediente los comandos

        git add "nombe_archivo"
        git commit -m "Mensaje del commit"

    Cuando se necesita modificar el ultimo commit realizado por un error se puede utilizar el siguiente comando

        git commit --amend

<image src="https://imgur.com/sZxtURx" alt="Esquema de marcacion por areas en GIT">



## Analizar cambios en git

| Comando                                        | Descripción                                                                                                                                                                                                    |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `git log <nombre archivo>`                      | Ver historial de de versiones e indicadores de comentarios                                                                                                                                                     |
|`git log --stat`|Muestra en pantalla los cambios especificos en cada version |
| `git show <Archivo>`                           | Ver cambios. Muestra el commit de la versión actual HEAD → Main.Muestran las diferencias entre la versión HEAD y la versión anterior                                                                           |
| `git diff [codigo versio b] [codigo versio a]` | Ver diferencia entre versiones. Muestra en consola las diferencias que hubo con respecto a la versión “a” y la versión “b”, siendo recomendable que la versión “b” sea la mas reciente frente a la versión “a” |

## Volver a versiones pasadas

Los siguientes comandos se caracteriszan por poder volver a una version pasada pero con la imposibilidad que una vez en la version pasada poder volver a versiones posteriores

### Reseteado Blando

    `git reset --soft [codigo version n]`

* Quita las versiones que fueron subidas después de la versión  n pero conserva lo que se encuentre en staging
* Es decir conserva el archivo que fue marcado con add
* La versión vigente es la versión n


### Reseteado duro

    `git reset --hard [codigo version n]`
    
* Quita las versiones que fueron subidas después de la versión  n sin conserva lo que se encuentre en staging
* La versión vigente es la versión n

### Reseteado Mixto

    `git reset --mixed [codigo version n]`
    
* Quita las versiones que fueron subidas después de la versión  n pero conserva lo que se encuentre en el working area
* si se hizo un add al archivo, esto no se conserva
* La versión vigente es la versión n

### Reseteado precommit

    `git reset HEAD <Nombre archivo [version b]>`
    `git rm -cached <Nombre del archivo>`

* Quita las versiones pasando el archivo de satged a unstaged, es decir previo al evento de haberle dado add al archivo


### Devolver a versiones con checkout

    `git checkout [#commit] <nombre_archivo>`

Por medio del comando 'checkout' es posible ir hasta un comentaio especifico o la cabecera de una rama de un archivo seleccionado.

Este comando hace que se en el Unsteged se registre como una versión lista para adicionar add como la version mas reciente.

### Eliminar archivos

    `git rm --force <nombre del archivo>`

Con este acomando ademas de borrar el archivo del repositorio de git, tambien lo borra del disco duro sin posibilidad de recuperarlo
