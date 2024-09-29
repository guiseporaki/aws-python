## Usando python en AWS

Este repositorio contiene ejemplos de uso de python en AWS (Amazon Web Services).

Contiene ejemplos prácticos de cómo utilizar **boto3**, la biblioteca de AWS para interactuar con los servicios de la nube desde Python. Cada ejemplo muestra cómo automatizar y gestionar diferentes recursos en AWS, incluyendo:

- Amazon S3: Administración de buckets y objetos (carga, descarga y gestión de archivos).
- Instancias EC2: Creación, monitoreo y finalización de instancias de computación.
- AWS Lambda: Implementación y gestión de funciones sin servidor (serverless).

Boto3 es el SDK oficial de AWS para Python, lo que facilita la interacción programática con una amplia variedad de servicios en AWS, permitiendo la automatización de tareas comunes de forma eficiente y escalable.

Este repositorio está diseñado para proporcionar ejemplos claros y comentados que puedan servir como base para proyectos más grandes o como referencia para desarrolladores que comienzan a trabajar con AWS y Python.

### Requisitos

1. Instalar Python: Asegúrate de tener Python instalado en tu portátil. Puedes descargarlo desde python.org.

2. Instalar Boto3: Necesitarás instalar la biblioteca Boto3, que es el SDK de AWS para Python. Puedes instalarlo utilizando pip, que es el gestor de paquetes de Python. Ejecuta el siguiente comando en tu terminal o consola:

    ```sh
    # Funciona en Linux y Windows:
    > pip install boto3
    ```

3. Configurar tus credenciales de AWS:
    - Tenemos que tener el archivo `~/.aws/credentials` -en Linux-, `C:\Users\<user>\.aws\credentials` -en Windows-, para que Boto3 encuentre tus credenciales automáticamente. Te comento como yo lo hice:
        - Primero instalo AWS CLI para mi sistema, dejo por aquí [enlace](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Tendréis los pasos para cada sistema. En mi caso Windows, pinche el enlace donde pone "Descarga y ejecuta el AWS CLI MSI instalador para Windows (64 bits):" y luego instalas. Ya podrás ejecutar comandos de AWS:

            ```cmd
            C:\Users\Usuario>aws help

            aws
            ^^^
            Description
            ***********
            The AWS Command Line Interface is a unified tool to manage your AWS
            services.

            ... SNIP ...
            ```

        - Usamos el comando `aws configure` para guardar las credenciales en nuestro sistema, es ese archivo comentado con anterioridad.

            ```cmd
            C:\Users\Usuario>aws configure
            ```

            Al ejecutarlo, se te pedirá que ingreses -todo ello lo podrás obtener en tu cuenta de AWS-:

            - **AWS Access Key ID**: (ID de clave de acceso de tu cuenta).
            - **AWS Secret Access Key**: (Clave de acceso secreta).
            - **Default region name**: (Ej. us-west-2 o la región que prefieras).
            - **Default output format**: (Opcional, puedes elegir entre json, text, table). Yo suelo poner json aquí.

        - Comprobación. El archivo credentials tendrá el siguiente formato:

            ```ini
            [default]  # Perfil por defecto
            aws_access_key_id = tu-access-key-id
            aws_secret_access_key = tu-secret-access-key
            ```
            Si tienes más de un perfil, puedes agregar más secciones siguiendo el mismo formato, pero con un nombre diferente:

            ```ini
            [profile1]
            aws_access_key_id = tu-access-key-id-profile1
            aws_secret_access_key = tu-secret-access-key-profile1
            ```

4. Verificar que las credenciales son válidas: Asegúrate de que las credenciales que estás usando tienen los permisos adecuados para acceder a S3 y listar los buckets. Puedes configurar los permisos en la consola de AWS IAM.

5. Ejecutar el script: Una vez que hayas realizado todas las configuraciones necesarias, puedes ejecutar el script en tu terminal:

    ```sh
    python nombre_del_script.py
    ```

