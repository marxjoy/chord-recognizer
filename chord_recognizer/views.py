from django.shortcuts import render
from django.http import HttpResponse
from . import notes



def index(request):
    message = ''
    if request.method == "POST": 
        score = request.POST['score']
        total = request.POST['total']
        root = request.POST['root']
        if notes.types[request.POST['choice']] == request.POST['guess']:
            message = "Good Job. Chord was: " + root + ' '+ request.POST['choice']
            score = int(score) + 1
        else:
            ans = ''
            for k, v in notes.types.items():
                if v == request.POST['guess']:
                    ans = k
            message = "Nope. Chord was: " + root + ' ' + ans
        total = int(total) + 1
    else:
        score = 0
        total = 0
        
    context = {
        'message': message, 
        'root': notes.random_root(),
        'type': notes.random_type(),
        'notes': notes.types,
        'score': score,
        'total': total

    }
    return render(request, "chord_recognizer/base.html", context)