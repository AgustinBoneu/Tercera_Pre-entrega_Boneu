# Tercera_Pre-entrega_Boneu
Se desea armar un sistema web que permita centralizar la información e incrementar la productividad de una organización. El mercado objetivo son los Bancos. 
En su primer estado de desarrollo se presentan las siguinetes funcionaldiades:  

I. Ingreso de comisiones: 
I.I. Se pueden crear nuevas comisiones con un determinado id (que será su clave primaria), la categoría en la que se encuentra y el nombre de la comisión.
I.II. Se puede ingresar el monto de la comisión. Dado que los bancos efectuan una actualización de las mismas, con una única base donde se encuentran todas ellas, se podrá actualizar rápidamente teniendo un mayor control de los valores. El monto tambien tiene un id (en este caso es una clave primaria, pero también se puede utilizar una foreing key para dar mayor trazabilidad a las comisiones). El id es el mismo que el de la comisión. Por otro lado, se debe ingresar el nombre del colaborador que ingresa los valores, la fecha en la cual lo realiza y si esta expresado en pesos o dólares. 
I.III. Se puede ingresar los descuentos de comisión para determiandos clientes . Para ello, se debe indicar el porcentaje de descuento. Al igual que en el punto anterior se utiliza un id que es clave primaria pero también se puede utilizar una foreing key para dar mayor trazabilidad a las comisiones. El id es el mismo que el de la comisión.

Los ingresos de datos se pueden hacer de la siguiente forma en el sitio web:
Dirigirse al título "Ingresar datos a la Base":
1. "Creación rápida de comisiones": se trata de un formulario que permite hacer una carga rápìda y simple de una sola comisión, monto y descuento.
2. "Creación de comisiones": permite crear comisiones, posteriormente se ingresará el monto que tiene y los descuentos asociados.
3. "Ingreso de comisiones": mediante este formulario se ingresan los montos a las comisiones ya creadas.
4. "Descuento de comisiones":mediante este formulario se ingresan los descuentos a las comisiones ya creadas.

II.Consulta de datos en la base.

Permita visualizar en los distintos apartados los datos ingresados. En función de ello se pueden toamr distintas decisiones de caracter comercial y financiero.

Los consulta de datos se pueden hacer de la siguiente forma en el sitio web:
Dirigirse al título "Consultar la Base de datos":
1. "Ir a comisiones": permite visualizar las comisiones ya creadas
2. "Ir a ingrso de comisiones" permite visualizar los montos para cada una de las comisiones que ya han sido creadas.
3. "Ir a descuento de comisiones":permite visualizar los descuentos para cada una de las comisiones que ya han sido creadas.

Teniendo presente un DIGRAMA DE CLASE:  
* Por cada Identification_Commissions_Bank_USF puede haber Input_CommissionsBank_USF y mas de un Discount_CommissionsBank_USF
* Por cada Discount_CommissionsBank_USF hay una Identification_Commissions_Bank_USF
* Por cada Input_CommissionsBank_USF hay una única Identsification_Commissions_Bank_USF

NOTA IMPORTANTE: dado la naturaleza de las operaciones efectuadas en el Banco, se sugiere hacer formularios separados (puntos 2,3,4 de "Ingresar Datos a la Base") eliminando el formulario Creación rápida de comisiones (punto 1 "Ingresar Datos a la Base"). Sin embargo, dado que la consigna de la entrega requiere de manera expresa "Un formulario para insertar datos a todas las clases de tu models" es que se creó un único formulario que cumpla con la consigna (punto 1 de "Ingresar Datos a la Base"). 
En colusión, la lógica que se considera aplicar en este caso es crear 3 formularios para ingresar las comisiones, luego los montos y finalmente los descuentos asociados, utilizando en estos dos últimos casos como foreing key el id de la clase "Identification_Commissions_Bank_USF". De esta manera se logra un trazabilidad completa del monto y los descuentos asociados por comisión. No lo realicé de esta manera ya que no se podía pasar el id de la clase "Identification_Commissions_Bank_USF" para usarla como foreing key en las clases "Input_CommissionsBank_USF" y "Discount_CommissionsBank_USF" sin antes efectuar el guardado del formulario.


Cordial saludo.





