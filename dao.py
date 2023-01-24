from sqlalchemy.orm import Session
from sqlalchemy.future import select
import models, networkModels


def get_user_by_name(db: Session, user_name: str):
    return db.query(models.User).filter(models.User.name == user_name).first()


def check_user(db: Session, user_name: str, user_password: str):
    return db.query(models.User).filter(models.User.name == user_name and models.User.password == user_password).first()


# 新建用户
def create_user(db: Session, request: networkModels.LoginRequest):
    db_user = models.User(name=request.name, password=request.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def query_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()


def query_user_notes(db: Session, user_id: int):
    sql = select(models.Note.id,models.Note.content).where(models.Note.user_id == user_id)
    q = db.execute(sql)
    return q.all()


def add_note(db: Session, user_id: int, content: str):
    db_note = models.Note(user_id=user_id, content=content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


def modify_note(db: Session, note_id: int, content: str):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    db_note.content = content
    db.commit()
    db.refresh(db_note)
    return db_note


def delete_note(db: Session, note_id: int):
    db.query(models.Note).filter(models.Note.id == note_id).delete()
    db.commit()
    return 0
