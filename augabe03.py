def teil_a():
    #Person A arbeitet hier
    return sum(
        zahl
        for zahl in range(1, 500_001)
        if zahl % 7 == 0 and zahl % 5 != 0
    )

def teil_b():
    #Person B arbeitet hier
    return 0

print(teil_a()+teil_b())
