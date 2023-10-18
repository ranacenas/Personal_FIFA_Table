from django import forms
from .models import game_history
import sqlite3


class fifaforms(forms.ModelForm):

    class Meta:
        model = game_history
        fields = ["hometeam",
		"homescore",
		"awayteam",
		"awayscore",
		]


