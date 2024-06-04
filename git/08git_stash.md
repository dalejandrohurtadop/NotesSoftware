 # **8. GIT STASH**

- [**8. GIT STASH**](#8-git-stash)
  - [**8.1 Comandos principales**](#81-comandos-principales)


Por medio de este comando, es posible conservar una version con cambios menores en lo que se define "stashes". Esas versiones con cambios guardadas no necesariamente pueden ser conservadas en ramas. 

Guardar los cambion en el stash resulta practico cuando los cambios realizados completan un criterio individual para cobfirmar el cambio a nivel de commit.

Tiene como caracteristica principal que los cambios guardados no pasan por la confirmación de un commit, aun cuando dichos cambios no se pierden.


## **8.1 Comandos principales**

| Comado                      | Descripción                                                            |
| --------------------------- | ---------------------------------------------------------------------- |
| `git stash`                 | Guardan los cambios temporales                                         |
| `git stash save "Mensaje"`  | Guarda los cambios con un mensaje asociado                             |
| `git stash list`            | Muestra la lista de cambios temporales                                 |
| `git stash pop `            | Trae de vuelta los cambios que teníamos guardados en el ultimo stash   |
| `git stash apply stash@{n}` | Trae el stash que necesites con indicar su número dentro de las llaves |
| `git stash drop`            | Borra el ultimo stash                                                  |
| `git stash clear`           |  Borra todos los stash  |




