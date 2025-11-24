from datetime import datetime, timezone

from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest


async def append_current_time_instruction(
    callback_context: CallbackContext,  # noqa: ARG001 - API互換のため受け取る
    llm_request: LlmRequest,
) -> None:
    """LLMリクエストのsystem instructionへ現在日時を追記するコールバック。"""
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


__all__ = ['append_current_time_instruction']

