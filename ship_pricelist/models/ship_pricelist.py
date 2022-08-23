from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

from datetime import datetime, date


class ShipPricelist(models.Model):
    _name = 'ship.pricelist'
    _description = 'Ship pricelist'

    name = fields.Char(string=_('Name'), required=1)
    service_type_id = fields.Many2one('service.type', string=_('Service Type'))
    from_location = fields.Many2one('res.country.state', string=_('From Location'), required=1)
    to_locations = fields.Many2many('res.country.state', string=_('To Locations'), required=1)
    fuel_fee = fields.Float(string=_('Fuel Fee'), digits='Product Unit of Measure')
    region_fee = fields.Float(string=_('Region Fee'), digits='Product Unit of Measure')
    year_apply = fields.Many2one('year.apply', string=_('Year apply'))
    over_weight = fields.Float(string=_('Over Weight (Gr)'), digits='Product Unit of Measure')
    over_weight_fee = fields.Float(string=_('Over Weight Fee'), digits='Product Unit of Measure')
    line_ids = fields.One2many('ship.pricelist.line', 'ship_pricelist_id', string=_('Pricelist Lines'), copy=True)
    active = fields.Boolean(string=_('Active'), default=True)
    has_vat = fields.Boolean(string='VAT')
    number_vat = fields.Float(string='VAT Number')
    collection = fields.Boolean(related='service_type_id.price_list', string='Price list collection')
    surcharge_ids = fields.One2many('surcharge', 'ship_pricelist_id', string='Surcharge')
    fees_collection_ids = fields.One2many('fees.collection', 'ship_pricelist_id', string='Fees collection')


    @api.constrains('line_ids')
    def validate_range_from_to_weight(self):
        error = []
        for line in self.line_ids:
            exist = self.line_ids.filtered(lambda l: l.id != line.id and (
                    l.from_weight <= line.from_weight <= l.to_weight or l.from_weight <= line.to_weight <= l.to_weight))
            if exist:
                error.append(line)
        if error:
            raise ValidationError(_("Ship pricelist line '%s': Weight range cannot be overlapped", ', '.join(e.name for e in error)))

    @api.constrains('surcharge_ids')
    def validate_range_from_to_weight_surcharge(self):
        error = []
        for line in self.surcharge_ids:
            exist = self.surcharge_ids.filtered(lambda l: l.id != line.id and (
                    l.price <= line.price))
            if exist:
                error.append(line)
        if error:
            raise ValidationError(
                _("Surcharge line '%s': Weight range cannot be overlapped", ', '.join(e.name for e in error)))

    @api.constrains('fees_collection_ids')
    def validate_range_from_to_weight_fees_collection(self):
        error = []
        for line in self.fees_collection_ids:
            exist = self.fees_collection_ids.filtered(lambda l: l.id != line.id and (
                    l.from_weight <= line.from_weight <= l.to_weight or l.from_weight <= line.to_weight <= l.to_weight))
            if exist:
                error.append(line)
        if error:
            raise ValidationError(
                _("Fees collection line '%s': Weight range cannot be overlapped", ', '.join(e.name for e in error)))