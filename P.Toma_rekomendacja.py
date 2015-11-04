#  Wzorowane na przykladzie Rona Zacharskiego

from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0},
         "Krzysiu": {"Blues Traveler": 3.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5},
         "Zdzisiu": {"Norah Jones": 5.0, "The Strokes": 3.0}

        }


def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""
    d = 0
    for zespol in rating1:
        if zespol in rating2:
            d = +abs(rating1[zespol] - rating2[zespol])
    if d > 0:
        return d
    else:
        return -1
        
print manhattan(users[ 'Gosia' ], users[ 'Hela' ])


def computeNearestNeighbor(username, users):
    """dla danego użytkownika username, zwróć ze słownika users nazwę użytkownika o najbliższych preferencjach"""
    nameOfNearestNeighbor = ""
    distances = []
    for osoba in users:
        if username != osoba:
            d = manhattan(users[osoba], users[username])
        if d > 0: 
            distances.append((d, osoba))
    distances.sort()
    nameOfNearestNeighbor = distances[0]
    return nameOfNearestNeighbor

print computeNearestNeighbor('Hela' , users)

def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada
    nearest = computeNearestNeighbor(username, users)[1]
    recomendations = []
    # TODO: wpisz kod
    a = users[nearest]
    b = users[username]
    for zespol in a:
        if not zespol in b:
            recomendations.append((zespol,a[zespol]))

    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad

    return sorted(recomendations,
                 key=lambda artistTuple: artistTuple[1],
                 reverse = True)


print( recommend('Hela' , users))
