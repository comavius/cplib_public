# Task_gcc Class Documentation

このクラスは、C++コードをオンラインジャッジ (Online Judge) に提出するタスクを管理します。

## Properties

- `url`: 提出先のURL (str型)
- `id`: ユニークなタスクID (uuid型)
- `testcase_path`: テストケースが保存されるパス (str型)
- `submission_path`: 提出コードが保存されるパス (str型)
- `exe_path`: 実行可能ファイルが保存されるパス (str型)
- `editing_path`: 編集中のファイルが保存されるパス (str型)
- `lib`: 使用するライブラリの内容 (str型)
- `is_accepted`: 提出結果の合格/不合格 (bool型)

## Methods

- `__init__(self, url, tempfile_dir, editing_path, lib_path, edittemp_path)`: クラスの初期化。指定されたパラメータで各プロパティを設定し、指定されたURLからテストケースをダウンロードします。
- `get_id(self)`: タスクIDを返します。
- `get_url(self)`: 提出先のURLを返します。
- `__make_editing_file(self, edittemp_path)`: 編集用テンプレートから編集ファイルを作成します。
- `__download_testcases(self)`: 指定されたURLからテストケースをダウンロードします。
- `test(self)`: 提出コードをコンパイルし、テストケースを用いてテストを行います。テスト結果を表示します。
- `submit(self)`: コードをオンラインジャッジに提出します。
- `marge(self)`: メイン関数とライブラリを結合して、提出用のコードを生成します。
- `__read_libfile(self, lib_path)`: ライブラリファイルを読み込みます。
- `__establish_bash(self)`: bashを操作するためのプロセスを生成します。

## Note

このクラスは、ライブラリとテストケースの管理、コードのテストと提出を行うためのもので、GNU Compiler Collection (GCC) の制約に従ったC++コードの操作を想定しています。
