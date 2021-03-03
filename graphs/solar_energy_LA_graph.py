import csv
from bokeh.plotting import figure, output_file, show


with open('LADWP_Solar_Incentive_Program.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = list(csv_reader)

    x_values = []
    y_values = []
    temp_row = []  # Almacena lso valores de la primera columna del csv

    for i in data:
        temp_row.append(i[0])
        y_values.append(i[1])

    x_values = list(range(len(temp_row)))  # Crea una lista del tamaño de la primera columna del csv


if __name__ == '__main__':
    output_file('solar_energy_LA_graph.html')
    graph = figure()

    graph.line(x_values, y_values, line_width=2)
    show(graph)

