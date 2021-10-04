from app.ai.model_ext import ModelExtension


def test_call_me():
    print("Test call me")


if __name__ == "__main__":
    me = ModelExtension()
    print(me.call_me())
    test_call_me()
