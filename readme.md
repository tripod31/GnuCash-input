# gnucash-input
GnuCashの取引データをexcelで入力するために作成しました。GnuCashの取引入力が面倒なためです。

## 取引の入力手順 
1. GnuCashへの取引の入力を独自の振替伝票形式のexcelファイルで行う 
2. pythonでgnucashのエクスポート形式CSVに変換
3. できたCSVファイルをGnuCashにインポート

## excelファイル
サンプルはinput.xlsxです。各列は以下の通り  
|列名|Gnucashのエクスポート形式CSV<br>対応項目|
|--|--|
|番号|番号|
|日付|日付|
|貸方勘定科目フルネーム|勘定科目名|
|借方勘定科目フルネーム|勘定科目名|
|摘要|摘要|
|金額数値|金額数値|
|説明|説明|
|備考|備考|

## 実行方法
```
usage: input2gnucash.py [-h] in_excel_file out_excel_file out_csv_file

positional arguments:
  in_excel_file   振替伝票入力形式のexcelファイル
  out_excel_file  gnucash形式のexcelファイル
  out_csv_file    gnucash形式のCSVファイル

optional arguments:
  -h, --help      show this help message and exit
```
