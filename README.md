# django-study
## 環境
| Products | Versions |
| --- | --- |
| MacBookPro | Mac OS X 10.15.7 19H2 |
| pyenv | 1.2.21 |
| python | 3.9.0 |
| django | 3.1.4 |

## 開発環境
`venv`にて仮想環境を作成し、開発する
- 仮想環境の作成
  ```
  $ python3 -m venv django-study
  ```
- 仮想環境の有効化
  ```
  $ cd django-study
  $ source venv/bin/activate
  ```
- pythonのローカルバージョン固定
  ```
  $ pyenv local 3.9.0
  ```
- djangoのインストール
  ```
  $ pip install django
  ```
- djangoのバージョン確認
  ```
  python -m django --version
  ```