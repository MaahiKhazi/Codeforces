from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = input()
    freq = Counter(s)
    most_freq_char = max(freq, key=freq.get)
    least_freq_char = min(freq, key=freq.get)
    s_list = list(s)
    if most_freq_char == least_freq_char:
        for i in range(len(s_list)):
            if s_list[i] != most_freq_char:
                s_list[i] = most_freq_char
                break
    else:
        for i in range(len(s_list)):
            if s_list[i] == least_freq_char:
                s_list[i] = most_freq_char
                break
    print(''.join(s_list))