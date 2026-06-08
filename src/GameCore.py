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
            
            
            
            # CliView を使って判定結果（ヒット数・ブロー数）を表示
            self._view.showGuessResult(result)
            
            # もし4ヒットならループを抜けてクリア処理へ
            if result.getHits() == 4:
                self._view.showSuccess()
                break

            