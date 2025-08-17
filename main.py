from game import guessingnumbergame

def main():
    mintanama = input("siapa namamu wahai player = ")
    gamestart = guessingnumbergame(mintanama)

    game = gamestart.game()

    if game == True:
        print("kamu menang")
    elif game == False:
        print("kamu kalah")


if __name__ == "__main__":
    main()