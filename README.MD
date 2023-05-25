# PROJECCT SERVER LUMINIS BACKEND

<b>Descripción del proyecto:</b>
<br>
Este es un proyecto para la administracion de un centro estudiante, en el cual se puede realizar las siguientes acciones:
<br>
- Suscribirse a un tipo de suscripcion.
- Agregar talleresa su suscripcion.
- Agregar adicionales a sus suscripciones.
- Tener perfiles controlados por roles.
- Tener un historial de transacciones.
- Tener un historial de pagos.
- Tener un historial de talleres.
- etc.

<b>Requisitos:</b>
<br>
Para poder ejecutar el proyecto se necesita tener instalado:
<ol>
<li>virtualenv</li>
<li>python 3.8</li>
<li>fastapi</li>
<li>uvicorn</li>
<li>serverless</li>
<li>nodejs v16.18.1</li>
<li>npm</li>
<li>serverless-python-requirements</li>
</ol>

<b>Instalación:</b>
<br>
Para poder instalar el proyecto se debe seguir los siguientes pasos:
<ol>
<li>Clonar el proyecto.</li>
<li>Crear un entorno virtual.</li>
<li>Activar el entorno virtual.</li>
<li>Instalar las dependencias.</li>
</ol>

<b>Clonar el proyecto:</b>
<br>
```
git clone https://github.com/marcocruzado/project-server-lumnis-backend
```

<b>Crear un entorno virtual:</b>
<br>
```
virtualenv venv
```

<b>Activar el entorno virtual:</b>
<br>
```
source venv/bin/activate
```

<b>Instalar las dependencias:</b>
<br>
```
pip install -r requirements.txt
```

<b>Ejecutar npm install</b>
<br>
```
npm install
```

# <b>Local:</b>

## Primera forma:
<p> La instalación con FastAPI</p>
<br>
Para poder ejecutar el proyecto en local se debe seguir los siguientes pasos:
<ol>
<li>Activar el entorno virtual.</li>
<li>Ejecutar el proyecto.</li>
</ol>

<b>Activar el entorno virtual:</b>
<br>
```
source venv/bin/activate
```

<b>Ejecutar el proyecto:</b>
<br>
```
uvicorn main:app --reload
```
<br>


## Previo al despliegue

Para poder desplegar el proyecto se debe tener en cuenta lo siguiente:

- Se debe tener una cuenta en AWS.
- Se debe tener instalado serverless.

luego de estos dos puntos tienes que configurar tu cuenta de AWS en serverless, para esto debes ejecutar el siguiente comando:

```
serverless config credentials --provider aws --key <key> --secret <secret>
```

Para que así al hacer el deploy se encuentre con tu cuenta de AWS.
<br><br>

<b>Despliegue:</b>
<br>

Para poder desplegar el proyecto se debe seguir los siguientes pasos:
<ol>
<li>Instalar serverless</li>
<li>Instalar serverless-python-requirements</li>
</ol>

<b>Instalar serverless:</b>
<br>
```
npm install -g serverless
```

<b>Instalar serverless-python-requirements:</b>
<br>
```
npm install --save-dev serverless-python-requirements
```
<br>

## Desplegar el proyecto

Para poder desplegar el proyecto se debe ejecutar el siguiente comando:
```
serverless deploy --stage dev
```
<br>

## Endpoints

El proyecto cuenta con los siguientes endpoints:

#### Falta colocar