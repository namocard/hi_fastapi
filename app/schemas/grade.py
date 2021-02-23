from pydantic import BaseModel


class GradeBase(BaseModel):
    name: str
    school_id: int


class GradeCreate(GradeBase):
    pass


class GradeUpdate(GradeBase):
    pass


class GradeDbBase(GradeBase):
    id: int

    class Config:
        orm_mode = True


class Grade(GradeDbBase):
    pass
