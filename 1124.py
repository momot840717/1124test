class Duck:
    def __init__(self, action) -> None:
        self.action = 'swim'

    @property
    def action_mode(self):
        return self.action

class SuperMan:
    def __init__(self, show_up) -> None:
        self.show_up = 'I\'m Superman.'

    @property
    def fly(self):
        return "I can fly."
    

class SuperManDuck(Duck, SuperMan):
    def __init__(self, action, show_up) -> None:
        Duck.__init__(self, action)
        SuperMan.__init__(self, show_up)
    
    def say_sentence(self):
        print(f"{self.fly} {self.show_up} I can {self.action_mode}.")

SuperManDuck('Run', "I'm super duck").say_sentence()