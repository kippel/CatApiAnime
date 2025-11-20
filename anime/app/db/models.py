from sqlalchemy import Column, Integer, String, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship, backref, mapped_column, Mapped, DeclarativeBase
from .database import Base
# Define the association table for the many-to-many relationship
import enum


    