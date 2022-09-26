# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class OpenAcademyCourses(models.Model):
    _name = 'oa.courses'
    _description = 'oa.courses'

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
    availability = fields.Boolean( 
        required=True, 
        default=False 
    )
    language = fields.Selection(
        required=True, 
        default='spanish',
        selection=[
            ('spanish', 'Spanish'),
            ('english', 'English'),
        ]
    )
    responsible_id = fields.Many2one(
        "res.users", 
        string="Responsible user"
    )
    sessions_id = fields.One2many(
        'oa.sessions', 
        'courses_id', 
        string='Sessions'
    )
    # groups_id = fields.One2many(
    #     'oa.groups', 
    #     'courses_id', 
    #     string='Groups'
    # )

    @api.constrains('name', 'description')
    def _check_seats_taken(self):
        for record in self:
            if record.name == record.description:
                raise ValidationError("The name and description of the course must be different.")