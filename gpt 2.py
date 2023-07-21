import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2', padding_side='left')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_response(user_input):
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=model.device)
    bot_output = model.generate(input_ids, attention_mask=attention_mask, pad_token_id=tokenizer.eos_token_id, max_new_tokens=100)
    bot_response = tokenizer.decode(bot_output[0], skip_special_tokens=True)
    return bot_response

# пример использования
user_input = "Привет, как дела?"
bot_response = generate_response(user_input)
print(bot_response)