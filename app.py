from llm import llm

response = llm.invoke(
    "Say hello from GrantGuard."
)

print(response.content)