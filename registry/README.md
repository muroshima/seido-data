# 対応表

制度を持つ団体と、その制度をどこから取るかの一覧です。取り込みはこの表に載った取得元だけを対象にします。どの団体がまだ取れていないかは [COVERAGE.md](COVERAGE.md) で見られます。

## entities.csv（団体）

| 列 | 中身 |
|---|---|
| `id` | 地方公共団体は `lg:<全国地方公共団体コード>`、国の機関は `gov:<法人番号>` |
| `kind` | `国` / `都道府県` / `市区町村` |
| `name` | 団体名 |
| `parent` | 外局なら親の府省、市区町村なら都道府県の `id` |
| `lg_code` | 全国地方公共団体コード（6 桁、検査数字つき） |
| `corporate_number` | 法人番号（13 桁）。地方公共団体は団体コードから計算する |
| `website` | 公式サイト |

`uv run seido registry entities --pref 13 --gov` で、総務省の[全国地方公共団体コード](https://www.soumu.go.jp/denshijiti/code.html)と Wikidata から作ります。既にある行は、手で直した値を残して空欄だけ埋めます。

出典: 総務省「全国地方公共団体コード」を加工して作成。公式サイトと国の機関の法人番号は Wikidata（CC0）から取得。全国の 47 都道府県と 1,741 市区町村が入っています（2026-11-27）。団体コードはあるが行政を行っていない北方領土の 6 村は入れません。

## sources.csv（取得元）

| 列 | 中身 |
|---|---|
| `source_id` | 英小文字・数字・ハイフン。取り込んだファイルの置き場所にも使う |
| `name` | 取得元の名前 |
| `provider` | 公開している団体の `id` |
| `covers` | 制度がこの取得元に載っている団体。`;` 区切り、`lg:13*` のようなワイルドカード可 |
| `scope` | 扱う制度の範囲。`全般` は分野を限定しない形式という意味で、網羅しているとは限らない。それ以外は `子育て（0-6歳）` のように分野を書く |
| `kind` | `api` / `opendata` / `web` |
| `format` | `json` / `csv` / `xlsx` / `html` など。`web` の行は `html`（一覧ページ）、`html-query`（一覧ページ。クエリ付きのリンクは / で終わっても制度ページ）、`html-page`（制度ページそのもの）、`pdf`（制度の説明の PDF） |
| `url` | 取得元の入口（データセットのページ、API の仕様など） |
| `license` | 利用条件。分からなければ `不明` |
| `publish` | 公開する範囲。`本文` は取得元の文章を `raw/` と `seido/` に置く。利用規約が二次利用を認めるもの（CC BY、公共データ利用規約など）だけ。`事実` は取得元の文章を置かず、制度名・URL・本文のハッシュと、取り出した制度の情報（対象者・支援内容・期間・利用方法・問い合わせ）だけを置く。`license` が `不明` なら `本文` にできない |
| `update` | 取得元の更新頻度。更新が止まっていれば `停止（YYYY-MM-DD 時点）` |
| `status` | 下の表のどれか |
| `checked` | この行を最後に確かめた日 |
| `note` | 取り込みで気をつけること |

| `status` | 意味 |
|---|---|
| `取込中` | 取り込んでいる。更新が止まっていなければ日次で回す |
| `取込予定` | 取り込める（`publish` の範囲で）。実装待ち |
| `調査中` | 中身や利用条件を確認している |
| `要利用申請` | 事実だけでも、取り込むには申請や契約が要る |
| `対象外` | 調べた結果、支援制度の一覧ではなかった |

`status` は取り込めるかどうか、`publish` は何を公開するかを表します。たとえば転載を禁止している自治体の一覧ページは、`status` が `取込予定`、`publish` が `事実` です。

## 取得元を足すとき

候補の行を `sources.csv` と同じ列の CSV に書き、書き込まずに試し取りします。国内の IP から動かしてください（海外から繋がらない自治体のサイトがあります）。

```sh
uv run seido trial --add candidates.csv          # 候補を試す（対応表は変えない）
uv run seido trial kumagaya-sumai-josei          # 対応表にある行を試し直す
uv run seido trial --add candidates.csv --apply  # 結果を sources.csv に反映する
```

取得元ごとに、取れたページ数と題名、題名のうち制度らしいもの（「手当」「助成」「補助」などを含み、「会議」「お知らせ」などを含まない）の割合を出します。`OK` は 60% 以上、`CHECK` は 40% 以上 60% 未満で題名を見て確かめるもの、`NG` は 40% 未満か取れなかったものです。`--apply` は 40% 以上の行を `取込中` にし（`html-page` の行は取れれば `取込中`）、`checked` を今日に、`note` の末尾に試行の結果を書きます。対応表に無い行は足し、取り込めないものは `取込予定` のままにします。

一覧ページに制度以外の案内が多いときは、主な制度のページを `html-page` の行で 1 件ずつ登録します。

## 取り込み方を変えたとき

本文領域や題名の見分け方を変えたら、新旧のコードで全取得元の結果を比べます。取ったページはディスクに置き、旧と新で同じバイト列を読みます。

```sh
git worktree add --detach ../seido-old main
(cd ../seido-old && uv run seido regress --cache /tmp/regcache --out /tmp/old.json)
uv run seido regress --cache /tmp/regcache --out /tmp/new.json
uv run seido regress --compare /tmp/old.json /tmp/new.json
```

取得元ごとに、ページの追加・削除と、題名・本文のハッシュが変わったページを出します。本文のハッシュが変わる取得元は CHANGELOG.md に書きます。

## 編集したら

```sh
uv run seido registry check      # 検証（CI でも走る）
uv run seido registry coverage   # COVERAGE.md・coverage/<都道府県コード>.md・coverage-map.svg を作り直す
```

## 地図（coverage-map.svg）

取込中の取得元がある市区町村を赤で塗った地図です。README の冒頭に出しています。境界は国土交通省「[国土数値情報（行政区域データ）](https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-N03-2024.html)」（2024 年 1 月 1 日時点、CC BY 4.0）を簡略化した `boundaries.json` から描きます。境界を作り直すときだけネットワークが要ります。

```sh
uv run seido registry boundaries --cache /tmp/n03   # 47 都道府県の zip（約 800 MB）を取って作り直す
```

関西など新しい地域に広げるときは、`builder/map.py` の `PANELS` に拡大図を足してから境界を作り直します。
