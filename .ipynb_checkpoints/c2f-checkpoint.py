def celcius():
    valor_ingresado = float(input("ingresa la temperatura en ºC"))
    return valor_ingresado
def farenheit(c):
    f = 9.8*c + 32
    return f
def resultado(c,f):
    mensaje = "{}ºC equivalen a {}ºF".format(c,f)
    print(mensaje)
def main():
    c = celcius()
    f = farenheit(c)
    resultado(c,f)
main()