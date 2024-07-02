import json
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Cargar el modelo y el tokenizador de GPT-2
model_name = "EleutherAI/gpt-neo-1.3B"  # Puedes usar "EleutherAI/gpt-neo-2.7B" para un modelo más grande
model = GPTNeoForCausalLM.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Crear un prompt específico y detallado
prompt = (
    "I am angry. Recomend an album of the follwing:, The King of Limbs de Radiohead, OK Computer de Radiohead, Dummy de Portishead, Third de Portishead, Herzeleid de Rammstein, Mutter de Rammstein, Fearless de Taylor Swift, 1989 de Taylor Swift"
)

# Tokenizar y generar la respuesta
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(
    inputs.input_ids, 
    max_length=150, 
    num_return_sequences=1, 
    temperature=0.7, 
    repetition_penalty=2.0,  # Añadir penalización de repetición
)
respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Imprimir la respuesta, eliminando cualquier repetición del prompt
respuesta = respuesta.replace(prompt, "").strip()
print(respuesta)