# -*- coding: utf-8 -*-

from odoo import models, fields


class OpenAcademyGroups(models.Model):
    _name = 'oa.groups'
    _description = 'oa.groups'

    name = fields.Char( required=True )
    description = fields.Text()

    courses_id = fields.Many2one(
        "oa.courses", 
        string="Course", 
        required=True
    )
