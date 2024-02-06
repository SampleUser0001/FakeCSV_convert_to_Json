# CSVもどきをJsonに変換する

## 前提

下記をjsonに変換するのだが、  
**そもそもこんなファイルを生成してはいけない！！**  
**これはCSVではない！！**  
**こんなファイルを作るのであれば、2ファイルに分けなければいけない。**

``` csv
PATTERN_A
a,b,b,c
hoge,piyo,1,fuga
aaa,bb,2,ccc
PATTERN_B
a,a,b,c,c
hoge,1,piyo,fuga,2
```

## アプローチ

複数のCSVに分けてからpandasでcsv -> json変換する。

## 実行方法

### 準備

``` bash
python -m venv venv
source venv/bin/activate
pip install pandas
```

### 実行

``` bash
source venv/bin/activate
python app.py datas.csv
```

``` txt
{<TypeEnum.PATTERN_A: 'PATTERN_A'>: [{'a': 'hoge', 'b': 'piyo', 'b.1': 1, 'c': 'fuga'}, {'a': 'aaa', 'b': 'bb', 'b.1': 2, 'c': 'ccc'}], <TypeEnum.PATTERN_B: 'PATTERN_B'>: [{'a': 'hoge', 'a.1': 1, 'b': 'piyo', 'c': 'fuga', 'c.1': 2}]}

```