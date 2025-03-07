import os
from dotenv import load_dotenv
from game.llm_client import LLMClient
from game.prompts import SYSTEM_PROMPT, CLAUDE_SYSTEM_PROMPT, TIME_TO_VOTE

load_dotenv()

class LLMPlayer:
    def __init__(self, name, model):
        self.name = name
        self.conversation = []  # Internal conversation log for this player.
        self.model = model
        self.client = LLMClient(model)

    def initialize_game(self):
        # if self.model == 'eu.anthropic.claude-3-5-sonnet-20240620-v1:0':
        #     self.conversation.append({"role": "user", "content": CLAUDE_SYSTEM_PROMPT})
        # else:
        self.conversation.append({"role": "user", "content": SYSTEM_PROMPT})

    def get_chat_message(self, global_chat_history):
        # Build context messages from the global chat history.
        context_messages = []
        for entry in global_chat_history:
            context_messages.append({"role": "user", "content": f"{entry['message']}"})
        
        # Combine the player's conversation log with the context.
        messages = self.conversation + context_messages
        response = self.client.chat(messages)
        
        # Save the generated message to the player's conversation log.
        self.conversation.append({"role": "assistant", "content": response})
        return response

    def get_final_vote(self):
        """
        Generates the final vote (either 'split' or 'steal') using the conversation context.
        
        :return: The final vote as a string.
        """
        messages = self.conversation + [{"role": "user", "content": TIME_TO_VOTE}]
        vote = self.client.vote(messages).lower().strip().replace(".", "")
        
        # Validate the vote. Default to 'split' if the response is unexpected.
        if vote not in ['split', 'steal']:
            raise ValueError(f"Invalid vote: {vote}")
        
        self.conversation.append({"role": "assistant", "content": vote})
        return vote