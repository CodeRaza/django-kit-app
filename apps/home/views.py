# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    # try:

    load_template = request.path.split('/')[-1]

    if load_template == 'admin':
        return HttpResponseRedirect(reverse('admin:index'))
    context['segment'] = load_template

    html_template = loader.get_template('home/' + load_template)
    return HttpResponse(html_template.render(context, request))

    # except template.TemplateDoesNotExist:

    #     html_template = loader.get_template('home/page-404.html')
    #     return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))



# views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Count
from .models import PlayerProfiles, PlayerLocations

@login_required(login_url="/login/")
def game_stats(request):
    total_players = PlayerProfiles.objects.count()
    players_spent_money = PlayerProfiles.objects.filter(has_spent_money=True).count()
    total_credits = PlayerProfiles.objects.aggregate(Sum('credits'))['credits__sum']
    us_bank_balance = PlayerProfiles.objects.aggregate(Sum('us_banking'))['us_banking__sum']
    mx_bank_balance = PlayerProfiles.objects.aggregate(Sum('mx_banking'))['mx_banking__sum']
    avg_account_age = PlayerProfiles.objects.aggregate(Avg('account_age'))['account_age__avg']
    avg_networth = PlayerProfiles.objects.aggregate(Avg('networth'))['networth__avg']
    top_10_players = PlayerProfiles.objects.order_by('-networth')[:10]
    jail_count = PlayerLocations.objects.filter(jail__gt=0).count()
    hospital_count = PlayerLocations.objects.filter(hospital__gt=0).count()
    users_per_city = PlayerLocations.objects.values('city').annotate(count=Count('id'))
    us_players = PlayerProfiles.objects.filter(country='US').count()
    eu_players = PlayerProfiles.objects.filter(country='EU').count()
    ch_players = PlayerProfiles.objects.filter(country='CH').count()
    ru_players = PlayerProfiles.objects.filter(country='RU').count()
    sa_players = PlayerProfiles.objects.filter(country__in=['IN', 'PK']).count()

    context = {
        'total_players': total_players,
        'players_spent_money': players_spent_money,
        'total_credits': total_credits,
        'us_bank_balance': us_bank_balance,
        'mx_bank_balance': mx_bank_balance,
        'avg_account_age': avg_account_age,
        'avg_networth': avg_networth,
        'top_10_players': top_10_players,
        'jail_count': jail_count,
        'hospital_count': hospital_count,
        'users_per_city': users_per_city,
        'us_players': us_players,
        'eu_players': eu_players,
        'ch_players': ch_players,
        'ru_players': ru_players,
        'sa_players': sa_players,
    }

    return render(request, 'custom/game_stats.html', context)


from django.shortcuts import render, redirect

from .models import PlayerProfiles as PlayerProfile

def leaderboard(request):
    players = PlayerProfiles.objects.order_by('-networth')
    return render(request, 'custom/leaderboard.html', {'players': players})


from .forms import PlayerProfileForm

def player_list(request):
    players = PlayerProfile.objects.all()
    return render(request, 'custom/player_list.html', {'players': players})

def player_search(request):
    query = request.GET.get('query', '')
    if query:
        players = PlayerProfile.objects.filter(username__icontains=query)
    else:
        players = PlayerProfile.objects.all()
    return render(request, 'custom/player_search.html', {'players': players})

def edit_player(request, player_id):
    player = get_object_or_404(PlayerProfile, id=player_id)

    if request.method == 'POST':
        form = PlayerProfileForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerProfileForm(instance=player)

    context = {
        'player': player,
        'form': form,
    }
    return render(request, 'custom/edit_player.html', context)


from django.shortcuts import render
from .models import TravelRoutes
from .forms import TravelRouteForm

def travel_routes(request):
    # Retrieve all travel routes from the model
    routes = TravelRoutes.objects.all()
    return render(request, 'custom/travel_routes.html', {'routes': routes})


def edit_travel_route(request, route_id):
    route = get_object_or_404(TravelRoutes, id=route_id)
    if request.method == 'POST':
        form = TravelRouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('travel_routes')
    else:
        form = TravelRouteForm(instance=route)
    return render(request, 'custom/edit_travel_route.html', {'form': form})