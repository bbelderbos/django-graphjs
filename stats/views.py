from collections import Counter
from math import ceil

from django.shortcuts import render

from stats.models import BiteStat


def _calculate_max_height_graph(values):
    max_value = float(max(values))
    return int(ceil(max_value / 100.0)) * 100


def index(request):
    stats = BiteStat.objects.order_by('completed')

    data = Counter()
    for row in stats:
        yymm = row.completed.strftime("%Y-%m")
        data[yymm] += 1

    # unpack dict keys / values into two lists
    labels, values = zip(*data.items())
    max_height = _calculate_max_height_graph(values)

    context = {
        "labels": labels,
        "values": values,
        "max_height": max_height,
    }
    return render(request, "graph.html", context)
