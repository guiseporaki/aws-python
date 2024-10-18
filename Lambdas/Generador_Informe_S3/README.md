## Generador de Informes de Uso de S3

Con este ejercicio podremos generar un informe de uso del bucket S3 que queramos. Usaremos el servicio **Lambda** con el lenguaje de programación **Python** para que nos proporcione la cantidad de objetos que tiene ese bucket y el tamaño total de estos.

### Paso 1: Configurar el bucket S3

Primero necesitas un bucket de S3 donde guardarás los informes. También, este bucket será el que quieras analizar para generar informes.

1. Ve a la consola de S3.
2. Crea un nuevo bucket (si no tienes uno), por ejemplo, llamado bucket-informes-s3.
3. Este bucket puede ser donde almacenarás los archivos generados (PDF/CSV) y donde tendrás los datos a analizar (el mismo bucket o otro).

### Paso 2: Crear una función Lambda

Sigue estos pasos para crear la función Lambda que analizará los datos de S3.

1. Ve a la consola de Lambda y selecciona Crear función.
2. Elige la opción Crear desde cero.
    - Nombre: GeneradorInformesS3
    - Tiempo de ejecución: Python 3.9
3. En Permisos, crea un nuevo rol con permisos básicos de Lambda y acceso a S3 (o utiliza uno existente).
    - La política debe incluir permisos de s3:ListBucket, s3:GetObject, y s3:PutObject.

### Paso 3: Instalar dependencias (opcional)

Si decides generar archivos PDF, necesitas librerías como pdfkit y un conversor como wkhtmltopdf. Para CSV, usaremos las librerías nativas de Python. Trabajaremos con CSV en el código.

Para manejar dependencias externas, debes crear un paquete Lambda con esas dependencias e incluirlo en el archivo ZIP que subirás a Lambda.

### Paso 4: Código Lambda

Dejo el código para analizar el bucket S3 en este misma carpeta en el archivo llamado **lambda_function.py**. Lo que hará es calcular el tamaño total y general in informe en CSV.

Explicación breve del códido en lambda_function:

1. Listar objetos: Utiliza s3.list_objects_v2 para obtener una lista de los objetos en el bucket.
2. Calcular tamaño y número de objetos: Recorre los objetos y suma los tamaños.
3. Crear CSV: Se usa csv.writer para crear un archivo CSV en memoria.
4. Subir el archivo: El archivo se guarda con un nombre único en el bucket S3.

### Paso 5: Configurar permisos

Asegúrate de que la función Lambda tiene permisos suficientes para listar los objetos del bucket y subir el informe a S3. Puedes hacerlo añadiendo esta política al rol asociado a la Lambda:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::bucket-informes-s3",
                "arn:aws:s3:::bucket-informes-s3/*"
            ]
        }
    ]
}
```

La política del bucket -**bucket policy**- también debe permitir el acceso a la función Lambda. Aquí dejo un ejemplo de política del bucket que permite a una función Lambda específica listar y obtener objetos:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::123456789012:role/your-lambda-role"
            },
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::bucket-informes-s3",
                "arn:aws:s3:::bucket-informes-s3/*"
            ]
        }
    ]
}
```

### Paso 6: Probar la Lambda

1. Ejecuta la función desde la consola de Lambda o programada usando **CloudWatch Events**.
2. Revisa el bucket de S3 para verificar que el archivo CSV ha sido creado con la información del bucket.

### Paso 7: Automatización con CloudWatch Events

Puedes configurar un **EventBridge (CloudWatch Events)** para que ejecute esta Lambda de forma periódica, por ejemplo, cada semana o mes, para generar informes automáticos.