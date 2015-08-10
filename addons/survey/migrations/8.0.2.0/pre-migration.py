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

from openerp.openupgrade import openupgrade


column_renames = {
    'survey_question': [
        ('column_name', None),
        ('comment_column', None),
        ('comment_field_type', None),
        ('comment_label', None),
        ('comment_maximum_date', None),
        ('comment_maximum_float', None),
        ('comment_maximum_no', None),
        ('comment_minimum_date', None),
        ('comment_minimum_float', None),
        ('comment_minimum_no', None),
        ('comment_valid_err_msg', None),
        ('comment_valid_type', None),
        ('in_visible_answer_type', None),
        ('in_visible_menu_choice', None),
        ('in_visible_rating_weight', None),
        ('is_comment_require', None),
        ('make_comment_field_err_msg', None),
        ('maximum_req_ans', None),
        ('minimum_req_ans', None),
        ('no_of_rows', None),
        ('numeric_required_sum', None),
        ('numeric_required_sum_err_msg', None),
        ('rating_allow_one_column_require', None),
        ('req_ans', None),
        ('required_type', None),
        ('validation_maximum_date', None),
        ('validation_maximum_float', None),
        ('validation_maximum_no', None),
        ('validation_minimum_date', None),
        ('validation_minimum_float', None),
        ('validation_minimum_no', None),
        ('validation_type', None),
        ],
    }

xmlid_renames = [
    ]

model_renames = [
    ('survey','survey.survey'),
    ]

table_renames = [
    ('survey','survey_survey'),
    ]


@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_columns(cr, column_renames)
    openupgrade.rename_models(cr, model_renames)
    openupgrade.rename_tables(cr, table_renames)
    openupgrade.rename_xmlids(cr, xmlid_renames)
