from datetime import datetime
import random

from game.llm_player import LLMPlayer
from game.llm_client import MODELS
from game.chat_manager import ChatManager
from game.logger import Logger

MAX_ROUNDS = 100


def choose_random_model():
    flattened = [i for s in list(MODELS.values()) for i in s]
    return random.choice(flattened)


class GameEngine:
    def __init__(self):
        # Initialize LLM players.
        self.player1, self.player2 = self.get_player_names()
        self.players = [self.player1, self.player2]

        # Initialize chat manager and logger.
        self.chat_manager = ChatManager()

        self.logger = Logger(datetime.now().strftime("%Y%m%d_%H%M%S"))

        # To store final votes.
        self.votes = {}

    def get_player_names(self):
        player1 = choose_random_model()
        player2 = choose_random_model()

        if player1 == player2:
            # If the model is playing itself, call the second instance `-2`
            return LLMPlayer(player1[1], player1[0]), LLMPlayer(player2[1] + "-2", player2[0])

        return LLMPlayer(player1[1], player1[0]), LLMPlayer(player2[1], player2[0])

    def start_game(self):
        for player in self.players:
            player.initialize_game()

        self.logger.log_event("Game started")
        self.run_chat_phase()
        self.collect_votes()
        self.reveal_votes()

    def run_chat_phase(self):
        """
        Runs the chat phase. In each round, players send messages. When a player's
        message equals "AGREE_TO_VOTE" (case-insensitive), they're marked as ready.
        The phase ends once all players are ready.
        """
        ready_players = set()
        round_counter = 0

        while len(ready_players) < 1:
            round_counter += 1
            for player in self.players:

                # Retrieve the player's message, providing the full chat history.
                message = player.get_chat_message(self.chat_manager.get_history())

                # Broadcast the message and log it.
                self.chat_manager.broadcast_message(player.name, message)
                self.logger.log_chat(player.name, message)

                # Check if the player signals readiness.
                if self.is_ready_message(message) or round_counter >= MAX_ROUNDS:
                    ready_players.add(player.name)

    def is_ready_message(self, message):
        return "AGREE_TO_VOTE" in message.strip().upper()

    def collect_votes(self):
        """
        Collects the final vote (e.g., 'split' or 'steal') from each player privately.
        The votes are logged but kept hidden until both are submitted.
        """
        for player in self.players:
            vote = player.get_final_vote()
            self.votes[f"{player.name} - {player.model}"] = vote
            self.logger.log_vote(player.name, vote)

    def reveal_votes(self):
        """
        Reveals the final votes publicly to all players by broadcasting a message.
        """
        reveal_message = f"Final Votes: {self.votes}"
        self.chat_manager.broadcast_message("SYSTEM", reveal_message)
        self.logger.log_event("Votes revealed", extra_data=self.votes)
