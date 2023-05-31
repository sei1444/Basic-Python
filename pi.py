text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

text_change = text.translate(str.maketrans({",":" ", ".":" "}))

word_list = text_change.split()

len_list = list(map(len, word_list))

ans = ''

for i in len_list:
    ans += str(i)

print(ans)
