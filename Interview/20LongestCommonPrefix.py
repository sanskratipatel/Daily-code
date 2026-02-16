str1 = ["FLOWER", "FLOW", "FLOWS"]

ans = ""

if len(str1) == 0:
    ans = ""
else:
    base = str1[0]

    for i in range(len(base)):
        for word in str1[1:]:
            if i == len(word) or word[i] != base[i]:
                print(ans)
                break
        else:
            ans += base[i]
            continue
        break

print(ans)