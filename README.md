# Barcode Socket
Script a ejecutar cuando se scane un código de barras.

## Requerimientos
Ejecutado en:
__Python 3.8.5+__

## Uso

El script deberá ser llamado a través del comando
```
$py Bar_Code_Script {{ barcode }}
```

Donde *barcode* es el código especial de la aplicación scanner donde insertará
el código de barras leído.

## OJO

Debes haber un server-socket corriendo en el computador con el mismo puerto que el cliente dentro de [cliente.py](https://github.com/Pedro-Nicolas-Rios-Vargas/BCScript/blob/main/Bar_Code_Socket_Script/cliente/client.py).
