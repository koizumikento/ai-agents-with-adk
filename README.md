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

開発環境は `.python-version` の Python 3.12.15 を使用します。依存関係を取得する前に、[公式の手順](https://docs.astral.sh/uv/getting-started/installation/)で uv を最新版に更新してください（検証済み: uv 0.13.5）。古い pip / ensurepip を使ったブートストラップは避け、pip を必要としない uv で環境を作成します。

```bash
# 固定した Python とロック済みの依存関係（開発用も含む）で .venv を作成・更新
uv sync --locked --all-groups --managed-python

# 実際に選択された Python、アプリ用 CA、同梱 pip の版を確認
uv run --locked python -c "import sys, certifi, ensurepip; print(sys.version); print('certifi:', certifi.__version__); print('ensurepip:', ensurepip.version())"
```

Python が固定版と一致しない、certifi が 2026.10.19 未満、または ensurepip が 26.2.2 未満の場合はセットアップを止め、使用する配布物・仮想環境を更新してください。

2026-10-24 に検証した uv 管理の Windows 版 Python 3.12.15 は、pip 26.2.2（内部の certifi は 2026.10.19）を同梱しています。アプリの certifi は `uv.lock` の 2026.10.23 です。別の配布元・OS では同梱内容が異なるため、pip が必要な場合は仮想環境ごとに [Python 公式の CA 更新手順](https://blog.python.org/2026/10/python-3151-3149-31317/)を確認し、pip 26.2.2 以上と内部の certifi 2026.10.19 以上を確認してください。アプリの certifi 更新だけでは、同梱 pip、既存環境、OS の信頼ストアは更新されません。

Python 3.12.15 は[9月のセキュリティリリース](https://www.python.org/downloads/release/python-31215/)です。10月22日に修正された [CVE-2026-114583（tar_filter）](https://github.com/python/cpython/pull/160098)の修正を含むとは扱いません。以後の修正版を確認し、ランタイムとこの固定版を継続して更新してください。

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
