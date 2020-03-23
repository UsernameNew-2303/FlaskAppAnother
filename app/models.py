from app import db

association_user_region = db.Table('user_region', db.Model.metadata,
                                   db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                                   db.Column('region_id', db.Integer, db.ForeignKey('region.id')))


class PartnerRegion(db.Model):
    __tablename__ = 'partner_region'
    id = db.Column(db.Integer, primary_key=True)
    partners = db.Column(db.Integer, db.ForeignKey('partner.id'), primary_key=True)
    regions = db.Column(db.Integer, db.ForeignKey('region.id', primary_key=True))
    partner_list = db.relationship('Partner', back_populates='regions')
    region_list = db.relationship('Region', back_populates='partners')


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    users = db.relationship("User", backref="roles")  # one to many


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    role = db.Column(db.Integer, db.ForeignKey('role.id'))
    regions = db.relationship('Region', secondary=association_user_region, back_populates='users')


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    users = db.relationship('User', secondary=association_user_region, back_populates='regions')
    partners = db.relationship('PartnerRegion', back_populates='regions')


class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    regions = db.relationship('PartnerRegion', back_populates='partners')
