from app.ai.model_ext import ModelExtension


def test_call_me_42():
    me = ModelExtension()
    assert me.call_me() == 42
