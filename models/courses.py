# -*- coding: utf-8 -*-

from fnmatch import translate
from odoo import models, fields, api, _
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
        
        return _("course_name_") + str(int(random() * 10000))
    
    name = fields.Char( 
        required=True, 
        copy=False, 
        translate=True,
        default=_get_random_name() 
    )
    description = fields.Text(translate=True)
    type = fields.Selection(
        default='online',
        required=True, 
        selection=[
            ('online', _('Online')),
            ('face-to-face', _('Face-to-face')),
            ('blended', _('Blended'))
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
            ('spanish', _('Spanish')),
            ('english', _('English')),
        ]
    )
    responsible_id = fields.Many2one(
        "res.users", 
        string=_("Responsible user")
    )
    sessions_id = fields.One2many(
        'oa.sessions', 
        'courses_id', 
        string=_('Sessions')
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
        ('name_unique', 'UNIQUE(name)', _('The title of the course must be unique.')),
        ('name_description_check', 'CHECK(name != description)', _("The title and description of the course must be different."))
    ]
    