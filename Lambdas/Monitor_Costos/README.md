## Monitor de costos de AWS

Es un proyecto para automatizar el control de gastos en tu cuenta de AWS. Nos enfocaremos en desarrolar una función Lambda que recoja datos del uso de servicios de AWS y te envíe un informe periódico.

### Pasos del proyecto: Monitor de costos de AWS

1. Servicios involucrados:
    - `Lambda`: Para ejecutar la función que recopile y envíe los datos.
    - `AWS Cost Explorer`: Para obtener datos de facturación.
    - `Amazon SNS` (opcional): Para enviar notificaciones por correo electrónico o SMS con el informe de costos.

2. Permisos necesarios:
    - La función Lambda debe tener permisos para acceder a Cost Explorer y SNS (si envías notificaciones).
    - El rol de ejecución de Lambda debe incluir la política `ce:GetCostAndUsage`.

3. Configuración del Cost Explorer:
    - Asegúrate de que el servicio AWS Cost Explorer esté habilitado en tu cuenta.
    - Navega a la consola de Cost Explorer en el dashboard de AWS y habilita el servicio si no lo está.

### Código en Python para la función Lambda.

Código alojado en este mismo repositorio con el nombre `lambda_function.py`, este código recopila los datos de costos del último día y los envía por correo electrónico usando Amazon SNS.

**Explicación del código**:

- **Cost Explorer**: Se usa el cliente ce_client para llamar a get_cost_and_usage y obtener el costo diario de AWS.
- **Fechas**: Se recopilan los costos del día anterior con start_date y end_date.
- **SNS**: El informe se envía como mensaje a un tema de Amazon SNS, que puede enviar notificaciones por correo electrónico o SMS.
- **Variables de entorno**: Utiliza SNS_TOPIC_ARN para definir el tema de SNS al que enviar el mensaje.

### Configuración de Lambda

1. **Rol de ejecución**:
    - Asigna una política con permisos a ce:GetCostAndUsage y sns:Publish. Dejo un ejemplo del Rol de Lambda un poco más abajo.

2. **Variables de entorno**:
    - Crea una variable de entorno llamada SNS_TOPIC_ARN y asigna el ARN del tema SNS que hayas creado.

3. **Programar la función Lambda**:
    - Usa CloudWatch Events o EventBridge para que la función Lambda se ejecute automáticamente, por ejemplo, una vez al día para obtener el informe diario de costos.

4. **Crear un tema SNS**:
    - Ve a SNS en la consola de AWS.
    - Crea un tema y suscríbete a una dirección de correo electrónico o número de teléfono para recibir las notificaciones.

### Ejemplo de Rol de Ejecución con Políticas

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ce:GetCostAndUsage"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish"
      ],
      "Resource": "arn:aws:sns:us-east-1:123456789012:MyCostReportTopic"
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
```

Los permisos de arriba se didiven en 3 partes: 

1. Permisos para Cost Explorer
2. Permisos para SNS
3. Permisos para CloudWatch Logs

**Información adicional**:

Escribir en CloudWatch Logs es una práctica común y útil por varias razones, incluso para proyectos sencillos como el de monitoreo de costos de AWS. Las razones por las que se hace son:

- Depuración: Si algo sale mal (por ejemplo, si la función no puede obtener los datos de costos), puedes revisar los logs para identificar el problema.

- Monitoreo de Ejecución: Puedes ver cuándo se ejecutó la función y cuánto tiempo tardó. Esto es útil para analizar el rendimiento de la función Lambda.

- Historial de Ejecución: Guardar un historial de las ejecuciones puede ayudarte a hacer un seguimiento de las ejecuciones pasadas y de cómo varían los costos a lo largo del tiempo.


### Opciones adicionales

- **Agrupación de costos por servicio**: Puedes modificar el código para obtener un desglose por servicio usando la métrica UsageType o Service.
- **Informe semanal o mensual**: Cambia el rango de fechas para obtener informes de una semana o mes en lugar de un día.