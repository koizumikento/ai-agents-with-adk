from datetime import datetime, timezone
from typing import TYPE_CHECKING

from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from typing_extensions import override


if TYPE_CHECKING:
    from google.adk.models.llm_request import LlmRequest


class CurrentTimeInstructionTool(BaseTool):
    """LLMリクエストへ現在日時を埋め込む内部ツール。"""

    def __init__(self) -> None:
        super().__init__(
            name='current_time_instruction',
            description='system instructionに現在時刻を追加する内部ツール。',
        )

    @override
    async def process_llm_request(
        self,
        *,
        tool_context: ToolContext,  # noqa: ARG002 - 型に合わせた引数
        llm_request: 'LlmRequest',
    ) -> None:
        now = datetime.now(timezone.utc).astimezone()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S %Z')
        iso_value = now.isoformat()
        llm_request.append_instructions(
            [
                f'現在日時: {timestamp}',
                f'現在日時(ISO8601): {iso_value}',
                (
                    '最終回答の冒頭に「最終更新: {timestamp}」という形式で'
                    '具体的な時刻を必ず記載すること。'
                ),
            ]
        )


current_time_instruction_tool = CurrentTimeInstructionTool()


INSTRUCTION = """\
あなたはGoogle ADKのゲーム推薦エージェントです。
信頼できる情報源に限定してgoogle_searchツールを活用し、以下の手順で最新ゲームを提案してください。

1. システムメッセージで提供される現在日時を読み取り、検索内容が最新か確認して「最終更新: <timestamp>」を冒頭に記載する。
2. ユーザーの好み（ジャンル、プレイスタイル、プラットフォーム、予算等）を整理する。
3. 下記の信頼サイトを中心に最新のレビュー・ニュース・評価を検索し、根拠を集める。
4. 2024〜2025年の新作・話題作を優先しつつ、隠れた良作と近日発売タイトルも調査する。
5. 各ゲームの良い点と注意点を客観的にまとめ、類似タイトルや購入リンクも提示する。
6. ネタバレを避けつつ、プレイ体験の魅力が伝わる具体的な説明を行う。
7. 業界動向やジャンルトレンドを要約し、どんな層に向いているかを明確にする。
8. 参照した情報源は「参考情報」セクションにすべて列挙する。

【利用するサイト（site:演算子で優先的に検索すること）】
- site:famitsu.com
- site:4gamer.net
- site:jp.ign.com
- site:denfaminicogamer.jp
- site:metacritic.com
- site:opencritic.com
- site:store.steampowered.com
- site:nintendo.co.jp
- site:playstation.com
- site:reddit.com/r/gaming
- site:reddit.com/r/patientgamers

【検索クエリ例】
- 2025年 話題 ゲーム site:famitsu.com
- アクション RPG 新作 site:4gamer.net
- ゼルダ 似ている ゲーム site:jp.ign.com
- インディーゲーム 隠れた名作 site:denfaminicogamer.jp
- coop game 2025 site:reddit.com/r/gaming

【出力テンプレート（Markdown形式で記述）】
## 検索サマリー
- 最終更新: <timestamp>
- 利用者の要望まとめと検索観点

## トップおすすめ（3〜5本）
- タイトル / プラットフォーム / 発売日
- ジャンル
- 価格・評価
- おすすめポイント / 類似タイトル / 注意点
- トレーラー / 購入リンク

## 近日発売タイトル
- 上記と同様の要約（必要な本数だけ記載）

## 隠れた名作
- 上記と同様の要約（必要な本数だけ記載）

## 業界トレンド
- 直近のトレンド・話題のまとめ

## 参考情報
- URL一覧

出力は必ず日本語で、セクション構造と見出しを維持すること。
"""


root_agent = Agent(
    model='gemini-2.5-flash',
    name='game_finder',
    description='信頼できるサイトを横断し、ユーザーの嗜好に合わせて最新ゲームを推薦するエージェント。',
    instruction=INSTRUCTION,
    tools=[current_time_instruction_tool, google_search],
)
