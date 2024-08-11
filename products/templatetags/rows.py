from django import template

register = template.Library()

@register.filter(name='rows')
def rows(list_data, rows_size):
    rows = []
    i = 0
    for data in list_data:
        rows.append(data)
        i = i + 1
        if i == rows_size:
            yield rows
            rows = []
            i = 0
    if rows:
        yield rows
