### Program Overview

The `HelpBot` program is an intelligent assistant capable of handling a variety of tasks, including weather queries, webpage access, math calculations, stock and ETF information retrieval, text summarization, and translation. It leverages several advanced technologies and libraries to achieve this functionality.

### Key Components and Technologies

1. **Libraries and Technologies:**
   - **Spacy**: Natural language processing for entity recognition and similarity matching.
   - **Requests**: Making HTTP requests for web content and APIs.
   - **Datetime**: Handling date and time operations.
   - **PyDictionary**: Fetching word definitions.
   - **ChatterBot**: Building and training a conversational bot.
   - **YFinance**: Fetching financial data for stocks and ETFs.
   - **Transformers**: Text summarization using models like GPT-2.
   - **MetaLlama**: Custom pipeline for generating responses, now including advanced configuration for loading a model with quantization.
   - **Re**: Regular expressions for detecting URLs and ticker symbols.
   - **Logging**: Logging errors and information.
   - **Deque**: Maintaining context in conversations.
   - **GoogleTransNew**: Translating text between languages.
   - **Torch**: Deep learning framework used with transformers.

2. **Additional Components:**
   - **JSON**: Handling configuration files for the `MetaLlama` class.
   - **AutoTokenizer** and **AutoModelForCausalLM** from **Transformers**: Tokenizing and loading models for natural language processing with quantization configuration.

### MetaLlama Class

The `MetaLlama` class is designed to generate responses using a model from the `transformers` library with specific configurations for quantization:

- **Initialization**: 
  - Loads configuration from a `config.json` file.
  - Sets up quantization configuration using `BitsAndBytesConfig`.
  - Loads the model (`Meta-Llama-3-8B`) with the specified configuration and HF_TOKEN.
  - Initializes the tokenizer and text generation pipeline.

- **Text Generation**:
  - The `get_response` method generates a response to a given prompt using the text generation pipeline.

### HelpBot Class

The `HelpBot` class integrates various functionalities:

- **Initialization**: Loads NLP model, initializes the chatbot, sets up logging, and maintains context.
- **Training**: Trains the bot using predefined conversations from a file.
- **Web Access**: Retrieves and returns webpage content.
- **Weather Information**: Fetches current weather using the Weatherbit API.
- **Response Generation**: Handles different types of queries, including weather, math, stock information, and text generation using `MetaLlama`.
- **Math Calculations**: Performs simple arithmetic operations.
- **Summarization and Translation**: Summarizes text and translates text between languages.
- **Ticker Symbol Handling**: Extracts and fetches information for stock and ETF ticker symbols.

<img width="1511" alt="image" src="https://github.com/iratansh/HelpBot/assets/151393106/62b74853-0a81-4162-8a2c-4623e2d43455">

