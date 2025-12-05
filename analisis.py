import pandas as pd

def analizar_ventas(ventas):
    """Lee el CSV de ventas y realiza un analisis usando pandas."""
    
    try:
        df = pd.DataFrame(ventas)
        if df.empty:
            print("No hay datos de ventas para analizar.")
            return
        print("\n-- Análisis de Ventas --")
        #Crear columna Total
        total = total_ventas(ventas)
        print(f"Total de ventas: ${total:,.2f}")
        
        productos_mas_vendidos = df.groupby('Producto')['Cantidad'].sum().idxmax()
        print(f"Producto más vendido: {productos_mas_vendidos}")
        
        producto_mayor_ingreso = df.groupby('Producto')['subtotal'].sum().idxmax()
        print(f"Producto que generó mayor ingreso: {producto_mayor_ingreso}")
        
        #Mejor cliente
        mejor_cliente = df.groupby('Cliente')['subtotal'].sum().idxmax()
        print(f"Mejor cliente: {mejor_cliente}")
        
        # Resumen por fecha
        print("\n--- Resumen de Ventas por Fecha ---")
        resumen_fecha = df.groupby("Fecha")["subtotal"].sum().to_string()
        print(resumen_fecha)
        
        
    except Exception as e:
        print(f"Error al analizar las ventas: {e}")
        
        
def total_ventas(ventas):
    """Calcula el total de ventas."""
    try:
        df = ventas
        df['subtotal'] = df['Cantidad'] * df['Precio']
        total = df['subtotal'].sum()
        return total
    except Exception as e:
        print(f"Error al calcular el total de ventas: {e}") 
        
        