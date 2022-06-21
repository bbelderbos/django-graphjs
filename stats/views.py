from collections import Counter, defaultdict
from math import ceil

from django.shortcuts import render

from stats.models import BiteStat


def index(request):
    stats = BiteStat.objects.order_by('completed')

    data_completion_per_month = Counter()
    data_user_level = defaultdict(list)
    for row in stats:
        yymm = row.completed.strftime("%Y-%m")
        data_completion_per_month[yymm] += 1
        data_user_level[row.exercise].append(row.level)

    # unpack dict keys / values into two lists for the completion stats
    labels_completion, values_completion = zip(*data_completion_per_month.items())

    # calculate average from user level stats
    data_average_user_level = defaultdict(int)
    for exercise in data_user_level:
        avg_val = sum(data_user_level[exercise])/len(data_user_level[exercise])
        data_average_user_level[exercise] = avg_val

    # unpack dict keys / values into two lists for the average stats
    labels_avg_user_level, values_avg_user_level = zip(*sorted(data_average_user_level.items()))

    context = {
        "labels_completion": labels_completion,
        "values_completion": values_completion,
        "labels_avg_user_level": labels_avg_user_level,
        "values_avg_user_level": values_avg_user_level,
    }

    return render(request, "graph.html", context)
