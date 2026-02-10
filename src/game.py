class Game:
    def __init__(self):
        self.score = 0

    def start(self):
        # FIXME: MethodCallError: self argument is not needed here
        self.play_round(self)

    def play_round(self):
        print("Playing...")


def check_score(score):
    if score > 100:
        print(f"점수({score})가 100점을 초과했습니다.")
        return True
    else:
        print(f"점수({score})가 100점 이하입니다.")
        return False


def set_level(level):
    if level > 5:
        difficulty = "Hard"
    # FIXME: UnboundLocalError: difficulty referenced before assignment if level <= 5
    print(f"Level set to {difficulty}")
