from WordProvider import WordProvider
from GuessJudge import GuessJudge
from CliView import CliView

class GameCore:
    def __init__(self):
        self._wordProvider = WordProvider()
        self._judge = GuessJudge()
        self._view = CliView()
        
        self._answer = self._wordProvider.getAnswer()
        
    def play(self):
        while True:
            #プレーヤーの入力を受け取る
            guess = self._view.readGuess()
            
            result = self._judge(self._answer, guess)
            