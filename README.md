# ORDERLY Python / Django Interview
Python / Django Web Developer

Hi, PinChia,

感謝您

這是根據您的回覆所訂製的問題，大約會花費 3- 5 小時的挑戰時間

若您決定要開始這項挑戰，請 fork 此專案，並將每個問題的答案放至對應的資料夾

完成後，請發個PR到此專案


### 挑戰一: python 檔案與資料操作 (folder: x_1)
> 請設計一個 CsvHanlder class，當它被初始化時，會偵測相同目錄下是否存在一個 ilovecoffee 資料夾，若無則建立，有則略過。賦予此 class 一個 create_csv() method, 當被呼叫時，會隨機寫入 500 筆客戶資料至 /ilovecoffee/customers.csv，結構如下:
```
customer_id,customer_name, customer_mobile, frequency
"y88xTa", "tom.y88xTa","+886938766119", "4"
"uYt49x", "peter.uYt49x","+886938922440", "6"
"p9g5As", "hank.p9g5As","+886918300227", "1"
.....
````

##### customer_id:
長度8, 由數字 [0-9], 大寫 [A-Z]，小寫 [a-z] 隨機組成，但開頭不可為數字

##### customer_email: 
隨意用 10 個英文名字建立一組 list: 如 ['tom','peter','hank'....]
將 customer_id 與隨機從 name list 中取出的一個元素進行合併，例如產出 "tom.y88xTa"

##### customer_mobile
隨機產生一個 +886 開頭的台灣電話號碼，若新產出的電話號碼有重複，則需要重新產生

##### frequency
從 [0-20] 中隨機進行選擇

>
> 賦予此 class 一個 calculate_csv() method, 當被呼叫時，會讀取 /ilovecoffee/customers.csv，並列印出frequency 的中數、眾數及平均數 (取至小數點後 5 位)
>


### 挑戰二: Django 客戶排序 (RFM) (folder: x_2)
> 請於 Django 中設計一個 view，並完成以下 4 個函式，再透過 URL GET，以 return json 的型式完成函式回傳。 

```
RFM 指標:
用三個向度分析消費者的重要程度：
1. Recency 新進度: 最後一次消費距離現在的時距
2. Frequency 消費頻率: 此消費者消費次數的密集度
3. Monetary Value 消費額: 此消費者的總消費金額
三種向度各分成五級，而 RFM 總值即為三項度值加總。
```

> 現在您的手上有所有消費者的 RFM 值 ( /x_2/rfm.csv )，需要設計四個函式將消費者列表分別以三種向度以及 RFM 總值排序。

> 已知的條件有: 
- 消費者列表: 所有消費者的 ID 及 RFM 值 ( `list<clients>` )
  - R ( `int` recency )
  - F ( `int` frequency )
  - M ( `int` monetary )
  - ID ( `int` ID)
 
> 需要設計的函式（亦可以寫在同一個函式，指標用 flag 判斷）: 
- 以 R 值排序 (大到小) ( `function` sort_by_recency( ) )
- 以 F 值排序 (大到小) ( `function` sort_by_frequency( ) )
- 以倒 M 值排序 (小到大) ( `function` sort_by_monetary( ) )
- 以 RFM 總值排序 (大到小) ( `function` sort_by_RFM( ) )

### 挑戰三: Project 開發分配 (folder: x_3)
> 現在有一個商用軟體產品，該產品剛上線滿一年，已有一定的客戶量體，但系統穩定度不足，且功能仍然簡陋，因此產品開始有許多的需求要被分配開發資源，假設現在是星期三早上10點鐘，請您針對以下狀況進行思考，並說明每一項的應對方式:
```
(A) 重量級客戶10天前提出的改進需求，需耗時6小時完成，此需求你評估認為非常實用。
(B) 昨天晚上系統發出的 alert, 警示訊息為客戶操作出錯
(C) 早上九點系統發出的 alert, 警示訊息為DB異常
(D) 剛剛你無意中注意到的前台破圖，大約20分鐘可搞定
(E) 近三天專注開發的一項功能，如果現在不接著工作，很可能會忘記重要事項
(F) 昨天寫程式時，無意中發現的程式bug，但不在自已掌管範圍內
.....
````


## 當您挑戰結束時，請在您的最後一次 commit 中輸入您對此份工作，在程式上的期待，謝謝您。

