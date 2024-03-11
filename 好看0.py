import os
import openai

# Load your API key from an environment variable or secret management service
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "sk-f2MibVXglvOvKnp5Pp76ZNKsrIGsXtYCjBQPRqyzlseu8y51"

# 修改接口地址
openai.api_base = "https://api.f2gpt.com/v1"

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])


def chat_gpt(prompt):
    # 你的问题
    prompt = prompt

    # 调用 ChatGPT 接口
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print(response)

chat_gpt('hi')