
 ░▒▓███████▓▒░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓████████▓▒░            ░▒▓███████▓▒░▒▓████████▓▒░▒▓████████▓▒░░▒▓██████▓▒░░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░               ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░               ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░                ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░                      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░                      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░  ░▒▓█▓▒░               ░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                                                                                                         
                                                                                                                                         
This is a game of Split or Steal, also known in the UK as Golden Balls, played by LLMs.

## Gameplay
This is a simple implementation of split/steal. Here's how the game works:
1. Two randomly chosen LLM instances are spun up and given a prompt explaining the game.
2. Immediately, the players start chatting with each other.
3. Once players agree to vote (by typing AGREE_TO_VOTE), shared conversation ends immediately.
4. Each player votes in private.

All game runs are recorded in `game_logs/` in dated `jsonl` files, for easy analysis across lots of runs.
See `example_game.jsonl` for an example of how this looks.

## LLM Providers
As-is, this game supports:
- all OpenAI models from OpenAI directly
- Sonnet through AWS Bedrock
- Deepseek R1 + Llama-405b via Fireworks

You may want to adjust or expand these. See config [here](./game/llm_client.py#L11-23).
To add a new LLM provider, make sure to add necessary credentials, then add the implementation
in `game/llms/new_provider.py`. The only required functions are `chat()` and `vote()`.

## How to run
This is quick to set up locally with [Poetry](https://python-poetry.org/docs/#installation):

```
poetry install
poetry shell
```

You can then run a game using `poetry run python main.py`.
