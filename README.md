### Program Overview

The `HelpBot` program is an intelligent assistant capable of handling a variety of tasks, including weather queries, webpage access, math calculations, stock and ETF information retrieval, text summarization, and translation. It leverages several advanced technologies and libraries to achieve this functionality.

### Limitations
When asking very complex questions the chatbot will face some issues with determining the user's intentions and outputting an appropriate result. Higher accuracy can be gained by further training the model on broader datasets but it will be hardware heavy to do so. If the chatbot can't understand the user's input, the chatbot will rely on Meta-Llama-3 for generative AI which may or may not generate an acceptable response to the input. 

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

### Requirements
- Python==3.8.19
- Chatterbot==1.0.4
- GPU - For MetaLlama
- ~20GB storage space (for MetaLlama or for model training)

### How to Use
- Run chainlit run program.py

### Some Examples
<img width="1511" alt="image" src="https://github.com/iratansh/HelpBot/assets/151393106/62b74853-0a81-4162-8a2c-4623e2d43455">
<img width="1511" alt="image" src="https://github.com/iratansh/HelpBot/assets/151393106/350f2cec-1dd8-4d00-af0f-d3094ca28e90">
<img width="1511" alt="image" src="https://github.com/iratansh/HelpBot/assets/151393106/e50b2d4a-1d15-4bff-baac-7a8c17a29668">
<img width="1511" alt="image" src="https://github.com/iratansh/HelpBot/assets/151393106/a4b892d9-c6f7-4809-aa0e-aab019571424">
<img width="1511" alt="image" src="https://github.com/iratansh/HelpBot/assets/151393106/6a9725b0-e407-4b1f-9495-2f2ef98a693e">
<img width="1511" alt="image" src="https://github.com/iratansh/HelpBot/assets/151393106/06927430-c7be-494b-9765-052bab207038">
<img width="1511" alt="image" src="https://github.com/iratansh/HelpBot/assets/151393106/0c01c28f-cbf4-4157-b50b-4f67c9de9edf">

References:
https://www.youtube.com/watch?v=J7afRW5XEb4&t=375s
