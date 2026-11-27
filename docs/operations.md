# 運用

日次の取り込みは、非公開の開発リポジトリの GitHub Actions が、国内に置いた self-hosted runner（ラベル `seido`）で動かしています。自治体のサイトには、海外の IP から繋がらないものがあるためです。runner は 1 台なので、ワークフローは同時には動かず、後ろに並びます。

## ワークフロー

| ワークフロー | 起動 | すること |
|---|---|---|
| `update.yml` | 毎日 03:23 JST（`scripts/kick.sh update`）。GitHub の定期実行は予備 | 取込中の取得元を巡回し、変化があれば取得元ごとにコミットする。GPU が 1 時間空かなければ、制度の情報の取り出しは見送って巡回の結果だけを書く |
| `fill.yml` | 1 日 5 回（`scripts/kick.sh fill` と GitHub の定期実行） | 巡回の日に見送った取り出しを、GPU が空いているときだけ進める。巡回はしない |
| `mirror.yml` | `main` が更新されたとき | 公開用のリポジトリへ `main` を同期する |
| `ci.yml` | PR | lint、テスト、対応表の検証、生成物（`COVERAGE.md`・`index.csv`）が最新かの確認 |

self-hosted runner を使えるのは、`schedule` と `workflow_dispatch` で起動するワークフローだけです（`tests/test_workflows.py` が確かめます）。

## 決まった時刻に起動する

GitHub の定期実行（`schedule`）は、数時間遅れたり飛ばされたりします。2026-11-26 と 11-27 の巡回は、03:00 の予定が 10 時過ぎに始まりました。そこで、runner とは別の端末から `scripts/kick.sh` で `workflow_dispatch` を起動します。

- `kick.sh update`: 18 時間以内に巡回が始まっていなければ起動する
- `kick.sh fill`: fill か update が待ち・実行中なら何もしない。GPU が空いているかは fill 自身が見る

GitHub の定期実行は、起動されなかった日の予備として残しています。`update.yml` は、予備の実行が始まったときに 18 時間以内の巡回（取り消したものを除く）があれば何もしません（`scripts/ran_recently.py`）。

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

- update は GPU のロックを最大 1 時間待ち、取れなければ取り出しを見送る
- fill はロックを待たない。取れたら 10 分ごとに手放し、その間にほかのジョブが取っていればそこでやめる

## 失敗したとき

- 取得元ごとに独立して取り込みます。1 つの取得元が失敗しても、ほかの取得元のコミットは積みます。失敗した取得元は、その回は 1 件も書き換えません。
- 失敗した取得元があると、ジョブは exit 2 で失敗になります。ログで `取り込み失敗` を探してください。サイトの作り替えで一覧の URL が変わったときは、`registry/sources.csv` の `url` を直します。
