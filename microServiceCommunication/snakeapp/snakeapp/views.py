from django.shortcuts import render

def snake_game_view(request):
    return render(request, 'snake_game.html')
