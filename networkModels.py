from pydantic import BaseModel
from typing import List, Optional


class BaseResponse(BaseModel):
    code: int
    msg: str


class LoginRequest(BaseModel):
    """
    请求模型验证：
    name:
    password:
    """
    name: str
    password: str


class AddNoteRequest(BaseModel):
    content: str


class ModifyNoteRequest(BaseModel):
    content: str


class Token(BaseModel):
    token: str


class LoginResp(BaseResponse):
    data: Token = None


class NoteInfo(BaseModel):
    id: int
    content: str


class QueryNoteResp(BaseResponse):
    data: NoteInfo = None


class QueryNoteListResp(BaseResponse):
    data: List[NoteInfo] = None


class QueryUserResp(BaseModel):
    name: str
    id: int

    class Config:
        orm_mode = True
