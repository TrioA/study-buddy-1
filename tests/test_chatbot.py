import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from chatbot import build_reply, load_user, remember_info


def test_build_reply_handles_menu_commands_and_memory(tmp_path, monkeypatch):
    os.chdir(tmp_path)
    user = load_user()

    reply = build_reply(user, ["greeting"], "hello")
    assert "How can I help you today" in reply or "Ready to learn" in reply

    memory_reply = remember_info(user, "my name is sara")
    assert "sara" in memory_reply.lower()

    menu_reply = build_reply(user, [], "1")
    assert "tip" in menu_reply.lower() or "quote" in menu_reply.lower() or "fact" in menu_reply.lower()
