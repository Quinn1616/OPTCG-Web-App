from django.shortcuts import render
import pypyodbc as odbc
from django.http import HttpResponseRedirect
import random
from django.db import connection
from credentials import username, password

# Create your views here.
def home(request):
    return render(request, 'optcg/home.html')

def random_card(request):
   
    server = 'mysqlserver16.database.windows.net'
    database = 'OPTCG'

    connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};Server='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()

    sql = '''SELECT * FROM [dbo].[Cards];'''
    cursor.execute(sql)
    dataset = cursor.fetchall()

    random_card = random.choice(dataset)
    card_number, name, cost, power, tag, effect, counter, card_type, is_blocker, is_rush, card_architype, _ = random_card



    context = {
        'card_number': card_number,
        'name': name,
        'cost': cost,
        'power': power,
        'tag': tag,
        'effect': effect,
        'counter': counter,
        'card_type': card_type,
        'is_blocker': is_blocker,
        'is_rush': is_rush,
        'card_architype': card_architype,
    }
    return render(request, 'optcg/random_card.html', context)

def search_card(request):
    if 'card_number' in request.GET:
        card_number = request.GET['card_number']
        server = 'mysqlserver16.database.windows.net'
        database = 'OPTCG'

        connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};Server='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

        sql = '''SELECT * FROM [dbo].[Cards] WHERE card_id = ?;'''
        cursor.execute(sql, (card_number,))
        card = cursor.fetchone()

        if card:
            card_number, name, cost, power, tag, effect, counter, card_type, is_blocker, is_rush, card_architype, _ = card

            context = {
                'card_number': card_number,
                'name': name,
                'cost': cost,
                'power': power,
                'tag': tag,
                'effect': effect,
                'counter': counter,
                'card_type': card_type,
                'is_blocker': is_blocker,
                'is_rush': is_rush,
                'card_architype': card_architype,
            }
            return render(request, 'optcg/search_result.html', context)
        else:
            return render(request, 'optcg/search_card.html', {'error': 'Card not found'})
    else:
        return render(request, 'optcg/search_card.html')
    
from django.shortcuts import render

def search_result(request):
    
    card_number = request.GET.get('card_number')
    name = "Card Name"  
    cost = "Card Cost"  
    power = "Card Power"  
    tag = "Card Tag"  
    effect = "Card Effect" 
    counter = "Card Counter"  
    card_type = "Card Type" 
    is_blocker = "Is Blocker" 
    is_rush = "Is Rush"  
    card_architype = "Card Architype"  
    
    context = {
        'card_number': card_number,
        'name': name,
        'cost': cost,
        'power': power,
        'tag': tag,
        'effect': effect,
        'counter': counter,
        'card_type': card_type,
        'is_blocker': is_blocker,
        'is_rush': is_rush,
        'card_architype': card_architype,
    }
    return render(request, 'optcg/search_result.html', context)

