from django.http import HttpResponse


def student_list(request):
    return HttpResponse("This is the students page.")
