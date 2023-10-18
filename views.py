from django.shortcuts import render

# Create your views here.
from .forms import *
from .models import game_history, standing
import psycopg2
import os
#from decouple import config
# Create your views here.


def showfifa(request):
    #homeform = HomeForm(request.POST)
    #awayform = AwayForm(request.POST)
    form = fifaforms(request.POST or None)
    if form.is_valid():
        form.save()
    stand = standing.objects.all().order_by('-percentage')
    fifa2 = game_history.objects.all().order_by('-id')
    listfifa = list(stand)
    sql = """UPDATE fifaone_standing SET mp = sub.matchesplayed, wins = sub.matchwon, losses = sub.matchlost, draws = sub.matchtied
FROM (SELECT team, COUNT(*) matchesplayed,
SUM ( CASE WHEN matchresult = 'won' THEN 1 ELSE 0 END ) AS matchwon,
SUM ( CASE WHEN matchresult = 'tied' THEN 1 ELSE 0 END ) AS matchtied,
SUM ( CASE WHEN matchresult = 'lost' THEN 1 ELSE 0 END ) AS matchlost
FROM
(
	SELECT hometeam AS team,
	CASE WHEN homescore>awayscore THEN 'won'
	WHEN homescore < awayscore THEN 'lost'
	WHEN homescore = awayscore THEN 'tied'
	END AS matchresult
	FROM fifaone_game_history

	UNION ALL
	SELECT awayteam AS team,
	CASE WHEN homescore<awayscore THEN 'won'
	WHEN homescore > awayscore THEN 'lost'
	WHEN homescore = awayscore THEN 'tied'
	END AS matchresult
	FROM fifaone_game_history

) A
GROUP BY team) AS sub
WHERE fifaone_standing.team = sub.team;"""

    sql2= """UPDATE fifaone_standing SET percentage =  CAST(wins AS float) / CAST(mp AS float) WHERE mp > 1;"""

    conn = psycopg2.connect(
        'REDACTED')


    #heroku
    # DATABASE_URL = os.environ['DATABASE_URL']
    # conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute(sql)
    cur.execute(sql2)
    conn.commit()
    cur.close()


    return render(request, "fifaone/table.html", {'form':form, 'fifa':fifa2, 'standings':stand, 'listfifa':listfifa})


