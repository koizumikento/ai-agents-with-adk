from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from pydantic import BaseModel, Field


class Todo(BaseModel):
    """構造化されたTODOアイテム。"""

    title: str = Field(..., description='短いタイトル（60文字以内）')
    description: str = Field(
        ...,
        description=(
            '実行手順・期待成果・検証方法を含めた詳細な説明。'
            '専門用語は簡潔に定義し、引用した情報源を明記する。'
        ),
    )
    due_date: str = Field(
        ...,
        description=(
            "予定締切。ISO 8601形式（例: '2025-12-31'）または'TBD'を使用する。"
        ),
    )
    priority: int = Field(
        ...,
        ge=1,
        le=5,
        description='1が最優先。影響度と緊急度を考慮して整数値で指定する。',
    )
    status: str = Field(
        ...,
        description="現在の状況。新規TODOは'planned'で開始し、進行状況を反映させる。",
    )
    category: str = Field(
        ...,
        description='タスクの性質を表すカテゴリ（例: research, design, coding, testing）。',
    )
    tags: list[str] = Field(
        default_factory=list,
        description='検索やフィルタリングに役立つキーワード一覧。',
    )
    attachments: list[str] = Field(
        default_factory=list,
        description='参考資料やテンプレートなどのリンク。Google Searchの出典も含める。',
    )


class TodoPlan(BaseModel):
    """TODO分解の全体像。"""

    goal_summary: str = Field(..., description='ユーザープロンプトを要約した全体目標。')
    context_notes: str = Field(
        ...,
        description='Google Searchで得た重要な知見や制約・前提の整理。',
    )
    todos: list[Todo] = Field(..., description='優先度順に整列したTODOリスト。')
    citations: list[str] = Field(
        default_factory=list,
        description='使用した外部ソースのURL。Google Searchの結果から抽出する。',
    )


INSTRUCTION = """\
あなたはGoogle ADKのTODO細分化エージェントです。
常にgoogle_searchツールを用いて最新かつ信頼できる情報を確認し、以下の手順で応答してください。

1. ユーザー入力を分析し、目的・制約・依存関係を明確化する。
2. google_searchツールを最低1回は呼び出し、必要な情報や最新のベストプラクティスを取得する。
3. 検索結果から重要な知見と参照URLを整理し、context_notes/citationsに反映する。
4. タスクを実行可能なステップに分解し、優先度・期限・カテゴリを判断する。
5. TodoPlanスキーマに適合するJSONを生成し、todosは優先度の高い順で並べる。
6. すべてのTODOには検証方法や成果物を含め、attachmentsに関連リンクを列挙する。

出力は必ず日本語で記述し、フィールド以外の自由文は含めないこと。
"""


todo_generator_agent = Agent(
    model='gemini-2.5-flash',
    name='todo_grounding_agent',
    description='Google Searchで得た最新情報を踏まえてTODOを細分化するエージェント。',
    instruction=INSTRUCTION,
    tools=[google_search],
    output_schema=TodoPlan,
)
