import json, torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline

class MetaLlama:
  def __init__(self):
    config_data = json.load(open('config.json'))
    HF_TOKEN = config_data['HF_TOKEN']
    bng_config = BitsAndBytesConfig(
      load_in_4bit=True,
      bnb_4bit_use_double_quant=True,
      bnb_4bit_quant_type="nf4",
      bnb_4bit_compute_dtype=torch.bfloat16
    )
    self.model = AutoModelForCausalLM.from_pretrained('meta-llama/Meta-Llama-3-8B', quantization_config=bng_config, device_map="auto", token=HF_TOKEN)
    self.tokenizer = AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3-8B', use_fast=True, config=bng_config, token=HF_TOKEN)
    self.tokenizer.pad = self.tokenizer.eos_token
    self.text_generator = pipeline(
        "text-generation",
        model=self.model,
        tokenizer=self.tokenizer,
        max_new_tokens=128
    )

  def get_response(self, prompt):
    """
    Generate a response to the user's input using MetaLlama.
    Input: prompt (str)
    Output: response (str)
    """
    response = self.text_generator(prompt)
    return response[0]['generated_text']





