import random

class enemy:
    def __init__(self):
        self.namamusuh = 'cemeng'
        self.nyawamusuh = 4
        

class guessingnumbergame:
    def __init__(self, player):
        self.player = player
        self.nyawa = 4
        self.skor = 0

    def game(self):
        bot = random.randint(1, 11)
        player = self.player
        hasil = None
        musuh = enemy()


        while self.nyawa > 0 and self.skor < 4:

            player = int(input("masukan tebakanmu = "))

            if player == bot:
                print('kamu menang')
                skor += 1
                musuh.nyawamusuh -= 1
                
            if player != bot:
                print("tebakan mu salah")
                self.nyawa -= 1
                print(f"sisa nyawa tinggal = {self.nyawa}, kamu kalah dari {musuh.namamusuh}")
        
        else:
            if self.nyawa < 0:
                hasil = False
                print("kamu kalah")
            elif self.skor > 4:
                hasil = True
                print("kamu menang")




        