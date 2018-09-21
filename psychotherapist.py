import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
Base = sqlalchemy.declarative_base()


class Specialization(Base):
    __tablename__ = "specialization"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)


class Psychotherapist(Base):
    __tablename__ = "psychotherapists"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    postal_code = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    town = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    fee_in_eur = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    specialization = sqlalchemy.Column(sqlalchemy.Integer,
                                       sqlalchemy.ForeignKey('specialization.id'),
                                       nullable=True)