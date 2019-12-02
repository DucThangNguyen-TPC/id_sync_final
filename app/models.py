from app import db


class IdPair(db.Model):
    __tablename__ = 'idpairs'
    # Unique constraint on battle net id and beeswax id, each pair cannot be inserted one time
    __table_args__ = (
        db.UniqueConstraint('battle_net_id', 'beeswax_id', name='unique_row'),
    )
    id = db.Column(db.Integer, primary_key=True)
    battle_net_id = db.Column(db.Integer, nullable=False)
    beeswax_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Battlenet Id: {} - Beeswax Id: {}'.format(self.battlenet_id, self.beeswax_id)