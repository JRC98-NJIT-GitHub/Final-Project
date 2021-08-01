"""Data models."""
from . import db


class Team(db.Model):
    """Data model for team accounts."""

    __tablename__ = 'mlbteams2012'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    Team = db.Column(
        db.String(12),
        index=False,
        unique=False,
        nullable=False
    )
    Payroll_millions = db.Column(
        db.Float,
        index=False,
        unique=False,
        nullable=False
    )
    Wins = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<Team {}>'.format(self.Team)