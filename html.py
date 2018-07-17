lines = html.split("\n")
result = ""
for line in lines:
    words = line.split(" ")
    for word in words:
        if word == "":
            continue
        elif word == "<br>":
            print result
            result = ""
        elif word == "<hr>":
            if result != "":
                print result
                result = ""
            print "-"*80
        elif result == "":
                result = word
            elif len(result) + len(word) < 80:
                result += " " + word
            else:
                print result
                result = word
print result