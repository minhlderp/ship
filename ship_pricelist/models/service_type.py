from odoo import fields, models, api, _


class ServiceType(models.Model):
    _name = 'service.type'
    _description = 'Service Type'

    name = fields.Char(string=_('Name'), required=1)
    active = fields.Boolean(string=_('Active'), default=True)
