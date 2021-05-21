from tours.data import departures


def navigation(request):
    depart = {'departures_context_for_menu': departures}
    return depart

