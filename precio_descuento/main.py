def main():
    precio_original = float(input("Ingrese el precio original del producto: "))
    descuento = precio_original * 0.10
    precio_final = precio_original - descuento
    print(f"Precio original: {precio_original}")
    print(f"Descuento (10%): {descuento}")
    print(f"Precio final: {precio_final}")

if __name__ == "__main__":
    main()