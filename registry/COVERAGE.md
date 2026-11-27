# カバー状況

`uv run seido registry coverage` で生成する。手で編集しない。

- ○: 取込中・取込予定の取得元があり、制度全般を扱う
- ◐: 取込中・取込予定の取得元はあるが、分野が限られる（子育てだけ、など）
- △: 取得元は見つかっているが、調査中・要利用申請・対象外のみ
- −: 取得元が見つかっていない

| 区分 | 団体数 | ○ | ◐ | △ | − |
|---|---:|---:|---:|---:|---:|
| 国 | 26 | 0 | 2 | 24 | 0 |
| 都道府県 | 47 | 4 | 8 | 35 | 0 |
| 市区町村 | 1741 | 90 | 419 | 1232 | 0 |

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
| 北海道 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 青森県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩手県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮城県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 秋田県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山形県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福島県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 茨城県 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ibaraki-pref-josei`（全般・取込中）, `ibaraki-pref-kosodate-qa`（子育て・取込予定） |
| 栃木県 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tochigi-pref-yushi-josei`（全般・取込中）, `tochigi-pref-kodomo-josei`（子育て・取込中）, `tochigi-pref-jigyosha-hojo`（事業者・取込中）, `tochigi-pref-jutaku-shien`（住まい・取込中） |
| 群馬県 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gunma-pref-hojokin`（全般・取込中）, `gunma-pref-jigyosha-hojo`（事業者・取込中）, `gunma-pref-fukushi-hojo`（健康・福祉・取込中） |
| 埼玉県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `saitama-pref-kosodate-teate`（子育て・取込中）, `saitama-pref-shogai-shien`（障害・取込中）, `saitama-pref-jigyosha-shien`（事業者・取込中）, `saitama-pref-sumai-shien`（住まい・取込予定） |
| 千葉県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chiba-pref-jigyosha-josei`（事業者・取込中）, `chiba-pref-shogai-shien`（障害・取込中） |
| 東京都 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込中）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-hojokin-search`（都の補助金・取込予定）, `tokyo-shien-navi`（全般・取込予定） |
| 神奈川県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kanagawa-pref-kankyo-hojo`（環境・取込中）, `kanagawa-pref-jigyosha-hojo`（事業者・取込予定） |
| 新潟県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富山県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 石川県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福井県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山梨県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長野県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岐阜県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 静岡県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 愛知県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三重県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 滋賀県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shiga-pref-jigyosha-hojo`（事業者・取込中）, `shiga-pref-hitorioya-shien`（子育て・取込中）, `shiga-pref-fukushi-iryo`（健康・福祉・取込中） |
| 京都府 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kyoto-pref-navi-hojo`（全般・要利用申請） |
| 大阪府 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `osaka-pref-kosodate-teate`（子育て・取込中）, `osaka-pref-hitorioya-shien`（子育て・取込中）, `osaka-pref-jigyosha-shienkin`（事業者・取込中） |
| 兵庫県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hyogo-pref-kenko-fukushi-hojo`（健康・福祉・取込中）, `hyogo-pref-kosodate-hojo`（子育て・取込中）, `hyogo-pref-jigyosha-hojo`（事業者・取込中）, `hyogo-pref-kurashi-kankyo-hojo`（環境・取込中） |
| 奈良県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nara-pref-kodomo-teate`（子育て・取込中）, `nara-pref-hitorioya-shien`（子育て・取込中）, `nara-pref-fukushi-iryo`（健康・福祉・取込中）, `nara-pref-shogai-josei`（障害・取込中）, `nara-pref-jigyosha-digital`（事業者・取込中） |
| 和歌山県 | 都道府県 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `wakayama-pref-hitorioya`（子育て・取込中） |
| 鳥取県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 島根県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岡山県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 広島県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山口県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 徳島県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 香川県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 愛媛県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高知県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福岡県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐賀県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長崎県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 熊本県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大分県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮崎県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿児島県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 沖縄県 | 都道府県 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 札幌市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 函館市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小樽市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 旭川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 室蘭市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 釧路市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 帯広市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北見市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 夕張市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩見沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 網走市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 留萌市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 苫小牧市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 稚内市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美唄市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 芦別市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 江別市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 赤平市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 紋別市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 士別市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 名寄市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三笠市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 根室市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 千歳市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 滝川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 砂川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 歌志内市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 深川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富良野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 登別市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 恵庭市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊達市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北広島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 石狩市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北斗市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 当別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新篠津村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松前町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 知内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 木古内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 七飯町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 森町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八雲町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長万部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 江差町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上ノ国町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 厚沢部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 乙部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奥尻町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 今金町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| せたな町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 島牧村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 寿都町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 黒松内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 蘭越町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| ニセコ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 真狩村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 留寿都村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 喜茂別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 京極町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 倶知安町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 共和町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 泊村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神恵内村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 積丹町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 古平町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 仁木町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 余市町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 赤井川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南幌町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奈井江町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上砂川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 由仁町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長沼町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 栗山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 月形町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浦臼町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新十津川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 妹背牛町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 秩父別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 雨竜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北竜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 沼田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鷹栖町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東神楽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 当麻町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 比布町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 愛別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美瑛町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上富良野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中富良野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南富良野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 占冠村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和寒町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 剣淵町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美深町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 音威子府村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 幌加内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 増毛町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小平町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 苫前町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 羽幌町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 初山別村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 遠別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 天塩町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 猿払村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浜頓別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中頓別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 枝幸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊富町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 礼文町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 利尻町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 利尻富士町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 幌延町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美幌町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 斜里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 清里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小清水町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 訓子府町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 置戸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐呂間町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 遠軽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湧別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 滝上町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 興部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西興部村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 雄武町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大空町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊浦町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 壮瞥町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白老町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 厚真町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 洞爺湖町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安平町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| むかわ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日高町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平取町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新冠町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浦河町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 様似町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| えりも町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新ひだか町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 音更町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 士幌町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上士幌町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿追町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新得町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 清水町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 芽室町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中札内村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 更別村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大樹町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 広尾町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 幕別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 池田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊頃町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 本別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 足寄町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 陸別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浦幌町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 釧路町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 厚岸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浜中町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 標茶町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 弟子屈町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鶴居村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白糠町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 別海町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中標津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 標津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 羅臼町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 青森市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 弘前市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 黒石市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五所川原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 十和田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| むつ市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| つがる市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 今別町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 蓬田村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 外ヶ浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鰺ヶ沢町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 深浦町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西目屋村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 藤崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大鰐町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田舎館村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 板柳町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鶴田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中泊町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 野辺地町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 七戸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 六戸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 横浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 六ヶ所村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| おいらせ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大間町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東通村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 風間浦村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐井村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三戸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五戸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 階上町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新郷村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 盛岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮古市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大船渡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 花巻市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北上市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 久慈市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 遠野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 一関市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 陸前高田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 釜石市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 二戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八幡平市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奥州市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 滝沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 雫石町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 葛巻町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩手町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 紫波町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 矢巾町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西和賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 金ケ崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平泉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 住田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大槌町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩泉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田野畑村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 普代村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 軽米町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 野田村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 九戸村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 洋野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 一戸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 仙台市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 石巻市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 塩竈市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 気仙沼市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白石市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 名取市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 角田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多賀城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩沼市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 登米市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 栗原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東松島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 蔵王町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 七ヶ宿町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大河原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 村田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 柴田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 丸森町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 亘理町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山元町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 七ヶ浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 利府町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大和町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大衡村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 色麻町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 加美町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 涌谷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 女川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南三陸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 秋田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 能代市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 横手市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大館市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 男鹿市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湯沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿角市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 由利本荘市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 潟上市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大仙市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北秋田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| にかほ市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 仙北市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小坂町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上小阿仁村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 藤里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三種町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八峰町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五城目町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八郎潟町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 井川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大潟村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 羽後町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東成瀬村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山形市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 米沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鶴岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 酒田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新庄市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 寒河江市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 村山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長井市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 天童市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東根市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 尾花沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南陽市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山辺町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 河北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 朝日町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大江町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大石田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 金山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 最上町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 舟形町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 真室川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大蔵村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鮭川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 戸沢村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高畠町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川西町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小国町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白鷹町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯豊町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 庄内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 遊佐町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 会津若松市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 郡山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| いわき市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白河市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 須賀川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 喜多方市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 相馬市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 二本松市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田村市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南相馬市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊達市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 本宮市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 桑折町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 国見町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川俣町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大玉村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鏡石町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 天栄村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 檜枝岐村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 只見町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南会津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北塩原村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西会津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 磐梯町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 猪苗代町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 会津坂下町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湯川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 柳津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 金山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 昭和村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 会津美里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西郷村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 泉崎村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中島村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 矢吹町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 棚倉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 矢祭町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 塙町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鮫川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 石川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 玉川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平田村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浅川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 古殿町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三春町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 広野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 楢葉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富岡町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川内村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大熊町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 双葉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浪江町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 葛尾村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新地町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯舘村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
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
| 嬬恋村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tsumagoi-kenko-fukushi`（健康・福祉・取込予定）, `tsumagoi-onsenken`（高齢者・取込中）, `tsumagoi-sagi-denwa`（高齢者・取込中）, `tsumagoi-kamiomutsu`（高齢者・取込中）, `tsumagoi-odekake-taxi`（高齢者・取込中）, `tsumagoi-kaigo-jinzai`（事業者・取込中）, `tsumagoi-seinen-kouken`（高齢者・取込中）, `tsumagoi-shintai-shogai`（障害・取込中）, `tsumagoi-chiteki-shogai`（障害・取込中）, `tsumagoi-seishin-shogai`（障害・取込中）, `tsumagoi-nanbyo-iryo`（障害・取込中）, `tsumagoi-shoman-iryo`（子育て・取込中）, `tsumagoi-nanbyo-mimai`（障害・取込中）, `tsumagoi-nichijo-yogu`（障害・取込中）, `tsumagoi-shoman-yogu`（子育て・取込中）, `tsumagoi-hosogu`（障害・取込中） |
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
| 熊谷市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kumagaya-ods-shien`（全般・取込中）, `kumagaya-kosodate-josei`（子育て・取込中）, `kumagaya-koreisha-josei`（高齢者・取込中）, `kumagaya-shogai-josei`（障害・取込中）, `kumagaya-jigyosha-josei`（事業者・取込中）, `kumagaya-sumai-josei`（住まい・取込中）, `kumagaya-bosai-josei`（災害・対象外）, `kumagaya-kenkohoken-josei`（医療・取込中）, `kumagaya-seikatsu-josei`（環境・取込中）, `kumagaya-gomi-josei`（環境・取込中）, `kumagaya-ninshin-josei`（子育て・取込中）, `kumagaya-funin-josei`（医療・取込中）, `kumagaya-kyoiku-josei`（子育て・取込中）, `kumagaya-nogyo-josei`（事業者・取込中） |
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
| 新潟市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三条市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 柏崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新発田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小千谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 加茂市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 十日町市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 見附市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 村上市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 燕市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 糸魚川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 妙高市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五泉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上越市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿賀野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐渡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 魚沼市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南魚沼市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 胎内市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 聖籠町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 弥彦村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田上町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 出雲崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湯沢町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 刈羽村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 関川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 粟島浦村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 魚津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 氷見市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 滑川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 黒部市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 砺波市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小矢部市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南砺市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 射水市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 舟橋村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上市町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 立山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 入善町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 朝日町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 金沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 七尾市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小松市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 輪島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 珠洲市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 加賀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 羽咋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| かほく市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 能美市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 野々市市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津幡町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 内灘町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 志賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宝達志水町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中能登町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 穴水町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 能登町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福井市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 敦賀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小浜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 勝山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鯖江市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| あわら市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 越前市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 坂井市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 永平寺町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 池田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南越前町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 越前町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| おおい町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 若狭町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 甲府市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富士吉田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 都留市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山梨市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大月市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 韮崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南アルプス市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北杜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 甲斐市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 笛吹市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上野原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 甲州市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中央市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 市川三郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 早川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 身延町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富士川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 昭和町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 道志村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西桂町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 忍野村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山中湖村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鳴沢村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富士河口湖町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小菅村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 丹波山村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松本市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岡谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 諏訪市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 須坂市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小諸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊那市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 駒ヶ根市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大町市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 茅野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 塩尻市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐久市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 千曲市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東御市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安曇野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小海町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川上村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南牧村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南相木村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北相木村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐久穂町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 軽井沢町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御代田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 立科町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 青木村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長和町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下諏訪町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富士見町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 原村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 辰野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 箕輪町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南箕輪村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮田村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高森町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿智村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平谷村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 根羽村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下條村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 売木村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 天龍村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 泰阜村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 喬木村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊丘村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大鹿村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上松町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南木曽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 木祖村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 王滝村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大桑村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 木曽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 麻績村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 生坂村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山形村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 朝日村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 筑北村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 池田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白馬村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小谷村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 坂城町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小布施町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高山村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山ノ内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 木島平村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 野沢温泉村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 信濃町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯綱町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 栄村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岐阜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大垣市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多治見市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 関市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中津川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美濃市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 瑞浪市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 羽島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 恵那市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美濃加茂市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 土岐市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 各務原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 可児市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山県市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 瑞穂市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飛騨市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 本巣市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 郡上市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下呂市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 海津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岐南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 笠松町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 養老町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 垂井町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 関ケ原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神戸町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 輪之内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安八町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 揖斐川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 池田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北方町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 坂祝町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富加町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川辺町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 七宗町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八百津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東白川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御嵩町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 静岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浜松市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 沼津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 熱海市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富士宮市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊東市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 島田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 富士市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 磐田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 焼津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 掛川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 藤枝市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御殿場市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 袋井市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 裾野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湖西市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊豆市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御前崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 菊川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊豆の国市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 牧之原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東伊豆町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 河津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南伊豆町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西伊豆町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 函南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 清水町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長泉町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川根本町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 森町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 名古屋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊橋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岡崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 一宮市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 瀬戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 半田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 春日井市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 碧南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 刈谷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西尾市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 蒲郡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 犬山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 常滑市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 江南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小牧市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 稲沢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東海市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大府市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 知多市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 知立市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 尾張旭市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高浜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩倉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊明市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日進市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 愛西市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 清須市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北名古屋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 弥富市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| みよし市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| あま市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長久手市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大口町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 扶桑町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大治町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 蟹江町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飛島村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿久比町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東浦町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南知多町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 武豊町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 幸田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 設楽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東栄町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊根村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 四日市市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊勢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松阪市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 桑名市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鈴鹿市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 名張市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 尾鷲市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 亀山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鳥羽市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 熊野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| いなべ市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 志摩市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊賀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 木曽岬町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東員町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 菰野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 朝日町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川越町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多気町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 明和町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大台町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 玉城町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 度会町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大紀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南伊勢町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 紀北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 紀宝町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大津市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `otsu-kosodate-teate`（子育て・取込中）, `otsu-shogai-teate`（障害・取込中）, `otsu-jigyosha-hojo`（事業者・取込中）, `otsu-machi-hojo`（住まい・取込中） |
| 彦根市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hikone-kosodate-teate`（子育て・取込中）, `hikone-fukushi-teate`（健康・福祉・取込中）, `hikone-kurashi-teate`（住まい・取込中）, `hikone-jigyosha-shisaku`（事業者・取込中） |
| 長浜市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nagahama-kosodate-teate`（子育て・取込中）, `nagahama-shogai-teate`（障害・取込中）, `nagahama-korei-shien`（高齢者・取込中）, `nagahama-jigyosha-hojo`（事業者・取込中） |
| 近江八幡市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `omihachiman-kosodate-support`（子育て・取込中）, `omihachiman-korei-service`（高齢者・取込中）, `omihachiman-jigyosha-shien`（事業者・取込中） |
| 草津市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shiga-kusatsu-kosodate-teate`（子育て・取込中）, `shiga-kusatsu-shogai-seido`（障害・取込中）, `shiga-kusatsu-korei-service`（高齢者・取込中）, `shiga-kusatsu-fukushi-iryo`（健康・福祉・取込中）, `shiga-kusatsu-jigyosha-hojo`（事業者・取込中） |
| 守山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `moriyama-kosodate-shien`（子育て・取込中）, `moriyama-korei-service`（高齢者・取込中）, `moriyama-jigyosha-hojo`（事業者・取込中） |
| 栗東市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ritto-kosodate-teate`（子育て・取込中）, `ritto-shogai-fukushi`（障害・取込中）, `ritto-jigyosha-shoko`（事業者・取込予定） |
| 甲賀市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `koka-hojokin-ichiran`（全般・取込中） |
| 野洲市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yasu-kosodate-shien`（子育て・取込中）, `yasu-shogai-support`（障害・取込中）, `yasu-korei-support`（高齢者・取込中）, `yasu-jigyosha-shien`（事業者・取込中） |
| 湖南市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shiga-konan-kosodate-teate`（子育て・取込中）, `shiga-konan-shogai-josei`（障害・取込中）, `shiga-konan-fukushi-iryo`（健康・福祉・取込中）, `shiga-konan-korei-fukushi`（高齢者・取込中）, `shiga-konan-jigyosha-shien`（事業者・取込中） |
| 高島市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takashima-kosodate`（子育て・取込予定）, `takashima-shogai-service`（障害・取込中）, `takashima-korei-service`（高齢者・取込中）, `takashima-jigyosha-josei`（事業者・取込中） |
| 東近江市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `higashiomi-hitorioya-shien`（子育て・取込中）, `higashiomi-shogai-fukushi`（障害・取込予定）, `higashiomi-korei-fukushi`（高齢者・取込中）, `higashiomi-jigyosha-hojo`（事業者・取込中） |
| 米原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `maibara-kosodate-teate`（子育て・取込中）, `maibara-shogai-okane`（障害・取込中）, `maibara-korei-service`（高齢者・取込中）, `maibara-jigyosha-shoko-hojo`（事業者・取込中） |
| 日野町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shiga-hino-kosodate-teate`（子育て・取込中）, `shiga-hino-korei-shien`（高齢者・取込中）, `shiga-hino-jigyosha-shien`（事業者・取込中） |
| 竜王町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ryuo-fukushi`（障害・取込中）, `ryuo-korei-kaigo`（高齢者・取込中）, `ryuo-sumai`（住まい・取込予定） |
| 愛荘町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `aisho-kosodate`（子育て・取込中）, `aisho-korei-kaigo`（高齢者・取込中） |
| 豊郷町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `toyosato-kosodate-shien`（子育て・取込中）, `toyosato-fukushi`（健康・福祉・取込中） |
| 甲良町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kora-kosodate`（子育て・取込予定）, `kora-jido-teate`（子育て・取込中）, `kora-omutsu`（子育て・取込中）, `kora-shussan-iwai`（子育て・取込中） |
| 多賀町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `taga-josei-hojokin`（全般・取込中）, `taga-fukushi-kaigo`（健康・福祉・取込予定） |
| 京都市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kyoto-shi-kosodate-index`（子育て・取込中）, `kyoto-shi-shogai-shiori`（障害・取込中）, `kyoto-shi-sumai-hojo`（住まい・取込中） |
| 福知山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `fukuchiyama-kosodate-umaretara`（子育て・取込予定）, `fukuchiyama-shogai-fukushi`（障害・取込中）, `fukuchiyama-korei-fukushi`（高齢者・取込中）, `fukuchiyama-jigyosha-shien`（事業者・取込中） |
| 舞鶴市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `maizuru-kosodate-teate`（子育て・取込中）, `maizuru-korei-shien`（高齢者・取込中）, `maizuru-jigyosha-shien`（事業者・取込中） |
| 綾部市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ayabe-kosodate-teate`（子育て・取込中）, `ayabe-shogai-fukushi`（障害・取込中）, `ayabe-korei-fukushi`（高齢者・取込中）, `ayabe-sumai-teiju`（住まい・取込中） |
| 宇治市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `uji-kosodate-teate-josei`（子育て・取込中）, `uji-kosodate-josei-shien`（子育て・取込中）, `uji-shogai-fukushi`（障害・取込予定）, `uji-josei-shien`（全般・取込中） |
| 宮津市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `miyazu-kosodate-josei`（子育て・取込中）, `miyazu-kosodate-teate`（子育て・取込中）, `miyazu-shogai-fukushi`（障害・取込中）, `miyazu-jigyosha-shien`（事業者・取込中） |
| 亀岡市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kameoka-korei-fukushi`（高齢者・取込中）, `kameoka-shogai-fukushi`（障害・取込予定）, `kameoka-jigyosha-shien`（事業者・取込中） |
| 城陽市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `joyo-korei-fukushi`（高齢者・取込中）, `joyo-shogai-fukushi`（障害・取込中）, `joyo-jigyosha-hojo`（事業者・取込中） |
| 向日市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `muko-korei-fukushi`（高齢者・取込中）, `muko-shogai-fukushi`（障害・取込予定）, `muko-kosodate-shien`（子育て・取込中）, `muko-jigyosha-shokogyo`（事業者・取込中） |
| 長岡京市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nagaokakyo-kosodate-teate`（子育て・取込中）, `nagaokakyo-iryohi-josei`（健康・福祉・取込中）, `nagaokakyo-korei-jigyo`（高齢者・取込予定）, `nagaokakyo-jigyosha-shokogyo`（事業者・取込予定） |
| 八幡市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yawata-kosodate-teate`（子育て・取込中）, `yawata-shogai-shien`（障害・取込中）, `yawata-korei-chiiki-shien`（高齢者・取込中）, `yawata-kyufukin`（全般・取込中）, `yawata-fukushi-iryo`（健康・福祉・取込中） |
| 京田辺市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kyotanabe-hojokin-kosodate`（子育て・取込中）, `kyotanabe-hojokin-shogai`（障害・取込中）, `kyotanabe-hojokin-korei`（高齢者・取込中）, `kyotanabe-hojokin-kurashi`（住まい・取込中）, `kyotanabe-hojokin-jigyosha`（事業者・取込中） |
| 京丹後市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kyotango-kosodate-hojo`（子育て・取込中）, `kyotango-iryo-hojo`（健康・福祉・取込中）, `kyotango-shogai-fukushi`（障害・取込中）, `kyotango-korei-fukushi`（高齢者・取込中）, `kyotango-jigyosha-shogyo-hojo`（事業者・取込中） |
| 南丹市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nantan-jido-fukushi`（子育て・取込中）, `nantan-fukushi-iryo`（健康・福祉・取込中）, `nantan-shogai-fukushi`（障害・取込予定）, `nantan-korei-fukushi`（高齢者・取込中） |
| 木津川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kizugawa-kosodate-teate`（子育て・取込中）, `kizugawa-shogai-fukushi`（障害・取込中）, `kizugawa-korei-fukushi-jigyo`（高齢者・取込中） |
| 大山崎町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oyamazaki-kosodate`（子育て・取込中） |
| 久御山町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kumiyama-jido-fukushi`（子育て・取込中）, `kumiyama-korei-fukushi`（高齢者・取込中）, `kumiyama-shogai-fukushi`（障害・取込中） |
| 井手町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ide-kosodate`（子育て・取込中）, `ide-ninshin-shussan`（子育て・取込予定） |
| 宇治田原町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ujitawara-kosodate-shien`（子育て・取込中）, `ujitawara-fukushi-kaigo`（健康・福祉・取込中） |
| 笠置町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kasagi-fukushi-kosodate`（健康・福祉・取込中） |
| 和束町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `wazuka-hojokin`（全般・取込中） |
| 精華町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `seika-kodomo-teate`（子育て・取込中）, `seika-iryohi-josei`（健康・福祉・取込中） |
| 南山城村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `minamiyamashiro-kosodate`（子育て・取込中） |
| 京丹波町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kyotamba-korei-support`（高齢者・取込中）, `kyotamba-kosodate`（子育て・取込予定） |
| 伊根町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ine-sapoto-josei`（全般・取込中） |
| 与謝野町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yosano-kosodate-josei-shien`（子育て・取込中）, `yosano-shogai-fukushi`（障害・取込予定）, `yosano-jigyosha-hojo`（事業者・取込中） |
| 大阪市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `osaka-city-kosodate-kinsen`（子育て・取込中）, `osaka-city-hitorioya-kinsen`（子育て・取込中）, `osaka-city-shogai-teate`（障害・取込中）, `osaka-city-sumai-hojo`（住まい・取込中）, `osaka-city-jigyosha-shien`（事業者・取込中） |
| 堺市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sakai-hitorioya-shien`（子育て・取込中）, `sakai-koreisha-seikatsu`（高齢者・取込中）, `sakai-sumai-otoku`（住まい・取込中） |
| 岸和田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kishiwada-kosodate-teate`（子育て・取込中）, `kishiwada-koreisha`（高齢者・取込予定）, `kishiwada-shogai`（障害・取込中）, `kishiwada-jigyosha-shien`（事業者・取込中）, `kishiwada-sumai-hojo`（住まい・取込中） |
| 豊中市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `toyonaka-kosodate-teate`（子育て・取込中）, `toyonaka-shogai-teate`（障害・取込予定）, `toyonaka-koreisha-shien`（高齢者・取込中）, `toyonaka-jigyosha-hojo`（事業者・取込中）, `toyonaka-teate-josei`（全般・取込中） |
| 池田市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ikeda-hojokin`（全般・取込中）, `ikeda-kosodate-teate`（子育て・取込中）, `ikeda-shogai-josei`（障害・取込中）, `ikeda-koreisha`（高齢者・取込中） |
| 吹田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `suita-kosodate-teate`（子育て・取込中）, `suita-koreisha-kyufu`（高齢者・取込中）, `suita-shogai-teate`（障害・取込中）, `suita-shogai-josei`（障害・取込中）, `suita-jigyosha-hojo`（事業者・取込中） |
| 泉大津市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `izumiotsu-shimin-hojo`（全般・取込中）, `izumiotsu-jigyosha-hojo`（事業者・取込中）, `izumiotsu-shogai`（障害・取込中） |
| 高槻市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takatsuki-kurashi-hojo`（住まい・取込中）, `takatsuki-fukushi-hojo`（障害・取込中）, `takatsuki-iryo-hojo`（健康・福祉・取込中）, `takatsuki-jigyosha-shoreikin`（事業者・取込中） |
| 貝塚市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kaizuka-kosodate-jido`（子育て・取込中）, `kaizuka-hitorioya`（子育て・取込中）, `kaizuka-shogai-teate`（障害・取込中）, `kaizuka-koreisha-fukushi`（高齢者・取込中） |
| 守口市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `moriguchi-kosodate-teate`（子育て・取込中）, `moriguchi-hitorioya`（子育て・取込中）, `moriguchi-shogai`（障害・取込中）, `moriguchi-koreisha-seikatsu`（高齢者・取込中）, `moriguchi-jigyosha-shien`（事業者・取込中） |
| 枚方市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hirakata-kosodate-teate`（子育て・取込中）, `hirakata-hitorioya`（子育て・取込中）, `hirakata-shogai`（障害・取込中）, `hirakata-jigyosha-shien`（事業者・取込中）, `hirakata-sumai-josei`（住まい・取込中） |
| 茨木市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ibarakishi-kosodate-hojo`（子育て・取込中）, `ibarakishi-fukushi-hojo`（健康・福祉・取込中）, `ibarakishi-kurashi-hojo`（住まい・取込中）, `ibarakishi-jigyosha-hojo`（事業者・取込中） |
| 八尾市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yao-kosodate-teate`（子育て・取込中）, `yao-shogai-teate`（障害・取込中）, `yao-jigyosha-hojo`（事業者・取込中） |
| 泉佐野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `izumisano-kosodate-teate`（子育て・取込中）, `izumisano-shogai`（障害・取込中）, `izumisano-koreisha`（高齢者・取込中） |
| 富田林市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tondabayashi-kosodate-teate`（子育て・取込中）, `tondabayashi-hitorioya`（子育て・取込中）, `tondabayashi-iryo-josei`（健康・福祉・取込中）, `tondabayashi-shogai`（障害・取込中）, `tondabayashi-jigyosha`（事業者・取込中） |
| 寝屋川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `neyagawa-kosodate-teate`（子育て・取込予定）, `neyagawa-iryohi-josei`（健康・福祉・取込中）, `neyagawa-shogai-kyufu`（障害・取込中）, `neyagawa-koreisha-sonota`（高齢者・取込中） |
| 河内長野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawachinagano-hitorioya`（子育て・取込中）, `kawachinagano-koreisha`（高齢者・取込中）, `kawachinagano-shogai`（障害・取込中）, `kawachinagano-sumai-hojo`（住まい・取込中）, `kawachinagano-jigyosha`（事業者・取込中） |
| 松原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `matsubara-jigyosha-hojo`（事業者・取込予定）, `matsubara-kosodate-josei`（子育て・取込中）, `matsubara-shogai`（障害・取込中）, `matsubara-koreisha`（高齢者・取込中） |
| 大東市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `daito-kosodate-kyufu`（子育て・取込中）, `daito-shogai`（障害・取込中） |
| 和泉市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `izumi-teate-josei`（全般・取込中） |
| 箕面市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `minoh-ods-shien`（全般・取込中）, `minoh-josei-teate`（全般・取込中）, `minoh-kosodate-teate`（子育て・取込中） |
| 柏原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kashiwara-kosodate-teate`（子育て・取込中）, `kashiwara-shogai-fukushi`（障害・取込予定）, `kashiwara-korei-kaigo`（高齢者・取込予定） |
| 羽曳野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `habikino-kosodate-teate`（子育て・取込中）, `habikino-shogai-service`（障害・取込中） |
| 門真市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kadoma-kosodate-teate`（子育て・取込中）, `kadoma-shogai-teate`（障害・取込中）, `kadoma-korei-service`（高齢者・取込中）, `kadoma-jigyosha-chusho`（事業者・取込中） |
| 摂津市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `settsu-kosodate-teate`（子育て・取込中）, `settsu-shogai-seido`（障害・取込中）, `settsu-korei-josei`（高齢者・取込中）, `settsu-jigyosha-hojo`（事業者・取込中） |
| 高石市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takaishi-kosodate`（子育て・取込中）, `takaishi-korei-fukushi`（高齢者・取込中）, `takaishi-shogai-fukushi`（障害・取込中） |
| 藤井寺市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `fujiidera-iryohi-josei`（健康・福祉・取込中）, `fujiidera-kosodate-shien`（子育て・取込中）, `fujiidera-shogai-fukushi`（障害・取込中）, `fujiidera-korei-fukushi`（高齢者・取込中） |
| 東大阪市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `higashiosaka-kosodate-teate`（子育て・取込中）, `higashiosaka-shogai-teate`（障害・取込中）, `higashiosaka-korei-jiritsu`（高齢者・取込中）, `higashiosaka-jigyosha-hojo`（事業者・取込中） |
| 泉南市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sennan-kosodate-teate`（子育て・取込中）, `sennan-shogai-fukushi`（障害・取込中）, `sennan-korei-service`（高齢者・取込中）, `sennan-jigyosha-shien`（事業者・取込中） |
| 四條畷市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shijonawate-kosodate-teate`（子育て・取込中）, `shijonawate-shogai-teate`（障害・取込中）, `shijonawate-korei-shien`（高齢者・取込予定） |
| 交野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `katano-kosodate-josei`（子育て・取込中）, `katano-jigyosha-sangyo`（事業者・取込予定） |
| 大阪狭山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `osakasayama-kosodate-shien`（子育て・取込中）, `osakasayama-shogai-fukushi`（障害・取込中）, `osakasayama-korei-support`（高齢者・取込中）, `osakasayama-jigyosha-shien`（事業者・取込中） |
| 阪南市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hannan-kosodate-nyuyouji`（子育て・取込中）, `hannan-shogai-service`（障害・取込中）, `hannan-jigyosha-sogyo`（事業者・取込予定） |
| 島本町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shimamoto-kosodate-teate`（子育て・取込中）, `shimamoto-shogai`（障害・取込中）, `shimamoto-korei-service`（高齢者・取込中） |
| 豊能町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `toyono-kosodate-jido`（子育て・取込中）, `toyono-shogai-fukushi`（障害・取込中）, `toyono-korei-fukushi`（高齢者・取込中） |
| 能勢町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nose-kosodate-teate`（子育て・取込中）, `nose-iryohi-josei`（健康・福祉・取込中）, `nose-shogai-fukushi`（障害・取込中） |
| 忠岡町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tadaoka-kosodate-shien`（子育て・取込中）, `tadaoka-shogai-support`（障害・取込中）, `tadaoka-korei-support`（高齢者・取込中） |
| 熊取町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kumatori-kosodate-josei`（子育て・取込中）, `kumatori-kenko-josei`（健康・福祉・取込中）, `kumatori-sumai-josei`（住まい・取込中）, `kumatori-jigyosha-hojo`（事業者・取込中）, `kumatori-shogai-support`（障害・取込中） |
| 田尻町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tajiri-teate-josei`（全般・取込中）, `tajiri-korei-fukushi`（高齢者・取込中） |
| 岬町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `misaki-kosodate-josei`（子育て・取込中）, `misaki-shogai`（障害・取込中）, `misaki-teiju-hojo`（住まい・取込中） |
| 太子町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `taishi-osaka-teate-josei`（全般・取込中）, `taishi-osaka-shogai`（障害・取込中） |
| 河南町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kanan-kosodate-teate`（子育て・取込中）, `kanan-korei-josei`（高齢者・取込中）, `kanan-shogai-josei`（障害・取込中） |
| 千早赤阪村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `chihayaakasaka-kosodate-teate`（子育て・取込中）, `chihayaakasaka-shogai`（障害・取込中） |
| 神戸市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kobe-kosodate-teate-josei`（子育て・取込中）, `kobe-shogai-seido`（障害・取込中）, `kobe-koreisha-fukushi`（高齢者・取込中）, `kobe-jigyosha-shien`（事業者・取込中） |
| 姫路市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `himeji-kosodate-teate`（子育て・取込中）, `himeji-hitorioya-shien`（子育て・取込中）, `himeji-shogaiji-teate`（障害・取込中）, `himeji-koreisha-zaitaku`（高齢者・取込中）, `himeji-jigyosha-shien`（事業者・取込中） |
| 尼崎市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `amagasaki-kosodate-jidoteate`（子育て・取込中）, `amagasaki-hitorioya-shien`（子育て・取込中）, `amagasaki-iryohi-josei`（健康・福祉・取込中）, `amagasaki-shogai-teate`（障害・取込中）, `amagasaki-koreisha-keizai-shien`（高齢者・取込中）, `amagasaki-jigyosha-shien`（事業者・取込中） |
| 明石市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `akashi-kosodate-teate-josei`（子育て・取込中）, `akashi-shogai-josei`（障害・取込中）, `akashi-jigyosha-shokogyo`（事業者・取込中） |
| 西宮市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nishinomiya-kosodate-teate`（子育て・取込中）, `nishinomiya-shogai-keizai`（障害・取込中）, `nishinomiya-koreisha`（高齢者・取込中）, `nishinomiya-jigyosha-sangyo`（事業者・取込中） |
| 洲本市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sumoto-kosodate-josei`（子育て・取込中）, `sumoto-fukushi-josei`（健康・福祉・取込中）, `sumoto-jigyosha-shien`（事業者・取込中） |
| 芦屋市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ashiya-iryohi-josei`（健康・福祉・取込中）, `ashiya-shogai-fukushi`（障害・取込中）, `ashiya-koreisha-fukushi`（高齢者・取込中） |
| 伊丹市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `itami-teate-josei`（全般・取込中） |
| 相生市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `aioi-kosodate-11keys`（子育て・取込中）, `aioi-koreisha-kaigo`（高齢者・取込中） |
| 豊岡市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `toyooka-kosodate-teate-josei`（子育て・取込中）, `toyooka-shogai-teate-josei`（障害・取込中）, `toyooka-koreisha-fukushi`（高齢者・取込中）, `toyooka-jigyosha-hojokin`（事業者・取込中） |
| 加古川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kakogawa-kosodate-teate-josei`（子育て・取込中）, `kakogawa-iryo-josei`（健康・福祉・取込中）, `kakogawa-koreisha-fukushi`（高齢者・取込中）, `kakogawa-jigyosha-shoko`（事業者・取込中） |
| 赤穂市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ako-josei-ichiran`（全般・取込中） |
| 西脇市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nishiwaki-teate-josei`（全般・取込中）, `nishiwaki-jigyosha-shoko`（事業者・取込中） |
| 宝塚市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takarazuka-kosodate-kyufu`（子育て・取込中）, `takarazuka-shogai-teate`（障害・取込中）, `takarazuka-koreisha-josei`（高齢者・取込中）, `takarazuka-jigyosha-shoko`（事業者・取込中） |
| 三木市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `miki-kosodate-kyufu`（子育て・取込中）, `miki-kosodate-josei`（子育て・取込中）, `miki-iryohi-josei`（健康・福祉・取込中）, `miki-jigyosha-shien`（事業者・取込中）, `miki-koreisha-fukushi`（高齢者・取込予定） |
| 高砂市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takasago-josei-hojo`（全般・取込中）, `takasago-teate`（子育て・取込中）, `takasago-shogai-josei`（障害・取込中）, `takasago-iryo-josei`（健康・福祉・取込中） |
| 川西市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawanishi-kosodate-life`（子育て・取込予定）, `kawanishi-shogai-teate`（障害・取込中）, `kawanishi-koreisha-life`（高齢者・取込中）, `kawanishi-jigyosha-hojo`（事業者・取込中） |
| 小野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ono-hyogo-kosodate-teate`（子育て・取込中）, `ono-hyogo-shogai-support`（障害・取込中）, `ono-hyogo-koreisha-support`（高齢者・取込中） |
| 三田市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sanda-hojo-josei`（全般・取込中）, `sanda-kosodate-teate`（子育て・取込中）, `sanda-shogai-seido`（障害・取込中）, `sanda-koreisha-support`（高齢者・取込中） |
| 加西市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kasai-kosodate-teate-josei`（子育て・取込中）, `kasai-fukushi-iryo`（健康・福祉・取込中） |
| 丹波篠山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tambasasayama-kosodate-okane`（子育て・取込中）, `tambasasayama-kenko-hojo`（健康・福祉・取込中）, `tambasasayama-korei-josei`（高齢者・取込中）, `tambasasayama-shogai-seido`（障害・取込中） |
| 養父市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yabu-kosodate-teate`（子育て・取込中）, `yabu-shogai-fukushi`（障害・取込中）, `yabu-korei-fukushi`（高齢者・取込中）, `yabu-jigyosha-hojo`（事業者・取込中） |
| 丹波市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tamba-kosodate-shien`（子育て・取込中）, `tamba-shogai-josei`（障害・取込中）, `tamba-korei-service`（高齢者・取込中）, `tamba-sumai-hojo`（住まい・取込中） |
| 南あわじ市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `minamiawaji-kosodate-shien`（子育て・取込中）, `minamiawaji-shogai`（障害・取込中） |
| 朝来市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `asago-kosodate-teate`（子育て・取込中）, `asago-shogai`（障害・取込中）, `asago-korei-josei`（高齢者・取込中）, `asago-jigyosha-josei`（事業者・取込中） |
| 淡路市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `awaji-fukushi-josei`（子育て・取込中）, `awaji-shogai-fukushi`（障害・取込中）, `awaji-korei-fukushi`（高齢者・取込中） |
| 宍粟市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shiso-kosodate-josei-teate`（子育て・取込中）, `shiso-shogai`（障害・取込中）, `shiso-jigyosha-yushi`（事業者・取込中） |
| 加東市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kato-kosodate-teate`（子育て・取込中）, `kato-shogai-fukushi`（障害・取込中）, `kato-jigyosha-sangyo`（事業者・取込中） |
| たつの市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tatsuno-kosodate-teate`（子育て・取込中）, `tatsuno-shogai-seido`（障害・取込中）, `tatsuno-korei-support`（高齢者・取込中）, `tatsuno-jigyosha-sangyo`（事業者・取込中） |
| 猪名川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `inagawa-kosodate-teate`（子育て・取込中）, `inagawa-shogai-support`（障害・取込中）, `inagawa-korei-support`（高齢者・取込中）, `inagawa-jigyosha-sangyo`（事業者・取込中） |
| 多可町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `taka-kosodate-shien`（子育て・取込中）, `taka-shogai-fukushi`（障害・取込中）, `taka-korei-fukushi`（高齢者・取込中）, `taka-sumai-josei`（住まい・取込中） |
| 稲美町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `inami-kosodate-teate`（子育て・取込中）, `inami-shogai-fukushi`（障害・取込中）, `inami-korei-fukushi`（高齢者・取込中）, `inami-jigyosha-shien`（事業者・取込中） |
| 播磨町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `harima-kosodate-teate`（子育て・取込中）, `harima-shogai-fukushi`（障害・取込中）, `harima-jigyosha-shokogyo`（事業者・取込中） |
| 市川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hyogo-ichikawa-kosodate`（子育て・取込予定）, `hyogo-ichikawa-shogai`（障害・取込中） |
| 福崎町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `fukusaki-kosodate-teate`（子育て・取込中）, `fukusaki-shogai`（障害・取込予定）, `fukusaki-korei`（高齢者・取込中） |
| 神河町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hyogo-kamikawa-hojo-teate-josei`（全般・取込中） |
| 太子町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hyogo-taishi-kosodate-teate`（子育て・取込中）, `hyogo-taishi-shogai`（障害・取込中）, `hyogo-taishi-jigyosha-yushi`（事業者・取込中） |
| 上郡町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamigori-shogai-support`（障害・取込中）, `kamigori-korei-support`（高齢者・取込中）, `kamigori-jigyosha-sangyo`（事業者・取込予定） |
| 佐用町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sayo-ikuji-tetsuzuki`（子育て・取込中）, `sayo-shogai-tetsuzuki`（障害・取込中） |
| 香美町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kami-kosodate-support`（子育て・取込予定）, `kami-shogai-fukushi`（障害・取込中）, `kami-korei-support`（高齢者・取込中）, `kami-jigyosha-sangyo`（事業者・取込中） |
| 新温泉町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shinonsen-jido-fukushi`（子育て・取込中）, `shinonsen-shogai-fukushi`（障害・取込予定）, `shinonsen-korei-fukushi`（高齢者・取込中） |
| 奈良市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nara-kosodate-teate`（子育て・取込中）, `nara-kosodate-hitorioya`（子育て・取込中）, `nara-shogai-teate`（障害・取込中）, `nara-iryohi-josei`（健康・福祉・取込中）, `nara-jigyosha-shien`（事業者・取込中）, `nara-sumai-taishin`（住まい・取込中） |
| 大和高田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yamatotakada-kosodate-teate`（子育て・取込中）, `yamatotakada-iryohi-josei`（健康・福祉・取込中）, `yamatotakada-shogai-teate`（障害・取込中）, `yamatotakada-jigyosha-shien`（事業者・取込中） |
| 大和郡山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yamatokoriyama-kosodate-josei`（子育て・取込中）, `yamatokoriyama-hitorioya-shien`（子育て・取込中）, `yamatokoriyama-korei-kaigo`（高齢者・取込中）, `yamatokoriyama-sumai-hojo`（住まい・取込中）, `yamatokoriyama-jigyosha-kigyo`（事業者・取込中） |
| 天理市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tenri-kodomo-teate`（子育て・取込中）, `tenri-shogai-teate`（障害・取込中）, `tenri-korei-shien`（高齢者・取込中）, `tenri-jigyosha-sangyo`（事業者・取込中） |
| 橿原市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kashihara-kosodate-teate`（子育て・取込中）, `kashihara-hitorioya`（子育て・取込中）, `kashihara-shogai-okane`（障害・取込中）, `kashihara-korei-okane`（高齢者・取込中）, `kashihara-jigyosha-shien`（事業者・取込中） |
| 桜井市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sakurai-josei-hojo`（健康・福祉・取込中）, `sakurai-kosodate-teate`（子育て・取込中）, `sakurai-korei-kyufu`（高齢者・取込中） |
| 五條市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gojo-kosodate-teate`（子育て・取込中）, `gojo-korei-fukushi`（高齢者・取込中）, `gojo-shogai-fukushi`（障害・取込予定）, `gojo-jigyosha-hojo`（事業者・取込予定） |
| 御所市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gose-kosodate-kyufu`（子育て・取込中）, `gose-korei-seikatsu`（高齢者・取込中）, `gose-shogai-fukushi`（障害・取込中）, `gose-jigyosha-sangyo`（事業者・取込中） |
| 生駒市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ikoma-kosodate-kyufu`（子育て・取込中）, `ikoma-kosodate-iryohi`（子育て・取込中）, `ikoma-shogai-fukushi`（障害・取込中）, `ikoma-korei-seikatsu`（高齢者・取込中）, `ikoma-kojin-hojo`（全般・取込中）, `ikoma-jigyosha-hojo`（事業者・取込中） |
| 香芝市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kashiba-kosodate-teate`（子育て・取込中）, `kashiba-shogai-fukushi`（障害・取込中）, `kashiba-korei-fukushi`（高齢者・取込中）, `kashiba-jigyosha-shien`（事業者・取込中）, `kashiba-sumai-jutaku`（住まい・取込予定） |
| 葛城市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `katsuragi-kosodate`（子育て・取込中）, `katsuragi-shogai-teate`（障害・取込中）, `katsuragi-shogai-support`（障害・取込中）, `katsuragi-iryo-josei`（健康・福祉・取込中） |
| 宇陀市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `uda-kosodate-shien`（子育て・取込予定）, `uda-shogai-fukushi`（障害・取込中）, `uda-korei-kaigo`（高齢者・取込中） |
| 山添村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yamazoe-fukushi`（健康・福祉・取込中） |
| 平群町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `heguri-hojo-josei`（全般・取込中） |
| 三郷町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `sango-kosodate-jidofukushi`（子育て・取込中）, `sango-korei-fukushi`（高齢者・取込中）, `sango-sumai`（住まい・取込予定） |
| 斑鳩町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ikaruga-kosodate-shien`（子育て・取込中）, `ikaruga-shogai-fukushi`（障害・取込中）, `ikaruga-korei-fukushi`（高齢者・取込中） |
| 安堵町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `ando-kosodate`（子育て・取込予定）, `ando-kaigo-fukushi`（健康・福祉・取込中） |
| 川西町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawanishi-nara-kosodate-kyufu`（子育て・取込予定）, `kawanishi-nara-shogai`（障害・取込中） |
| 三宅町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `miyake-nara-ikuji`（子育て・取込中）, `miyake-nara-shogai`（障害・取込中） |
| 田原本町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tawaramoto-kosodate-teate`（子育て・取込中）, `tawaramoto-iryohi-josei`（健康・福祉・取込中）, `tawaramoto-shogai-fukushi`（障害・取込中）, `tawaramoto-korei-fukushi`（高齢者・取込中） |
| 曽爾村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `soni-fukushi`（健康・福祉・取込中）, `soni-sumai`（住まい・取込予定）, `soni-makistove`（住まい・取込中）, `soni-teiju`（住まい・取込中） |
| 御杖村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `mitsue-kenko-fukushi`（健康・福祉・取込予定）, `mitsue-jigyosha-sangyo`（事業者・取込予定）, `mitsue-kodomo-iryo`（子育て・取込中）, `mitsue-shinshin-iryo`（障害・取込中）, `mitsue-hitorioya-iryo`（子育て・取込中）, `mitsue-jushin-iryo`（障害・取込中）, `mitsue-sogyo`（事業者・取込中）, `mitsue-shikaku`（事業者・取込中）, `mitsue-shuno`（事業者・取込中） |
| 高取町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `takatori-kosodate-teate`（子育て・取込中）, `takatori-shogai-fukushi`（障害・取込中） |
| 明日香村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `asuka-kosodate`（子育て・取込中）, `asuka-kenko-fukushi`（健康・福祉・取込予定） |
| 上牧町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kanmaki-kosodate-jidofukushi`（子育て・取込中）, `kanmaki-korei-kaigo`（高齢者・取込中） |
| 王寺町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oji-kosodate-teate`（子育て・取込中）, `oji-kosodate-iryohi`（子育て・取込中）, `oji-shogai-josei`（障害・取込中）, `oji-korei-jigyo`（高齢者・取込中）, `oji-jigyosha-hojo`（事業者・取込中） |
| 広陵町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `koryo-kosodate-teate`（子育て・取込中）, `koryo-shogai-fukushi`（障害・取込中）, `koryo-jigyosha-shien`（事業者・取込中） |
| 河合町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawai-kosodate`（子育て・取込中）, `kawai-iryohi-josei`（健康・福祉・取込中） |
| 吉野町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yoshino-kosodate-keizai`（子育て・取込中）, `yoshino-fukushi-service`（健康・福祉・取込中）, `yoshino-jigyosha-keiei`（事業者・取込中） |
| 大淀町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `oyodo-shogai-fukushi`（障害・取込中）, `oyodo-hitorioya`（子育て・取込中） |
| 下市町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shimoichi-fukushi-kaigo`（健康・福祉・取込中）, `shimoichi-kosodate`（子育て・取込中） |
| 黒滝村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kurotaki-hoken-fukushi`（健康・福祉・取込予定）, `kurotaki-fukushi-iryo`（健康・福祉・取込中）, `kurotaki-taxi`（健康・福祉・取込中）, `kurotaki-shogai`（障害・取込中） |
| 天川村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tenkawa-teate`（健康・福祉・取込中） |
| 野迫川村 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nosegawa-kurashi`（全般・取込中） |
| 十津川村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `totsukawa-hitorioya`（子育て・取込中）, `totsukawa-kourei`（高齢者・取込中）, `totsukawa-syougai`（障害・取込中）, `totsukawa-ninshin`（子育て・取込中）, `totsukawa-hoiku`（子育て・取込中）, `totsukawa-gakko`（子育て・取込中）, `totsukawa-shinchiku`（住まい・取込中） |
| 下北山村 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shimokitayama-hojokin`（全般・取込中）, `shimokitayama-fukushi`（健康・福祉・取込中） |
| 上北山村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamikitayama-kosodate-shien`（子育て・取込中） |
| 川上村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kawakami-hoken-fukushi`（健康・福祉・取込予定）, `kawakami-hochoki`（高齢者・取込中）, `kawakami-fukushi-iryo`（健康・福祉・取込中）, `kawakami-shogai`（障害・取込中）, `kawakami-korei`（高齢者・取込中） |
| 東吉野村 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `higashiyoshino-hojokin`（全般・取込中） |
| 和歌山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `wakayama-city-kosodate-teate`（子育て・取込中）, `wakayama-city-shogai`（障害・取込中）, `wakayama-city-korei`（高齢者・取込中）, `wakayama-city-jigyosha-shien`（事業者・取込中） |
| 海南市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kainan-kosodate-shien`（子育て・取込中）, `kainan-shogai-fukushi`（障害・取込中） |
| 橋本市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hashimoto-kosodate-jido`（子育て・取込中）, `hashimoto-shogai-fukushi`（障害・取込中）, `hashimoto-korei-fukushi`（高齢者・取込中）, `hashimoto-jigyosha-sangyo`（事業者・取込予定） |
| 有田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `arida-kosodate-teate`（子育て・取込中）, `arida-shogai`（障害・取込予定） |
| 御坊市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `gobo-kosodate-teate`（子育て・取込中）, `gobo-shogai-fukushi`（障害・取込中） |
| 田辺市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tanabe-kosodate-seikatsu`（子育て・取込中）, `tanabe-shogai-teate`（障害・取込中）, `tanabe-jigyosha-hojo`（事業者・取込中） |
| 新宮市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shingu-kosodate`（子育て・取込中） |
| 紀の川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kinokawa-kosodate-teate`（子育て・取込中）, `kinokawa-shogai`（障害・取込中）, `kinokawa-jigyosha-shien`（事業者・取込中） |
| 岩出市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `iwade-shien-kosodate`（子育て・取込中）, `iwade-shien-fukushi`（健康・福祉・取込中） |
| 紀美野町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kimino-kosodate-teate`（子育て・取込中）, `kimino-shogai-kyufu`（障害・取込中） |
| かつらぎ町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `wakayama-katsuragi-fukushi`（健康・福祉・取込中） |
| 九度山町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kudoyama-kosodate`（子育て・取込中）, `kudoyama-kyufukin`（全般・取込中） |
| 高野町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `koya-fukushi-tetsuzuki`（健康・福祉・取込中） |
| 湯浅町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yuasa-kosodate-josei`（子育て・取込中）, `yuasa-shogai`（障害・取込中）, `yuasa-iryohi-josei`（健康・福祉・取込中） |
| 広川町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hirogawa-shien-seido`（全般・取込中） |
| 有田川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `aridagawa-kosodate`（子育て・取込中）, `aridagawa-iryohi-josei`（健康・福祉・取込中）, `aridagawa-shogai`（障害・取込中）, `aridagawa-korei-josei`（高齢者・取込中） |
| 美浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `mihama-wakayama-https`（全般・調査中） |
| 日高町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hidaka-wakayama-https`（全般・調査中） |
| 由良町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `yura-kosodate-hojo`（子育て・取込中）, `yura-ninshin`（子育て・取込中）, `yura-sumai-hojo`（住まい・取込中） |
| 印南町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `inami-josei-teate`（全般・取込中） |
| みなべ町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `minabe-kosodate-josei`（子育て・取込中）, `minabe-shogai-teate`（障害・取込中） |
| 日高川町 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `hidakagawa-hojo-jigyo`（全般・取込中）, `hidakagawa-kosodate-shien`（子育て・取込中） |
| 白浜町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `shirahama-fukushi`（健康・福祉・取込中） |
| 上富田町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kamitonda-kosodate`（子育て・取込予定）, `kamitonda-ninpu-kyufu`（子育て・取込中）, `kamitonda-jido-teate`（子育て・取込中）, `kamitonda-kodomo-iryo`（子育て・取込中）, `kamitonda-mijukuji`（子育て・取込中）, `kamitonda-shugaku`（子育て・取込中）, `kamitonda-jido-fuyo`（子育て・取込中）, `kamitonda-hitorioya-iryo`（子育て・取込中）, `kamitonda-funin`（子育て・取込中） |
| すさみ町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `susami-kosodate`（子育て・取込中）, `susami-shogai`（障害・取込中） |
| 那智勝浦町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `nachikatsuura-fukushi`（健康・福祉・取込予定）, `nachikatsuura-kodomo-iryo`（子育て・取込中）, `nachikatsuura-kosodate-kyufu`（子育て・取込中）, `nachikatsuura-choukaku`（子育て・取込中）, `nachikatsuura-mushoka`（子育て・取込中）, `nachikatsuura-korei`（高齢者・取込中）, `nachikatsuura-shogai`（障害・取込中） |
| 太地町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `taiji-kodomo-teate`（子育て・取込中） |
| 古座川町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kozagawa-ninshin`（子育て・取込中）, `kozagawa-kosodate`（子育て・取込中）, `kozagawa-iryo-fukushi`（健康・福祉・取込中）, `kozagawa-kourei`（高齢者・取込中）, `kozagawa-sasaeai`（高齢者・取込中）, `kozagawa-kaigo-jinzai`（事業者・取込中）, `kozagawa-sangyo`（事業者・取込中）, `kozagawa-teiju-shinchiku`（住まい・取込中） |
| 北山村 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kitayama-jumin`（全般・取込中） |
| 串本町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `kushimoto-kodomo-fukushi`（子育て・取込中）, `kushimoto-fukushi-iryo`（健康・福祉・取込中）, `kushimoto-korei`（高齢者・取込中） |
| 鳥取市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 米子市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 倉吉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 境港市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩美町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 若桜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 智頭町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八頭町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三朝町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湯梨浜町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 琴浦町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北栄町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日吉津村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伯耆町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 江府町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松江市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浜田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 出雲市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 益田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安来市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 江津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 雲南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奥出雲町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川本町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 邑南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津和野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 海士町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西ノ島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 知夫村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 隠岐の島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岡山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 倉敷市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 玉野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 笠岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 井原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 総社市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高梁市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新見市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 備前市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 瀬戸内市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 赤磐市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 真庭市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美作市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浅口市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和気町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 早島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 里庄町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 矢掛町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新庄村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鏡野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 勝央町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奈義町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西粟倉村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 久米南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美咲町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉備中央町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 広島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 呉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 竹原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 尾道市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 府中市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三次市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 庄原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大竹市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東広島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 廿日市市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安芸高田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 江田島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 府中町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 海田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 熊野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 坂町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安芸太田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北広島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大崎上島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 世羅町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神石高原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下関市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇部市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山口市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 萩市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 防府市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 下松市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岩国市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 光市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長門市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 柳井市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美祢市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 周南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山陽小野田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 周防大島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和木町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上関町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田布施町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平生町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿武町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 徳島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鳴門市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小松島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉野川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿波市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美馬市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三好市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 勝浦町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上勝町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐那河内村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 石井町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 牟岐町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美波町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 海陽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松茂町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 藍住町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 板野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上板町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| つるぎ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東みよし町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高松市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 丸亀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 坂出市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 善通寺市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 観音寺市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| さぬき市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東かがわ市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三豊市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 土庄町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小豆島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三木町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 直島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇多津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 綾川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 琴平町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多度津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| まんのう町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松山市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 今治市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇和島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八幡浜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新居浜市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西条市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大洲市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊予市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 四国中央市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西予市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東温市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 久万高原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松前町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 砥部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 内子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊方町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鬼北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 愛南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高知市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 室戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安芸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南国市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 土佐市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 須崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宿毛市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 土佐清水市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 四万十市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 香南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 香美市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東洋町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奈半利町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 安田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 馬路村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 芸西村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 本山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大豊町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 土佐町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大川村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| いの町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 仁淀川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中土佐町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 越知町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 梼原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日高村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津野町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 四万十町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大月町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三原村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 黒潮町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北九州市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大牟田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 久留米市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 直方市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 飯塚市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 田川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 柳川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八女市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 筑後市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 行橋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊前市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中間市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小郡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 筑紫野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 春日市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大野城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宗像市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 太宰府市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 古賀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| うきは市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮若市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 嘉麻市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 朝倉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| みやま市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 糸島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那珂川市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇美町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 篠栗町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 志免町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 須恵町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新宮町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 久山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 粕屋町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 芦屋町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 水巻町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 岡垣町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 遠賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小竹町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鞍手町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 桂川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 筑前町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東峰村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大刀洗町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大木町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 広川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 香春町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 添田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 糸田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大任町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 赤村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 福智町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 苅田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| みやこ町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉富町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上毛町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 築上町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐賀市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 唐津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鳥栖市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多久市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊万里市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 武雄市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 嬉野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 神埼市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 吉野ヶ里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 基山町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上峰町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| みやき町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 玄海町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 有田町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大町町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 江北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 白石町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 太良町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐世保市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 島原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 諫早市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大村市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 平戸市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 松浦市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 対馬市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 壱岐市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西海市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 雲仙市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南島原市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長与町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 時津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東彼杵町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川棚町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 波佐見町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小値賀町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐々町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新上五島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 熊本市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八代市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 人吉市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 荒尾市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 水俣市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 玉名市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山鹿市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 菊池市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇土市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 上天草市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿蘇市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 天草市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 合志市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美里町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 玉東町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南関町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長洲町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和水町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大津町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 菊陽町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南小国町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小国町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 産山村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高森町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西原村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南阿蘇村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 御船町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 嘉島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 益城町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 甲佐町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山都町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 氷川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 芦北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津奈木町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 錦町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多良木町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湯前町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 水上村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 相良村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五木村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 山江村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 球磨村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| あさぎり町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 苓北町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大分市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 別府市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中津市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 佐伯市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 臼杵市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 津久見市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 竹田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊後高田市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 杵築市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇佐市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊後大野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 由布市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 国東市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 姫島村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日出町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 九重町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 玖珠町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 都城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 延岡市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日南市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 小林市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日向市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 串間市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西都市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| えびの市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三股町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 国富町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 綾町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高鍋町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 新富町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西米良村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 木城町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 川南町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 都農町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 門川町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 諸塚村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 椎葉村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 美郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 高千穂町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日之影町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 五ヶ瀬町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿児島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 鹿屋市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 枕崎市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 阿久根市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 出水市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 指宿市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西之表市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 垂水市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 薩摩川内市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 日置市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 曽於市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 霧島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| いちき串木野市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南さつま市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 志布志市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 奄美市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南九州市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊佐市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 姶良市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 三島村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 十島村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| さつま町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 長島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 湧水町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大崎町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東串良町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 錦江町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南大隅町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 肝付町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中種子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南種子町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 屋久島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大和村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宇検村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 瀬戸内町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 龍郷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 喜界町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 徳之島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 天城町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊仙町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 和泊町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 知名町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 与論町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 那覇市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宜野湾市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 石垣市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 浦添市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 名護市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 糸満市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 沖縄市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 豊見城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| うるま市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宮古島市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南城市 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 国頭村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 大宜味村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 東村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 今帰仁村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 本部町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 恩納村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 宜野座村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 金武町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊江村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 読谷村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 嘉手納町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北谷町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北中城村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 中城村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 西原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 与那原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南風原町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 渡嘉敷村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 座間味村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 粟国村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 渡名喜村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 南大東村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 北大東村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊平屋村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 伊是名村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 久米島町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 八重瀬町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 多良間村 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 竹富町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
| 与那国町 | 市区町村 | △ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請） |
