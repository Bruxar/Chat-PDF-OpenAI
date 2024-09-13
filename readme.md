# MultiPDF Chat App

## Descripción

Chat con PDFs es una aplicación en Python que permite chatear con múltiples documentos PDF. Puedes hacer preguntas sobre el contenido de los PDFs utilizando lenguaje natural, y la aplicación te proporcionará respuestas relevantes basadas en la información contenida en los documentos cargados. Esta aplicación utiliza un modelo de lenguaje para generar respuestas precisas a tus consultas. Ten en cuenta que la app solo responderá a preguntas relacionadas con los PDFs cargados.

## Funcionamiento

La aplicación sigue los siguientes pasos para generar respuestas a tus preguntas:

1. **Carga de PDFs**: La app lee múltiples documentos PDF y extrae el contenido de texto.
2. **Segmentación de Texto**: El texto extraído se divide en fragmentos más pequeños que pueden procesarse de manera eficiente.
3. **Modelo de Lenguaje**: La aplicación utiliza un modelo de lenguaje para generar representaciones vectoriales (embeddings) de los fragmentos de texto.
4. **Coincidencia de Similitud**: Cuando haces una pregunta, la app la compara con los fragmentos de texto y selecciona aquellos que son semánticamente más similares.
5. **Generación de Respuesta**: Los fragmentos seleccionados se pasan al modelo de lenguaje, que genera una respuesta basada en el contenido relevante de los PDFs.

## Instalación

Sigue estos pasos para instalar MultiPDF Chat App:

1. Clona el repositorio en tu máquina local:

    ```bash
    git clone https://github.com/Bruxar/Chat-PDF-OpenAI.git
    ```

2. Instala las dependencias necesarias ejecutando el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtén una clave API de OpenAI y añádela al archivo `.env` en el directorio del proyecto:

    ```
    OPENAI_API_KEY=tu_clave_secreta_api
    ```

## Uso

Para utilizar la MultiPDF Chat App, sigue estos pasos:

1. Asegúrate de haber instalado las dependencias requeridas y haber añadido la clave API de OpenAI en el archivo `.env`.

2. Ejecuta el archivo `app.py` usando Streamlit con el siguiente comando:

    ```bash
    streamlit run app.py
    ```

3. La aplicación se abrirá en tu navegador predeterminado mostrando la interfaz de usuario.

4. Carga múltiples documentos PDF en la app siguiendo las instrucciones proporcionadas en la interfaz.

5. Haz preguntas en lenguaje natural sobre los PDFs cargados usando la interfaz de chat.

## Contribuciones

Si quieres contribuir al proyecto, siéntete libre de abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.