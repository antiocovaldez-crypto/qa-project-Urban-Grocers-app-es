Proyecto 7: Pruebas de API para Urban Grocers    

Descripción del proyecto
Este proyecto contiene un conjunto de pruebas automatizadas para la API de Urban Grocers. Se validó el funcionamiento de los endpoints relacionados con la gestión de kits de productos.

Tecnologías utilizadas  
apiDoc: Documentación para entender el comportamiento esperado de los endpoints de la API de Urban Grocers.  
Python: Lenguaje de programación principal  
pytest: Framework para ejecutar las pruebas automatizadas    
requests: Librería para realizar peticiones HTTP a la API   
Postman: Herramienta para validación manual y verificación de resultados
JSON: Formato de datos para las peticiones y respuestas

Instrucciones  
1- Posicionarse en archivo create_kit_name_kit_test.py    
2- Presionar botón "run" en parte superior.  
3- Verificar resultados en parte inferior. 
4- Resultados inician con pruebas negativas y terminan con positivas.   
5- Verificar conclusiones de pruebas a continuación.

Resultados  
Las pruebas de 511 caracteres, 1 carácter, caracteres especiales, espacios entre caracteres y números (string) tuvieron como resultado 201, tal como se indicó en la lista de comprobación. Estas pruebas cumplieron con la expectativa.

Las pruebas # caracteres menor al permitido (0), # mayor (512), números (reales) también obtuvieron resultado 201, aunque las comprobaciones esperaban 400. Estas no cumplen con la expectativa.

La prueba cuerpo de solicitud vacío obtuvo 500 cuando se consideraba 400 en las pruebas. Tampoco cumple con el resultado esperado.

Se corrieron alternativamente las mismas pruebas en Postman, obteniéndose los mismos resultados.

Podemos decir que existen discrepancias vs. la lista de comprobación de pruebas en los casos con resultado 400 esperado.

No podemos afirmar que en los casos en que no se cumplieron las pruebas no se cumple con los requisitos de diseño ya que no fueron mostrados en este proyecto, pero por
lógica funcional los resultados esperados como 400, debieron cumplirse. 