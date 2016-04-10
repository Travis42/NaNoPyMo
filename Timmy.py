#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This is an attempt to write novel for NanoWriMo programmatically,
using Python:  NaNoPyMo

Novels must be 50k words.  NaNoWriMo is typically November, but hey.
---------------

I present, for your reading pleasure:  Timmy.

'''

import datetime, random

title = 'Timmy'
author = 'Timmy'
year = datetime.date.today().year
punctuation = [
                '.','?',';',',','!',':'
                ]

def TitlePage (title, author, year):
    print (title)
    print ('by ', author)
    print ('Published ', str(year))
    print (' ')


def intro ():
    print ('Ahem. ')


def ending():
    print('Timmy.')


def main():
    TitlePage(title, author, year)
    intro()
    word = 'Timmy'
    counter = 1
    for i in range(50001):
        counter += 1
        if counter < 11 and (random.randint(counter, 10) > 8):
            print (word + punctuation[random.randint(0, 5)], end = ' ')
        else:
            counter = 1
        print (word, end=' ')
    ending()


if __name__ == '__main__':
    main()