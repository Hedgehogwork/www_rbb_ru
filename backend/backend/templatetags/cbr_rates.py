# -*- coding: utf-8 -*-
from xmltodict import parse
import requests
import pyfscache
from django import template

register = template.Library()
cache_it = pyfscache.FSCache('/tmp/rates.cache', minutes=60)


@register.assignment_tag
def get_cbr_rates():
    try:
        return cache_it['rates']
    except KeyError:
        pass
    try:
        result = get_cbr_rates_cached()
        cache_it['rates'] = result
        return result
    except:
        return None


def get_cbr_rates_cached():
    rates = dict()

    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    response.encoding = 'cp1251'
    text = response.text.encode('utf-8').replace('windows-1251', 'utf-8')

    cbr = parse(text)

    rates['Date'] = cbr['ValCurs']['@Date']

    for valute in cbr['ValCurs']['Valute']:
        valute['Value'] = float(valute['Value'].replace(',', '.'))
        rates[valute['CharCode']] = valute

    return rates
