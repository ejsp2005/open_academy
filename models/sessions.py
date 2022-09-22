# -*- coding: utf-8 -*-

from ast import If
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class OpenAcademySessions(models.Model):
    _name = 'oa.sessions'
    _description = 'oa.sessions'

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
    courses_id = fields.Many2one(
        "oa.courses", 
        string="Course", 
        required=True
    )
    active = fields.Boolean(default=True)
    
    seats = fields.Integer()
    
    # Attendees
    partners_ids = fields.Many2many("res.partner")

    # Seats taken must not exceed the seats number    
    @api.constrains('partners_ids')
    def _check_seats_taken(self):
        for record in self:
            if len(record.partners_ids) > record.seats:
                raise ValidationError("Number of seats must be up to: %s" % record.seats)
    

    # Progress bar that shows percent of taken seats against the number of seats    
    seats_taken = fields.Integer(compute="_compute_seats_taken")
    
    @api.onchange("partners_ids")
    def _compute_seats_taken(self):
        for record in self:
            record.seats_taken = (len(record.partners_ids)*100) // record.seats

    # Instructor must not be among the attendees
    @api.constrains('partners_ids', 'instructor')
    def _check_attendees(self):
        for record in self:
            if record.instructor == record.partners_ids:
                raise ValidationError("The following person should not be among the attendees because he/she is the instructor: %s" % record.instructor)
    

