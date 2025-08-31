from django.http import HttpResponse


def score_list(request):
    return HttpResponse("Scores app is working!")
