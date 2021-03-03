from bokeh.plotting import figure, output_file, show


if __name__ == '__main__':
    output_file('simple_graph.html')
    graph = figure()

    print('**** GRAFICADOR ****')
    total_values = int(input('➡ Cuántos valores quieres graficar: '))
    x_values = list(range(total_values))
    y_values = []

    for i in x_values:
        value = int(input(f'Valor y para {i}'))
        y_values.append(value)

    graph.line(x_values, y_values, line_width=2)
    show(graph)
