def sum(t1, t2):
    result = {}
    result["h"] = t1["h"] + t2["h"]
    result["m"] = t1["m"] + t2["m"]
    result["s"] = t1["s"] + t2["s"]
    
    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] += 1

    if result["m"] >= 60:
        result["m"] -= 60 
        result["h"] += 1 
    return result

def subtract(t1, t2):
    result = {}
    if t2["h"] > t1["h"]:
        result["h"] = t2["h"] - t1["h"]
        result["m"] = t2["m"] - t1["m"]
        result["s"] = t2["s"] - t1["s"]
    else:
        result["h"] = t1["h"] - t2["h"]
        result["m"] = t1["m"] - t2["m"]
        result["s"] = t1["s"] - t2["s"]

    if result["s"] < 0:
        result["m"] -= 1
        result["s"] += 60
    
    if result["m"] < 0:
        result["h"] -= 1
        result["s"] += 60
    
    if result["h"] < 0:
        print("invalid!")
 
    return result

def show(result):
    print(f"{result['h']} : {result['m']} : {result['s']}")
    
time1 = {"h":8 , "m": 45 , "s": 35}
time2 = {"h":9 , "m": 35 , "s": 20}

result_s = sum(time1, time2)
show(result_s)

result_sub = subtract(time1, time2)