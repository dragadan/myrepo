# -*- coding: utf-8 -*-

import openerp
from openerp import netsvc, tools, pooler
from openerp.osv import fields, osv


class hr_extension(osv.osv):
    
    _name='hr.employee'
    
    _inherit='hr.employee'
    
    _columns = {
            'zied':fields.char('zied', size=64, required=True),
                    }
    
hr_extension()    