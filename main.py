import pandas as pd
import re
pattern = r"(?:https?:\/\/|ftps?:\/\/|www\.)(?:(?![.,?!;:()]*(?:\s|$))[^\s]){2,}"
df = pd.read_csv('./file.csv', delimiter=';')

# links = df[df['Текст'].str.contains(r'vk.com')]
links = df[df['Текст'].str.contains(f'https?://[^\"\s>]+')]
links = links['Текст']


def clear_and_write(list_strings):
    result = []
    for string in list_strings:
        result.append(re.search(pattern, string)[0])
    with open('links.txt', 'w') as file:
        file.write(pd.Series(result).to_string())

clear_and_write(links)
