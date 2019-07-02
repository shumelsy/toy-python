#!/usr/bin/env python3.6

import linecache

def hashtop10(textfile):
    fin = open(textfile, 'r', encoding='utf8')
    hashDict= {}
    wordDict = {}
    wordDictCount = {}
    wordDictTop = {}
    n = 1
    #Часть кода, определяющая top10 хэштегов:
    for line in fin:
        #Перевод букв в нижний регистр для корректного подсчета и удаление знаков препинания
        line = line.lower()
        line = line.replace(',', '')
        line = line.replace('.', '')
        line = line.replace('!', '')
        line = line.replace('?', '')
        #Поиск хэштегов и номеров строк, в которых они содержатся, добавление их в словарь
        for h in line.split():
            if h.startswith('#'):
                if h in hashDict:
                    hashDict[h].append(n)
                else:
                    hashDict[h] = [n]
        n += 1
    #Сортировка словаря по количеству строк, содержащих хэштег. Остаются 10 первых, которые затем передаются в stdout
    hashDict = dict(sorted(hashDict.items(), key=lambda x: len(x[1]), reverse=True))
    hashTop = dict(list(hashDict.items())[:10])
    print(list(hashTop.keys()))

    #Часть кода, определяющая 5 топовых слов
    for ht in hashTop.keys():
        for ln in hashTop[ht]:
            #Для анализа берутся ранее запомненные строки
            lns = linecache.getline(textfile, ln)
            #Перевод букв в нижний регистр для корректного подсчета и удаление знаков препинания и служ.символов
            lns = lns.lower()
            lns = lns.replace('\n', '')
            lns = lns.replace('.', '')
            lns = lns.replace(',', '')
            lns = lns.replace('!', '')
            lns = lns.replace(':', '')
            lns = lns.replace(';', '')
            lns = lns.replace('?', '')
            lns = lns.replace('"', '')
            #Формирование словаря из значимых слов
            for s in lns.split():
                if s.isalpha():
                    if ht in wordDict:
                        wordDict[ht].append(s)
                    else:
                        wordDict[ht] = [s]
            #Подсчет количества повторяющихся слов, сортировка и вывод списка top-5
            wordDictCount[ht] = {i: wordDict[ht].count(i) for i in wordDict[ht]}
            wordDictCount[ht] = dict(sorted(wordDictCount[ht].items(), key=lambda x: x[1], reverse=True))
            wordDictTop[ht] = list(wordDictCount[ht].keys())[:5]
    print(wordDictTop)
    fin.close()

hashtop10('in.txt')
