# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.game_stats, name='home'),
    path('game-stats/', views.game_stats, name='game_stats'),  # New route for game statistics
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('players/', views.player_list, name='player_list'),
    path('players/search/', views.player_search, name='player_search'),
    path('players/edit/<int:player_id>/', views.edit_player, name='edit_player'),
    path('travel-routes/', views.travel_routes, name='travel_routes'),
    path('travel-routes/edit/<int:route_id>/', views.edit_travel_route, name='edit_travel_route'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
