from .base_model import BaseModel


class ModelExtension(BaseModel):
    class_var: int = 255

    def call_me(self):
        return 42
