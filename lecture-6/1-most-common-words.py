def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


a = {"Nika": 5, "Lizi": 5, "Nino": 4, "Gio": 4, "Saba": 3}
# print(most_common_words(a))
