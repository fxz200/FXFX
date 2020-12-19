# -*- coding: utf-8 -*-

#  進入迴圈，直到玩家正確設定難度
while(True):
    # 取得使用者輸入的難度
    levelset=(input('請輸入難度(1~5):'))
    #各難度對應的次數
    if levelset==('1'):
            time=25#次數
            print("難度已設定為1")#顯示遊戲難度
            print("-------------------------------------------------------")
            break#跳出迴圈
    if levelset==('2'):
            time=17
            print("難度已設定為2")
            print("-------------------------------------------------------")
            break
    elif levelset==('3'):
            time=13
            print("難度已設定為3")
            print("-------------------------------------------------------")
            break
    elif levelset==('4'):
            time=10
            print("難度已設定為4")
            print("-------------------------------------------------------")
            break
    elif levelset==('5'):
            time=7
            print("難度已設定為5")
            print("-------------------------------------------------------")
            break
    #檢測難度是否入正確
    if not levelset==("1") or levelset==("2") or levelset==("3") or levelset==("4") or levelset==("5") or levelset.isdigit() or levelset!=1:
         #提醒使用者輸入正確難度
         print('請輸入正確難度(1~5)')


# 導入 random 套件，用以產生隨機變數
import random

answer = '' # initial user answer (存放產生的 4 位數字) 
a_count=0 # initial A count (正確數字和正確位置計數)
b_count=0 # initial B count (正確數字不正確位置計數)


# 數字列表 (list)
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# 數字列表 (list)
items_1=[1,2,3,4,5,6,7,8,9]


x=''# 存放產生的1位數字
# shuffle() 方法將序列的所有元素隨機排序
random.shuffle(items_1)
# 從數字列表中挑選第1個數字
for z in range(1):
    # 產生隨機一個數字(x)
    x+=str(items_1[z]) # 將正確答案以字串格式處理



#進入迴圈直到爆炸數字為不重複的四位數字
while(True):
    
    
    boom=''# 存放產生的4位的爆炸數字
# shuffle() 方法將序列的所有元素隨機排序
    random.shuffle(items)
# 從數字列表中挑選前4個數字
    for i in range(4):        
    # 產生隨機四個數字(answer)
          answer+=str(items[i]) # 將正確答案以字串格式處理
    # 產生隨機四個數字=>boom(answer-x)
          boom=str(int(answer)-int(x))  # 將正確答案以字串格式處理
    #將爆炸數字變為串列
    boom_list=list(boom)
    #刪除串列裡的重複數字
    set_boom_list=set(boom_list)
    
    #判斷是否為四位數字
    if int(boom)>=1000:
        break
    if int(boom)<1000:
        #將正確答案和爆炸數字歸零
        answer=0
        boom=0
    #判斷是否有重複數字
    if len(set_boom_list)==len(boom_list):
        break
    if not len(set_boom_list)==len(boom_list):
        answer=0
        boom=0
    

#####################        

########################

print("!!請小心!!炸彈數字會導致爆炸\n且炸彈數字接近正確答案:)")
print("-------------------------------------------------------")
# start 進入迴圈，直到玩家正確猜出數字
while(True):  
    # 取得使用者輸入的數字，number 屬於 string type
    number=input('請輸入數字: ')
    #如果使用者輸入的數字等於爆炸值則結束遊戲
    if number==boom:
        #輸出{爆炸}圖示
        print("      .:sdNMMMMMMMMMMMMMh-                                                                    ")
        print("    -yNMMMMMdy+/:::/sdMMMN/                                  `...                          .NMMN. ")   
        print("  `sNMMMMMMM-        `hMMMh        `             .+ys:.`    `ymNmo                        `dMMM+     ")
        print("  yMMMd/yMMMo         hMMMm`    `+yhhhys/`      :mMMMMmdo`  -MMMMm`            `.`        +MMMd`     ")
        print(" `hMMh` :MMMm.       :NMMMs    `yMMMMMMMMm+    :NMMMMMMMMd- `NMMMN.           :hmmo`     .NMMN:      ")
        print("  `/+`  `mMMMo      :NMMMN-   `yMMMMmdmMMMM/  /NMMMNyoNMMMh .MMMMM/          +NMMMN.     yMMMh       ")
        print("         oMMMd`    /NMMMN+    :MMMMo` .mMMMd``dMMMyo  yMMMN`.MMMMMh`        oMMMMMh`    -NMMN-       ")
        print("         .NMMN-  -hMMMMN/     hMMMd-   oMMMM.:NMMN-/  oMMMM..MMMMMM-      .yMMMMMM:     sMMMy        ")
        print("         `dMMMy`+NMMMMh-     `mMMN+.   sMMMM:dMMMy /  yMMMm`:MMMMMM+     .hMMMMMMm`    :MMMM.        ")
        print("          /MMMNmMMMMN+`      /MMMh:.   sMMMM.mMMM/ : `mMMMh +MMMMMMM-   .dMMMMMMMo     yMMMh         ")
        print("          `dMMMMMMMd+:-`     yMMMo..  `mMMMh-MMMN. : :MMMM: yMMMMMMMd  .dMMMMMMMN.    .mMMM:         ")
        print("           sMMMMMMMMMMMMNho- yMMMo`-  /MMMM/-MMMN- -.mMMMd`.NMMMMMMMM:.mMMMMMMMMy     +MMMh          ")
        print("           +MMMMMmmdhmmMMMMMohMMM/   `dMMMm``NMMM: `hMMMN- +MMMMMMMMMdmMMMMNMMMM+    `dMMM/          ")
        print("            /MMMN.     -yMMMMMMMMo   hMMMM:  yMMMdomMMMN-  dMMMM-hMMMMMMMM+yMMMM:     yMNs`          ")
        print("            `dMMM+      :MMMMNMMMd.-hMMMM+   .dMMMMMMMh-  :MMMMd -NMMMMMMy`sMMMM.     `-`            ")
        print("             /MMMm.   `+NMMMd:dMMMNNMMMN+     .smMMmy:`   sMMMM/  yMMMMMm` hMMMM`   :dNm:            ")
        print("             `hMMMs .+mMMMMd. `sNMMMMNy.        `..`     `mMMMm`  .NMMMm-  dMMMN    hMMMo            ")
        print("              :MMMNyNMMMMdo`    ./++-`                   `mMMN:    .sy+`   hMMMh    /mmy.            ")
                                                             

        
        break#跳出迴圈
    # 判斷使用者是否輸入非數字或少於 4 個數字的內容
    # isdigit() 方法檢測字串是否只由數位組成
    # len() 方法用以取得變數的長度
    if not number.isdigit() or len(number) != 4:  #cheak all input is digit
        # 使用者輸入非數字的內容，提醒使用者輸入 4 個數字
        print('請輸入4個數字')
    # 使用者正確輸入數字
    else:
        # 使用者輸入正確 4 個數字
        if number==answer:
             #輸出{勝利}圖示
            print( "      ````                       ````          ```                               ``       ")         
            print( "    .//:://+++++/   `++++++oo` `-/::/++ooooo/`./:://++++++` :++++++++o+-      ``./://///////- ")     
            print( "   ``:+-``..---:yd.  +/.:::/sd/`./.`.-:++ooyds./..-::////sh..y.::::///+dh`    ``./--:+syhdddms  ")    
            print( "    `.//-````..:dds .y`o-.-.sdh`/:..`.----hmd./:`.```...hd/`y-+:------/dd+   ``.::`.``...-+Nd.    ")  
            print( "     `.soo``````smd-o/:/``..-md-y.+...---+Nm+`y./.`````smy /o-o........ydd.    .s.-:``````dm/       ")
            print( "       /hh+`````.mmyy.s......ymd//:....--mmy`s/-+````.:Nd-.y.o-........:dds    o:.o....``oNy`       ")
            print( "        yhh:..```+Nm:o-```.../mh-s......smd-:s.s.`````dm+ s:/+.....:....+md:  :s`o:.....:md-        ")
            print( "        .dhy--....hd:o``````..d/o:...../dd+`y.//`````oNh`:s-s.....-mo`...ydh``h./o----..hmo         ")
            print( "         +hho--.-./dy.````````+so....-.dmh`++.s-...`-mm:`y.o:.....hNd:...-dmyy/-y::::::+mh`         ")
            print( "         `hsy+/:-:-yo---....``-h-..-:-smd:-y`s/:----hms o/:o...-.+Nmhy:---+mmy.y+///+//dd:          ")
            print( "          -y/s++/:::--:--mo--...``..-:mms`y:/y:::::omd.-y.y.``..-mmohhs::-:sh/+o///++/yms     ")
            print( "           osoyo+/:::::-yNm/::-...```hNd./o.h+/::::mm/`y-o+-...`ymh`:hho:-::ohy-::://+md.       ")    
            print( "           `hoysso+///:/mmyy//:----.+Nm/.y.sso++/:ymy`++:y::---/mm-  oyy:::-:s:--::::mm/          ")  
            print( "            :y+hsys+++:hdmsoo//:-::-mNy s::hoooo++md-.y.y/:::::dm+   `h+s.-------::-yNy             ")
            print( "            sssyyyso+ommoh-o//::--yNd.:s.hsssso/dm+`s:+s/:-:-ymy`    :s:+`...---::/Nm.             ")
            print( "             .h+ysso+:mmh`oo/s//:-/mm+`h-+hsyso+ymh`:o-h++/:-+md-      s+o-```.....mm+              ")
            print( "              /yyhhhhhmm/ `hodhhyyddy`o++hsssooomd:`y:yysssoodm+       .hohoooooooymh`              ")
            print( "              `+ssssssoo`  :ooooooso. +yyyyyyyyyy+ .syyyyyyyyyo`        -oooooosssss-               ")
            break#跳出迴圈

            
        # 判斷使用者輸入的 4 個數字有幾個對
        # i 用以指向使用者輸入的第 i 個位置
        for i in range(4):
            # j 用以指向正確答案的第 j 個位置
            for j in range(4):
                
                # 計數位置對且數字對的個數
                if i==j and number[i]==answer[j]:
                    a_count+=1
                # 計數位置錯但數字對的個數
                elif number[i]==answer[j]:
                    b_count+=1

        # 告訴使用者輸入的數字 XAXB
        print('{0}A{1}B'.format(a_count,b_count))
        #每猜一次則次數-1 
        time-=1
        #若次數=0則遊戲結束
        if time==0 :
             #輸出{失敗}圖示
                    print( "                           .:-                                           ")
                    print( "                           dMN.                                          ")                  
                    print( "                           dMM.                          ``                 ")                
                    print( "                           dMM.         /hdyo+:        /hmmd:     :yyoo/:`   ")              
                    print( "                           yMM.        sMMdydNNh.     +MMyoo-     mMMmNMNs    ")            
                    print( "                           yMM.       -NMh` `:mMh`   `NMh`        mMM:.-:`    ")        
                    print( "                           yMM-       oMMo    oMM+   -MMo         hMM.       ")        
                    print( "                           oMM:       hMMo    :MMd   .NMy         hMN.       ")      
                    print( "                           +MM/       mMM/    -MMM`   yMN-        hMm`    ")    
                    print( "                           +MM+       mMM-    `MMM`   .dMm-       mMNoo+-  ")  
                    print( "                           +MMo       mMM`     NMM`    .dMN:      mMMNNMh    ")
                    print( "                           +MMo       mMM`     dMM.     .hMN/    `mMM:--`  ")
                    print( "                           /MMs       mMM.     dMM.      .dMN-   `NMM-   ")
                    print( "                           :MMy       dMM-     dMM.       -MMy   `NMM-   ")
                    print( "                           .NMh       sMM/     NMM`        dMm   `NMN.  ")
                    print( "                           .NMd       /MMs    .MMm         dMm   `mMN.  ")
                    print( "                           `mMm`      `mMm`   oMMs        .MMh    mMN.  ")
                    print( "                            mMN-...    +MMo` -NMN.       `yMN:   `mMM-   ")
                    print( "                            dMMMMMN.    sMMhyNMm:    .hhydMm/    `NMMdhhhs`  ")
                    #告知使用者正確答案
                    print(f'答案是:{answer}')
                                                                                                                              
                    break#跳出迴圈
        #告知使用者剩餘次數
        print(f'剩餘{time}次機會')
         # 將計數歸零
        a_count=0
        b_count=0

       
# end 進入迴圈，直到玩家正確猜出數字
