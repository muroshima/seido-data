# 運用

日次の取り込みは、非公開の開発リポジトリの GitHub Actions が、国内に置いた self-hosted runner（ラベル `seido`）で動かしています。自治体のサイトには、海外の IP から繋がらないものがあるためです。runner は 1 台なので、ワークフローは同時には動かず、後ろに並びます。

## ワークフロー

| ワークフロー | 起動 | すること |
|---|---|---|
| `update.yml` | 毎日 03:23 JST（`scripts/kick.sh update`）。GitHub の定期実行は予備 | 取込中の取得元を巡回し、変化があれば取得元ごとにコミットする。48 の取得元を並べて取る（同じホストへは 1 秒以上あけて 1 本ずつ）。制度の情報の取り出しはしない |
| `fill.yml` | 1 日 5 回（`scripts/kick.sh fill` と GitHub の定期実行） | 巡回で新しく取ったページや本文が変わったページから、制度の情報を取り出す。GPU が空いているときだけ進める。巡回はしない |
| `mirror.yml` | `main` が更新されたとき | 公開用のリポジトリへ `main` を同期する |
| `ci.yml` | PR | lint、テスト、対応表の検証、生成物（`COVERAGE.md`・`index.csv`）が最新かの確認 |

self-hosted runner を使えるのは、`schedule` と `workflow_dispatch` で起動するワークフローだけです（`tests/test_workflows.py` が確かめます）。

## 決まった時刻に起動する

GitHub の定期実行（`schedule`）は、数時間遅れたり飛ばされたりします。2026-11-26 と 11-27 の巡回は、03:00 の予定が 10 時過ぎに始まりました。そこで、runner とは別の端末から `scripts/kick.sh` で `workflow_dispatch` を起動します。

- `kick.sh update`: 12 時間以内に巡回が始まっていなければ起動する
- `kick.sh fill`: fill か update が待ち・実行中なら何もしない。GPU が空いているかは fill 自身が見る

GitHub の定期実行は、起動されなかった日の予備として残しています。`update.yml` は、予備の実行が始まったときに 12 時間以内の巡回（update ジョブが実際に動いたもの。予備の実行が見送った回や取り消した回は数えない）があれば何もしません（`scripts/ran_recently.py`）。12 時間は、予備の定期実行の遅れ（実測で 7 時間前後）より長く、1 日より十分短い長さです。

macOS の launchd で起動する例です（`gh` が認証済みであること）。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>seido.update-kick</string>
  <key>ProgramArguments</key>
  <array><string>/path/to/kick.sh</string><string>update</string></array>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>3</integer><key>Minute</key><integer>23</integer></dict>
  <key>StandardOutPath</key><string>/path/to/seido-kick.log</string>
  <key>StandardErrorPath</key><string>/path/to/seido-kick.log</string>
</dict>
</plist>
```

端末が眠っていた時刻の起動は、launchd が目覚めたときに行います。

## GPU

制度の情報の取り出しには、runner 機の GPU でローカル LLM を動かします。GPU はほかのジョブ（Kaggle）と共有していて、そちらを優先します。

- update は GPU を使わない。取り出しは fill に任せる（2026-11-28 の巡回は、新しい取得元の初回の取り出しに時間を使い、約 4,000 件のうち 464 件しか回れなかった）
- fill はロックを待たない。取れたら 10 分ごとに手放し、その間にほかのジョブが取っていればそこでやめる

## 失敗したとき

- 取得元ごとに独立して取り込みます。1 つの取得元が失敗しても、ほかの取得元のコミットは積みます。失敗した取得元は、その回は 1 件も書き換えません。
- 制度ページが前回より大きく減ったとき（0 件になった、または 6 件以上あったものが半分未満になった）も失敗として扱い、書き換えません。サイトの作り替えで一覧が空になると、その取得元の制度がまとめて削除されて見えるためです。意図した減少なら `seido update <source_id> --allow-drop <source_id>`（update.yml では `allow_drop` の入力）で書き込みます。
- 失敗した取得元があると、ジョブは exit 2 で失敗になり、ラベル「巡回の失敗」の Issue に取得元と理由が載ります（`scripts/report_failures.py`）。開いた Issue があればコメントを足し、無ければ立てます。直したら Issue を閉じてください。
- サイトの作り替えで一覧の URL が変わったときは、`registry/sources.csv` の `url` を直します。
