# -*- coding: utf-8 -*-

from odoo import models, fields


class OpenAcademyCourses(models.Model):
    _name = 'open_academy_courses.open_academy_courses'
    _description = 'open_academy_courses.open_academy_courses'

    name = fields.Char( required=True )
    description = fields.Text()
    type = fields.Selection(
        default='online',
        required=True, 
        selection=[
            ('online', 'Online'),
            ('face-to-face', 'Face-to-face'),
            ('blended', 'Blended')
        ]
    )
    availability = fields.Boolean( required=True, default=False )
    language = fields.Selection(
        required=True, 
        default='spanish',
        selection=[
            ('spanish', 'Spanish'),
            ('english', 'English'),
        ]
    )
    sessions_id = fields.One2many('open_academy_sessions.open_academy_sessions', 'courses_id', string='Sessions')
    groups_id = fields.One2many('open_academy_groups.open_academy_groups', 'courses_id', string='Groups')
