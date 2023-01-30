
    function sumar1 (valor) {
        /* TODAS LAS FUNCIONES SUMAR SIGUIENTES HACEN LO MISMO ******* ESTA REPETiCIÓN DE CODIGO ES HORRIBLE xD **********.
           Función para calcular el importe de cada producto, lo calculará o por el valor de metros o el valor de faldas(los dos no se puede)
           Básicamente multiplica el valor de la de la "precio" por el valor de la columna "metros" o "faldas" y lo muestra en el input "importe" */
    
        var total = 0;	    // Variable para acumular el total
        total = parseFloat(valor); // Se convierte el valor de entrada a float
        precio1 = Number(document.getElementById("precio1").value);  // Se obtiene el valor del precio con id precio1
        metros1 = Number(document.getElementById("metros1").value);  // Se obtiene el valor del metros con id metros1
        faldas1 = Number(document.getElementById("faldas1").value);  // Se obtiene el valor de las faldas con id faldas1
        
        // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
    
            if (faldas1 > 0 && metros1 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                console.log("Ambos estan llenos");
            }
            else if (faldas1 == 0) {
                total = (parseFloat(precio1) * parseFloat(metros1));        // Multiplica el precio por los metros. cuando no hay faldas.
               
                sumar_total()
            }else if (metros1 == 0) {
                total = (parseFloat(precio1) * parseFloat(faldas1));        // Multiplica el precio por las faldas. cuando no hay metros.
                sumar_total()
            }
            document.getElementById('importe1').value = total;              // Se muestra el total en el input con id importe1
            sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
        }
           
        function sumar2 (valor) {
    
                var total = 0;	    // Variable para acumular el total
                var sub_total = 0;  // Variable para acumular la suma de todos los productos
                total = parseFloat(valor);
                sub_total = parseFloat(sub_total);
                precio2 = Number(document.getElementById("precio2").value);
                metros2 = Number(document.getElementById("metros2").value);
                faldas2 = Number(document.getElementById("faldas2").value);
                console.log("Faldas2",typeof (faldas2), faldas2);
                // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
                    
                console.log(faldas2);
                    if (faldas2 > 0 && metros2 > 0){      // Verifica si campo faldas y campo metros son mayores que 0, entonces no realiza los calculos
                        console.log("Ambos estan llenos");
                    }
                    else if (faldas2 == 0) {
                        total = (parseFloat(precio2) * parseFloat(metros2));        // Multiplica el precio por los metros. cuando no hay faldas.
                       
                        sumar_total()
                    }else if (metros2 == 0) {
                        total = (parseFloat(precio2) * parseFloat(faldas2));        // Multiplica el precio por las faldas. cuando no hay metros.
                        sumar_total()
                    }
        // Colocar el resultado de la suma en el control "span".
        document.getElementById('importe2').value = total;
        sumar_total();
       }
       function sumar3 (valor) {
    
        var total = 0;	    // Variable para acumular el total
        total = parseFloat(valor); // Se convierte el valor de entrada a float
        precio3 = Number(document.getElementById("precio3").value);  // Se obtiene el valor del precio con id precio1
        metros3 = Number(document.getElementById("metros3").value);  // Se obtiene el valor del metros con id metros1
        faldas3 = Number(document.getElementById("faldas3").value);  // Se obtiene el valor de las faldas con id faldas1
        
        // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
    
            if (faldas3 > 0 && metros3 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                console.log("Ambos estan llenos");
            }
            else if (faldas3 == 0) {
                total = (parseFloat(precio3) * parseFloat(metros3));        // Multiplica el precio por los metros. cuando no hay faldas.
                sumar_total()
            }else if (metros3 == 0) {
                total = (parseFloat(precio3) * parseFloat(faldas3));        // Multiplica el precio por las faldas. cuando no hay metros.
                sumar_total()
            }
            document.getElementById('importe3').value = total;
            sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
        }
        function sumar4 (valor) {
    
            var total = 0;	    // Variable para acumular el total
            total = parseFloat(valor); // Se convierte el valor de entrada a float
            precio4 = Number(document.getElementById("precio4").value);  // Se obtiene el valor del precio con id precio1
            metros4 = Number(document.getElementById("metros4").value);  // Se obtiene el valor del metros con id metros1
            faldas4 = Number(document.getElementById("faldas4").value);  // Se obtiene el valor de las faldas con id faldas1
            
            // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
        
                if (faldas4 > 0 && metros4 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                    console.log("Ambos estan llenos");
                }
                else if (faldas4 == 0) {
                    total = (parseFloat(precio4) * parseFloat(metros4));        // Multiplica el precio por los metros. cuando no hay faldas.
                    sumar_total()
                }else if (metros4 == 0) {
                    total = (parseFloat(precio4) * parseFloat(faldas4));        // Multiplica el precio por las faldas. cuando no hay metros.
                    sumar_total()
                }
                document.getElementById('importe4').value = total;
                sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
            }
            function sumar5 (valor) {
    
                var total = 0;	    // Variable para acumular el total
                total = parseFloat(valor); // Se convierte el valor de entrada a float
                precio5 = Number(document.getElementById("precio5").value);  // Se obtiene el valor del precio con id precio1
                metros5 = Number(document.getElementById("metros5").value);  // Se obtiene el valor del metros con id metros1
                faldas5 = Number(document.getElementById("faldas5").value);  // Se obtiene el valor de las faldas con id faldas1
                
                // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
            
                    if (faldas5 > 0 && metros5 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                        console.log("Ambos estan llenos");
                    }
                    else if (faldas5 == 0) {
                        total = (parseFloat(precio5) * parseFloat(metros5));        // Multiplica el precio por los metros. cuando no hay faldas.
                        sumar_total()
                    }else if (metros5 == 0) {
                        total = (parseFloat(precio5) * parseFloat(faldas5));        // Multiplica el precio por las faldas. cuando no hay metros.
                        sumar_total()
                    }
                    document.getElementById('importe5').value = total;
                    sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
                }
                function sumar6 (valor) {
    
                    var total = 0;	    // Variable para acumular el total
                    total = parseFloat(valor); // Se convierte el valor de entrada a float
                    precio6 = Number(document.getElementById("precio6").value);  // Se obtiene el valor del precio con id precio1
                    metros6 = Number(document.getElementById("metros6").value);  // Se obtiene el valor del metros con id metros1
                    faldas6 = Number(document.getElementById("faldas6").value);  // Se obtiene el valor de las faldas con id faldas1
                    
                    // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
                
                        if (faldas6 > 0 && metros6 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                            console.log("Ambos estan llenos");
                        }
                        else if (faldas6 == 0) {
                            total = (parseFloat(precio6) * parseFloat(metros6));        // Multiplica el precio por los metros. cuando no hay faldas.
                            sumar_total()
                        }else if (metros6 == 0) {
                            total = (parseFloat(precio6) * parseFloat(faldas6));        // Multiplica el precio por las faldas. cuando no hay metros.
                            sumar_total()
                        }
                        document.getElementById('importe6').value = total;
                        sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
                    }
                    function sumar7 (valor) {
    
                        var total = 0;	    // Variable para acumular el total
                        total = parseFloat(valor); // Se convierte el valor de entrada a float
                        precio7 = Number(document.getElementById("precio7").value);  // Se obtiene el valor del precio con id precio1
                        metros7 = Number(document.getElementById("metros7").value);  // Se obtiene el valor del metros con id metros1
                        faldas7 = Number(document.getElementById("faldas7").value);  // Se obtiene el valor de las faldas con id faldas1
                        
                        // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
                    
                            if (faldas7 > 0 && metros7 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                                console.log("Ambos estan llenos");
                            }
                            else if (faldas7 == 0) {
                                total = (parseFloat(precio7) * parseFloat(metros7));        // Multiplica el precio por los metros. cuando no hay faldas.
                                sumar_total()
                            }else if (metros7 == 0) {
                                total = (parseFloat(precio7) * parseFloat(faldas7));        // Multiplica el precio por las faldas. cuando no hay metros.
                                sumar_total()
                            }
                            document.getElementById('importe7').value = total;
                            sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
                        }
                        
                        
                        function sumar8 (valor) {
    
                            var total = 0;	    // Variable para acumular el total
                            total = parseFloat(valor); // Se convierte el valor de entrada a float
                            precio8 = Number(document.getElementById("precio8").value);  // Se obtiene el valor del precio con id precio1
                            metros8 = Number(document.getElementById("metros8").value);  // Se obtiene el valor del metros con id metros1
                            faldas8 = Number(document.getElementById("faldas8").value);  // Se obtiene el valor de las faldas con id faldas1
                            
                            // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
                        
                                if (faldas8 > 0 && metros8 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                                    console.log("Ambos estan llenos");
                                }
                                else if (faldas8 == 0) {
                                    total = (parseFloat(precio8) * parseFloat(metros8));        // Multiplica el precio por los metros. cuando no hay faldas.
                                    sumar_total()
                                }else if (metros8 == 0) {
                                    total = (parseFloat(precio8) * parseFloat(faldas8));        // Multiplica el precio por las faldas. cuando no hay metros.
                                    sumar_total()
                                }
                                document.getElementById('importe8').value = total;
                                sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
                            }
                            function sumar9 (valor) {
    
                                var total = 0;	    // Variable para acumular el total
                                total = parseFloat(valor); // Se convierte el valor de entrada a float
                                precio9 = Number(document.getElementById("precio9").value);  // Se obtiene el valor del precio con id precio1
                                metros9 = Number(document.getElementById("metros9").value);  // Se obtiene el valor del metros con id metros1
                                faldas9 = Number(document.getElementById("faldas9").value);  // Se obtiene el valor de las faldas con id faldas1
                                
                                // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
                            
                                    if (faldas9 > 0 && metros9 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                                        console.log("Ambos estan llenos");
                                    }
                                    else if (faldas9 == 0) {
                                        total = (parseFloat(precio9) * parseFloat(metros9));        // Multiplica el precio por los metros. cuando no hay faldas.
                                        sumar_total()
                                    }else if (metros9 == 0) {
                                        total = (parseFloat(precio9) * parseFloat(faldas9));        // Multiplica el precio por las faldas. cuando no hay metros.
                                        sumar_total()
                                    }
                                    document.getElementById('importe9').value = total;
                                    sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
                                }
                                function sumar10 (valor) {
    
                                    var total = 0;	    // Variable para acumular el total
                                    total = parseFloat(valor); // Se convierte el valor de entrada a float
                                    precio10 = Number(document.getElementById("precio10").value);  // Se obtiene el valor del precio con id precio1
                                    metros10 = Number(document.getElementById("metros10").value);  // Se obtiene el valor del metros con id metros1
                                    faldas10 = Number(document.getElementById("faldas10").value);  // Se obtiene el valor de las faldas con id faldas1
                                    
                                    // Aquí valido si hay un valor previo, si no hay datos, le pongo un cero "0".
                                
                                        if (faldas10 > 0 && metros10 > 0){      // Verifica si campo faldas y campo metros son mayores que 0,si lo son entonces no realiza los calculos
                                            console.log("Ambos estan llenos");
                                        }
                                        else if (faldas10 == 0) {
                                            total = (parseFloat(precio10) * parseFloat(metros10));        // Multiplica el precio por los metros. cuando no hay faldas.
                                            sumar_total()
                                        }else if (metros10 == 0) {
                                            total = (parseFloat(precio10) * parseFloat(faldas10));        // Multiplica el precio por las faldas. cuando no hay metros.
                                            sumar_total()
                                        }
                                        document.getElementById('importe10').value = total;
                                        sumar_total();  // Llamo a la función para sumar el total de todos los inputs "importe".
                                    }
    
    function sumar_total(){
        /* Este código primero sumara todos los valores de la columna "total".
           Tambien pondra la suma en el input del texto "total", el valor para el input de iva y el total con el valor de iva.*/arguments
     
           total1 = Number(document.getElementById("importe1").value).toFixed(2);
           total2 = Number(document.getElementById("importe2").value).toFixed(2);
           total3 = Number(document.getElementById("importe3").value).toFixed(2);
           total4 = Number(document.getElementById("importe4").value).toFixed(2);
           total5 = Number(document.getElementById("importe5").value).toFixed(2);
           total6 = Number(document.getElementById("importe6").value).toFixed(2);
           total7 = Number(document.getElementById("importe7").value).toFixed(2);
           total8 = Number(document.getElementById("importe8").value).toFixed(2);
           total9 = Number(document.getElementById("importe9").value).toFixed(2);
           total10 = Number(document.getElementById("importe10").value).toFixed(2);
    
        total = parseFloat(total1) + parseFloat(total2) + parseFloat(total3) + parseFloat(total4) + parseFloat(total5) + parseFloat(total6) + parseFloat(total7) + parseFloat(total8) +  parseFloat(total9) + parseFloat(total10);
        document.getElementById('sub_total_sin_iva').value = total.toFixed(2);    // Añadido limete 2 de numeros decimales para que no se vuelva loco a la hora de hacer los cálculos
        document.getElementById("iva_input").value=  (total * 0.21).toFixed(2); // Añadido limete 2 de numeros decimales para que no se vuelva loco a la hora de hacer los cálculos
        iva = total * 0.21;
        iva.toFixed(2);
        document.getElementById("total_con_iva").value = (total + iva).toFixed(2); 
    
    
    }
       //Cambiar tecla tabulador por la tecla intro, para pasar de un campo a otro en el formulario de la factura.
       document.addEventListener('keydown', function (event) {
        if (event.keyCode === 13 && event.target.nodeName === 'INPUT') {
             var form = event.target.form;
             var index = Array.prototype.indexOf.call(form, event.target);
             form.elements[index + 1].focus();
             event.preventDefault();
        }
    });
    

sumar_total();  //En editar se llama a sumar_total para que nada mas entrar en la página, se sumen los valores de los inputs. y de los totales
function ver_modal(){
var myModal = new bootstrap.Modal(document.getElementById('myModal'));
myModal.show();
}
