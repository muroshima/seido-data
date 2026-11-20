# カバー状況

`uv run seido registry coverage` で生成する。手で編集しない。

- ○: 取込中・取込予定の取得元があり、制度全般を扱う
- ◐: 取込中・取込予定の取得元はあるが、分野が限られる（子育てだけ、など）
- △: 取得元は見つかっているが、調査中・要利用申請・対象外のみ
- −: 取得元が見つかっていない

| 区分 | 団体数 | ○ | ◐ | △ | − |
|---|---:|---:|---:|---:|---:|
| 国 | 26 | 0 | 2 | 24 | 0 |
| 都道府県 | 7 | 1 | 0 | 6 | 0 |
| 市区町村 | 316 | 15 | 47 | 254 | 0 |

## 団体別

| 団体 | 区分 | 状況 | 取得元 |
|---|---|---|---|
| 法務省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 中小企業庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `mirasapo-subsidy`（中小企業向けの主要補助金・助成金・調査中）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `chusho-hojyokin-kobo`（中小企業向け補助金の公募・調査中）, `chusho-g-book`（中小企業施策全般・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 環境省 | 国 | ◐ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `env-carbon-neutral-subsidy`（脱炭素分野の補助・委託事業（自治体・事業者・個人）・取込予定）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 内閣府 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 総務省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 特許庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `jpo-genmen`（特許料・審査請求料の減免（中小企業・個人など）・調査中）, `jpo-chusho-support`（中小企業向けの知財支援（減免・助成・相談）・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 国土交通省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `mlit-jutaku-shienjigyo`（住宅取得・リフォームの補助・税制・融資（個人・事業者）・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 水産庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `jfa-hozyo-kobo`（水産分野の補助事業の公募・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 資源エネルギー庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `mirasapo-subsidy`（中小企業向けの主要補助金・助成金・調査中）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `enecho-public-offer`（エネルギー分野の補助金・委託の公募・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 復興庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 林野庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `rinya-hojyo-kobo`（林業分野の補助事業の公募・調査中）, `rinya-hojojigyou`（林業関係の補助事業（予算ごと）・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 経済産業省 | 国 | ◐ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `mirasapo-subsidy`（中小企業向けの主要補助金・助成金・調査中）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `env-carbon-neutral-subsidy`（脱炭素分野の補助・委託事業（自治体・事業者・個人）・取込予定）, `chusho-g-book`（中小企業施策全般・調査中）, `meti-kobo`（補助金・委託などの公募・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 消費者庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| スポーツ庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `sports-boshu`（スポーツ分野の公募・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 農林水産省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `maff-hozyo-kobo`（農業分野の補助事業の公募・調査中）, `maff-aid`（農林水産分野の補助事業・税制の入口・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 金融庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 文化庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `bunka-joseishien`（文化財分野の助成・支援・調査中）, `bunka-kobo`（文化芸術の補助金・委託の公募・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 厚生労働省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `mirasapo-subsidy`（中小企業向けの主要補助金・助成金・調査中）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `mhlw-joseikin-shoureikin`（事業主・事業主団体・労働者向けの助成金・給付金・調査中）, `mhlw-koyou-kyufukin`（事業主向けの雇用関係助成金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| こども家庭庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 国税庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 文部科学省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `mext-boshu`（文部科学分野の公募・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| デジタル庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 財務省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 外務省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 観光庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `kankocho-kobo`（観光分野の補助事業などの公募・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 防衛省 | 国 | △ | `jgrants`（事業者向け補助金・調査中）, `jnet21-snavi-support-rss`（事業者向け補助金・助成金・融資（国＋都道府県・市区町村）・要利用申請）, `jnet21-snavi-search`（事業者向け補助金・助成金・融資・要利用申請）, `gbiz-portal-search`（事業者向け行政手続・補助金・調査中）, `cao-bousai-kakusyuseido`（被災者向けの給付・貸付・減免・住宅支援（府省横断）・調査中）, `rssystem-review-csv`（全府省の予算事業（補助金事業を含む）・調査中）, `egov-dataportal-ckan`（府省のオープンデータ全般・対象外）, `govonline`（暮らしの広報記事・対象外） |
| 茨城県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 栃木県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 群馬県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 埼玉県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 千葉県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東京都 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-hojokin-search`（都の補助金・取込予定）, `tokyo-shien-navi`（全般・取込予定） |
| 神奈川県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 水戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日立市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 土浦市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 古河市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 石岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 結城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 龍ケ崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下妻市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 常総市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 常陸太田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高萩市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北茨城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 笠間市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 取手市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 牛久市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| つくば市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| ひたちなか市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿嶋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 潮来市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 守谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 常陸大宮市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那珂市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 筑西市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 坂東市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 稲敷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| かすみがうら市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 桜川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神栖市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 行方市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鉾田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| つくばみらい市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小美玉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 茨城町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大洗町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 城里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東海村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美浦村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿見町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 河内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八千代町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五霞町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 境町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 利根町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇都宮市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 足利市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 栃木市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿沼市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日光市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 真岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大田原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 矢板市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那須塩原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| さくら市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那須烏山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上三川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 益子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 茂木町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 市貝町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 芳賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 壬生町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 野木町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 塩谷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高根沢町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那須町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那珂川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 前橋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 桐生市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊勢崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 太田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 沼田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 館林市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 渋川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 藤岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安中市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| みどり市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 榛東村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉岡町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上野村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神流町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下仁田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南牧村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 甘楽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中之条町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長野原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 嬬恋村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 草津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高山村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東吾妻町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 片品村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川場村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 昭和村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| みなかみ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 玉村町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 板倉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 明和町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 千代田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大泉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 邑楽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| さいたま市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川越市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 熊谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川口市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 行田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 秩父市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 所沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯能市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 加須市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 本庄市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東松山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 春日部市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 狭山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 羽生市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鴻巣市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 深谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上尾市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 草加市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 越谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 蕨市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 戸田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 入間市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 朝霞市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 志木市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和光市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新座市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 桶川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 久喜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北本市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八潮市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富士見市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三郷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 蓮田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 坂戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 幸手市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鶴ヶ島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日高市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| ふじみ野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊奈町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三芳町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 毛呂山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 越生町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 滑川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 嵐山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉見町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鳩山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| ときがわ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 横瀬町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 皆野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長瀞町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小鹿野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東秩父村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 寄居町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮代町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 杉戸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松伏町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 千葉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 銚子市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 市川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 船橋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 館山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 木更津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 野田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 茂原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 成田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐倉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東金市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 旭市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 習志野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 柏市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 勝浦市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 市原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 流山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八千代市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 我孫子市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鴨川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鎌ケ谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 君津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浦安市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 四街道市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 袖ケ浦市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八街市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 印西市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白井市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富里市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南房総市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 匝瑳市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 香取市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山武市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| いすみ市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大網白里市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 酒々井町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 栄町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多古町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東庄町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 九十九里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 芝山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 横芝光町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 一宮町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 睦沢町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長生村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長柄町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大多喜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御宿町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鋸南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 千代田区 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `chiyoda-teate-josei`（全般・取込中）, `chiyoda-shogaisha`（障害・取込予定）, `chiyoda-jigyosha`（事業者・取込予定）, `chiyoda-jigyosha-rss`（事業者・調査中） |
| 中央区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `chuo-kosodate-teate`（子育て・取込中）, `chuo-koureisha-teate`（高齢者・取込予定）, `chuo-shougai-teate`（障害・取込予定）, `chuo-sumai-kyojuushien`（住まい・取込予定）, `chuo-hojokin`（事業者・取込予定）, `chuo-sitemap`（全般・調査中） |
| 港区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `minato-kodomo-teate`（子育て・取込中）, `minato-shogaisha-teate`（障害・取込中）, `minato-chushokigyo-hojo`（事業者・取込予定）, `minato-sitemap`（全般・調査中）, `minato-opendata-ckan`（全般・対象外） |
| 新宿区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `shinjuku-kodomo-teate`（子育て・取込予定）, `shinjuku-fukushi-teate`（障害・取込中）, `shinjuku-opendata`（全般・対象外） |
| 文京区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `bunkyo-kosodate-teate`（子育て・取込予定）, `bunkyo-shougai-teate`（障害・取込予定）, `bunkyo-hojokin`（事業者・取込中）, `bunkyo-sitemap`（全般・調査中）, `bunkyo-opendata`（全般・対象外） |
| 台東区 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `taito-teate-josei`（全般・取込中）, `taito-opendata`（全般・対象外） |
| 墨田区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `sumida-kosodate-teate`（子育て・取込中）, `sumida-koureisya`（高齢者・取込予定）, `sumida-koureisya-netakiri`（高齢者・取込中）, `sumida-syougai`（障害・取込予定）, `sumida-syougai-teate`（障害・取込中）, `sumida-syougai-waribiki`（障害・取込中）, `sumida-hojokin-joseikin`（事業者・取込中）, `sumida-sitemap`（全般・調査中）, `sumida-opendata`（全般・対象外） |
| 江東区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `koto-kodomo-teate`（子育て・取込予定）, `koto-shogaisha-waribiki`（障害・取込予定）, `koto-chusho-hojokin`（事業者・取込中）, `koto-fukushi-rss`（健康・福祉・調査中） |
| 品川区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `shinagawa-kodomo-teate`（子育て・取込中）, `shinagawa-koreisha-josei`（高齢者・取込予定）, `shinagawa-shogai-josei`（障害・取込予定）, `shinagawa-sumai-josei`（住まい・取込予定） |
| 目黒区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `meguro-kosodate-teate`（子育て・取込予定）, `meguro-koureisha-josei`（高齢者・取込予定）, `meguro-shougaisha-teatejosei`（障害・取込中）, `meguro-sitemap`（全般・調査中）, `meguro-opendata`（全般・対象外） |
| 大田区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `ota-kodomo-teate`（子育て・取込予定）, `ota-kourei-kyufu`（高齢者・取込予定）, `ota-shougai-teate`（障害・取込中）, `ota-jigyousha-chushou`（事業者・取込予定）, `ota-sitemap`（全般・調査中）, `ota-opendata`（全般・対象外） |
| 世田谷区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `setagaya-kosodate-teate`（子育て・取込予定）, `setagaya-kosodate-josei`（子育て・取込中）, `setagaya-sitemap`（全般・調査中）, `setagaya-opendata`（全般・対象外） |
| 渋谷区 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `shibuya-shinsei-josei`（全般・取込中）, `shibuya-kodomo-teate`（子育て・取込予定）, `shibuya-iryo-teate-josei`（医療・取込予定）, `shibuya-sitemap`（全般・調査中） |
| 中野区 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-ods-support-131148`（全般・取込中）, `nakano-jigyosha-josei`（事業者・取込予定） |
| 杉並区 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `suginami-news-teate-kyufu`（全般・取込予定）, `suginami-kosodate-teate`（子育て・取込中）, `suginami-sumai-josei`（住まい・取込予定）, `suginami-sitemap`（全般・調査中）, `suginami-kenkou-rss`（健康・福祉・調査中）, `suginami-opendata`（全般・対象外） |
| 豊島区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `toshima-kosodate-teate`（子育て・取込予定）, `toshima-shogai-teate`（障害・取込中）, `toshima-sumai-josei`（住まい・取込予定）, `toshima-sangyo-hojokin`（事業者・取込予定） |
| 北区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `kita-kodomo-teate`（子育て・取込中）, `kita-elderly-josei`（高齢者・取込中）, `kita-disabilities-teate`（障害・取込予定）, `kita-housing-josei`（住まい・取込中）, `kita-business-hojo`（事業者・取込予定）, `kita-opendata`（全般・対象外） |
| 荒川区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `arakawa-kosodate-teate`（子育て・取込予定）, `arakawa-koureisha-shien`（高齢者・取込予定）, `arakawa-shougaisha-teate`（障害・取込中）, `arakawa-sumai-josei`（住まい・取込予定）, `arakawa-sitemap`（全般・調査中） |
| 板橋区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `itabashi-kosodate-teate`（子育て・取込予定）, `itabashi-kourei-josei`（高齢者・取込予定）, `itabashi-shogai-teate`（障害・取込予定）, `itabashi-iryohi-josei`（医療・取込中）, `itabashi-kenko-rss`（健康・福祉・調査中）, `itabashi-opendata-list`（全般・対象外） |
| 練馬区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `nerima-kodomo-teate`（子育て・取込中）, `nerima-shogai-teate`（障害・取込中）, `nerima-sitemap`（全般・調査中）, `nerima-hokenfukushi-rss`（健康・福祉・調査中）, `nerima-opendata`（全般・対象外） |
| 足立区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `adachi-kosodate-teate`（子育て・取込中）, `adachi-shinshin`（障害・取込予定）, `adachi-shinshin-teate`（障害・取込中）, `adachi-shinshin-genmen`（障害・取込中）, `adachi-chushokigyo`（事業者・取込予定）, `adachi-opendata`（全般・対象外） |
| 葛飾区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `katsushika-kosodate-teate`（子育て・取込予定）, `katsushika-shogai-josei`（障害・取込予定）, `katsushika-business-hojo`（事業者・取込中） |
| 江戸川区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `edogawa-kosodate-teateshien`（子育て・取込中）, `edogawa-shogaisha-teate`（障害・取込予定）, `edogawa-sumaiguide`（住まい・取込予定）, `edogawa-kenko-rss`（健康・福祉・調査中）, `edogawa-opendata`（全般・対象外） |
| 八王子市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `hachioji-kosodate-teate`（子育て・取込予定）, `hachioji-hitorioya-teate`（子育て・取込中）, `hachioji-nyuyoji-teate`（子育て・取込中）, `hachioji-shogai-teate`（障害・取込中）, `hachioji-jigyosha-hojo`（事業者・取込中）, `hachioji-jigyosha-yushi`（事業者・取込中）, `hachioji-sitemap`（全般・調査中） |
| 立川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tachikawa-kosodate-teate`（子育て・取込中）, `tachikawa-shogai-teate`（障害・取込中）, `tachikawa-jigyosha-josei`（事業者・取込中） |
| 武蔵野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `musashino-kosodate-teate`（子育て・取込中）, `musashino-shogai-josei`（障害・取込中） |
| 三鷹市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `mitaka-kosodate-teate`（子育て・取込中）, `mitaka-shogai-josei`（障害・取込中）, `mitaka-koureisha-josei`（高齢者・取込中）, `mitaka-jigyosha-hojo`（事業者・取込中） |
| 青梅市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-ods-support-132055`（全般・取込中）, `ome-kosodate-teate`（子育て・取込予定）, `ome-shogai-hojo`（障害・取込予定）, `ome-shogai-teate`（障害・取込予定） |
| 府中市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `fuchu-jutaku-josei`（住まい・取込中）, `fuchu-saigai-josei`（災害・取込中）, `fuchu-jigyosha-shien`（事業者・取込中） |
| 昭島市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `akishima-jigyosha-hojo`（事業者・取込中） |
| 調布市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `chofu-teate-josei`（全般・取込予定）, `chofu-kosodate-teate`（子育て・取込中）, `chofu-hitorioya-teate`（子育て・取込中）, `chofu-sumai-hojo`（住まい・取込中）, `chofu-jigyosha-yushi`（事業者・取込中）, `chofu-sitemap`（全般・調査中） |
| 町田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `machida-jigyosha-shien`（事業者・取込予定）, `machida-kosodate-teate`（子育て・取込中）, `machida-shogai-teate`（障害・取込中）, `machida-shogai-iryohi`（障害・取込中）, `machida-sitemap`（全般・調査中） |
| 小金井市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-ods-support-132101`（全般・取込中）, `koganei-kosodate-teate`（子育て・取込予定）, `koganei-kankyo-hojo`（環境・取込予定）, `koganei-sumai-josei`（住まい・取込予定） |
| 小平市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `kodaira-kosodate-teate`（子育て・取込予定）, `kodaira-hojo`（環境・取込中）, `kodaira-koureisha-josei`（高齢者・取込中）, `kodaira-shogai-teate`（障害・取込中）, `kodaira-hitorioya-teate`（子育て・取込中） |
| 日野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `hino-jigyosha-hojo`（事業者・取込中）, `hino-kenchiku-hojo`（住まい・取込中） |
| 東村山市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-ods-support-132136`（全般・取込中）, `higashimurayama-kyufu`（全般・取込予定）, `higashimurayama-kosodate-hojo`（子育て・取込予定） |
| 国分寺市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `kokubunji-kosodate-teate`（子育て・取込中）, `kokubunji-shogai-teate`（障害・取込中） |
| 国立市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `kunitachi-kosodate-teate`（子育て・取込中）, `kunitachi-sitemap`（全般・調査中） |
| 福生市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `fussa-opendata-kyufu`（全般・取込中）, `fussa-kosodate-shien`（子育て・取込予定）, `fussa-koureisha`（高齢者・取込予定）, `fussa-shogai`（障害・取込予定）, `fussa-gomi-josei`（環境・取込予定） |
| 狛江市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `komae-kyufu-hojo`（全般・取込予定）, `komae-genmen-josei`（環境・取込予定）, `komae-shogai-teate`（障害・取込中）, `komae-koureisha-service`（高齢者・取込中）, `komae-kosodate-jidoufukushi`（子育て・取込中）, `komae-kosodate-hitorioya`（子育て・取込中）, `komae-kosodate-shussan`（子育て・取込中）, `komae-kosodate-ninshin`（子育て・取込中）, `komae-kosodate-yochien`（子育て・取込予定） |
| 東大和市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `higashiyamato-kosodate-josei`（子育て・取込中）, `higashiyamato-koureisha-josei`（高齢者・取込中） |
| 清瀬市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `kiyose-kosodate-hojo`（子育て・取込中）, `kiyose-shogai-josei`（障害・取込中）, `kiyose-iryohi-josei`（医療・取込中）, `kiyose-sumai-hojo`（住まい・取込中）, `kiyose-jigyosha-yushi`（事業者・取込中） |
| 東久留米市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `higashikurume-kosodate-teate`（子育て・取込中）, `higashikurume-sitemap`（全般・調査中） |
| 武蔵村山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `musashimurayama-kosodate-teate`（子育て・取込中）, `musashimurayama-koureisha-josei`（高齢者・取込中）, `musashimurayama-shogai-josei`（障害・取込中）, `musashimurayama-kankyo-hojo`（環境・取込中） |
| 多摩市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tama-kosodate-teate`（子育て・取込中） |
| 稲城市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `inagi-kosodate-teate`（子育て・取込中）, `inagi-shogai-josei`（障害・取込中） |
| 羽村市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `hamura-kosodate-iryo`（子育て・取込中）, `hamura-kosodate-teate`（子育て・取込中）, `hamura-shogai-josei`（障害・取込中）, `hamura-kankyo-josei`（環境・取込中）, `hamura-jigyosha-josei`（事業者・取込中） |
| あきる野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `akiruno-kosodate-teate`（子育て・取込中）, `akiruno-jigyosha-yushi`（事業者・取込予定） |
| 西東京市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `nishitokyo-kosodate-teate`（子育て・取込中）, `nishitokyo-shogai-teate`（障害・取込中）, `nishitokyo-jigyosha-yushi`（事業者・取込中） |
| 瑞穂町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `mizuho-koureisha-josei`（高齢者・取込中）, `mizuho-shogai-josei`（障害・取込中）, `mizuho-kosodate-teate`（子育て・取込中）, `mizuho-jutaku-josei`（住まい・取込中）, `mizuho-sitemap`（全般・調査中） |
| 日の出町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `hinode-hojo`（全般・取込予定）, `hinode-kosodate-josei`（子育て・取込中）, `hinode-koureisha-josei`（高齢者・取込中）, `hinode-hojokin`（全般・取込中） |
| 檜原村 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `hinohara-hojo-ichiran`（全般・取込中）, `hinohara-hojo`（全般・取込予定） |
| 奥多摩町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `okutama-sitemap`（全般・調査中）, `okutama-kosodate-teate`（子育て・取込中）, `okutama-koureisha-shien`（高齢者・取込中） |
| 大島町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `oshima-kosodate`（子育て・取込中）, `oshima-jigyosha-josei`（事業者・取込予定） |
| 利島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `toshima-mura-fukushi`（健康・福祉・取込中）, `toshima-mura-shussan`（子育て・取込中） |
| 新島村 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `niijima-hojo`（全般・取込予定）, `niijima-jidou-hitorioya`（子育て・取込中）, `niijima-shougaisha`（障害・取込予定）, `niijima-iryoukyuufu`（健康・医療・取込中） |
| 神津島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `kouzushima-sitemap`（全般・調査中）, `kouzushima-kodomo-iryohi`（子育て・取込中）, `kouzushima-namagomi-hojo`（環境・取込中）, `kouzushima-shogakukin`（子育て・取込中）, `kouzushima-teiju`（住まい・取込中）, `kouzushima-tokusanhin-hojo`（事業者・取込中） |
| 三宅村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `miyake-iryo-josei`（医療・取込予定）, `miyake-shogaisha`（障害・取込中） |
| 御蔵島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `mikurasima-jigyosha-hojo`（事業者・取込中）, `mikurasima-heli-josei`（交通・取込中）, `mikurasima-manabi-hojo`（地域活動・取込中）, `mikurasima-kigyou-shien`（事業者・取込中） |
| 八丈町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `hachijo-kosodate-josei`（子育て・取込中）, `hachijo-seikatsu-shien`（生活支援・取込中）, `hachijo-josei-shien`（事業者・取込中）, `hachijo-sitemap`（全般・調査中） |
| 青ヶ島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `aogashima-site`（全般・対象外） |
| 小笠原村 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `ogasawara-sitemap`（全般・調査中）, `ogasawara-iryohi-josei`（子育て・対象外）, `ogasawara-sonmin`（全般・取込中） |
| 横浜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 相模原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 横須賀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平塚市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鎌倉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 藤沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小田原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 茅ヶ崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 逗子市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三浦市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 秦野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 厚木市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大和市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊勢原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 海老名市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 座間市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南足柄市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 綾瀬市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 葉山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 寒川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大磯町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 二宮町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中井町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大井町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 開成町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 箱根町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 真鶴町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湯河原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 愛川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 清川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
