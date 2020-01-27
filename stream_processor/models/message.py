import faust


class OriginalMessage(faust.Record):
    msg: str


class TransformedMessage(faust.Record):
    msg_id: int
    msg_data: str
    msg_base64: str
    created_at: float 
    source_topic: str
    target_topic: str
    deleted: bool