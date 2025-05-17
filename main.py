import streamlit as st
from openai import OpenAI

st.title("Simple Website to use API KEY")
Input_text=st.text_input("Give me a Prompt to search")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="meta-llama/llama-3.3-8b-instruct:free",
  messages=[
    {
      "role": "user",
      "content": Input_text
    }
  ]
)
if Input_text:
  st.write(completion.choices[0].message.content)