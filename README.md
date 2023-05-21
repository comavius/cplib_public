# CP_LIB(LIBrary and tools for Competitive Programming)
## 目的と機能
CP_LIBは競技プログラミング用のテスト・提出支援ツールで、コンテスト中の認知負荷を下げることを目的としています。そのために、以下のような機能を持っています。
- [online-judge-tools](https://github.com/online-judge-tools/oj/blob/master/docs/getting-started.ja.md)(以降oj)を利用した自動テスト・提出
- ojの操作の自動化
- 作業を行うファイルの自動生成
- ./lib/に格納された自作ライブラリと作業ファイルの、提出ファイルへの自動マージ
## コンテスト中の操作方法
まず、/online_judge/main.pyを立ち上げます。ターミナルでの操作は以下のような方法で行います。
1. ユーザーにコンテストの種類と番号を入力するように促します。
2. コンテストのインスタンスを生成します。
3. ユーザーに次のコマンドを入力するように促します。
   - `t`: 現在のタスクをテストします。ターミナルの標準出力にojからの出力が出力されます。
   - `c`: 現在のタスクを切り替えます。切り替える先を第2引数で指定します。
   - `s`: 現在のタスクを提出します。
   - `exit_from_this_contest`: このコンテストから退出します。

以下は入出力の例です。

```
>>> Welcome to CPLIB!
>>> Please enter the contest type: abc
>>> Please enter the contest number: 302
>>> Is this correct? (y/n): y
{repo_path}/temp/550c821b-8ad7-4ac2-bbbd-e63021e63c33/lib.cpp
{repo_path}/temp/550c821b-8ad7-4ac2-bbbd-e63021e63c33/lib.cpp
{repo_path}/temp/550c821b-8ad7-4ac2-bbbd-e63021e63c33/lib.cpp
{repo_path}/temp/550c821b-8ad7-4ac2-bbbd-e63021e63c33/lib.cpp
{repo_path}/temp/550c821b-8ad7-4ac2-bbbd-e63021e63c33/lib.cpp
{repo_path}/temp/550c821b-8ad7-4ac2-bbbd-e63021e63c33/lib.cpp
{repo_path}/temp/550c821b-8ad7-4ac2-bbbd-e63021e63c33/lib.cpp
{repo_path}/temp/550c821b-8ad7-4ac2-bbbd-e63021e63c33/lib.cpp
>>> t
[INFO] online-judge-tools 11.5.1 (+ online-judge-api-client 10.10.1)
[INFO] 3 cases found

[INFO] sample-1
[INFO] time: 0.002214 sec
[SUCCESS] AC

[INFO] sample-2
[INFO] time: 0.002007 sec
[SUCCESS] AC

[INFO] sample-3
[INFO] time: 0.001995 sec
[SUCCESS] AC

[INFO] slowest: 0.002214 sec  (for sample-1)
[INFO] max memory: 3.476000 MB  (for sample-3)
[SUCCESS] test success: 3 cases

>>> s
(中略 提出成功 AC)

>>> c c
>>> t
[INFO] online-judge-tools 11.5.1 (+ online-judge-api-client 10.10.1)
[INFO] 3 cases found

[INFO] sample-1
[INFO] time: 0.002471 sec
[SUCCESS] AC

[INFO] sample-2
[INFO] time: 0.001912 sec
[SUCCESS] AC

[INFO] sample-3
[INFO] time: 0.001843 sec
[SUCCESS] AC

[INFO] slowest: 0.002471 sec  (for sample-1)
[INFO] max memory: 3.680000 MB  (for sample-1)
[SUCCESS] test success: 3 cases

>>> exit_from_this_conteset
>>> Bye!
```

## 自作ライブラリの設定方法
自作ライブラリは以下の様は方法で追加することができます。
1. ソースファイルとヘッダファイルを用意します。(マクロの宣言など、本来ソースファイルが必要ない場合もソースファイルが必要です。)
2. ライブラリの名前を決め、/lib/直下にその名前のフォルダを作成します。
3. 2で作ったフォルダの中に、"2で決めた名前".cppと"2で決めた名前".hppを作成します。
4. /lib/cplib_main.hppにライブラリのヘッダファイルをインクルードします。
5. /lib/list.csvの新しい行に2で決めた名前を追加します。

## 対応環境
- AtCoder(abc, arc, agc)
- C++(gcc)
- online-judge-tools
- テスト環境 : Linux(Ubuntu 22.04.2 LTS)

## 今後の予定
今後追加したい機能です。
- seleniumを利用したブラウザの制御
- watchdogやasyncioを利用した作業ファイルの監視とテストの完全自動化
- ライブラリの追加の簡略化、あるいはgitを利用した管理
- AtCoder以外のサービスやC++以外の言語への対応
- ojの出力の色情報の維持

## 連絡先
[こま/Comavius on twitter](https://twitter.com/comavius)