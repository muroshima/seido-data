#!/bin/zsh
# seido の巡回（update）と取り出し（fill）を決まった時刻に起動する。launchd や cron から呼ぶ。
# GitHub の定期実行は数時間遅れたり飛ばされたりするため。runner は 1 台なので、積んでも後ろに並ぶ。
#   kick.sh update  18 時間以内に巡回が始まっていなければ起動する
#   kick.sh fill    fill か update が待ち・実行中なら何もしない。GPU が空いているかは fill 自身が見る
# gh が認証済みであること
set -u
REPO=${SEIDO_REPO:-muroshima/seido}
echo "== $(date '+%F %T') $1"
case $1 in
  update)
    recent=$(gh run list -R $REPO -w update.yml -L 10 --json createdAt,conclusion \
      --jq '[.[]|select(.conclusion!="cancelled")|select((.createdAt|fromdateiso8601) > now-18*3600)]|length')
    if (( recent > 0 )); then
      echo "18 時間以内に巡回が始まっているので見送る"
      exit 0
    fi
    ;;
  fill)
    busy=$(for w in fill.yml update.yml; do
      gh run list -R $REPO -w $w -L 5 --json status --jq '.[]|select(.status!="completed")|.status'
    done)
    if [[ -n $busy ]]; then
      echo "動いている回があるので見送る: $(echo $busy | tr '\n' ' ')"
      exit 0
    fi
    ;;
  *)
    echo "使い方: kick.sh update|fill" >&2
    exit 1
    ;;
esac
gh workflow run $1.yml -R $REPO && echo "$1 を起動した"
