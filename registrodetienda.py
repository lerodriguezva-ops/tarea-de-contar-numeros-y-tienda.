producto=input("ingrese el nombre del producto: (FIN para terminar): ")

productosregistrados=0
productoscondescuentos=0
totaldeproductos=0
totalcompras=0
totalpagado=0

while producto!="FIN":
    cantidad=int(input("ingrese la cantidad del producto: "))
    precio=float(input("ingrese el precio del producto: "))
    productosregistrados+=1
    totaldeproductos=float(cantidad*precio)
    descuento=0

    if (totaldeproductos>1000):
        descuentos=totaldeproductos*0.10
        productoscondescuentos+=1

    elif (totaldeproductos>500):
        descuentos=totaldeproductos*0.05
        productoscondescuentos+=1

    valorfinal=totaldeproductos-descuentos 

    input("producto "+str(producto)) 
    input("valor original: $ "+str(totaldeproductos))
    input("descuento: $ "+str(descuento))
    input("valor a pagar: $ "+str(valorfinal))

    totalcompras+=totaldeproductos
    totalpagado+=valorfinal
    producto=input("ingrese el nombre del producto: (FIN para terminar): ")
    
input("------RESUMEN DE LA COMPRA---")
input("productos registrados: "+ str(productosregistrados))
input("productos con descuentos: "+ str(productoscondescuentos))
input("total de compras: $ "+str(totalcompras))
input("valor final a pagar: $ "+str(totalpagado))
    


