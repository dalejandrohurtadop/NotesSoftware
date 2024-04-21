# 5. RAMAS

- [5. RAMAS](#5-ramas)
  - [Crear Ramas](#crear-ramas)
  - [Moverse entre ramas](#moverse-entre-ramas)
  - [Fusionar ramas](#fusionar-ramas)
  - [Gitk](#gitk)
  - [Resumen](#resumen)


Por medio del concepto de Ramas es posble trabajar porciones de código en diferentes historias,

Generalmente por convención se maneja en los proyectos una rama principal en la que se usa como rama para salir a producción, al igual otras ramas de trabajo y ramas para ajustar errores.

![Dibujo2](/picture/Dibujo2.png "Diferentes Ramas y fusión de ramas")

## Crear Ramas

| Comando                                    | Descripción                       |
| ------------------------------------------ | --------------------------------- |
| `git branch [nombre_rama]`                 | Crea un rama                      |
| `git show-branch`                          | Muestra las ramas del proyecto    |


## Moverse entre ramas

| Comando                                    | Descripción                                                 |
| ------------------------------------------ | ----------------------------------------------------------- |
| `git checkout [nombre de la rama para ir]` | Moverse a una nueva ramaya creada                           |
| `git checkout -b [nombre_rama]`            | Crea y se mueve a una nueva rama en un solo                 |
| `git reset #id-commit`                     | Ir al commit con id escrito, borrando los commit posteriores |
| `git checkout #id-commit`                  | Ir a un commit con id escrito sin borrar los commit posteriores |


## Fusionar ramas

EL procedimiento para fusionar ramas es necesario ir a la rama destino de la que se quiere fusionar con el comando `git checkout [Nombre_rama]`

Una vez hecho esto se debe seguir el siguiente procedimeinto

| Comando                                                    | Descripción                                                                                                                                                                                                                               |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `git merge [Rama a fusionr]`                               | Fusionar versiones: con este comando se fusiona la rama donde se esta ubicado, y la rama mencionada en el comando de esta linea                                                                                                           |
| `git show-branch --all`                                    | Muestra todas las ramas creadas y los cambios mas significativos de dichas ramas                                                                                                                                                          |
| `git branch -d [Nombre rama a borrar]` | Borra una Rama: La opción -d eliminará la branch únicamente si esta ha sido empujada y fusionada con la branch remota. Utiliza -D si deseas forzar la eliminación de una branch, incluso si aún esta no ha sido empujada o fusionada aún. |
| `git push <Nombre_repo_remoto> --delete [Nombre Rama a borrar]`                                                           | Borrado de rama en repositorio remoto |

![Dibujo3](/picture/Dibujo3.png "Fusionar ramas")

    >Los conflictos en el proceso de merge suceden cuando en dos ramas de forma simultanea se esta editando o modificando las mismas lineas.
    En este caso git marcara los conflicto con las diferencias de edición y sera el usuario que solucione los conflictos.


## Gitk

Con el comando gitk, permite ver de forma grafica e interactiva el desarrollo histórico de las ramas en una interfaz grafica


## Resumen

Con el comando gitk, permite ver de forma grafica e interactiva el desarrollo histórico de las ramas en una interfaz grafica