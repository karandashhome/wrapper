#python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# загрузка модели и токенизатора
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# задание начального текста для генерации ответа
prompt_text = "Hello, how are you today?"

# токенизация начального текста
input_ids = tokenizer.encode(prompt_text, return_tensors="pt")

# генерация ответа
output = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

# декодирование ответа в текстовый формат
response_text = tokenizer.decode(output[0], skip_special_tokens=True)

# вывод ответа на экран
print(response_text)
