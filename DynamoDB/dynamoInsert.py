import boto3

#Creacion un cliente de DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1') 

#Nombre de la tabla de DynamoDB
tabla_nombre = 'songs'
i = 0

#Datos a insertar
items = [
    {
        'corleone': {'S': 'corleone-2'},
        'artist': {'S': 'Don Toliver'},
        'duration': {'S':'180'},
        'genre': {'L': [{'S':'Trap'}, {'S':'Atlanta Trap'}, {'S':'New Era'}]},
        'name': {'S':'No Idea'},
        'year': {'S':'2020'}
    },
    {
         'corleone': {'S': 'corleone-3'},
         'artist': {'S': 'Kadavar'},
         'duration': {'S':'660'},
         'genre': {'L': [{'S':'Progressive Metal'}, {'S':'Stone Rock'}, {'S':'Psychedelic Rock'}]},
         'name': {'S':'Blood Moon Night'},
         'year': {'S':'2021'}
    },
    {
         'corleone': {'S': 'corleone-4'},
         'artist': {'S': 'Metallica'},
         'duration': {'S':'300'},
         'genre': {'L': [{'S':'Trash Metal'}, {'S':'Heavy Metal'}, {'S':'Hard Rock'}]},
         'name': {'S':'Master of Puppets'},
         'year': {'S':'1984'}
     },
     {
         'corleone': {'S': 'corleone-5'},
         'artist': {'S': 'Michael Jackson'},
         'duration': {'S':'500'},
         'genre': {'L': [{'S':'Pop'}, {'S':'Funk'}, {'S':'Disco'}]},
         'name': {'S':'Thriller'},
         'year': {'S':'1982'}
     },
     {
         'corleone': {'S': 'corleone-6'},
         'artist': {'S': 'The Beatles'},
         'duration': {'S':'200'},
         'genre': {'L': [{'S':'Rock'}, {'S':'Rock and Roll'}, {'S':'Classic'}]},
         'name': {'S':'Hey Jude'},
         'year': {'S':'1968'}
     },
     {
         'corleone': {'S': 'corleone-7'},
         'artist': {'S': 'Canserbero'},
         'duration': {'S':'420'},
         'genre': {'L': [{'S':'Rap'}, {'S':'Hip Hop'}, {'S':'Latin Rap'}]},
         'name': {'S':'Es Épico'},
         'year': {'S':'2012'}
     },
     {
         'corleone': {'S': 'corleone-8'},
         'artist': {'S': 'Cream'},
         'duration': {'S':'160'},
         'genre': {'L': [{'S':'Rock'}, {'S':'Rock and Roll'}, {'S':'Classic'}]},
         'name': {'S':'Sunshine of Your Love'},
         'year': {'S':'1967'}
     },
     {
         'corleone': {'S': 'corleone-9'},
         'artist': {'S': 'Eminem'},
         'duration': {'S':'350'},
         'genre': {'L': [{'S':'Rap'}, {'S':'Hip Hop'}, {'S':'Comedy Rap'}]},
         'name': {'S':'Without Me'},
         'year': {'S':'2002'}
     },
     {
         'corleone': {'S': 'corleone-10'},
         'artist': {'S': '50 Cent'},
         'duration': {'S':'180'},
         'genre': {'L': [{'S':'Rap'}, {'S':'Hip Hop'}, {'S':'East Coast Rap'}]},
         'name': {'S':'In Da Club'},
         'year': {'S':'2003'}
     },
     {
         'corleone': {'S': 'corleone-11'},
         'artist': {'S': 'Elvis Presley'},
         'duration': {'S':'500'},
         'genre': {'L': [{'S':'Blues'}, {'S':'Pop'}, {'S':'Rock and Roll'}]},
         'name': {'S':'Cant Help Falling in Love'},
         'year': {'S':'1961'}
     },
     {
         'corleone': {'S': 'corleone-12'},
         'artist': {'S': 'Dr Dre'},
         'duration': {'S':'120'},
         'genre': {'L': [{'S':'Rap'}, {'S':'Gangsta Rap'}, {'S':'West Coast Rap'}]},
         'name': {'S':'Still D.R.E'},
         'year': {'S':'1999'}
     },
     {
         'corleone': {'S': 'corleone-13'},
         'artist': {'S': 'Tool'},
         'duration': {'S':'770'},
         'genre': {'L': [{'S':'Progressive Metal'}, {'S':'Heavy Metal'}, {'S':'Alternative Metal'}]},
         'name': {'S':'Forty Six & 2'},
         'year': {'S':'1996'}
     },
     {
         'corleone': {'S': 'corleone-14'},
         'artist': {'S': 'Lewis Capaldi'},
         'duration': {'S':'440'},
         'genre': {'L': [{'S':'Pop'}, {'S':'Pop Rock'}, {'S':'Indie Pop'}]},
         'name': {'S':'Someone You Loved'},
         'year': {'S':'2019'}
     },
     {
         'corleone': {'S': 'corleone-15'},
         'artist': {'S': 'Eazy E'},
         'duration': {'S':'290'},
        'genre': {'L': [{'S':'Rap'}, {'S':'Gangsta Rap'}, {'S':'West Coast Rap'}]},
         'name': {'S':'Boyz N The Hood'},
         'year': {'S':'1987'}
     },
     {
         'corleone': {'S': 'corleone-16'},
         'artist': {'S': 'The Beach Boys'},
         'duration': {'S':'120'},
        'genre': {'L': [{'S':'Surf Rock'}, {'S':'Rock and Roll'}, {'S':'California Sound'}]},
         'name': {'S':'Good Vibrations'},
         'year': {'S':'1966'}
     },
     {
         'corleone': {'S': 'corleone-17'},
         'artist': {'S': 'Nach'},
         'duration': {'S':'260'},
         'genre': {'L': [{'S':'Rap'}, {'S':'Hip Hop'}, {'S':'Spanish Rap'}]},
         'name': {'S':'Los Zurdos Mueren Antes'},
         'year': {'S':'2019'}
     },
     {
         'corleone': {'S': 'corleone-18'},
         'artist': {'S': 'System of a Down'},
         'duration': {'S':'600'},
         'genre': {'L': [{'S':'Progressive Metal'}, {'S':'Nu Metal'}, {'S':'Alternative Metal'}]},
         'name': {'S':'Chop Suey'},
         'year': {'S':'2001'}
     },
     {
         'corleone': {'S': 'corleone-19'},
         'artist': {'S': 'Wu Tang Clan'},
         'duration': {'S':'200'},
         'genre': {'L': [{'S':'Rap'}, {'S':'Hip Hop'}, {'S':'East Coast Rap'}]},
         'name': {'S':'C.R.E.A.M'}, 
         'year': {'S':'1993'}
     }
]

#Solicitudes de escritura
solicitudes_de_escritura = []
for item in items:
    solicitud_de_escritura = {
        'PutRequest': {
            'Item': item
        }
    }
    solicitudes_de_escritura.append(solicitud_de_escritura)

#Divide las solicitudes en grupos de 25 (límite de escritura de DynamoDB)
for i in range(0, len(solicitudes_de_escritura), 25):
    songs = solicitudes_de_escritura[i:i+25]
    dynamodb.batch_write_item(
        RequestItems={
            tabla_nombre: songs
        }
    )

print("Datos insertados exitosamente.")