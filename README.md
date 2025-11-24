# AI Agents with Google ADK

Google Agent Developer Kit (ADK) を使用したAIエージェント集

## 概要

このプロジェクトは、Google ADKとGemini 2.5 Flashモデルを使用した2つの実用的なAIエージェントを実装しています。

## エージェント

### 1. Game Finder Agent (`game_finder/`)

ゲーム推薦エージェント。信頼できるゲーム情報サイトを横断検索し、ユーザーの嗜好に合わせて最新ゲームを推薦します。

**特徴:**

- Google Searchツールで最新ゲーム情報を取得
- 信頼できる情報源（ファミ通、4Gamer、IGN、電ファミニコゲーマー等）に限定
- 現在時刻を自動埋め込みする内部ツールを実装
- 構造化されたMarkdown形式で出力

### 2. TODO Generator Agent (`todo_generator/`)

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
from game_finder.agent import game_finder_agent
from todo_generator.agent import todo_generator_agent
```
