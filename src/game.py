class Game:
    def __init__(self):
        self.score = 0
    
    def start(self):
        # FIXME: MethodCallError: self argument is not needed here
        self.play_round(self)

    def play_round(self):
        print("Playing...")

def check_score(score):
    # FIXME: AssertError: 10 is not greater than 100
    assert score > 100

def set_level(level):
    if level > 5:
        difficulty = "Hard"
    # FIXME: UnboundLocalError: difficulty referenced before assignment if level <= 5
    print(f"Level set to {difficulty}")
