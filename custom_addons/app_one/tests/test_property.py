from odoo.tests.common import TransactionCase
from odoo import fields

class TestProperty(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestProperty, self).setUp()
        self.property_01_record = self.env['property'].create(
            {
                'ref': 'PRT1000',
                'name': 'property 1000',
                'garden_orientation': 'west',
                'date_availability': fields.Date.today(),
                'expected_price': 1000,
                'selling_price': 800,
            }
        )

    def test_01_property_values(self):
        property_id = self.property_01_record

        self.assertRecordValues(property_id, [{
                'ref': 'PRT1000',
                'name': 'property 1000',
                'garden_orientation': 'west',
                'date_availability': fields.Date.today(),
                'expected_price': 1000,
                'selling_price': 800,
            }])

