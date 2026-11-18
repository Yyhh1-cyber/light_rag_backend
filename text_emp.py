import dashscope
from dashscope import TextEmbedding
# 填你.env里面的sk
dashscope.api_key = "sk-ws-H.PERIYRH.Uc8u.MEQCIHyCr8a5hgSWu0lph7aELr0cxJa4ciS4p9dBsXiMYHPlAiAPFg6afG9oaQP40pnsYzU-fqAhR61Lj1cbfuVVS1tf1w"

resp = TextEmbedding.call(
    model="text-embedding-v2",
    input=["测试一下向量"]
)
print("resp:", resp)
print("code:", resp.code)
print("msg:", resp.message)
print("output:", resp.output)
