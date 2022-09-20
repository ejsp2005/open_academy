# -*- coding: utf-8 -*-

from odoo import models, fields


class OpenAcademyGroups(models.Model):
    _name = 'open_academy_groups.open_academy_groups'
    _description = 'open_academy_groups.open_academy_groups'

    name = fields.Char( required=True )
    description = fields.Text()

    courses_id = fields.Many2one(
        "open_academy_courses.open_academy_courses", 
        string="Course", 
        required=True
    )
