# seido

日本の支援制度（給付・助成・補助金・減免・貸付・現物支給）を、git の履歴として残すリポジトリです。

自治体の制度ページは上書きで更新され、古い版は残りません。「去年の所得制限はいくらだったか」「いつ対象年齢が変わったか」は、多くの場合あとから確かめられません。このリポジトリは取得元を定期的に見に行き、変化があればコミットします。`git log` が制度の改正履歴になり、`git diff` が何が変わったかを示します。

着想は [houritsu](https://github.com/Kohei-Wada/houritsu)（法令を 1 改正 1 コミットで残す）です。

> **v1.0 までは履歴を作り直して force-push することがあります。**

## いまの状態

制度のデータはまだ取り込んでいません。先に、制度を持つ団体と取得元の対応表を [registry/](registry/) に作っています。どの団体の制度がどこから取れるかは [registry/COVERAGE.md](registry/COVERAGE.md) にあります。

対象は国の府省庁と東京都・都内区市町村から始め、関東、関西の順に広げます。

## ライセンス

- データ（`registry/` と今後の取り込み結果）: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja)。元データの出典は各ファイルに記載します
- コード（`builder/`）: [MIT](LICENSE)

## 動かす

```sh
uv sync
uv run seido registry check
uv run pytest
```
