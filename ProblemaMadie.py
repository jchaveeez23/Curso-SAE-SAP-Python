"""
Se le contrata para que pueda realizar lo que se pide a continuación, desarrolle el código para
un programa para una tienda de venta de abarrotes, que permita ingresar las compras de un
cliente, los datos de ingreso son la cantidad de (libras): arroz (Q2.00), frijol (Q1.75), Azúcar
(Q2.50), sino se va a comprar alguno de los productos se ingresa cero. 
Debe calcular el pago a realizar: la suma de las multiplicaciones de las cantidades por el precio respectivo, 
luego calcular el IVA (12%) y luego calcular un pago: pago de las compras más el IVA calculado.
Pero la tienda hace 1 descuento: si el pago es mayor a Q15.00 el descuento es del 2.5%. El
porcentaje se aplica sobre el pago. Otro descuento que hace la Tienda es si se compran más
de 10 libras de arroz y más de 5 libras de frijol, el porcentaje es del 3.% de descuento. 
Debe mostrar: 1) el pago antes del IVA 
2) el IVA 
3) el Pago con el IVA incluido
4) el o los descuentos
5) el pago final: pago con el IVA incluido menos el o los descuentos."""
precio_arroz = 2.0
precio_frijol = 1.75
precio_azucar = 2.5
print('Si no desea ninguno de los productos Ingrese 0...')
lbarroz = int(input('Ingrese la cantidad de libras de arroz a llevar: '))
lbfrijol = int(input('Ingrese la cantidad de libras de frijol a llevar: '))
lbazucar = int(input('Ingrese la cantidad de libras de azucar a llevar: '))
totarroz = lbarroz * precio_arroz
totfrijol = lbfrijol * precio_frijol
totazucar = lbazucar * precio_azucar
subtotal = totarroz + totazucar + totfrijol
iva = subtotal* 0.12
siniva = subtotal - iva
if subtotal > 15 and (lbarroz < 10 and lbfrijol < 5 ):
    descuento = subtotal * 0.025
    total = subtotal - descuento
    print('El monto a pagar sin iva es de: Q.',siniva)
    print('El monto a pagar de iva es de: Q.',iva)
    print('El monto a pagar con iva es de: Q.',subtotal)
    print('El monto de descuento aplicado es de: Q.',descuento)
    print('El monto final de: Q.',total)
elif subtotal > 15 and lbarroz > 10 and lbfrijol > 5:
    descuento = subtotal * 0.03
    total = subtotal -  descuento
    print('El monto a pagar sin iva es de: Q.',siniva)
    print('El monto a pagar de iva es de: Q.',iva)
    print('El monto a pagar con iva es de: Q.',subtotal)
    print('El monto de descuento aplicado es de: Q.',descuento)
    print('El monto final de: Q.',total)
else:
    print('El monto a pagar sin iva es de: Q.',siniva)
    print('El monto a pagar de iva es de: Q.',iva)
    print('El monto a pagar con iva es de: Q.',subtotal)
    print('El monto de descuento aplicado es de: NO APLICA')
    print('El monto final de: Q.',subtotal)


