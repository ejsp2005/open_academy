# -*- coding: utf-8 -*-

from odoo import models, fields


class OpenAcademySessions(models.Model):
    _name = 'open_academy_sessions.open_academy_sessions'
    _description = 'open_academy_sessions.open_academy_sessions'

    name = fields.Char( required=True )
    startdate = fields.Date(
        copy=False, 
        required=True,
        default=lambda self: fields.Date.add(fields.Date.today(), days=15)
    )
    duration = fields.Integer(
        copy=False, 
        required=True,
        default=10
    )
    instructor_id = fields.Many2one(
        "res.partner", 
        string="Instructor"
    )
    seats = fields.Integer()
    
    courses_id = fields.Many2one(
        "open_academy_courses.open_academy_courses", 
        string="Course", 
        required=True
    )
    # Attendees
    partners_ids = fields.Many2many("res.partner")
