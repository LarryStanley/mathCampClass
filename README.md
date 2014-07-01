Python
=========

>1989 年，人在阿姆斯特丹的 Guido van Rossum 於耶誕假期著手開發Python ，其目的是設計出一種優美而強大，提供給非專業程式設計師使用的語言，同時採取開放策略，使 Python 能夠完美結合如 C 、 C++ 和 Java 等其他語言。時至今日， Python 已經是相當受歡迎的入門教學語言。

Python 的設計哲學是 
+ 優雅
+ 明確 
+ 簡單

因此 Python 的格言為  
###There is only one way to do it.###
___________
Python 內建許多有用的資料型態，像是整數 (integer) 、
浮點數 (floating-point number) 、字串 (string)…

####浮點數: 
    因為十進位浮點數值並沒有精確的二進位表示式。而這個原因，可能會導致失去一些精確度，且某些浮點作業可能產生未預期的結果。
縮排是 Python 劃分程式區塊 (block) 的方式，通常以  四個空白鍵作為一階

我們運用的等號，其實屬於指派運算子 (assignment operator)，所謂的指派是把

__等號右邊的值給左邊的變數__     **存值的地方<--要傳的值**
```
a = 4
a += 2  # a 會等於 6
```
一般而言，程式中的選擇 (selection) 就是依條件 (condition) 使程式有不同的執行方向，若條件為真，也就是 True ，程式就會跳過 False 的部份執行 True 的部份，反之亦然。
而選擇結構有單一選擇跟多重選擇，兩者都使用 if 陳述， if 為關鍵字 (keyword) 之一，若是多重選擇 if 須與 elif 或 else 連用。

Python 中有兩種迴圈，分別是 while 迴圈 (while loop) 與 for 迴圈 (for loop)

while loop
--------
```
i = 10        # 設定控制變數
while i > 0:
   print(i)   # 迴圈工作區
   i -= 1     # 調整控制變數值
```
>這個迴圈所進行的工作很簡單，先在命令列上印出 10，然後一路遞減到 0 為止while 迴圈的控制變數 (control variable) 必須在 while 之前就先設定好當控制變數i大於0時，迴圈便會重複執行。

所以當我們明確知道重複次數的時候，我們得利用控制變數來記錄 while 迴圈所進行次數，這樣 while 迴圈才會有結束的一天，不然若是三個與控制變數相關的部份，漏了任一部份時，就有可能導致無窮迴圈 (infinite loop) 的發生，例如
```
i = 10          # 設定控制變數
while i > 0:
    print(i)    # 迴圈工作區
                #缺調整控制變數值
```
>這樣一來，控制變數 i 永遠大於 0，所以迴圈會一直重複執行，此例中會不斷的在命令列印出 10 ，直到強制結束程式的執行為止。

(Ctrl+C)*2 為強停指令!!

for loop
-----
for 與 in 連用， in 後面接多個元素的物件。這個 for 迴圈與上面的 while 迴圈功能完全相同，寫成與上方while相同解的範例程式，如下:
```
for i in range(10, 0, -1):
    print(i)
	print()
	```
>此例的 range() 用了三個參數，
+ 第一個參數為起始值
+ 第二個參數為結束值
+ 第三個參數為遞增值


多層FOR
---------
藉由一層層的for迴圈達成多變數的情況





def(函數)
-----
定義函數使用關鍵字 (keyword) def ，其後空一格接函數名稱與小括弧，小括弧用來放參數列 (parameter list) ，函數可以有參數 (parameter) 也可以沒有參數，沒有參數的函數的小括弧留空，另外函數可用 return 設定回傳值 (return value)。



```
n = int(input("> "))
```
執行時可以輸入一個整數值，然後將其值存入n中
在*input*時會先在螢幕上顯示出""內的字元
```
while True:
    n = int(input("> "))
    for i in range(n) :
        print( " " * (n-1-i) , "*" * (2*i+1) , sep='' )
```
