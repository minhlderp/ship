from odoo import fields, models, api, _


class ServiceType(models.Model):
    _name = 'service.type'
    _description = 'Service Type'

    name = fields.Char(string=_('Name'), required=1)
    active = fields.Boolean(string=_('Active'), default=True)
    price_list = fields.Boolean('Bảng giá thu hộ')
<<<<<<< HEAD

class YearApply(models.Model):
    _name = 'year.apply'


    name = fields.Char('Year apply')
=======
>>>>>>> 131a8e3bf586708491630fa78f85c10c67411111
