def main():
    nombre = input("Ingrese su nombre: ")
    edad_actual = int(input("Ingrese su edad actual: "))
    edad_futura = edad_actual + 5
    print(f"{nombre}, actualmente tiene {edad_actual} años. "
          f"Dentro de cinco años tendrá {edad_futura} años.")

if __name__ == "__main__":
    main()