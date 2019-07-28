# -*- coding:utf-8 -*-


import sys
from probs import *

class losHelper:
    
    cookie = ""

    def prob_choose(self):
        try:
            print("문제의 이름을 입력하세요. : ")
            prob = sys.stdin.readline().split()
            prob = ''.join(prob)
            
            globals()[prob](self.cookie)
        except KeyError as e:
            print("없는 문제를 입력하셨습니다.")
            sys.exit()


        
    
    def __init__(self):
        print("현재 세션 쿠기 값을 입력하세요. : ")
        cookie_data = sys.stdin.readline().split()
        cookie_data = ''.join(cookie_data)
        
        # self.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        self.cookie = cookie_data   
        
if __name__ == "__main__":

    helper = losHelper()
    prob = helper.prob_choose()
        
