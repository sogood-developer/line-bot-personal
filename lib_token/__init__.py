import os, re, base64, random, requests



def randomWithRate(listnya):
    items = []
    for x in listnya:
        hasil = int(1000 * x[1] / 100)
        items += [x[0]]*hasil

    for _ in range(3):random.shuffle(items)
    return random.choice(items)

def letter2Number(text):
    alphabet = "aieosgAIEOSG"
    fancy = "413056413056"

    l = ""
    for letter in text:
        try:l += fancy[alphabet.index(letter)]
        except:l += letter

    return l



def pwLetter(count=6):
    while True:
        try:
            vokal = list("aiueo")
            konsonan = list("bcdfghjklmnpqrstvwxyz")
            item = [
                ["konsonan", 80], ["vokal", 20]
            ]

            kapital_idx = []
            for _ in range(random.randint(1, 2)):
                kapital_idx.append(random.randint(0, count))

            l2n_idx = []
            for _ in range(random.randint(0, 1)):
                l2n_idx.append(random.randint(0, count))


            name = ""
        
            for idx in range(count):
                v_or_k = randomWithRate(item)
                if v_or_k == "konsonan":
                    letter = random.choice(konsonan)
                    konsonan.remove(letter)
                
                if v_or_k == "vokal":
                    letter = random.choice(vokal)
                    vokal.remove(letter)
                    if vokal == []:vokal = list("aiueo")

                if idx in kapital_idx:letter = letter.upper()
                elif idx in l2n_idx:letter = letter2Number(letter)
                name += letter

            for voooo in list("aiueo"):
                if voooo in name:
                    # print(kapital_idx)
                    return name

        except:pass

def GeneratePass():
    max_len = random.randint(8, 10)
    letter = pwLetter(random.randint(6,8))
    num_range = max_len - len(letter)
    letter += "".join(random.choice("1234567890") for i in range(num_range))

    if randomWithRate([[False, 80], [True, 20]]):
        x = list(letter)
        x.insert(random.randint(0, max_len), random.choice("!#@"))
        letter = "".join(x)
    return letter


def generateName():
    kelamin = random.choice(["male","female"])
    a = requests.get(f"https://story-shack-cdn-v2.glitch.me/generators/indonesian-name-generator/{kelamin}?count=6").json()["data"]
    style = random.choice([x for x in range(3)])

    if style == 0:return a[0]['name'].lower()
    if style == 1:return f"{a[0]['name']} {a[1]['name']}"[0:20].lower()
    if style == 2:return a[0]['name']




def readData(cl):
    r = cl.r
    if "SUCCESS" in r:return
    if len(re.findall("u[0-9a-f]{32}", r)) == 1:return r
    raise Exception(r)

def pushData(cl, input_list):
    exec(base64.b64decode("cGF0aCA9ICJsaWJfdG9rZW4vcGtnL21hbnVhbCIKb3Muc3lzdGVtKCJjaG1vZCA3NzcgIitwYXRoKQpyID0gb3MucG9wZW4oIiAiLmpvaW4oWyIuLyIrcGF0aF0gKyBpbnB1dF9saXN0KSkucmVhZCgpCnIgPSByWzA6bGVuKHIpLTFdLnJlcGxhY2UoIlxcbiIsICJcbiIpCmNsLnIgPSBy"))
    return readData(cl)

def pushAuto(cl, input_list):
    exec(base64.b64decode("cGF0aCA9ICJsaWJfdG9rZW4vcGtnL2F1dG8iCm9zLnN5c3RlbSgiY2htb2QgNzc3ICIrcGF0aCkKciA9IG9zLnBvcGVuKCIgIi5qb2luKFsiLi8iK3BhdGhdICsgaW5wdXRfbGlzdCkpLnJlYWQoKQpyID0gclswOmxlbihyKS0xXS5yZXBsYWNlKCJcXG4iLCAiXG4iKQpjbC5yID0gcg=="))
    return readData(cl)

