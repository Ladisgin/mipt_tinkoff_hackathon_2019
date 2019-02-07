from fuzzywuzzy import fuzz
import json
import os
import xlrd
import gensim
# import difflib
import textdistance
import nltk
import numpy
import sklearn
import gensim.models.keyedvectors as word2vec
# from weighted_levenshtein import lev, osa, dam_lev

rqs_path = "/Users/kalugin/git_proj/mipt_tinkoff_hackathon_2019/data/asks.json"

name_w = 1
atr_w = 1
price_w = 0.00001
path_w = 1
discount_w = 10

categories = [f.path for f in os.scandir(".") if f.is_dir()]
offers = []
for i in categories:
    offers += [f.path for f in os.scandir(i) if f.is_dir()]
print(offers)


# path = './GoogleNews-vectors-negative300.bin'
# path = './180/model.bin'
# model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
# model.save("word2vec.model")
# model = word2vec.KeyedVectors.load_word2vec_format(path, binary=True)

with open(rqs_path) as f:
    rqs = json.load(f)
    ans = []
    for rq in rqs:
        deals = []
        print(rq)
        print(rq["name"], float(rq["price_to"]), float(rq["price_from"]))
        for p in rq["customers"]:
            pt = "./" + rq["category"] + "/" + p +  "/v_data.xls"
            try:
                rb = xlrd.open_workbook(pt, formatting_info=True)
            except FileNotFoundError:
                print("not open: " + pt)
                continue
            sheet_r = rb.sheet_by_index(0)
            for rownum in range(1, sheet_r.nrows):
                row = sheet_r.row_values(rownum)
                name = row[0]
                discr = row[1]
                price = row[2]
                price_float = float(price)
                # discount =  price_float/float(row[3])
                path = row[4]
                # print(discr)
                if(float(rq["price_to"]) > price_float and float(rq["price_from"]) < price_float):
                    cur_w = 0
                    k = 0
                    # cur_w = name_w * (fuzz.ratio(name, rq["name"]) + 1) #atr_w * fuzz.token_set_ratio(discr, rq["attributes"])
                    # cur_w *= 1 / (1 + abs(textdistance.levenshtein(name.lower(), rq["name"].lower())))
                    # cur_w += nltk.edit_distance(name, rq["name"])
                    t = path.lower().split("~")
                    for i in rq["name"].split():
                        o = str(i).lower().strip()
                        if str(name).lower()[:max(int(len(str(name)) * 0.8), 4)].count(o) or str(path).lower().count(o):
                            cur_w += 1

                        cur_w += str(name).lower().split(" ")[:2].count(o)

                    if (cur_w/len(rq["name"].split())) > 0.5:
                        deals.append([cur_w, p, {"Item": name, "Attributes": path  + "\n" + discr, "price": price}])
        deals = sorted(deals, key=lambda x : (-x[0], len(x[2]['Item'])))
        deals = deals[:5]
        for i in deals:
            print("\t" + str(i[0]), str(i[1]), str(i[2]))
        ans_p = {}
        for i in deals:
            if i[0] > 0:
                if(ans_p.keys().__contains__(i[1])):
                    ans_p[i[1]].append(i[2])
                else:
                    ans_p[i[1]] = [i[2]]
        for i in ans_p:
            pt = "./" + rq["category"] + "/" + i + "/meta.xls"
            try:
                rb = xlrd.open_workbook(pt, formatting_info=True)
            except FileNotFoundError:
                print("not open: " + pt)
                continue
            sheet_r = rb.sheet_by_index(0)
            t = sheet_r.row_values(1)
            offe = {"offer": t[0], "web": t[1], "cashback": t[2], "period": t[3], "offer_type": t[4], "advert_text":t[5]}
            ans_p_tr = {"offer":offe, "products":ans_p[i]}
            ans.append(ans_p_tr)
        for p in rq["customers"][0:2]:
            pt = "./" + rq["category"] + "/" + i + "/meta.xls"
            try:
                rb = xlrd.open_workbook(pt, formatting_info=True)
            except FileNotFoundError:
                print("not open: " + pt)
                continue
            sheet_r = rb.sheet_by_index(0)
            t = sheet_r.row_values(1)

            offe = {"offer": t[0], "web": t[1], "cashback": t[2], "period": t[3], "offer_type": t[4],
                    "advert_text": t[5]}

            ans_p_tr = {"offer": offe, "products": ans_p[i]}
            ans.append(ans_p_tr)
    print(ans)
    t = rqs_path.split('.')
    pp = "".join(t[0:-1] + ["_ans."] + [t[-1]])
    with open(pp, 'w', encoding='utf8') as outfile:
        json.dump(ans, outfile, ensure_ascii=False, indent=2)