from transformers import GPTNeoForCausalLM, GPT2Tokenizer

model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")

prompt = (
    "I am angry. Recomend an album of the follwing:, The King of Limbs de Radiohead, OK Computer de Radiohead, Dummy de Portishead, Third de Portishead, Herzeleid de Rammstein, Mutter de Rammstein, Fearless de Taylor Swift, 1989 de Taylor Swift"
)

input_ids = tokenizer(prompt, return_tensors="pt").input_ids

gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.9,
    max_length=100,
)
gen_text = tokenizer.batch_decode(gen_tokens)[0]
print(gen_text)