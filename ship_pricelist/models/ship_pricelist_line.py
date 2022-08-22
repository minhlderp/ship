from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ShipPricelistLine(models.Model):
    _name = 'ship.pricelist.line'
    _order = 'from_weight, to_weight, fee'
    _description = 'Ship Pricelist Line'

    name = fields.Char(string=_('Level'))
    from_weight = fields.Float(string=_('From Weight (Gr)'), digits='Product Unit of Measure')
    to_weight = fields.Float(string=_('To Weight (Gr)'), digits='Product Unit of Measure')
    fee = fields.Float(string=_('Fee'), digits='Product Unit of Measure')
    ship_pricelist_id = fields.Many2one('ship.pricelist', string=_('Ship Pricelist'), required=1, ondelete='cascade')
    progressive = fields.Boolean('Progressive ')
    progressive_level = fields.Float('Progressive level')

    @api.constrains('from_weight', 'to_weight')
    def validate_from_to_weight(self):
        for line in self:
            if line.from_weight > line.to_weight:
                raise ValidationError(_("Ship pricelist lines '%s': from weight cannot be greater than to weight", line.name))

class TypeSurcharge(models.Model):
    _name = 'type.surcharge'

    name = fields.Char('Name')

class Surcharge(models.Model):
    _name = 'surcharge'
    _description = 'Surcharge'

    price = fields.Float('Price')
    cpn = fields.Boolean('CPN')
    type_surcharge = fields.Many2one('type.surcharge', string='Type surcharge')
    ship_pricelist_id = fields.Many2one('ship.pricelist')

class FeesCollection(models.Model):
    _name = 'fees.collection'
    _description = 'Fees for collection'

    name = fields.Char('Name')
    from_weight = fields.Float(string=_('From value'), digits='Product Unit of Measure')
    to_weight = fields.Float(string=_('To value'), digits='Product Unit of Measure')
    fee_money = fields.Integer('Fee money')
    percentage_fee = fields.Float('Fee by %')
    ship_pricelist_id = fields.Many2one('ship.pricelist')

