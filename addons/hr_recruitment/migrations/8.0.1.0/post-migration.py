# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, a suite of business apps
#    This module Copyright (C) 2014 Therp BV (<http://therp.nl>).
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

from openerp.modules.registry import RegistryManager
from openerp import SUPERUSER_ID as uid
from openerp.openupgrade import openupgrade, openupgrade_80


def update_hr_applicant_response(cr, registry):
    """ 
    """
    hr_att_obj = registry['hr.applicant']
    user_input_obj = registry['survey.user_input']
    for att in hr_att_obj.browse(cr, uid, hr_att_obj.search(cr, uid, [])):
        if att.response_id == 0:
            resp = False
            if att.survey and att.survey.id:
                user_input_ids = user_input_obj.search(cr, uid, [('survey_id', '=', att.survey.id)])
                if user_input_ids:
                    resp = user_input_ids[0]
            att.write({'response_id': resp})


@openupgrade.migrate()
def migrate(cr, version):
    """
    """
    registry = RegistryManager.get(cr.dbname)
    update_hr_applicant_response(cr, registry)