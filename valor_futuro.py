# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:15:21 2023

@author: Andres
"""

def calcular_valor_futuro(vpn, tasa_descuento, numero_periodos):
    flujo_ingresos_futuro = vpn * ((1 + tasa_descuento) ** numero_periodos)
    return flujo_ingresos_futuro

tasa_descuento = 0.0239
numero_periodos = 12
vpn = 10000  # Valor Presente Neto

ingresos_futuro = calcular_valor_futuro(vpn, tasa_descuento, numero_periodos)
print(f"Valor futuro: {ingresos_futuro} Tasa mensual {tasa_descuento} Periodos:{numero_periodos}")