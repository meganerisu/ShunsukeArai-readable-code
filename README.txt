Python

仕様2:実行手順
1. "上手"という文字列を任意の変数(task1_word)に代入
2. その変数をprint関数の引数として使用
3. ファイルを実行

仕様3:データについて
1. dictionary_data.pyをshiyou1ファイルにimport
2. dictionary_dataの中のtask1_wordをprint関数の引数に使用

仕様4: 実行手順
1. dictionary_data.pyをmain.pyにimport
2. dictionary_dataの中のword1-3をprint関数の引数に使用
3. ファイルの実行

仕様6:
1. arparseを使って引数をCLIからユーザが指定できるようにする (e.g. --id)
2. read_wordでCLIから受け取ったIDを指定
    実行例：
    ```
    $ python main.py --id 2
    2: 市場
    ```

仕様7:
1. arparseを使って引数をCLIからユーザが指定できるようにする (e.g. --id)
2. read_wordでCLIから受け取ったIDを指定
    実行例：
    ```
    $ python main.py --id 2
    2: 市場 いちば
    ```