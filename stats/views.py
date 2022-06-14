from collections import Counter
from math import ceil

from django.shortcuts import render

from stats.models import BiteStat


def index(request):
    stats = BiteStat.objects.order_by('completed')

    data = Counter()
    for row in stats:
        yymm = row.completed.strftime("%Y-%m")
        data[yymm] += 1

    # unpack dict keys / values into two lists
    labels, values = zip(*data.items())

    context = {
        "labels": labels,
        "values": values,
    }
    return render(request, "graph.html", context)
