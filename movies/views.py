from django.shortcuts import render


def movie_main(request):
    return render(request, 'movies/main/main.html')



