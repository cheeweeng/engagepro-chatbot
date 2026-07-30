from llm.llm_factory import get_llm

llm = get_llm()

response = llm.invoke("Introduce yourself in one sentence.")

print(response.content)