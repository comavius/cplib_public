# Contest Class Documentation

このクラスは、特定の競技コンテストとその各タスクを管理します。

## Properties

- `id`: ユニークなコンテストID (uuid型)
- `contest_name`: コンテストの名前 (str型)
- `repo_path`: レポジトリのパス (str型)
- `temp_path`: 一時ファイルが保存されるパス (str型)
- `lib_path`: 使用するライブラリの内容が保存されるパス (str型)
- `tasks`: このコンテストの各タスクオブジェクトが保存されるディクショナリ

## Methods

- `__init__(self, repo_path, type, contest_number)`: クラスの初期化。指定されたパラメータで各プロパティを設定し、タスクを設定します。
- `set_tasks(self, type, tempfile_dir, lib_path)`: 指定されたタイプ、一時ファイルディレクトリ、ライブラリパスを元に、各タスクを設定します。
- `get_libs(self)`: ライブラリの内容を取得します。
- `get_edittemp(self)`: 編集用テンプレートを取得します。
- `test(self, task_name)`: 指定したタスク名のテストを実行します。
- `marge(self, task_name)`: 指定したタスク名のメイン関数とライブラリを結合します。
- `submit(self, task_name)`: 指定したタスク名のコードをオンラインジャッジに提出します。

## Note

このクラスは、競技プログラミングの特定のコンテストとその各タスクを管理します。コンテストとタスクの情報を元に、テストケースの取得、コードのテスト、コードの提出を行います。
