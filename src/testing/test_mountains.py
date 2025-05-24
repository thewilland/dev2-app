#import pytest 
from dev2il_devops_app.mountains import highestmountain

def test_highestmountain():
    mountains = [
        {'name': 'Spitzmauer', 'height': 2446}, 
        {'name': 'Gr. Priel', 'height': 2515},
        {'name': 'Schermberg', 'height': 2396}
    ]

    assert highestmountain(mountains) == {'name': 'Gr. Priel', 'height': 2515}

