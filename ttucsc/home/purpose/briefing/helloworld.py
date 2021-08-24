#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''Python 範例

這是一個 Python 範例，示範 Python 大部份語法的使用方式。'''

SUFFIXES = {1000: ['KB',  'MB',  'GB',  'TB',  'PB',  'EB',  'ZB',  'YB' ],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_killobyte_is_1024_bytes=True):
    '''將檔案大小轉換成人類易讀的格式。
    
    參數:
    size                      -- 以 byte 表示的檔案大小
    a_killobyte_is_1024_bytes -- 如為 True (預設), 使用 1024 為倍數
                                 如為 False, 使用 1000 為倍數
                                 
    回傳值: string
    
    這個 Hello World 程式來自於以 CC-BY-SA 授權的 Dive into Python 這本書。
    線上版本： diveintopython.org
    '''
    
    if size < 0:
        raise ValueError('數字必須是非負的數字')
        
    multiple = 1024 if a_killobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
            
    raise ValueError('數字過大')

def fib(n):
    '''傳回到 n 的費氏數列。
    
    本程式來自於 http://docs.python.org/tutorial/controlflow.html#defining-functions。'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def primes(m):
    '''傳回到 n 的質數串列。
    
    本程式來自於 http://docs.python.org/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops。'''
    result = []
    for n in range(2, m):
        for x in range(2, n):
            if n % x == 0:
                # print n, '等於', x, '*', n/x
                break
        else:
            # 當沒有找到任何因數 (迴圈完整執行) 時進入這邊
            # print n, '是一個質數'
            result.append(n)
    return result

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print '執行自我測試'
        print approximate_size(1000000000000, False)
        print approximate_size(1000000000000)
        print fib(10)
        print primes(100)
    else:
        print '以使用者要求的參數執行'
        print sys.argv
        print sys.argv[1:]
        print map(int, sys.argv[1:])
        print approximate_size(*map(int, sys.argv[1:]))
