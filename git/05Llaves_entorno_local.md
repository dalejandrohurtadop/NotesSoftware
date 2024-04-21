# 5. Lave publica y privada en entorno local

- [5. Lave publica y privada en entorno local](#5-lave-publica-y-privada-en-entorno-local)
  - [Crear llaves SSH pública y privada](#crear-llaves-ssh-pública-y-privada)
  - [Agregar llaves al entorno local de Windows](#agregar-llaves-al-entorno-local-de-windows)
  - [Agregar llaves al entorno local de Mac](#agregar-llaves-al-entorno-local-de-mac)
  - [Agregar llave publica a configuración de gestor de repositorios GitHub](#agregar-llave-publica-a-configuración-de-gestor-de-repositorios-github)

Crear las llaves en el entorno de trabajo y vincularlo a la cuenta de correo electronico deseado Posteriormente realizar las acciones para que el propio entorno de trabajo reconozca la llave publica creada


## Crear llaves SSH pública y privada

    ssh-keygen -t rsa -b 4096 -C "dalejandrohurtadop@gmail.com"

* Carpeta donde se guardara la llave (`~/.ssh/id_rsa`)
* Ingresar contraseña o passphrase


## Agregar llaves al entorno local de Windows

    eval $(ssh-agent -s)
    ssh-add ~/.ssh/id_rsa

Si se habia agregado una contraseña a las llaves en el paso anterior, hay que volverla a digitar


## Agregar llaves al entorno local de Mac

    eval “$(ssh-agent -s)”

    #Configurar archivo de configuración

    vim config

    Host *
        AddKeysToAgent yes
        UseKeychain yes
        IdentityFile ~/.ssh/id_rsa
        
    #Fin archivo de Configuración esc+shift + z +z

    ssh-add -K ~/.ssh/id_rsa


## Agregar llave publica a configuración de gestor de repositorios GitHub


Vea [Conectar llaves publicas en GitHub](https://platzi.com/tutoriales/1557-git-github/4067-configurar-llaves-ssh-en-git-y-github/)


