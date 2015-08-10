# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 ONESTEiN B.V.
#              (C) 2014 Therp B.V.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
from openerp.openupgrade import openupgrade


logger = logging.getLogger('OpenUpgrade.stock')

column_renames = {
    'hr_applicant': [
        ('response', 'response_id'),
    ],
}
# 
# def update_hr_applicant_response(cr, registry):
#     """ 
#     """
#     hr_att_obj = registry['hr.applicant']
#     user_input_obj = registry['survey.user_input']
#     for att in hr_att_obj.browse(cr, uid, hr_att_obj.search(cr, uid, [])):
#         if att.response_id == 0:
#             resp = False
#             if att.survey and att.survey.id:
#                 user_input_ids = user_input_obj.search(cr, uid, [('survey_id', '=', att.survey.id)])
#                 if user_input_ids:
#                     resp = user_input_ids[0]
#             att.write({'response_id': resp})

def update_response_zero(cr):
    """
    """
    #q1 = cr.execute('select id, job_id from hr_applicant where response_id is not null')
    openupgrade.logged_query(cr, """update hr_applicant set response=null where response=0;""")
    
@openupgrade.migrate()
def migrate(cr, version):
    update_response_zero(cr)
    openupgrade.rename_columns(cr, column_renames)
#     create_stock_move_fields(cr)    