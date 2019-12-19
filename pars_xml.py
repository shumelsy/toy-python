#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import urllib.request

def pars_xml(url='http://www.cbr.ru/scripts/XML_daily.asp', valute='HKD'):
    try:
        #try request url
        new_xml = urllib.request.urlopen(url)
        #parsing url
        tree = ET.parse(new_xml)
        root = tree.getroot()
        #looking for nessesary block and add items in dictionary
        for elem in root:
            for subelem in elem:
                if subelem.text == valute: result = elem
        new_dict = {}
        for children in result:
            new_dict[children.tag] = children.text
        #replace ',' with '.'
        new_dict['Value'] = float(new_dict['Value'].replace(',','.'))
        #get result
        ratio = float(new_dict['Value']) / float(new_dict['Nominal'])
        print(('По состоянию на {} курс {} по отношению к Российскому рублю составляет: {} руб. за 1 {}').format(root.attrib['Date'], new_dict['Name'], ratio, valute))
        return ratio
    #if url is not available
    except urllib.error.URLError:
        print(('Urlopen error: {} connection refused').format(url))
        return 0

if __name__ == "__main__":
    pars_xml()

