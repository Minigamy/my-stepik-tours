from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from tours.data import departures, tours
from tours.templatetags import function


def main_view(request):
    return render(request, 'tours/index.html', context={'six_tours': function.random_six_tours(),

                                                        })


def departure_view(request, departure):
    depart_tours = function.depart_filter(departure)
    depart_tours_info = function.tours_info(departure)
    return render(request, 'tours/departure.html', context={'tours': depart_tours,
                                                            'direction': departures[departure],
                                                            'tours_info': depart_tours_info,

                                                            })


def tour_view(request, tour_id):
    tour = tours[tour_id]
    return render(request, 'tours/tour.html', context={'tours': tour,
                                                       'departures': departures[tour['departure']],
                                                       'star': tour['stars'],

                                                       })


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 Страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
