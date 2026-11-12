# カバー状況

`uv run seido registry coverage` で生成する。手で編集しない。

- ○: 取込中・取込予定の取得元があり、制度全般を扱う
- ◐: 取込中・取込予定の取得元はあるが、分野が限られる（子育てだけ、など）
- △: 取得元は見つかっているが、調査中・要利用申請・対象外のみ
- −: 取得元が見つかっていない

| 区分 | 団体数 | ○ | ◐ | △ | − |
|---|---:|---:|---:|---:|---:|
| 国 | 26 | 0 | 0 | 26 | 0 |
| 都道府県 | 1 | 1 | 0 | 0 | 0 |
| 市区町村 | 62 | 4 | 58 | 0 | 0 |

## 団体別

| 団体 | 区分 | 状況 | 取得元 |
|---|---|---|---|
| 法務省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 中小企業庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 環境省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 内閣府 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 総務省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 特許庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 国土交通省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 水産庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 資源エネルギー庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 復興庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 林野庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 経済産業省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 消費者庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| スポーツ庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 農林水産省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 金融庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 文化庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 厚生労働省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| こども家庭庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 国税庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 文部科学省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| デジタル庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 財務省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 外務省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 観光庁 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 防衛省 | 国 | △ | `jgrants`（事業者向け補助金・調査中） |
| 東京都 | 都道府県 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-hojokin-search`（都の補助金・取込予定）, `tokyo-shien-navi`（全般・取込予定） |
| 千代田区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 中央区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 港区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 新宿区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 文京区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 台東区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 墨田区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 江東区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 品川区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 目黒区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 大田区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 世田谷区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 渋谷区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 中野区 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-ods-support-131148`（全般・取込予定） |
| 杉並区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 豊島区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 北区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 荒川区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 板橋区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 練馬区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 足立区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 葛飾区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 江戸川区 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 八王子市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 立川市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 武蔵野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 三鷹市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 青梅市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-ods-support-132055`（全般・取込予定） |
| 府中市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 昭島市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 調布市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 町田市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 小金井市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-ods-support-132101`（全般・取込予定） |
| 小平市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 日野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 東村山市 | 市区町村 | ○ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中）, `tokyo-ods-support-132136`（全般・取込予定） |
| 国分寺市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 国立市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 福生市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 狛江市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 東大和市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 清瀬市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 東久留米市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 武蔵村山市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 多摩市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 稲城市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 羽村市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| あきる野市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 西東京市 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 瑞穂町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 日の出町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 檜原村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 奥多摩町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 大島町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 利島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 新島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 神津島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 三宅村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 御蔵島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 八丈町 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 青ヶ島村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
| 小笠原村 | 市区町村 | ◐ | `jgrants`（事業者向け補助金・調査中）, `digital-kosodate-registry`（子育て（主に0-6歳）・要利用申請）, `tokyo-kosodate-registry`（子育て（0-6歳）・取込予定）, `tokyo-kosodate-registry-7-18`（子育て（7-18歳）・調査中） |
