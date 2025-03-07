from game.game_engine import GameEngine

def main():
    # Initialize the game engine.
    # The engine will handle player initialization, chat management,
    # and the "agree to vote" mechanism.
    game = GameEngine()
    game.start_game()

if __name__ == "__main__":
    main()