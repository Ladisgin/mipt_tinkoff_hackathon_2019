import json

order = open("/Users/kalugin/git_proj/mipt_tinkoff_hackathon_2019/data/query_text_final.txt", "r")
answer_path = "result.json"

with open(answer_path) as f:
    rqs = json.load(f)
    for i in rqs:
