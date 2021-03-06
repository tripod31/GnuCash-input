# GnuCash-input
GnuCashは、フリーの会計ソフトです。https://www.gnucash.org/  
GnuCashの取引データをExcelで入力するために作成しました。GnuCashの取引入力画面で入力するより効率的だと思います。Excelで入力すれば、同じパターンの取引データをコピーして入力する等できて効率的です。  
GnuCashの取引データエクスポート形式CSVからGnuCashにインポートできます。しかし、GnuCash形式CSVは貸方と借方が２行に分かれており、データを作成しづらいです。このため、振替伝票形式（独自形式）のExcelファイルをpythonでGnuCash形式に変換するプログラムを作成しました。
## 動作確認環境
* Windows11
* python3.8.1
* GnuCash4.10
## 必要ライブラリ
* pandas
## 取引の入力手順 
1. Excelで取引を振替伝票形式(独自形式）のExcelファイルへ入力 
2. pythonでExcelファイルをGnuCashのエクスポート形式CSVに変換(このプログラムを使用)
3. GnuCashでCSVファイルをインポート
## Excelファイル
サンプルはinput.xlsxです。各列は以下の通り  
|列名|Gnucashの取引データエクスポート形式CSV<br>対応項目|
|--|--|
|番号|番号|
|日付|日付|
|貸方勘定科目フルネーム|勘定科目フルネーム|
|借方勘定科目フルネーム|勘定科目フルネーム|
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
例：  
```
>python input2gnucash.py input.xslx gnucash-input.xslx gnucash-input.csv
```
## Excelファイルイメージ
![gnucash-input](https://user-images.githubusercontent.com/6335693/152723968-307a9e9e-4d2f-44a9-8fff-d052e8cb8b2d.png)
