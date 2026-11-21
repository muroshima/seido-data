# カバー状況

`uv run seido registry coverage` で生成する。手で編集しない。

- ○: 取込中・取込予定の取得元があり、制度全般を扱う
- ◐: 取込中・取込予定の取得元はあるが、分野が限られる（子育てだけ、など）
- △: 取得元は見つかっているが、調査中・要利用申請・対象外のみ
- −: 取得元が見つかっていない

| 区分 | 団体数 | ○ | ◐ | △ | − |
|---|---:|---:|---:|---:|---:|
| 国 | 26 | 0 | 2 | 24 | 0 |
| 都道府県 | 13 | 4 | 3 | 6 | 0 |
| 市区町村 | 514 | 61 | 252 | 201 | 0 |

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
| 茨城県 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ibaraki-pref-josei`（全般・取込中）, `ibaraki-pref-kosodate-qa`（子育て・取込予定） |
| 栃木県 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tochigi-pref-yushi-josei`（全般・取込中）, `tochigi-pref-kodomo-josei`（子育て・取込中）, `tochigi-pref-jigyosha-hojo`（事業者・取込中）, `tochigi-pref-jutaku-shien`（住まい・取込中） |
| 群馬県 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gunma-pref-hojokin`（全般・取込中）, `gunma-pref-jigyosha-hojo`（事業者・取込中）, `gunma-pref-fukushi-hojo`（健康・福祉・取込中） |
| 埼玉県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `saitama-pref-kosodate-teate`（子育て・取込中）, `saitama-pref-shogai-shien`（障害・取込中）, `saitama-pref-jigyosha-shien`（事業者・取込中）, `saitama-pref-sumai-shien`（住まい・取込予定） |
| 千葉県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chiba-pref-jigyosha-josei`（事業者・取込中）, `chiba-pref-shogai-shien`（障害・取込中） |
| 東京都 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-hojokin-search`（都の補助金・取込予定）, `tokyo-shien-navi`（全般・取込予定） |
| 神奈川県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kanagawa-pref-kankyo-hojo`（環境・取込中）, `kanagawa-pref-jigyosha-hojo`（事業者・取込予定） |
| 滋賀県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 京都府 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大阪府 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 兵庫県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奈良県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和歌山県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 水戸市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `mito-kosodate-teate`（子育て・取込予定）, `mito-shogai-teate`（障害・取込中）, `mito-koreisha-fukushi`（高齢者・取込中） |
| 日立市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hitachi-hojokin-kojin`（全般・取込中）, `hitachi-hojokin-jigyosha`（事業者・取込中）, `hitachi-kosodate-josei`（子育て・取込中） |
| 土浦市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tsuchiura-kosodate-teate`（子育て・取込中）, `tsuchiura-shogai-josei`（障害・取込中）, `tsuchiura-koreisha-kyufu`（高齢者・取込中）, `tsuchiura-jigyosha-shien`（事業者・取込中） |
| 古河市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `koga-kosodate-teate`（子育て・取込中）, `koga-koreisha-service`（高齢者・取込中）, `koga-shogai-fukushi`（障害・取込中） |
| 石岡市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ishioka-josei-teate`（全般・取込中）, `ishioka-hojokin`（全般・取込中） |
| 結城市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yuki-hojokin`（全般・取込中）, `yuki-shogai-fukushi`（障害・取込中）, `yuki-koreisha-service`（高齢者・取込中） |
| 龍ケ崎市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ryugasaki-kosodate-josei`（子育て・取込中）, `ryugasaki-koreisha-service`（高齢者・取込中）, `ryugasaki-shogai-fukushi`（障害・取込中）, `ryugasaki-jigyosha-yushi`（事業者・取込中） |
| 下妻市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shimotsuma-kosodate-teate`（子育て・取込中）, `shimotsuma-shogai-josei`（障害・取込中）, `shimotsuma-koreisha-service`（高齢者・取込中） |
| 常総市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `joso-kosodate-shien`（子育て・取込中）, `joso-koreisha-josei`（高齢者・取込中）, `joso-shogai-fukushi`（障害・取込中）, `joso-jigyosha-chusho`（事業者・取込中） |
| 常陸太田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hitachiota-kosodate-tanjo`（子育て・取込予定）, `hitachiota-koreisha-service`（高齢者・取込中） |
| 高萩市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takahagi-kosodate-teate`（子育て・取込中）, `takahagi-jigyosha-shokogyo`（事業者・取込予定） |
| 北茨城市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kitaibaraki-kosodate`（子育て・取込予定）, `kitaibaraki-fukushi-kaigo`（健康・福祉・取込予定） |
| 笠間市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kasama-kosodate-money`（子育て・取込中）, `kasama-shogai-fukushi`（障害・取込中）, `kasama-koreisha-shien`（高齢者・取込中）, `kasama-jigyosha-shogyo`（事業者・取込中） |
| 取手市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `toride-hojokin-joseikin`（全般・取込中） |
| 牛久市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ushiku-shogai-teate`（障害・取込中）, `ushiku-koreisha-shien`（高齢者・取込中）, `ushiku-kosodate`（子育て・取込中）, `ushiku-jigyosha-shien-yushi`（事業者・取込中） |
| つくば市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tsukuba-kosodate-teate`（子育て・取込中）, `tsukuba-ninshin-josei`（子育て・取込中）, `tsukuba-shogai-josei-teate`（障害・取込中）, `tsukuba-koreisha-zaitaku`（高齢者・取込中）, `tsukuba-jigyosha-hojo`（事業者・取込中） |
| ひたちなか市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hitachinaka-kosodate-josei`（子育て・取込中）, `hitachinaka-shogai-teate`（障害・取込中）, `hitachinaka-teate-josei`（全般・取込中）, `hitachinaka-jigyosha-shien`（事業者・取込中） |
| 鹿嶋市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kashima-ibaraki-fukushi-josei`（健康・福祉・取込中）, `kashima-ibaraki-kosodate-josei`（子育て・取込中）, `kashima-ibaraki-jigyosha-shien`（事業者・取込中）, `kashima-ibaraki-sumai-josei`（住まい・取込中） |
| 潮来市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `itako-shogai-josei-teate`（障害・取込中）, `itako-koreisha-fukushi`（高齢者・取込中）, `itako-kenko-josei`（健康・福祉・取込中）, `itako-hitorioya`（子育て・取込中） |
| 守谷市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `moriya-kosodate-teate`（子育て・取込中）, `moriya-shogai-teate`（障害・取込中）, `moriya-kankyo-hojo`（環境・取込中） |
| 常陸大宮市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hitachiomiya-hojokin`（全般・取込中） |
| 那珂市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `naka-hojokin`（全般・取込中）, `naka-kosodate-teate`（子育て・取込中）, `naka-shogai-teate`（障害・取込中）, `naka-koreisha-shien`（高齢者・取込中） |
| 筑西市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chikusei-ods-shien`（全般・対象外）, `chikusei-kosodate-teate`（子育て・取込中）, `chikusei-josei`（全般・取込中）, `chikusei-koreisha`（高齢者・取込中） |
| 坂東市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `bando-kosodate-teate`（子育て・取込中）, `bando-koreisha`（高齢者・取込中）, `bando-sumai-shien`（住まい・取込中） |
| 稲敷市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `inashiki-kosodate-teate`（子育て・取込中）, `inashiki-shogai-teate`（障害・取込中）, `inashiki-jigyosha-shien`（事業者・取込中） |
| かすみがうら市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kasumigaura-kosodate-ouen`（子育て・取込中）, `kasumigaura-shogai`（障害・取込中）, `kasumigaura-koreisha`（高齢者・取込中）, `kasumigaura-jigyosha-keiei`（事業者・取込中） |
| 桜川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sakuragawa-kosodate`（子育て・取込中）, `sakuragawa-shogai-keigen`（障害・取込中）, `sakuragawa-koreisha`（高齢者・取込中） |
| 神栖市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamisu-kosodate-teate`（子育て・取込中）, `kamisu-shogai-teate`（障害・取込中）, `kamisu-koreisha-seikatsu`（高齢者・取込中）, `kamisu-sumai-josei`（住まい・取込中） |
| 行方市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `namegata-kosodate-shien`（子育て・取込中）, `namegata-koreisha`（高齢者・取込予定） |
| 鉾田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hokota-kosodate-shien`（子育て・取込中）, `hokota-jigyosha-shien`（事業者・取込中） |
| つくばみらい市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tsukubamirai-kosodate-ouen`（子育て・取込中）, `tsukubamirai-kosodate-sonota`（子育て・取込中）, `tsukubamirai-shogai-shien`（障害・取込中）, `tsukubamirai-iryo-teate`（健康・福祉・取込中） |
| 小美玉市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `omitama-josei`（全般・取込中）, `omitama-kosodate-shien`（子育て・取込予定）, `omitama-koreisha`（高齢者・取込予定） |
| 茨城町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ibaraki-machi-kosodate-teate`（子育て・取込中）, `ibaraki-machi-shogai`（障害・取込中） |
| 大洗町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oarai-hojokin-joseikin`（全般・取込予定）, `oarai-shogai-josei`（障害・取込予定）, `oarai-koreisha-shien`（高齢者・取込予定） |
| 城里町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shirosato-shogai-fukushi`（障害・取込中）, `shirosato-jido-fukushi`（子育て・取込中） |
| 東海村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokai-shogai-jumin`（障害・取込中）, `tokai-koreisha-shien`（高齢者・取込中）, `tokai-kosodate`（子育て・取込中）, `tokai-jigyosha-shien`（事業者・取込中） |
| 大子町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `daigo-kosodate`（子育て・取込予定）, `daigo-shogai`（障害・取込中）, `daigo-koreisha`（高齢者・取込予定）, `daigo-shokogyo`（事業者・取込予定） |
| 美浦村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `miho-kosodate-teate-hojokin`（子育て・取込中）, `miho-shogai-fukushi`（障害・取込中） |
| 阿見町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ami-kosodate-teate-josei`（子育て・取込中）, `ami-shogai-fukushi`（障害・取込中）, `ami-koreisha-service`（高齢者・取込中） |
| 河内町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ibaraki-kawachi-shogai-fukushi`（障害・取込中）, `ibaraki-kawachi-jido-fukushi`（子育て・取込中） |
| 八千代町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ibaraki-yachiyo-kosodate-josei-teate`（子育て・取込中）, `ibaraki-yachiyo-koreisha`（高齢者・取込中）, `ibaraki-yachiyo-jigyosha-josei`（事業者・取込中）, `ibaraki-yachiyo-shogai`（障害・取込中） |
| 五霞町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `goka-shogai-shien`（障害・取込中）, `goka-ikuji-kosodate`（子育て・取込中） |
| 境町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ibaraki-sakai-kosodate-seido`（子育て・取込中）, `ibaraki-sakai-fukushi-kaigo`（高齢者・取込中）, `ibaraki-sakai-iryohi-josei`（健康・福祉・取込中）, `ibaraki-sakai-shoreikin`（住まい・取込中） |
| 利根町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tone-ibaraki-shogai-fukushi`（障害・取込中）, `tone-ibaraki-koreisha`（高齢者・取込予定）, `tone-ibaraki-jido-fukushi`（子育て・取込中） |
| 宇都宮市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `utsunomiya-shogai-teate`（障害・取込中）, `utsunomiya-koureisha-service`（高齢者・取込中）, `utsunomiya-kosodate-shien`（子育て・取込中） |
| 足利市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ashikaga-kodomo-josei`（子育て・取込中）, `ashikaga-shogai-seido`（障害・取込中）, `ashikaga-koureisha-service`（高齢者・取込中）, `ashikaga-jigyosha-hojo`（事業者・取込中） |
| 栃木市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tochigi-city-kosodate-teate`（子育て・取込中）, `tochigi-city-shogai`（障害・取込中）, `tochigi-city-koureisha`（高齢者・取込中）, `tochigi-city-jigyosha-shien`（事業者・取込中） |
| 佐野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sano-kosodate-shussan`（子育て・取込中）, `sano-iryohi-josei`（健康・福祉・取込中）, `sano-shogai`（障害・取込中）, `sano-koureisha`（高齢者・取込中）, `sano-jigyosha-shien`（事業者・取込中） |
| 鹿沼市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kanuma-hojokin-library`（全般・取込中）, `kanuma-shogai-teate`（障害・取込中）, `kanuma-koureisha-zaitaku`（高齢者・取込中）, `kanuma-kosodate-shien`（子育て・取込中） |
| 日光市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nikko-kosodate-okane`（子育て・取込中）, `nikko-shogai-okane`（障害・取込中）, `nikko-jigyosha-hojo`（事業者・取込中） |
| 小山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oyama-kosodate-josei`（子育て・取込中）, `oyama-kosodate-teate`（子育て・取込中）, `oyama-shogai-teate`（障害・取込中）, `oyama-koureisha-zaitaku`（高齢者・取込中）, `oyama-sumai`（住まい・取込予定） |
| 真岡市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `moka-kosodate-teate`（子育て・取込中）, `moka-shogai-support`（障害・取込中）, `moka-koureisha-hojo`（高齢者・取込中）, `moka-jigyosha-hojo`（事業者・取込中） |
| 大田原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ohtawara-kodomo-shien`（子育て・取込予定）, `ohtawara-fukushi`（障害・取込予定） |
| 矢板市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yaita-hojo-josei`（全般・取込中）, `yaita-kosodate-teate`（子育て・取込中） |
| 那須塩原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nasushiobara-jido-teate`（子育て・取込中）, `nasushiobara-iryohi-josei`（健康・福祉・取込中）, `nasushiobara-shogai`（障害・取込中）, `nasushiobara-koureisha-service`（高齢者・取込中）, `nasushiobara-jigyosha-shien`（事業者・取込中） |
| さくら市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sakura-kodomo-josei`（子育て・取込中）, `sakura-shogai-teate`（障害・取込中）, `sakura-koureisha-zaitaku`（高齢者・取込中）, `sakura-jigyosha-hojo`（事業者・取込中） |
| 那須烏山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nasukarasuyama-shogai`（障害・取込中）, `nasukarasuyama-koureisha`（高齢者・取込中） |
| 下野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shimotsuke-kosodate-kinsen`（子育て・取込中）, `shimotsuke-shogai-teate`（障害・取込予定）, `shimotsuke-koureisha-support`（高齢者・取込中）, `shimotsuke-shogyo`（事業者・取込中） |
| 上三川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kaminokawa-kosodate-josei`（子育て・取込中）, `kaminokawa-kosodate-teate`（子育て・取込中）, `kaminokawa-shogai-teate`（障害・取込中） |
| 益子町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `mashiko-hojo-josei`（全般・取込中）, `mashiko-shogai`（障害・取込中）, `mashiko-koureisha`（高齢者・取込中） |
| 茂木町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `motegi-kosodate-shien`（子育て・取込予定）, `motegi-koureisha`（高齢者・取込予定） |
| 市貝町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ichikai-kosodate`（子育て・取込中）, `ichikai-fukushi-kaigo`（高齢者・取込中） |
| 芳賀町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `haga-kosodate`（子育て・取込予定）, `haga-koureisha-seikatsushien`（高齢者・取込中）, `haga-shogai`（障害・取込中） |
| 壬生町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `mibu-kosodate-josei`（子育て・取込中）, `mibu-fukushi-josei`（健康・福祉・取込予定） |
| 野木町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nogi-kosodate-josei`（子育て・取込中）, `nogi-shogai`（障害・取込中）, `nogi-koureisha`（高齢者・取込中） |
| 塩谷町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shioya-kosodate`（子育て・取込予定）, `shioya-fukushi-kaigo`（健康・福祉・取込中） |
| 高根沢町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takanezawa-kosodate-teate`（子育て・取込中）, `takanezawa-koureisha-service`（高齢者・取込中）, `takanezawa-shogai`（障害・取込中）, `takanezawa-jigyosha-shien`（事業者・取込中） |
| 那須町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nasu-kosodate-shien`（子育て・取込中）, `nasu-shogai-teate`（障害・取込中）, `nasu-koureisha-zaitaku`（高齢者・取込中） |
| 那珂川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nakagawa-kosodate`（子育て・取込中）, `nakagawa-shogai`（障害・取込予定） |
| 前橋市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `maebashi-kosodate-hojo`（子育て・取込中）, `maebashi-ninshin-hojo`（子育て・取込中）, `maebashi-shogai-seikatsu`（障害・取込中）, `maebashi-koureisha-fukushi`（高齢者・取込中）, `maebashi-jigyosha-hojo`（事業者・取込中） |
| 高崎市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takasaki-kosodate-shien`（子育て・取込中）, `takasaki-shogai-seido`（障害・取込中）, `takasaki-iryo-josei`（健康・福祉・取込中）, `takasaki-jigyosha-hojo`（事業者・取込中） |
| 桐生市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kiryu-hojokin`（全般・取込中）, `kiryu-kosodate-teate`（子育て・取込中）, `kiryu-shogai-service`（障害・取込中）, `kiryu-koureisha-fukushi`（高齢者・取込中）, `kiryu-jigyosha-hojo`（事業者・取込中） |
| 伊勢崎市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `isesaki-kosodate-teate`（子育て・取込中）, `isesaki-shogai-service`（障害・取込中）, `isesaki-koureisha-support`（高齢者・取込中）, `isesaki-jigyosha-hojo`（事業者・取込中） |
| 太田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gunma-ota-kosodate-kyufu`（子育て・取込中）, `gunma-ota-shogai`（障害・取込中）, `gunma-ota-koureisha`（高齢者・取込中）, `gunma-ota-jigyosha`（事業者・取込中） |
| 沼田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `numata-kosodate-teate`（子育て・取込中）, `numata-koureisha-zaitaku`（高齢者・取込中）, `numata-shogai-service`（障害・取込中）, `numata-jigyosha-yushi`（事業者・取込中） |
| 館林市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tatebayashi-kosodate-teate`（子育て・取込中）, `tatebayashi-shogai-fukushi`（障害・取込中）, `tatebayashi-koureisha`（高齢者・取込中）, `tatebayashi-jigyosha-hojo`（事業者・取込中） |
| 渋川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shibukawa-hitorioya-shien`（子育て・取込中）, `shibukawa-shogai-seido`（障害・取込中）, `shibukawa-koureisha-zaitaku`（高齢者・取込中）, `shibukawa-jigyosha-shien`（事業者・取込中） |
| 藤岡市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `fujioka-hojokin`（全般・取込中）, `fujioka-kosodate-teate`（子育て・取込中）, `fujioka-shogai-seido`（障害・取込中） |
| 富岡市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tomioka-hojokin`（全般・取込予定） |
| 安中市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `annaka-kosodate-shien`（子育て・取込中）, `annaka-hitorioya`（子育て・取込中）, `annaka-shogai`（障害・取込予定）, `annaka-koureisha`（高齢者・取込中）, `annaka-jigyosha`（事業者・取込中） |
| みどり市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `midori-kosodate-teate`（子育て・取込中）, `midori-koureisha-fukushi`（高齢者・取込中）, `midori-shogai-fukushi`（障害・取込中）, `midori-jigyosha-shien`（事業者・取込中） |
| 榛東村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shinto-kosodate-jidofukushi`（子育て・取込中）, `shinto-koureisha-fukushi`（高齢者・取込中） |
| 吉岡町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yoshioka-kosodate`（子育て・取込中）, `yoshioka-shogai-fukushi`（障害・取込中） |
| 上野村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `uenomura-kosodate-teate`（子育て・取込予定）, `uenomura-koureisha-fukushi`（高齢者・取込中）, `uenomura-shogai-fukushi`（障害・取込中） |
| 神流町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kanna-kosodate-hitorioya`（子育て・取込中） |
| 下仁田町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shimonita-fukushi`（健康・福祉・取込中）, `shimonita-koureisha`（高齢者・取込中） |
| 南牧村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nanmoku-kenko-fukushi`（健康・福祉・取込予定） |
| 甘楽町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kanra-kosodate`（子育て・取込中）, `kanra-kaigo-fukushi`（健康・福祉・取込中） |
| 中之条町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nakanojo-josei-shien`（全般・取込中）, `nakanojo-kosodate-teate`（子育て・取込中）, `nakanojo-koureisha`（高齢者・取込中） |
| 長野原町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `naganohara-kurashi-shienkin`（全般・取込予定）, `naganohara-koureisha`（高齢者・取込中）, `naganohara-shogai`（障害・取込中） |
| 嬬恋村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tsumagoi-kenko-fukushi`（健康・福祉・取込中） |
| 草津町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kusatsu-todokede`（全般・取込予定） |
| 高山村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gunma-takayama-fukushi`（健康・福祉・取込中）, `gunma-takayama-kosodate`（子育て・取込予定） |
| 東吾妻町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `higashiagatsuma-fukushi-kaigo`（健康・福祉・取込予定）, `higashiagatsuma-kodomo`（子育て・取込予定）, `higashiagatsuma-jutaku`（住まい・取込予定） |
| 片品村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `katashina-shussan-ikuji`（子育て・取込中）, `katashina-hoken-fukushi`（健康・福祉・取込中） |
| 川場村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawaba-kosodate`（子育て・取込中）, `kawaba-fukushi`（健康・福祉・取込中） |
| 昭和村 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gunma-showa-hojokin`（全般・取込中）, `gunma-showa-josei`（健康・福祉・取込中） |
| みなかみ町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `minakami-kosodate-shien`（子育て・取込中）, `minakami-shakai-fukushi`（障害・取込中）, `minakami-hojokin-shien`（事業者・取込中） |
| 玉村町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tamamura-kosodate-shien`（子育て・取込中）, `tamamura-koureisha`（高齢者・取込中）, `tamamura-shogai`（障害・取込予定） |
| 板倉町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `itakura-kosodate-teate`（子育て・取込中）, `itakura-koureisha-kaigo`（高齢者・取込中） |
| 明和町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `meiwa-kosodate-mokuteki`（子育て・取込予定）, `meiwa-shogai-fukushi`（障害・取込中） |
| 千代田町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gunma-chiyoda-hojo-josei`（全般・取込中） |
| 大泉町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oizumi-kosodate-teate`（子育て・取込中）, `oizumi-shogai-fukushi`（障害・取込中）, `oizumi-koureisha-fukushi`（高齢者・取込中）, `oizumi-jigyosha-yushi`（事業者・取込中） |
| 邑楽町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ora-jido-teate`（子育て・取込中）, `ora-shogai-fukushi`（障害・取込中）, `ora-koureisha-fukushi`（高齢者・取込予定）, `ora-sangyo-kigyo`（事業者・取込予定） |
| さいたま市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `saitama-shi-kosodate-teate`（子育て・取込中）, `saitama-shi-shogai-teate`（障害・取込中）, `saitama-shi-shogai-seikatsu`（障害・取込中）, `saitama-shi-hitorioya`（子育て・取込中）, `saitama-shi-jigyosha-hojo`（事業者・取込中） |
| 川越市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawagoe-kosodate-teate`（子育て・取込中）, `kawagoe-shogai`（障害・取込予定）, `kawagoe-koreisha`（高齢者・取込中）, `kawagoe-jigyosha-hojo`（事業者・取込中） |
| 熊谷市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kumagaya-ods-shien`（全般・取込中）, `kumagaya-kosodate-josei`（子育て・取込中）, `kumagaya-koreisha-josei`（高齢者・取込中）, `kumagaya-shogai-josei`（障害・取込中）, `kumagaya-jigyosha-josei`（事業者・取込中）, `kumagaya-sumai-josei`（住まい・取込中） |
| 川口市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawaguchi-kosodate-teate`（子育て・取込中）, `kawaguchi-shogai-seikatsu`（障害・取込中）, `kawaguchi-jigyosha-keiei`（事業者・取込中） |
| 行田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gyoda-kosodate-teate`（子育て・取込中）, `gyoda-shogai-support`（障害・取込中）, `gyoda-koreisha-support`（高齢者・取込中）, `gyoda-sumai-hojo`（住まい・取込中）, `gyoda-jigyosha-shien`（事業者・取込中） |
| 秩父市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chichibu-kosodate-teate`（子育て・取込予定）, `chichibu-shogai`（障害・取込予定） |
| 所沢市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokorozawa-hojo-kyufu`（全般・取込中）, `tokorozawa-kosodate-teate`（子育て・取込中）, `tokorozawa-shogai-teate`（障害・取込中）, `tokorozawa-koreisha-teate`（高齢者・取込中） |
| 飯能市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hanno-hojokin`（全般・取込中）, `hanno-kosodate-teate`（子育て・取込中）, `hanno-shogai-teate`（障害・取込中）, `hanno-shogai-seikatsu`（障害・取込中）, `hanno-koreisha`（高齢者・取込予定） |
| 加須市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kazo-kosodate-teate`（子育て・取込中）, `kazo-shogai-teate`（障害・取込中）, `kazo-koreisha-seikatsu`（高齢者・取込中）, `kazo-jigyosha-hojo`（事業者・取込中） |
| 本庄市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `honjo-kosodate-teate`（子育て・取込中）, `honjo-koreisha`（高齢者・取込中）, `honjo-shogai`（障害・取込中） |
| 東松山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `higashimatsuyama-kosodate-shien`（子育て・取込予定）, `higashimatsuyama-shogai`（障害・取込中）, `higashimatsuyama-korei`（高齢者・取込中）, `higashimatsuyama-sumai-shien`（住まい・取込中）, `higashimatsuyama-jigyosha`（事業者・取込中） |
| 春日部市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kasukabe-ods-shien`（全般・取込中）, `kasukabe-kosodate-teate`（子育て・取込中）, `kasukabe-shogai`（障害・取込中）, `kasukabe-korei-seikatsu`（高齢者・取込中）, `kasukabe-jigyosha-keiei`（事業者・取込中）, `kasukabe-sumai`（住まい・取込予定） |
| 狭山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sayama-kosodate-teate`（子育て・取込中）, `sayama-shogai-josei`（障害・取込中）, `sayama-korei-service`（高齢者・取込中）, `sayama-jigyosha-shisaku`（事業者・取込中）, `sayama-sumai-josei`（住まい・取込中）, `sayama-kankyo-josei`（環境・取込中） |
| 羽生市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hanyu-kosodate-teate`（子育て・取込予定）, `hanyu-shogai`（障害・取込予定）, `hanyu-korei`（高齢者・取込予定）, `hanyu-jigyosha-hojo`（事業者・取込中） |
| 鴻巣市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kounosu-kosodate-shien`（子育て・取込中）, `kounosu-shogai-josei`（障害・取込中）, `kounosu-jigyosha`（事業者・取込中）, `kounosu-sumai`（住まい・取込中） |
| 深谷市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `fukaya-kosodate-teate`（子育て・取込中）, `fukaya-shogai-josei`（障害・取込中）, `fukaya-korei-service`（高齢者・取込中）, `fukaya-jigyosha-shien`（事業者・取込中）, `fukaya-sumai-hojo`（住まい・取込中） |
| 上尾市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ageo-kosodate-teate`（子育て・取込中）, `ageo-shogai`（障害・取込中）, `ageo-korei`（高齢者・取込中）, `ageo-jigyosha`（事業者・取込中）, `ageo-hojo`（住まい・取込中） |
| 草加市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `soka-kosodate-teate`（子育て・取込中）, `soka-shogai-josei`（障害・取込中）, `soka-shogai-shien`（障害・取込中）, `soka-korei-zaitaku`（高齢者・取込中）, `soka-jigyosha-yushi`（事業者・取込中）, `soka-sumai`（住まい・取込予定） |
| 越谷市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `koshigaya-shogai-josei`（障害・取込中）, `koshigaya-shogai-nichijo`（障害・取込中）, `koshigaya-korei-zaitaku`（高齢者・取込中）, `koshigaya-jigyosha-hojo`（事業者・取込中）, `koshigaya-jigyosha-yushi`（事業者・取込中）, `koshigaya-sumai`（住まい・取込中） |
| 蕨市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `warabi-kosodate-teate`（子育て・取込中）, `warabi-hitorioya`（子育て・取込中）, `warabi-shogai`（障害・取込中）, `warabi-korei-service`（高齢者・取込中）, `warabi-korei-teate`（高齢者・取込中）, `warabi-jigyosha-yushi`（事業者・取込中） |
| 戸田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `toda-kosodate-teate`（子育て・取込中）, `toda-shogai-teate`（障害・取込中）, `toda-korei-fukushi`（高齢者・取込中）, `toda-sumai-hojo`（住まい・取込中） |
| 入間市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `iruma-ods-shien`（全般・取込中）, `iruma-kosodate-teate`（子育て・取込中）, `iruma-shogai-shien`（障害・取込中）, `iruma-korei-shien`（高齢者・取込中） |
| 朝霞市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `asaka-iryohi-josei`（健康・福祉・取込中）, `asaka-kosodate-shien`（子育て・取込中）, `asaka-shogai`（障害・取込中）, `asaka-korei`（高齢者・取込中）, `asaka-jigyosha-hojo`（事業者・取込中） |
| 志木市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shiki-kosodate-josei`（子育て・取込中）, `shiki-fukushi-josei`（健康・福祉・取込中）, `shiki-jigyosha-shien`（事業者・取込中）, `shiki-sumai-hojo`（住まい・取込中） |
| 和光市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `wako-ods-shien`（全般・取込中）, `wako-kosodate-josei`（子育て・取込中）, `wako-shogai-teate`（障害・取込中）, `wako-korei-shien`（高齢者・取込中）, `wako-jigyosha-shien`（事業者・取込中） |
| 新座市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `niiza-kosodate-teate`（子育て・取込中）, `niiza-shogai`（障害・取込予定）, `niiza-jigyosha-shien`（事業者・取込中）, `niiza-sumai`（住まい・取込中） |
| 桶川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `okegawa-kosodate-teate`（子育て・取込中）, `okegawa-shogai-josei`（障害・取込中）, `okegawa-korei-fukushi`（高齢者・取込中）, `okegawa-iryo-josei`（健康・福祉・取込中）, `okegawa-jigyosha-shien`（事業者・取込中） |
| 久喜市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kuki-kosodate-teate`（子育て・取込中）, `kuki-shogai-service`（障害・取込中）, `kuki-shogai-teate`（障害・取込中）, `kuki-korei-fukushi`（高齢者・取込中）, `kuki-jigyosha-shien`（事業者・取込予定） |
| 北本市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kitamoto-kosodate-teate`（子育て・取込中）, `kitamoto-shogai-teate`（障害・取込中）, `kitamoto-sumai-hojo`（住まい・取込中）, `kitamoto-kurashi-hojo`（環境・取込中）, `kitamoto-jigyosha-hojo`（事業者・取込中） |
| 八潮市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yashio-kosodate-teate`（子育て・取込中）, `yashio-shogai-iryo-teate`（障害・取込中）, `yashio-shogai-shien`（障害・取込予定）, `yashio-jigyosha-josei`（事業者・取込中） |
| 富士見市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `fujimi-saitama-kosodate-teate`（子育て・取込中）, `fujimi-saitama-shogai-nichijo`（障害・取込中）, `fujimi-saitama-korei-service`（高齢者・取込中）, `fujimi-saitama-jigyosha-shien`（事業者・取込中） |
| 三郷市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `misato-kosodate-josei`（子育て・取込中）, `misato-koreisha-josei`（高齢者・取込中）, `misato-shogai-josei`（障害・取込中）, `misato-sumai-hojo`（住まい・取込中）, `misato-jigyosha-hojo`（事業者・取込中） |
| 蓮田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hasuda-kosodate-teate`（子育て・取込中）, `hasuda-koreisha-teate`（高齢者・取込中）, `hasuda-shogai-fukushi`（障害・取込中）, `hasuda-kankyo-hojo`（環境・取込中） |
| 坂戸市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sakado-josei-teate`（全般・取込中） |
| 幸手市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `satte-kosodate-teate`（子育て・取込中）, `satte-shogai-teate`（障害・取込中）, `satte-kaigo-josei`（高齢者・取込中）, `satte-jigyosha-shien`（事業者・取込中） |
| 鶴ヶ島市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tsurugashima-kosodate-teate`（子育て・取込中）, `tsurugashima-shogai-teate`（障害・取込中）, `tsurugashima-koreisha-fukushi`（高齢者・取込中）, `tsurugashima-sumai-jutaku`（住まい・取込予定） |
| 日高市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hidaka-kosodate-teate`（子育て・取込中）, `hidaka-shogai-kyufu`（障害・取込中）, `hidaka-shogai-teate`（障害・取込中）, `hidaka-jigyosha`（事業者・取込中） |
| 吉川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yoshikawa-kosodate-teate`（子育て・取込中）, `yoshikawa-shogai-iryohi`（障害・取込中）, `yoshikawa-koreisha-josei`（高齢者・取込中）, `yoshikawa-jigyosha-hojo`（事業者・取込中）, `yoshikawa-sumai-taishin`（住まい・取込予定） |
| ふじみ野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `fujimino-kosodate-teate`（子育て・取込中）, `fujimino-shogai-fukushi`（障害・取込中）, `fujimino-koreisha-service`（高齢者・取込中）, `fujimino-jigyosha-chusho`（事業者・取込中）, `fujimino-jigyosha-sangyo`（事業者・取込中） |
| 白岡市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shiraoka-kosodate-teate`（子育て・取込中）, `shiraoka-shogai-fukushi`（障害・取込予定）, `shiraoka-koreisha-fukushi`（高齢者・取込中）, `shiraoka-jigyosha-josei`（事業者・取込中） |
| 伊奈町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `saitama-ina-kosodate-teate`（子育て・取込中）, `saitama-ina-shogai-fukushi`（障害・取込中） |
| 三芳町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `miyoshi-kosodate-teate`（子育て・取込中）, `miyoshi-shogai`（障害・取込中）, `miyoshi-koureisha`（高齢者・取込中） |
| 毛呂山町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `moroyama-kosodate-okane`（子育て・取込中）, `moroyama-shogai-fukushi`（障害・取込中）, `moroyama-iryo-josei`（健康・福祉・取込中） |
| 越生町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ogose-kosodate-teate`（子育て・取込中）, `ogose-shogai-fukushi`（障害・取込中）, `ogose-korei-fukushi`（高齢者・取込中） |
| 滑川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `namegawa-kosodate-jidofukushi`（子育て・取込中）, `namegawa-shogai-teate`（障害・取込中）, `namegawa-koreisha-support`（高齢者・取込予定） |
| 嵐山町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ranzan-kosodate-teate`（子育て・取込中）, `ranzan-korei-fukushi`（高齢者・取込中）, `ranzan-shogai-fukushi`（障害・取込予定） |
| 小川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ogawa-shogai-fukushi`（障害・取込中）, `ogawa-kosodate-support`（子育て・取込中）, `ogawa-korei-fukushi`（高齢者・取込中）, `ogawa-iryo-josei`（健康・福祉・取込中） |
| 川島町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawajima-kosodate-kinsenteki-shien`（子育て・取込予定）, `kawajima-shogai-shien`（障害・取込予定）, `kawajima-korei-kaigo`（高齢者・取込予定） |
| 吉見町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yoshimi-kosodate-teate`（子育て・取込中）, `yoshimi-korei-fukushi`（高齢者・取込中）, `yoshimi-shogai-fukushi`（障害・取込中） |
| 鳩山町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hatoyama-kosodate-keizaiteki-shien`（子育て・取込中）, `hatoyama-shogai-shien`（障害・取込中）, `hatoyama-koreisha`（高齢者・取込予定）, `hatoyama-sumai-hojo`（住まい・取込中） |
| ときがわ町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokigawa-shogai`（障害・取込中）, `tokigawa-jutaku`（住まい・取込予定） |
| 横瀬町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yokoze-teate-josei`（全般・取込中）, `yokoze-kodomo-teate`（子育て・取込予定）, `yokoze-shogai`（障害・取込中） |
| 皆野町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `minano-josei-teate`（全般・取込予定） |
| 長瀞町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nagatoro-kurashi`（全般・取込中） |
| 小鹿野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東秩父村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `higashichichibu-fukushi-kosodate`（健康・福祉・取込中） |
| 美里町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `misatomachi-kosodate-josei`（子育て・取込中）, `misatomachi-shogai`（障害・取込中）, `misatomachi-kenko-josei`（健康・福祉・取込中）, `misatomachi-kankyo`（環境・取込予定） |
| 神川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamikawa-chominfukushi-josei`（子育て・取込中）, `kamikawa-bosaikankyou-josei`（住まい・取込中）, `kamikawa-keizaikan-josei`（事業者・取込中）, `kamikawa-hokenkenko-josei`（高齢者・取込中） |
| 上里町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamisato-kosodate-josei`（子育て・取込予定） |
| 寄居町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yorii-josei`（全般・取込中） |
| 宮代町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `miyashiro-kosodate-teate`（子育て・取込中）, `miyashiro-shogai-hojo`（障害・取込中）, `miyashiro-koreisha`（高齢者・取込中）, `miyashiro-jigyosha`（事業者・取込中） |
| 杉戸町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sugito-kosodate-josei`（子育て・取込中）, `sugito-fukushi-josei`（健康・福祉・取込中） |
| 松伏町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `matsubushi-kosodate-teate`（子育て・取込中）, `matsubushi-koreisha-fukushi`（高齢者・取込中）, `matsubushi-shogai-service`（障害・取込中） |
| 千葉市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chiba-city-kosodate-josei`（子育て・取込中）, `chiba-city-shogai-josei`（障害・取込中）, `chiba-city-korei-josei`（高齢者・取込中）, `chiba-city-jigyosha-shien`（事業者・取込中） |
| 銚子市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `choshi-hojo-josei`（全般・取込中）, `choshi-kosodate-teate`（子育て・取込中）, `choshi-shogai-fukushi`（障害・取込中） |
| 市川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ichikawa-kosodate-josei`（子育て・取込中）, `ichikawa-shogai-josei`（障害・取込中）, `ichikawa-korei-josei`（高齢者・取込中）, `ichikawa-jigyosha-josei`（事業者・取込中） |
| 船橋市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `funabashi-kosodate-teate`（子育て・取込中）, `funabashi-shogai-teate`（障害・取込中）, `funabashi-shogai-kotsu`（障害・取込中）, `funabashi-jigyosha-hojo`（事業者・取込中） |
| 館山市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tateyama-hojokin`（全般・取込中）, `tateyama-kosodate-teate`（子育て・取込中）, `tateyama-shogai-shien`（障害・取込中） |
| 木更津市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kisarazu-kosodate-teate`（子育て・取込中）, `kisarazu-shogai-josei`（障害・取込中） |
| 松戸市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `matsudo-josei-teate`（全般・取込中）, `matsudo-kosodate-teate`（子育て・取込中）, `matsudo-shogai-teate`（障害・取込中） |
| 野田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `noda-kosodate-teate`（子育て・取込中）, `noda-shogai-josei`（障害・取込中）, `noda-korei-service`（高齢者・取込中） |
| 茂原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `mobara-kosodate-teate`（子育て・取込中）, `mobara-shogai-teate`（障害・取込中）, `mobara-shogai-seikatsu`（障害・取込中）, `mobara-korei-service`（高齢者・取込中） |
| 成田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `narita-kosodate-josei`（子育て・取込中）, `narita-shogai-josei`（障害・取込中）, `narita-shogai-teate`（障害・取込中）, `narita-korei-josei`（高齢者・取込中）, `narita-jigyosha`（事業者・取込中） |
| 佐倉市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sakura-kosodate-teate`（子育て・取込中）, `sakura-shogai-okane`（障害・取込中）, `sakura-shogai-seikatsu`（障害・取込中） |
| 東金市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `togane-kosodate-teate`（子育て・取込中）, `togane-shogai-teate`（障害・取込中）, `togane-shogai-seikatsu`（障害・取込中）, `togane-korei-service`（高齢者・取込中）, `togane-jigyosha-shien`（事業者・取込中） |
| 旭市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `asahi-chiba-fukushi`（健康・福祉・取込中）, `asahi-chiba-kosodate-shien`（子育て・取込中） |
| 習志野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `narashino-kosodate-teate`（子育て・取込中）, `narashino-shogai-seido`（障害・取込中）, `narashino-korei-teate`（高齢者・取込中） |
| 柏市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kashiwa-kosodate-teate`（子育て・取込中）, `kashiwa-shogai-teate`（障害・取込中）, `kashiwa-shogai-josei`（障害・取込中）, `kashiwa-korei-nichijo`（高齢者・取込中） |
| 勝浦市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `katsuura-chiba-shogai`（障害・取込中）, `katsuura-chiba-korei`（高齢者・取込中）, `katsuura-chiba-kosodate`（子育て・取込中） |
| 市原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 流山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nagareyama-kosodate-teate`（子育て・取込中）, `nagareyama-shogai-service`（障害・取込中）, `nagareyama-korei`（高齢者・取込中） |
| 八千代市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yachiyo-fukushi-josei`（健康・福祉・取込中）, `yachiyo-kosodate-josei`（子育て・取込中）, `yachiyo-jigyosha-josei`（事業者・取込中） |
| 我孫子市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `abiko-kosodate-josei`（子育て・取込中）, `abiko-shogai-josei`（障害・取込中）, `abiko-sumai-josei`（住まい・取込中）, `abiko-korei-seikatsu`（高齢者・取込予定） |
| 鴨川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamogawa-chiba-kosodate-josei`（子育て・取込中）, `kamogawa-chiba-shogai`（障害・取込中）, `kamogawa-chiba-korei`（高齢者・取込予定） |
| 鎌ケ谷市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamagaya-kosodate-teate`（子育て・取込中）, `kamagaya-shogai-teate`（障害・取込中）, `kamagaya-shogai-seikatsu`（障害・取込中）, `kamagaya-korei-teate`（高齢者・取込中） |
| 君津市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kimitsu-kosodate-teate`（子育て・取込中）, `kimitsu-shogai`（障害・取込中）, `kimitsu-korei`（高齢者・取込予定）, `kimitsu-jigyosha-shien`（事業者・取込予定） |
| 富津市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `futtsu-kosodate-teate`（子育て・取込中）, `futtsu-shogai`（障害・取込中）, `futtsu-kurashi-hojo`（全般・取込中）, `futtsu-jigyosha-hojo`（事業者・取込中） |
| 浦安市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `urayasu-kosodate-teate`（子育て・取込中）, `urayasu-shogai-teate`（障害・取込中）, `urayasu-shogai-enjo`（障害・取込中）, `urayasu-korei-josei`（高齢者・取込中） |
| 四街道市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yotsukaido-kosodate-teate`（子育て・取込中）, `yotsukaido-shogai-teate`（障害・取込中）, `yotsukaido-shogai-nichijo`（障害・取込中）, `yotsukaido-korei-service`（高齢者・取込中） |
| 袖ケ浦市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sodegaura-kosodate-shien`（子育て・取込中）, `sodegaura-shogai`（障害・取込中）, `sodegaura-korei-josei`（高齢者・取込中）, `sodegaura-iryohi-josei`（健康・福祉・取込中） |
| 八街市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yachimata-kosodate-josei`（子育て・取込中）, `yachimata-fukushi-josei`（健康・福祉・取込中）, `yachimata-jigyosha-shien`（事業者・取込中）, `yachimata-sumai-hojo`（住まい・取込中） |
| 印西市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `inzai-kosodate-hitorioya`（子育て・取込中）, `inzai-kosodate-shien`（子育て・取込中）, `inzai-shogai-teate`（障害・取込中）, `inzai-shogai-josei`（障害・取込中）, `inzai-koreisha-service`（高齢者・取込中）, `inzai-jigyosha-shien`（事業者・取込中）, `inzai-sumai-hojo`（住まい・取込中） |
| 白井市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shiroi-kosodate-shien`（子育て・取込中）, `shiroi-kosodate-hitorioya`（子育て・取込中）, `shiroi-shogai-josei`（障害・取込中）, `shiroi-koreisha-seikatsu`（高齢者・取込中）, `shiroi-jigyosha-josei`（事業者・取込中）, `shiroi-sumai-josei`（住まい・取込中） |
| 富里市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tomisato-hojokin`（全般・取込中）, `tomisato-shogai-teate`（障害・取込中）, `tomisato-koreisha-seikatsu`（高齢者・取込中） |
| 南房総市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `minamiboso-kosodate-hojo`（子育て・取込中）, `minamiboso-kosodate-hitorioya`（子育て・取込中）, `minamiboso-shogai-kotsu`（障害・取込中）, `minamiboso-koreisha-service`（高齢者・取込中）, `minamiboso-jigyosha-shien`（事業者・取込中）, `minamiboso-sumai-jutaku`（住まい・取込中）, `minamiboso-iju`（住まい・取込中） |
| 匝瑳市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sosa-kosodate-teate`（子育て・取込中）, `sosa-shogai-fukushi`（障害・取込中）, `sosa-koreisha-fukushi`（高齢者・取込中）, `sosa-jigyosha-shoko`（事業者・取込中） |
| 香取市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `katori-kosodate-teate`（子育て・取込中）, `katori-shogai-fukushi`（障害・取込中）, `katori-koreisha-fukushi`（高齢者・取込予定）, `katori-jigyosha-shoko`（事業者・取込中） |
| 山武市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sammu-hojokin`（全般・取込中）, `sammu-kosodate-teate`（子育て・取込中）, `sammu-koreisha-fukushi`（高齢者・取込中） |
| いすみ市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `isumi-kosodate-josei`（子育て・取込中）, `isumi-shogai-josei`（障害・取込中）, `isumi-koreisha-fukushi`（高齢者・取込中）, `isumi-sumai`（住まい・取込中） |
| 大網白里市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oamishirasato-kosodate-teate`（子育て・取込中）, `oamishirasato-shogai-fukushi`（障害・取込中）, `oamishirasato-koreisha-fukushi`（高齢者・取込中）, `oamishirasato-jigyosha-shien`（事業者・取込中） |
| 酒々井町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shisui-kosodate-oen`（子育て・取込予定）, `shisui-sumai`（住まい・取込予定） |
| 栄町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sakae-kosodate-josei`（子育て・取込中）, `sakae-kosodate-shien`（子育て・取込中）, `sakae-fukushi`（健康・福祉・取込中）, `sakae-jigyosha-hojokin`（事業者・取込中） |
| 神崎町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kozaki-kosodate-teate`（子育て・取込中）, `kozaki-fukushi`（健康・福祉・取込中） |
| 多古町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tako-hojokin`（全般・取込予定）, `tako-fukushi`（健康・福祉・取込予定） |
| 東庄町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tohnosho-hojokin`（全般・取込中）, `tohnosho-koreisha-support`（高齢者・取込中）, `tohnosho-shogai-support`（障害・取込中）, `tohnosho-kosodate-mishugakuji`（子育て・取込予定） |
| 九十九里町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kujukuri-kosodate-shien`（子育て・取込中）, `kujukuri-shogai-fukushi`（障害・取込中）, `kujukuri-koreisha-fukushi`（高齢者・取込予定）, `kujukuri-iju-teiju`（住まい・取込中）, `kujukuri-jigyosha-shoko`（事業者・取込予定） |
| 芝山町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shibayama-hojokin`（全般・取込中）, `shibayama-kosodate`（子育て・取込中） |
| 横芝光町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yokoshibahikari-kosodate-josei`（子育て・取込中）, `yokoshibahikari-fukushi-josei`（健康・福祉・取込中）, `yokoshibahikari-seikatsu-josei`（住まい・取込中） |
| 一宮町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ichinomiya-hojokin-kosodate`（子育て・取込予定）, `ichinomiya-hojokin-iryo`（健康・福祉・取込予定） |
| 睦沢町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `mutsuzawa-teate-josei`（全般・取込中）, `mutsuzawa-kosodate-teate`（子育て・取込予定）, `mutsuzawa-kurashi-teate`（住まい・取込予定） |
| 長生村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chosei-kosodate-teate`（子育て・取込中）, `chosei-shogai-fukushi`（障害・取込中）, `chosei-koreisha-fukushi`（高齢者・取込中）, `chosei-jigyosha-shien`（事業者・取込中） |
| 白子町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shirako-kakushu-josei`（全般・取込中）, `shirako-koreisha-fukushi`（高齢者・取込予定） |
| 長柄町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nagara-hojokin`（全般・取込中） |
| 長南町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chonan-iryohi-josei`（健康・福祉・取込中）, `chonan-shogai`（障害・取込中）, `chonan-koreisha`（高齢者・取込中）, `chonan-kosodate`（子育て・取込予定） |
| 大多喜町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `otaki-kosodate-shien`（子育て・取込中）, `otaki-shogai-fukushi`（障害・取込予定）, `otaki-sumai`（住まい・取込予定）, `otaki-jigyosha-sangyou`（事業者・取込中） |
| 御宿町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鋸南町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kyonan-kosodate`（子育て・取込予定）, `kyonan-fukushi`（健康・福祉・取込中） |
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
| 横浜市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yokohama-kosodate-teate`（子育て・取込中）, `yokohama-shogai-teate`（障害・取込中）, `yokohama-koreisha-shien`（高齢者・取込中）, `yokohama-jigyosha-keiei`（事業者・取込中） |
| 川崎市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawasaki-kosodate-teate`（子育て・取込中）, `kawasaki-kosodate-iryo`（子育て・取込中）, `kawasaki-iryohi-josei`（健康・福祉・取込中）, `kawasaki-shogai-service`（障害・取込中）, `kawasaki-jigyosha-hojo`（事業者・取込中） |
| 相模原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sagamihara-kosodate-teate`（子育て・取込中）, `sagamihara-shogai-seido`（障害・取込中）, `sagamihara-koreisha-shien`（高齢者・取込中）, `sagamihara-jigyosha`（事業者・取込中） |
| 横須賀市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yokosuka-kosodate-teate`（子育て・取込中）, `yokosuka-hitorioya-shien`（子育て・取込中）, `yokosuka-shogai-fukushi`（障害・取込中）, `yokosuka-jigyosha-hojo`（事業者・取込中） |
| 平塚市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hiratsuka-kosodate-shien`（子育て・取込中）, `hiratsuka-shogai`（障害・取込中）, `hiratsuka-koreisha-shien`（高齢者・取込中）, `hiratsuka-jigyosha-hojo`（事業者・取込中） |
| 鎌倉市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamakura-kosodate-teate`（子育て・取込中）, `kamakura-shogai-fukushi`（障害・取込中）, `kamakura-koreisha`（高齢者・取込中）, `kamakura-jigyosha-hojo`（事業者・取込中）, `kamakura-kenko-josei`（健康・福祉・取込中） |
| 藤沢市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `fujisawa-kosodate-teate`（子育て・取込中）, `fujisawa-hitorioya-shien`（子育て・取込中）, `fujisawa-iryohi-josei`（健康・福祉・取込中）, `fujisawa-koreisha-seikatsu`（高齢者・取込中） |
| 小田原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `odawara-kosodate-teate`（子育て・取込中）, `odawara-shogai-teate`（障害・取込中）, `odawara-shogai-josei`（障害・取込中）, `odawara-koreisha-zaitaku`（高齢者・取込予定） |
| 茅ヶ崎市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chigasaki-kosodate-teate`（子育て・取込中）, `chigasaki-hitorioya`（子育て・取込中）, `chigasaki-shogai`（障害・取込中）, `chigasaki-jigyosha-hojo`（事業者・取込中） |
| 逗子市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `zushi-kosodate-teate`（子育て・取込中）, `zushi-shogai-fukushi`（障害・取込中）, `zushi-gomi-josei`（環境・取込中） |
| 三浦市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `miura-kosodate-jidofukushi`（子育て・取込中）, `miura-shogai-support`（障害・取込中）, `miura-jigyosha-shien`（事業者・取込中）, `miura-sumai`（住まい・取込中） |
| 秦野市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hadano-hojokin`（全般・取込中） |
| 厚木市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `atsugi-kosodate-teate`（子育て・取込中）, `atsugi-koreisha-support`（高齢者・取込中）, `atsugi-iryo-josei`（健康・福祉・取込中） |
| 大和市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yamato-shogai-teate`（障害・取込中）, `yamato-shogai-josei`（障害・取込中）, `yamato-kenko-josei`（健康・福祉・取込中）, `yamato-kankyo-hojo`（環境・取込中） |
| 伊勢原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `isehara-hitorioya-teate`（子育て・取込予定）, `isehara-shien-teate`（子育て・取込予定） |
| 海老名市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ebina-kosodate-teate`（子育て・取込中）, `ebina-hitorioya`（子育て・取込中）, `ebina-shogai`（障害・取込中）, `ebina-jigyosha-chusho`（事業者・取込中） |
| 座間市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `zama-kosodate-teate`（子育て・取込中）, `zama-shogai-josei-teate`（障害・取込中）, `zama-koreisha-service`（高齢者・取込中） |
| 南足柄市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `minamiashigara-kosodate-teate`（子育て・取込中）, `minamiashigara-shogai-josei`（障害・取込中）, `minamiashigara-shogai-teate`（障害・取込中）, `minamiashigara-jigyosha`（事業者・取込中） |
| 綾瀬市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ayase-kosodate-teate`（子育て・取込中）, `ayase-hitorioya`（子育て・取込中）, `ayase-shogai-teate`（障害・取込中）, `ayase-shogai-service`（障害・取込中）, `ayase-jigyosha-shien`（事業者・取込中） |
| 葉山町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hayama-kosodate-teate`（子育て・取込中）, `hayama-shogai-teate`（障害・取込中）, `hayama-iryo-kyufu`（健康・福祉・取込中）, `hayama-koreisha`（高齢者・取込中） |
| 寒川町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `samukawa-hojokin`（全般・取込中） |
| 大磯町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oiso-kosodate-teate`（子育て・取込中）, `oiso-koreisha`（高齢者・取込中） |
| 二宮町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ninomiya-kosodate-teate`（子育て・取込中）, `ninomiya-shogai-teate`（障害・取込中）, `ninomiya-shogai-josei`（障害・取込中）, `ninomiya-jigyosha-hojo`（事業者・取込中） |
| 中井町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nakai-kosodate-teate`（子育て・取込中）, `nakai-shogai`（障害・取込中）, `nakai-jigyosha-shien`（事業者・取込中） |
| 大井町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oi-sumai-hojo`（住まい・取込中）, `oi-jidofukushi`（子育て・取込中） |
| 松田町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `matsuda-kosodate-shien`（子育て・取込中）, `matsuda-sumai`（住まい・取込中） |
| 山北町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yamakita-kosodate-teate`（子育て・取込中） |
| 開成町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kaisei-kosodate-shien`（子育て・取込中）, `kaisei-jigyosha-shien`（事業者・取込中） |
| 箱根町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hakone-kosodate-teate`（子育て・取込予定）, `hakone-shogai-teate`（障害・取込予定）, `hakone-jigyosha-hojo`（事業者・取込予定） |
| 真鶴町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `manazuru-kosodate-shien`（子育て・取込中）, `manazuru-shogai-fukushi`（障害・取込中） |
| 湯河原町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yugawara-kosodate-shien`（子育て・取込中）, `yugawara-hitorioya`（子育て・取込中） |
| 愛川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `aikawa-kosodate-teate`（子育て・取込中）, `aikawa-iryohi-josei`（健康・福祉・取込中）, `aikawa-shogai`（障害・取込中） |
| 清川村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kiyokawa-kosodate-teate`（子育て・取込中）, `kiyokawa-sumai-hojo`（住まい・取込中）, `kiyokawa-shogai`（障害・取込中） |
| 大津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 彦根市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長浜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 近江八幡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 草津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 守山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 栗東市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 甲賀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 野洲市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湖南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東近江市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 米原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 竜王町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 愛荘町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 甲良町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 京都市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福知山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 舞鶴市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 綾部市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇治市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 亀岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 城陽市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 向日市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長岡京市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八幡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 京田辺市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 京丹後市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南丹市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 木津川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大山崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 久御山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 井手町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇治田原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 笠置町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和束町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 精華町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南山城村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 京丹波町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊根町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 与謝野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大阪市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 堺市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岸和田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊中市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 池田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吹田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 泉大津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高槻市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 貝塚市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 守口市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 枚方市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 茨木市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八尾市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 泉佐野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富田林市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 寝屋川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 河内長野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大東市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和泉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 箕面市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 柏原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 羽曳野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 門真市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 摂津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高石市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 藤井寺市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東大阪市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 泉南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 四條畷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 交野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大阪狭山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阪南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 島本町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊能町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 能勢町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 忠岡町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 熊取町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田尻町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岬町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 太子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 河南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 千早赤阪村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 姫路市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 尼崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 明石市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西宮市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 洲本市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 芦屋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊丹市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 相生市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 加古川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 赤穂市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西脇市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宝塚市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三木市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高砂市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川西市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 加西市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 丹波篠山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 養父市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 丹波市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南あわじ市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 朝来市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 淡路市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宍粟市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 加東市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| たつの市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 猪名川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多可町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 稲美町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 播磨町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 市川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神河町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 太子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上郡町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐用町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 香美町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新温泉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奈良市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大和高田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大和郡山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 天理市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 橿原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 桜井市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五條市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御所市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 生駒市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 香芝市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 葛城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇陀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山添村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平群町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 斑鳩町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安堵町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川西町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三宅町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田原本町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 曽爾村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御杖村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高取町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 明日香村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上牧町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 王寺町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 広陵町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 河合町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大淀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下市町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 黒滝村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 天川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 野迫川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 十津川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下北山村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上北山村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川上村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東吉野村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和歌山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 海南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 橋本市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 有田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御坊市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田辺市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新宮市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 紀の川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩出市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 紀美野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| かつらぎ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 九度山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湯浅町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 広川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 有田川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日高町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 由良町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 印南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| みなべ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日高川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上富田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| すさみ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那智勝浦町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 太地町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 古座川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北山村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 串本町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
