class ChatManager:
    def __init__(self):
        # This list will store each message as a dictionary with 'sender' and 'message' keys.
        self.history = []

    def broadcast_message(self, sender, message):
        """
        Broadcasts a message from the sender to all participants.
        Stores the message in the conversation history.

        :param sender: The name of the sender (e.g., 'Player 1', 'Player 2', or 'SYSTEM').
        :param message: The content of the message.
        """
        entry = {"sender": sender, "message": message}
        self.history.append(entry)

    def get_history(self):
        """
        Returns the complete conversation history as a list of dictionaries.
        Each dictionary contains 'sender' and 'message' keys.

        :return: List of all broadcasted messages.
        """

        return self.history
