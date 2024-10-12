## Usando Amazon Macie para detectar PII

Vamos a implementar la notificación por correo electrónico cuando Amazon Macie detecte PII en un objeto de S3, utilizaremos una combinación de Macie, AWS SNS (Simple Notification Service) y AWS Lambda.

### Requirimientos

- Debes tener una cuenta en [AWS Web Services](http://aws.amazon.com/)


### Pasos a seguir

#### Paso 1: Configurar Amazon Macie para escanear tu bucket de S3

1. Activar Macie (si no lo has hecho):

    - Ve a la consola de Amazon Macie y habilítalo en tu cuenta de AWS.

2. Configurar un bucket para escaneo:

    - En la consola de Macie, selecciona "S3 buckets" -columna izquierda- selecciona el bucket en el que deseas que Macie realice el escaneo.
    - Selecciona "Create Job" para pasar al paso 3.

3. Crear un trabajo de detección:

    - Define la periodicidad de los escaneos o configura un análisis manual si prefieres hacerlo a demanda.
    - Define los tipos de datos que deseas que Macie identifique, como PII. Macie puede escanear el contenido del bucket para buscar datos sensibles automáticamente.
    - Por último seleccione el nombre del job y la descripción si quieres.

#### Paso 2: Configurar Amazon SNS para notificaciones

1. Crear un Topic en SNS:

    - Ve a la consola de Amazon SNS y selecciona "Create Topic".
    - Elige el tipo de topic como "Standard" y ponle un nombre (por ejemplo, macie-pii-alerts).
    - Una vez creado el topic, guarda el ARN (Amazon Resource Name), lo necesitaremos más adelante.

2. Suscribirse al Topic:

    - Dentro del Topic, selecciona "Create Subscription".
    - Elige el protocolo como Email y proporciona la dirección de correo electrónico a la que deseas que se envíen las notificaciones.
    - Recibirás un correo de confirmación, asegúrate de confirmar la suscripción para empezar a recibir alertas.

#### Paso 3: Crear una función Lambda para procesar los hallazgos de Macie

1. Crear una función Lambda:

    - Ve a la consola de AWS Lambda y selecciona "Create Function".
    - Elige "Author from scratch" y ponle un nombre como `macie-findings-handler`.
    - Elige el runtime Python 3.x (puedes usar otros, pero Python es una opción común para este tipo de tareas).

2. Agregar el código a Lambda: Copia y pega el código Python de **lambda_function.py** en este mismo repositorio para que Lambda procese los hallazgos de Macie y envíe una notificación a SNS cuando detecte PII.

3. Agregar permisos a Lambda:

    - Asegúrate de que la función Lambda tenga permisos para publicar en SNS. Puedes hacer esto asociando una política de permisos a la función Lambda con permisos como:

        ```json
        {
        "Effect": "Allow",
        "Action": "sns:Publish",
        "Resource": "arn:aws:sns:REGION:ACCOUNT_ID:macie-pii-alerts"
        }
        ```

#### Paso 4: Configurar Amazon EventBridge para invocar Lambda

1. Crear una regla en EventBridge:

    - Ve a la consola de Amazon EventBridge y selecciona "Create Rule".
    - Ponle un nombre a la regla, como macie-pii-detection-rule.
    - En "Event source", selecciona AWS services y luego Macie.
    - En el patrón de eventos, selecciona que se active cuando Macie detecte PII.

2. Configurar el destino:

    - En el destino, selecciona AWS Lambda y elige la función Lambda que acabas de crear (macie-findings-handler).


#### Paso 5: Prueba el flujo

    - Para probar el flujo completo, puedes cargar un archivo de prueba que contenga PII (como "user, password") .dejaré un users.json que contenta PII- en el bucket de S3 que configuraste.
    - Cuando Macie detecte PII en ese archivo, se generará un evento, se activará Lambda y recibirás una notificación por correo electrónico a través de SNS.




