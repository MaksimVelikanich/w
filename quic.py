key = [
    {"key" :7, "info" : "info 7"},
    {"key" :3, "info" : "info 3"},
    {"key" :1, "info" : "info 1"},
    {"key" :2, "info" : "info 2"},
    {"key" :5, "info" : "info 5"},
    {"key" :4, "info" : "info 4"},
    {"key" :6, "info" : "info 6"},
    {"key" :8, "info" : "info 8"},
    {"key" :10, "info" : "info 10"},
    {"key" :9, "info" : "info 9"}
]

def quicSort(key):
    if len(key) <= 1:
        return key
    else:
        pivot = key[0]
        less = []
        great = []
        for i in key[1:]:
            if i["key"] < pivot["key"]:
                less.append(i)
            else:
                great.append(i)
        return quicSort(less) + [pivot] + quicSort(great)
print(quicSort(key))