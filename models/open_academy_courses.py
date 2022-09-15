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
            ('portuguese', 'Portuguese'),
            ('french', 'French'),
            ('german', 'German'),
            ('japanese', 'Japanese'),
            ('chinese', 'Chinese'),
            ('arab', 'Arab'),
            ('russian', 'Russian'),
            ('chinese', 'Chinese'),
            ('turkish', 'Turkish'),
            ('korean', 'Korean')
        ]
    )
    startdate = fields.Date(
        copy=False, 
        required=True,
        default=lambda self: fields.Date.add(fields.Date.today(), days=15)
    )
    enddate = fields.Date(
        copy=False, 
        required=True,
        default=lambda self: fields.Date.add(fields.Date.today(), days=25)
    )