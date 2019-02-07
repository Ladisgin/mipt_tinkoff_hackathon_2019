from fuzzywuzzy import fuzz
import json
import os
import xlrd
import textdistance

rqs_path = "/Users/kalugin/git_proj/mipt_tinkoff_hackathon_2019/data/result.json"

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

costil = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 136, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 298, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 314, 315, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 364, 365, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 481, 482, 485, 486, 487, 488, 489, 490, 491, 492, 493, 495, 496, 498, 499]

with open(rqs_path) as f:
    rqs = json.load(f)
    q = 0
    for rq in rqs[:100]:
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
                # if(float(rq["price_to"]) > price_float and float(rq["price_from"]) < price_float):
                if(True):
                    cur_w = 0
                    k = 0
                    t = path.lower().split("~")
                    for i in rq["name"]:
                        o = str(i).lower().strip()
                        if str(name).lower()[:max(int(len(str(name)) * 0.8), 4)].count(o) or str(path).lower().count(o):
                            cur_w += 0.9

                        l = name.split()
                        for j in range(len(l)):
                            m = str(l[j]).lower().strip()
                            d = textdistance.levenshtein(o, m)
                            if(d < 3):
                                cur_w += 0.3 / (j/2 + d + 1)

                        l = path.split("~")
                        for j in range(len(l)):
                            m = str(l[j]).lower().strip()
                            d = textdistance.levenshtein(o, m)
                            if (d < 3):
                                cur_w += 0.3 / (len(l) - j + d/2 + 1)


                    if (cur_w/len(rq["name"])) > 0.1:
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

        ans = []
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
        if(len(ans_p) == 0):
            for p in rq["customers"][0:2]:
                pt = "./" + rq["category"] + "/" + p + "/meta.xls"
                try:
                    rb = xlrd.open_workbook(pt, formatting_info=True)
                except FileNotFoundError:
                    print("not open: " + pt)
                    continue
                sheet_r = rb.sheet_by_index(0)
                t = sheet_r.row_values(1)

                offe = {"offer": t[0], "web": t[1], "cashback": t[2], "period": t[3], "offer_type": t[4],
                        "advert_text": t[5]}
                ans_t = [{"Item": "К сожалению, в нашей базе пока нет этого товара. Но у вас возможно получится найти его на этом сайте. С любовью, Tinkoff", "Attributes": "", "price": 0}]
                ans_p_tr = {"offer": offe, "products": ans_t}
                ans.append(ans_p_tr)
        print(ans)
        t = rqs_path.split('/')
        pp = "/".join(t[0:-1] + ["answers/ans_" + str(costil[q]) + "." + t[-1]])
        with open(pp, 'w', encoding='utf8') as outfile:
            json.dump(ans, outfile, ensure_ascii=False, indent=2)
        q += 1