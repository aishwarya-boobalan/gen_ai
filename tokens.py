#implementation of a tokenizer using tiktoken-
# text input, tokeniser, output of token ids, list of tokens, total number of tokens


import tiktoken
encoder = tiktoken.get_encoding("cl100k_base")

text="My first implementation of a tokenizer using tiktoken."
token_ids=encoder.encode(text)
print(f"Token ids are {token_ids}")
token=[]
for tok in token_ids:
    tokens =encoder.decode([tok])
    token.append(tokens)
print(f"List of tokens are {token}")
print("***********************************************************************")
for tok in token_ids:
    list_of_tokens =encoder.decode([tok]) 
    print(f"Token id {tok} corresponds to token '{list_of_tokens}'")
  
print("***********************************************************************")
print(f"Total number of tokens: {len(token_ids)}")
