# AI Agents with Google ADK

Google Agent Developer Kit (ADK) を使用したAIエージェント集

## 概要

このプロジェクトは、Google ADKとGemini 2.5 Flashモデルを使用した2つの実用的なAIエージェントを実装しています。

## エージェント

### 1. Finance Agent (`finance_agent/`)

株式投資アドバイザーエージェント。階層型マルチエージェント構造で、日本株と米国株の分析を専門エージェントに委譲し、最適な投資判断情報を提供します。

**特徴:**

- **階層型マルチエージェント設計**: コーディネーターが市場を判断し、専門エージェントへ自動委譲
  - `finance_coordinator`: ルートエージェント（日米市場の振り分け）
  - `stock_finder_jp`: 日本株専門エージェント
  - `stock_finder_us`: 米国株専門エージェント
- **信頼できる情報源の活用**:
  - 日本株: Yahoo!ファイナンス、日経新聞、株探、みんかぶ、IRBank、BuffettCode等
  - 米国株: Yahoo Finance、Seeking Alpha、SEC EDGAR、Finviz、Morningstar等
- **包括的な分析手法**:
  - ファンダメンタル指標（PER、PBR、ROE、EPS成長率、配当利回り等）
  - テクニカル指標（トレンド、移動平均、RSI、出来高等）
  - 最新ニュース、決算情報、業界動向、マクロ経済の影響分析
- **構造化された出力**: 推奨銘柄、目標株価、リスク要因、参考URLを含む詳細レポート
- **時刻自動埋め込み**: 分析結果に最終更新時刻を自動付与

### 2. Game Finder Agent (`game_finder/`)

ゲーム推薦エージェント。信頼できるゲーム情報サイトを横断検索し、ユーザーの嗜好に合わせて最新ゲームを推薦します。

**特徴:**

- Google Searchツールで最新ゲーム情報を取得
- 信頼できる情報源（ファミ通、4Gamer、IGN、電ファミニコゲーマー等）に限定
- 現在時刻を自動埋め込みする内部ツールを実装
- 構造化されたMarkdown形式で出力

### 3. TODO Generator Agent (`todo_generator/`)

TODO細分化エージェント。Google Searchで最新情報を参照しながら、タスクを実行可能なステップに分解します。

**特徴:**

- Google Searchで最新のベストプラクティスを取得
- Pydanticモデルによる構造化された出力
- 優先度、期限、カテゴリを自動判断
- 参照URLと検証方法を含む詳細なTODOを生成

## 技術スタック

- **Python**: 3.12以上
- **Google ADK**: 1.19.0以上
- **LLM**: Gemini 2.5 Flash
- **パッケージ管理**: uv

## セットアップ

```bash
# 依存関係のインストール
uv sync

# 開発用依存関係も含める場合
uv sync --group dev
```

## 使用方法

各エージェントは独立したモジュールとしてインポート可能です：

```python
# 株式投資アドバイザー（階層型マルチエージェント）
from finance_agent import root_agent, stock_finder_jp_agent, stock_finder_us_agent

# ゲーム推薦
from game_finder.agent import game_finder_agent

# TODO生成
from todo_generator.agent import todo_generator_agent
```
