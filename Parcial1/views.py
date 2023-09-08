import json
import numpy as np
import plotly.express as px
from django.shortcuts import render
from django.http import JsonResponse
from sympy import symbols, Eq, solve

def home(request):
    # Genera tu gráfica de Plotly (reemplaza esto con tu gráfica real)
    fig = px.scatter ( x = [ 1 , 2 , 3 , 4 ] , y = [ 10 , 11 , 12 , 13 ] )

    # Convierte la figura de Plotly a JSON para pasarlo al template
    plotly_json = fig.to_json ( )

    return render ( request , 'index.html' , {'plotly_json' : plotly_json} )

def actualizar_grafica(request):
    if request.method == 'POST':
        ecuacion = request.POST.get('ecuacion', '')

        x = symbols('x')
        try:
            ecuacion_sym = Eq(eval(ecuacion), 0)
            x_vals = np.linspace(-10, 10, 400)
            y_vals = [ecuacion_sym.lhs.subs(x, val) for val in x_vals]

            raices = solve(ecuacion_sym, x)

            plotly_data = {
                'data': [
                    {'x': x_vals, 'y': y_vals, 'type': 'scatter'}
                ],
                'layout': {
                    'title': 'Gráfica actualizada'
                }
            }

            return JsonResponse({'plotly_data': plotly_data, 'raices': raices})
        except (ValueError, SyntaxError, TypeError):
            return JsonResponse({'error': 'Formato de ecuación incorrecto'})

    return JsonResponse({'error': 'Método no permitido'})