import time
import json
import os
def create_or_login():
    def fc_createorlogin():
        a = input('"create" or "log in": ')
        while a not in ('create', 'log in'):
            a = input('"create" or "log in": ')
        if a == 'create':
            return 1
        elif a == 'log in':
            return 2
    def fc_create(content): # 創帳號
        ID = input('User ID: ')
        while ID in content.keys():
            print('ID is used.')
            ID = input('Please input another ID: ')
        print('Money you have: $0')
        content[ID] = 0
        with open('idnmoney.json','w') as file_object:# 存檔
                json.dump(content,file_object)
        return ID
    def fc_login(content): # 搜尋
        ID = input('User ID: ')
        if ID in content.keys(): # 若ID存在
            ps = content[ID]
            print('Money you have: $%s' % ps)# 印出錢
            return ID 
        else:
            print('Not found.')
            return False
    if os.path.isfile('idnmoney.json'):# 如果存在舊有檔案
        with open('idnmoney.json','r') as file_object:# 開啟舊檔案
            content = json.load(file_object)
        sig = fc_createorlogin()
        if sig == 1:# 輸入了create才會執行 
            return fc_create(content)
        elif sig == 2:# 輸入了 log in 才會執行
            return fc_login(content)
    else:    
        content = {}# 沒有舊檔的話就設一個空的dictionary
        sig = fc_createorlogin()
        if sig == 1:
            return fc_create(content)
            
        elif sig == 2:
            return fc_login(content)
        
def skill():
    print("你想用賺來的錢投資重吉，讓他成為校園風雲人物嗎？ ")
    a=input('Enter Yes or No: ')
    while a not in ('Yes','No'):  #防止輸入錯誤
        print('(Please enter "Yes" or "No".)')
        a = input('Enter Yes or No: ')
        
    if a == 'Yes':
        print('請選擇才藝 ： 1吉他或樂器 2運動 3說話技巧 4跳舞 5美術 6棋藝 7插花')
        s = int(input("請輸入代碼："))
        while s not in (1,2,3,4,5,6,7):  #防止輸入錯誤
            print('(Please enter 編號1~7)')
            a = input('請輸入代碼：')
        print("夯~夯~夯~  夯番薯都沒你夯( ～'ω')～")
        time.sleep(2)
        print('重吉因為您的投資魅力又提升了') 
def cram_school():
    print("你想用賺來的錢投資重吉，花$1500讓他去補習嗎?..._〆(°▽°*) Enter Yes or No ")
    ans = input()
    while ans not in ('Yes','"Yes"','No','"No"'): #防止輸入錯誤
        print('(Please enter "Yes" or "No".)')
        ans = input()
    if ans in ('Yes','"Yes"'):
        print('請選擇課程 : Calculus or Accounting or Python or English')
        school = input()
        while school not in ('Calculus','Accounting','Python','English'): #防止輸入錯誤
            print('(Please enter Calculus or Accounting or Python or English.)')
            school = input()
        print("投資現在，就是掌握未來!!d(✪ω✪)b")
        time.sleep(2)
        print("感謝您投資重吉的未來，重吉在精通 %s 的路上又更棒棒了! (๑•̀ㅂ•́)و✧" %school)
        time.sleep(2)
        #print("您的錢尚有 $ %d" %)
    else:
        print("自己就是自己最好的老師! (°ω° ฅ)")
        time.sleep(2)
        print("重吉自立自強，自學靠自己，補習費就是給補教名師發大財R。嘖嘖(´- ω ก`)")
def deal_or_no_deal():
    import random
    def case(r): # r是回合數。此function回傳每回合場上遺留的箱子數，banker裡面會用到
        c = [6,5,4,3,2,2,1,1,1]
        t = 0
        for i in range(0,r):
            t += c[i]
        return 26 - t
    def banker(dt,r): # dt的型態為dictionary，其內容就是箱子和所對應金額的組合。 r是回合數
        print("It's the banker.")
        time.sleep(1)
        print("He's making you an offer of...")
        time.sleep(1)
        ttm = 0 # total money，由於要算平均數，所以先求總額
        for i in range(1,27):
            ix = 'box' + str(i)
            ttm += float(dt[ix][1:]) # [1:]是要忽略符號'$'
        average = int(ttm / case(r))
        print('$%d' % (average))
        time.sleep(1)
        print('Do you accept it?  (Yes / No)')
        ip = input()
        while ip not in ('Yes','"Yes"','No','"No"'): # 防止亂輸入
            print('(Please enter "Yes" or "No".)')
            ip = input()
        if ip in ('Yes','"Yes"'):
            print('Congratulations!\nYour deal: $%d' % average)
            return [average, 0] # 用於結束遊戲
        elif ip in ('No','"No"'):
            return [0,1] # 用於繼續遊戲 
    def prt_money(m): #　m是list，內容是已喪失金額。此functoin能印出一張關於剩餘金額的表，已喪失金額會變成紅色
        money = ["$0.01","$1","$5","$10","$25","$50","$75","$100","$200","$300","$400","$500","$750","$1000","$5000","$10000","$25000",'$50000',"$75000","$100000","$200000","$300000","$400000","$500000","$750000","$1000000"]
        print('')
        print("剩餘獎金:")
        for i in money:
            if i in m: # 如果該金額已被拋棄
                print("\033[1;31;40m %s \033[0m" %i,end = " | ") # 該金額會變成紅色
            else:
                print(i,end = " | ")
        print('')
    def new_box(remove_list): # remove_list 的型態是list，其內容為已拋棄箱子。此function用來印出剩餘箱子的表，已拋棄箱子會從表中消失
        box=[]
        for i in range(1,27):
            box.append(i)
        newbox = []
        for j in box :        
            if  ('box'+ str(j)) not in remove_list: # 若該箱子不在remove_list裡面
                newbox.append(j)
        for k in newbox:
            print(k,end='|') # 產生剩餘箱子的表。顯然，已拋棄箱子不會出現在表中
        return newbox
    def examine_key_available(ip,dt): # ip是string，dt是dictionary。原則上，ip是dt的key，而此function用來測驗ip是否已被選過
        while True:
            if ip not in dt.keys(): # 若ip非dt的key，要求重新輸入
                ip = input('不要鬧，請重新輸入(例如: box1): \n')
            elif dt[ip] == '$0': # 若該箱子已被拋棄，其中的金額被設為$0
                ip = input('\n這個箱子你選過了，請輸入別的箱子: \n')
            else:
                break
        return ip
    rule = "挑一個箱子後，選擇25個箱子中的6個捨棄，接著銀行就會給你一個金額，看要不要接受，接受則遊戲結束，不接受則繼續選擇，每一階段丟棄的箱子數將減少，最後箱子的金額就是你拿到的錢。Good luck!"


    play=input("Deal or Rules: ")
    while play not in ('Deal', 'Rules'):
        play = input('請輸入"Deal"或"Rules"\n')
    if play=="Rules":
        print(rule)

    box = ["box1","box2","box3","box4","box5","box6","box7","box8","box9","box10","box11","box12","box13","box14","box15","box16","box17","box18","box19","box20","box21","box22","box23","box24","box25","box26"]
    money = ["$0.01","$1","$5","$10","$25","$50","$75","$100","$200","$300","$400","$500","$750","$1000","$5000","$10000","$25000","$50000","$75000","$100000","$200000","$300000","$400000","$500000","$750000","$1000000"]
    random.shuffle(money)
    combine = dict(zip(box,money))
    remove_money = [] 
    remove_box = []
    r = 1 # 回合數
    for j in [6,5,4,3,2,2,1,1,'final']:
        if j == 'final':
            print('\n請丟1個箱子')
            print('請選擇第1個箱子(例如: box1): ')
            box_to_be_removed = input()
            op = examine_key_available(box_to_be_removed, combine) # 測試 box_to_be_removed 是否為combine的key，以及是否重複輸入
            remove_money.append(combine[op]) # 將所拋棄的箱子所對應的金額包含進 remove_money這個list裡面
            remove_box.append(op) # 將所拋棄的箱子包含進 remove_box 這個list裡面
            new_box(remove_box) # 印出剩餘箱子表
            prt_money(remove_money) # 印出剩餘金額表
            combine[op] = '$0' # 將所拋棄的箱子裡的金額設為$0
            for k in range(1,27):
                if combine['box' + str(k)] != '$0':
                    print('你得到了最後一個箱子的錢: ')
                    print(combine['box' + str(k)])
                    return int(combine['box' + str(k)][1:]) # string轉int，且省略'$'
        else:
            print('\n請丟%d個箱子' % j)
            for i1 in range(0,j):
                print('請選擇第%d個箱子(例如: box1): ' % (i1 + 1))
                box_to_be_removed = input()
                op = examine_key_available(box_to_be_removed, combine) # 測試 box_to_be_removed 是否為combine的key
                remove_money.append(combine[op]) # 將所拋棄的箱子所對應的金額包含進 remove_money這個list裡面
                remove_box.append(op) # 將所拋棄的箱子包含進 remove_box 這個list裡面
                new_box(remove_box) # 印出剩餘箱子表
                prt_money(remove_money) # 印出剩餘金額表
                combine[op] = '$0' # 將所拋棄的箱子裡的金額設為$0
            game_terminater = banker(combine,r)
            if game_terminater[1] == 0: # 結束遊戲
                return game_terminater[0]
            else:
                r += 1 # 回合數加一
def skill_cram_game(ID):
    def exa_money(ID, fee):
        with open('idnmoney.json','r') as file_object:# 開啟舊檔案
            content = json.load(file_object)
        if content[ID] >= fee:
            return True
        else:
            return False
        
    print('學才藝?補習?賺錢?')
    ip = input('請擇一輸入(例: 補習): ')
    while ip not in ('學才藝', '補習', '賺錢'):
        ip = input('不要鬧，請重新輸入(例: 賺錢): ')
    if ip == '學才藝':
        if exa_money(ID, 2000):
            with open('idnmoney.json','r') as file_object:# 開啟舊檔案
                content = json.load(file_object)
            content[ID] -= 2000
            with open('idnmoney.json','w') as file_object:# 存檔
                json.dump(content,file_object)
            skill()
        else:
            print('錢不夠，請去賺錢')
    elif ip == '補習':
        if exa_money(ID, 1500):
            with open('idnmoney.json','r') as file_object:# 開啟舊檔案
                content = json.load(file_object)
            content[ID] -= 1500
            with open('idnmoney.json','w') as file_object:# 存檔
                json.dump(content,file_object)
            cram_school()
        else:
            print('錢不夠，請去賺錢')
    else:
        print('賺錢囉')
        with open('idnmoney.json','r') as file_object:# 開啟舊檔案
            content = json.load(file_object)
        content[ID] += deal_or_no_deal()
        with open('idnmoney.json','w') as file_object:# 存檔
            json.dump(content,file_object)
order = create_or_login()
if order:
    skill_cram_game(order)
    print('\n離開?繼續?')
    ip = input('請輸入(例: 離開): ')
    while ip not in ('繼續', '離開'): # 亂輸入，就重新輸入
        ip = input('不要鬧，請輸入(例: 離開): ')
    while ip != '離開':
        skill_cram_game(order)
        print('離開?繼續?')
        ip = input('請輸入(例: 離開): ')
        while ip not in ('繼續', '離開'): # 亂輸入，就重新輸入
            ip = input('不要鬧，請輸入(例: 離開): ')


