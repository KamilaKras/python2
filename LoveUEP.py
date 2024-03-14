moje_niu = "82535"
# pętla od 1 do 100
for i in range(1, 101):
    # warunek dla liczby 50
    if i == 50:
        print(moje_niu)
    # podzielne przez 3 i 5
    elif i % 3 == 0 and i % 5 == 0:
        print("LoveUEP")
    # podzielne przez 3
    elif i % 3 == 0:
        print("Love")
    # podzielne przez 5
    elif i % 5 == 0:
        print("UEP")
    # pozostałe liczby
    else:
        print(i)
