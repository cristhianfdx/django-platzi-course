from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'image': 'https://picsum.photos/200/200/?image=1036'
    },
     {
        'name': 'Via lactea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'image': 'https://picsum.photos/200/200/?image=903'
    },
     {
        'name': 'Nuevo auditorio',
        'user': 'The Test',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'image': 'https://picsum.photos/200/200/?image=1076'
    }
]

# Create your views here.

def list_posts(request):
    content = []
    for post in posts:
        content.append('''
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure>
                <img src='{image}' />
            </figure>
        '''.format(**post))
    return HttpResponse('<br>'.join(content))

