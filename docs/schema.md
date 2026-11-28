# データの定義

`seido/` と `raw/` のファイル、一覧（`seido/<都道府県>/index.csv`）、コミットの書式の定義です。件数は 2026-11-21 時点。

## 制度ファイル（`seido/**/*.md`）

`seido/<都道府県コード2桁>/<団体コード6桁>/<source_id>/<ID>.md` に、制度 1 件を置きます。

### frontmatter

| 項目 | 型 | 中身 |
|---|---|---|
| `title` | 文字列 | 制度名。取得元の表記のまま |
| `lg_code` | 文字列（6 桁） | 制度を持つ団体の全国地方公共団体コード（検査数字つき）。東京都は `130001` |
| `lg_name` | 文字列 | 団体名。[registry/entities.csv](../registry/entities.csv) の名前 |
| `support` | `金銭` / `現物` / `金銭・現物` / `null` | 支援の種類。取得元が区別しているときだけ入る（2,234 件は `null`） |
| `url` | 文字列 / `null` | 制度の案内ページ。申請の前にはここで確かめる |
| `source` | 文字列 | 取得元の `source_id`（[registry/sources.csv](../registry/sources.csv)） |
| `source_id` | 文字列 | 取得元の中での ID。ファイル名の `<ID>` と同じ |
| `source_updated` | 日付 / `null` | 取得元が示す更新日 |
| `license` | 文字列 | 取得元の利用条件 |
| `attribution` | 文字列 | 出典表記。再利用するときはこれを表示する |
| `content_sha256` | 文字列 | ページの本文のハッシュ。Web の取得元だけ（1,750 件） |
| `facts_sha256` | 文字列 | 下の節をどの本文から取り出したか。`content_sha256` と同じなら最新の本文から取り出している |

### 節

frontmatter の後に `# 制度名` と、次の `## 見出し` が続きます。取得元に無い節は出しません。

| 見出し | 件数 | 中身 |
|---|---:|---|
| `概要` | 6,649 | 制度の説明 |
| `対象者` | 7,705 | 誰が使えるか |
| `支援の対象` | 484 | 何が対象か（取得元が対象者と分けているとき） |
| `支援内容` | 8,187 | 金額・現物の内容 |
| `期間` | 1,345 | 申請期間・支給期間 |
| `利用方法` | 6,559 | 申請の手順 |
| `持ち物` | 2,379 | 申請に要るもの |
| `根拠法令` | 5,669 | 条例・要綱など |
| `問い合わせ` | 8,094 | 担当の部署と連絡先 |

転載を禁止している取得元（`registry/sources.csv` の `publish` が `事実`）のファイルは、`概要` を持たず、`対象者`・`支援内容`・`期間`・`利用方法`・`問い合わせ` だけを、ローカル LLM でページから取り出して短く書きます。取り出せなかった節は出しません。

### ID

- 取得元に ID 列があれば、それを使います（例: `psid3.0_8000020131148_1_UM1`）。
- Web の取得元は、ページの URL の末尾の名前と、パスのハッシュ 8 桁から作ります（例: `20211116-tokuji-67bb17b1`）。
- どちらも無ければ制度名から作ります。名前が変わると、削除と追加の 2 件に見えます。

## 一覧（`seido/<都道府県>/index.csv`）

都道府県（`seido/` の下の 2 桁のフォルダ）ごとに 1 つ。その都道府県の制度 1 件 1 行、`path` の昇順。2026-11-28 までは、全国で 1 つの `seido/index.csv` でした。UTF-8、ヘッダあり、改行は LF。

| 列 | 中身 |
|---|---|
| `path` | 制度ファイルのパス |
| `lg_code` | frontmatter の `lg_code` |
| `lg_name` | frontmatter の `lg_name` |
| `title` | frontmatter の `title` |
| `support` | frontmatter の `support`（`null` は空） |
| `source` | frontmatter の `source` |
| `source_id` | frontmatter の `source_id` |
| `url` | frontmatter の `url` |
| `license` | frontmatter の `license` |
| `attribution` | frontmatter の `attribution` |

`uv run seido index` で作り直せます。取り込みは、制度ファイルと同じコミットで一覧を更新します。

## 取得元のレコード（`raw/**/*.json`）

`raw/<source_id>/<団体コード6桁>/<ID>.json` に、取得元の 1 レコードを置きます。キーは取得元ごとに違います。

| 取得元 | 中身 |
|---|---|
| 東京都 子育て支援制度レジストリ（`tokyo-kosodate-registry`） | API の 1 制度をそのまま |
| 自治体標準オープンデータセット（`tokyo-ods-support-*` など） | CSV の 1 行。キーは列名 |
| Web の一覧ページ（`kind` が `web`） | `url`・`title`・`content_sha256`・`content_length` だけ。本文は置かない |

## コミット

```
<source_id>: <N>件追加・<N>件更新・<N>件削除（<観測日> 観測）

Source: <source_id>
Source-Url: <取得元の入口の URL>
Observed: <観測日 YYYY-MM-DD>
Builder-Version: <取り込みのコードの版>
```

- author と committer の日時は、どちらも観測日の 00:00 JST です。更新が止まった取得元は、止まった日にします。
- 1 コミットは 1 つの取得元の 1 回の観測で、`raw/` と `seido/`（一覧を含む）だけを変えます。
- コードや対応表の変更のコミットは、この書式を持ちません（trailer の `Source` が無い）。

日次の巡回は制度の情報を取り出しません。新しく取ったページや本文が変わったページは、あとで GPU の空いた時間に取り出し、別のコミットにします。前回の巡回のときと本文が同じページだけが対象で、`seido/` の項目と `facts_sha256` だけを変えます（`raw/` と一覧は変えません）。

```
<source_id>: 前回の巡回で取った本文から制度の情報を取り出す

Source: <source_id>
Source-Url: <取得元の入口の URL>
Extracted: <取り出した日 YYYY-MM-DD>
Builder-Version: <取り込みのコードの版>
```

- `Observed` を持たず、author と committer の日時は取り出した時刻です。観測のコミットだけを見たいときは `Observed` のあるコミットに絞ってください。
