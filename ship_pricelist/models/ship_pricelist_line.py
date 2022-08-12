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

    @api.constrains('from_weight', 'to_weight')
    def validate_from_to_weight(self):
        for line in self:
            if line.from_weight > line.to_weight:
                raise ValidationError(_("Ship pricelist lines '%s': from weight cannot be greater than to weight", line.name))
