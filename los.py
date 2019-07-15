# -*- coding:utf-8 -*-


import sys
from probs import *

class losHelper:
    headers = {'User-Agent' : "" ,'cookie': ""}

    def prob_choose(self):
        print("문제의 이름을 입력하세요. : ")
        prob = sys.stdin.readline().split()
        prob = ''.join(prob)
        
        globals()[prob](self.headers)

        
    
    def __init__(self):
        print("현재 세션 쿠기 값을 입력하세요. : ")
        cookie_data = sys.stdin.readline().split()
        cookie_data = ''.join(cookie_data)
        
        self.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"
        self.headers['cookie'] = cookie_data
    
        
if __name__ == "__main__":

    helper = losHelper()
    prob = helper.prob_choose()
        
