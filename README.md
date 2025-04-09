# Bitwarden CSV Duplicate Remover

🛡️ A simple Python script to remove duplicate entries from a Bitwarden-exported CSV file.

Bitwarden からエクスポートされた CSV ファイルの重複エントリを削除するシンプルな Python スクリプトです。

## Features / 特徴

🧹 Removes duplicates based on login_uri, login_username, and login_password

🧾 Accepts custom input/output file names via command-line arguments

🗂 Keeps only the first occurrence of each duplicate entry

## Requirements / 必要要件

Python 3.x

## Installation / インストール

```bash
git clone https://github.com/your-username/bitwarden-dedupe-script.git
cd bitwarden-dedupe-script
```

- 外部ライブラリのインストールは不要です。

## Usage / 使い方

Basic Usage / 基本的な使い方

```
python dedupe_bitwarden.py
```

This will:

Read from bitwarden.csv

Write deduplicated data to bitwarden_unique.csv

これは bitwarden.csv を読み込み、重複を削除した内容を bitwarden_unique.csv に出力します。

### Custom Input/Output Files / 入出力ファイルを指定する場合

```
python dedupe_bitwarden.py --input my_export.csv --output cleaned.csv
```

または省略形：

```
python dedupe_bitwarden.py -i my_export.csv -o cleaned.csv
```

Duplicate Detection Criteria / 重複の判定基準
The script considers entries duplicates if all of the following fields match:

スクリプトは以下すべての項目が一致する場合に「重複」と判定します：

- login_uri

- login_username

- login_password

### Output / 出力ファイル

The resulting CSV will contain the original header and only unique rows based on the above criteria.

出力される CSV には元のヘッダーと、上記の基準で一意な行のみが含まれます。
