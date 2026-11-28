# 貢献のしかた

## 報告と提案

[Issue](https://github.com/muroshima/seido-data/issues) で受け付けます。

- **取り出した内容の誤り**: 制度ファイルのパスと、どこが違うか（取得元のページの記載）を書いてください。LLM で取り出した項目の誤りは、取り出し方を直して作り直します。ファイルを手で直すことはしません。
- **取得元の追加**: 団体名、制度の一覧ページの URL、そのサイトの利用規約（著作権・リンクのページ）の URL を書いてください。[registry/README.md](registry/README.md) の列で整理して [registry/sources.csv](registry/sources.csv) に足します。
- **取得元の利用規約の誤り**: `registry/sources.csv` の `license` と `publish` が実際の規約と違うときに教えてください。

## Pull Request

コードと対応表の変更は PR でも受け付けます。ただし、このリポジトリは非公開の開発リポジトリから同期しているので、PR はこちらで開発リポジトリに取り込んでから反映し、PR は閉じます。`seido/` と `raw/` は取り込みが書き換えるので、手で直す PR は受け付けません。

外部からの PR では、ワークフローは管理者が承認してから動きます。

## 手元で動かす

```sh
uv sync
uv run ruff check . && uv run ruff format --check .
uv run seido registry check
uv run pytest
```

対応表を変えたら `uv run seido registry coverage` で `registry/COVERAGE.md` と `registry/coverage/` を、制度ファイルを変えたら `uv run seido index` で `seido/<都道府県>/index.csv` を作り直してください。CI がこの 2 つが最新かを確かめます。
