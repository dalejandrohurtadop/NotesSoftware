from bokeh.plotting import figure, output_file, show


if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()
    total_val = int(input("mencioan la cantidad de valores que deseas graficar: "))
    x_vals = list(range(total_val))
    y_val = []

    for x in x_vals:
        val = int(input(f'Valor y para {x}: '))
        y_val.append(val)

    fig.line(x_vals, y_val, line_width = 2)
    show(fig)

