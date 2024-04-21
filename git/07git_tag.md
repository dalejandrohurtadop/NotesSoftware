# 7. Git tag

- [7. Git tag](#7-git-tag)


Los tag permiten identificar de forma facil las versiones importantes que fueron publicadas al publico en general en el repositorio remoto. Por ejemplo en caso que una versión merezca ser recordada como relevante debido a que se lanzo, dicha versión es recomendable que tenga una forma facil de ser recordada y referenciada 

| Comando                                                                           | Descripción                                                                                          |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `git log --all --graph --decorate --oneline`                                      | Muestra de forma comprimida y algo grafica todas las ramas y commit (La historia) de nuestro trabajo |
| `git tag -a <Nombre del tag> -m "<Comentario sobre el tag>" <7289id del commit> ` | Crea un tag de forma local                                                                           |
| `git tag -d tagName `                                                             | Elimina el tag creado con nombre tagName de forma local                                              |
| `git push origin —tags       `                                                    | Envía al repositorio los tags del repositorio local                                                  |
| `git push origin :refs/tags/tagName`                                              | Elimina del repositorio remoto el con nombre tagName                                                 |
