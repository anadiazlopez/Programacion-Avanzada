#EJERCICIO 1
from functools import reduce    # Función que aplica operaciones acumulativas

def operation_logger(funcion):
    def wrapper(operacion, *args, **kwargs):
        nombres_op = {
            add: "Suma",
            subtract: "Resta", 
            multiply: "Multiplicación",
            divide: "División"
        }
        
        nombre_operacion = nombres_op.get(operacion, "operación")
    
        try:
            resultado = funcion(operacion, *args, **kwargs)
            
            print(f"{nombre_operacion} de los valores {args}. Resultado = {resultado}.")
            return resultado
            
        except Exception as e:
            print(f"ERROR en '{nombre_operacion}': {e}")
            raise
    
    return wrapper

# FUNCIONES LAMBDA
add = lambda *args: sum(args)
subtract = lambda *args: args[0] - sum(args[1:]) 
multiply = lambda *args: reduce(lambda x, y: x * y, args, 1)
divide = lambda *args: reduce(lambda x, y: x / y, args)

@operation_logger
def math_operation(operacion, *args, **kwargs):
    resultado = operacion(*args)
    
    # Para el uso de **kwargs:
    if kwargs.get('porcentaje'):
        resultado = f"{resultado*100:,.2f}%"
    
    if kwargs.get('redondear'):
        resultado = round(resultado, kwargs['redondear'])
    
    if kwargs.get('moneda'):
        resultado = f"{resultado:,.2f}€"
    
    return resultado

math_operation(add, 5, 3, moneda = True)
math_operation(subtract, 10, 4)
math_operation(multiply, 2, 6)
math_operation(divide, 17, 6, redondear = 2)
math_operation(divide, 1, 3, porcentaje = 2)

try:
    math_operation(divide, 10, 0)
except:
    pass

math_operation(add, 1, 2, 3, 4, 5)

































