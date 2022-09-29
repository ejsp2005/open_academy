# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
# seed the pseudorandom number generator
from random import seed, random

class OpenAcademyCourses(models.Model):
    _name = 'oa.courses'
    _description = 'oa.courses'

    def _get_random_name ():
        # seed random number generator
        seed(random()*10)
        # generate some random numbers
        
        return "course_name_" + str(int(random() * 10000))
    
    name = fields.Char( 
        required=True, 
        copy=False, 
        default=_get_random_name() 
    )
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

    # @api.constrains('name', 'description')
    # def _check_seats_taken(self):
    #     for record in self:
    #         if record.name == record.description:
    #             raise ValidationError("The name and description of the course must be different.")
    
    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'The title of the course must be unique.'),
        ('name_description_check', 'CHECK(name != description)', "The title and description of the course must be different.")
    ]
    