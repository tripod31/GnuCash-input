gnucash_cols=[
        "日付","取引 ID","番号","説明","備考","商品・通貨","無効理由","アクション","摘要","勘定科目フルネーム","勘定科目名",
        "記号付き金額","金額数値","照合","照合日","レート/金額"
]

def gnucash_empty_row():
    """
        returns:
            {"日付":"",...}
    """
    return dict(list(map(lambda x:(x,""),gnucash_cols)))
