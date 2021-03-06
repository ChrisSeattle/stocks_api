from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio, Stock, Account, AccountRole


class StockSchema(ModelSchema):
    class Meta:
        model = Stock


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account


class PortfolioSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'portfolios', 'roles', 'date_created', 'date_updated',
    ))
    class Meta:
        model = Portfolio
