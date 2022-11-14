from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PhoneBook(Base):
    __tablename__ = 'PhoneBook'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    patronymic = Column(String(50), nullable=True)
    birthday = Column(Date, nullable=True)
    phone_person = Column(String(12), nullable=False)
    phone_work = Column(String(12), nullable=True)
    email = Column(String, nullable=True)
    group = Column(String, nullable=True)
    city_id = Column('City', ForeignKey('city.id'))

    def __repr__(self):
        return  f'ФАМИЛИЯ {self.last_name.upper()}, ' \
                f'Имя {self.first_name}, ' \
                f'личный телефон {self.phone_person}'


    # Dict = {
    #     "id" : None,
    #     "first_name" : None,
    #     "last_name" : None,
    #     "patronymic" : None,
    #     "birthday" : None,
    #     "phone_person" : None,
    #     "phone_work" : None,
    #     "email" : None,
    #     "group" : None,
    #     "city_id" : None,
    #     }


class city(Base):
    __tablename__ = 'City'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)

    def __repr__(self):
        return f'Город {self.city}'
