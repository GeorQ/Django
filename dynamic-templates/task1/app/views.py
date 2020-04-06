from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    file  = open("inflation_russia.csv", "r")
    csv_reader = csv.reader(file, delimiter=";")
    header = next(csv_reader)
    row_len = int(len(header) - 1)
    content = []
    for row in csv_reader:
        content.append(row)
    print(content[0][1])
    print(type(content[0][1]))

    # чтение csv-файла и заполнение контекста
    context = {
        "header": header,
        "content": content,
        "lene": row_len,
    }
    file.close()
    return render(request, template_name,
                  context)
