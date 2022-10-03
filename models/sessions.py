# -*- coding: utf-8 -*-

from ast import If
from datetime import datetime, date, timedelta
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
    enddate = fields.Date(compute="_set_enddate")
    
    @api.depends("startdate", "duration")
    def _set_enddate(self):
        for rec in self:
            if rec.startdate and rec.duration:
                enddate = datetime.strptime(str(rec.startdate), "%Y-%m-%d") + timedelta(days=rec.duration)
                rec.enddate = enddate.strftime("%Y-%m-%d")
            else:
                rec.enddate = rec.startdate
        
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

    # Progress bar that shows percent of taken seats against the number of seats
    seats_taken = fields.Integer(compute="_compute_seats_taken")

    # Percent of taken seats
    @api.depends("seats", "partners_ids")
    def _compute_seats_taken(self):
        for rec in self:
            if rec.seats > 0:
                rec.seats_taken = (len(rec.partners_ids)*100) // rec.seats
            else:
                rec.seats_taken = 0

    # Instructor must not be among the attendees
    @api.constrains('partners_ids', 'instructor_id')
    def _check_attendees(self):
        for record in self:
            if record.instructor_id in record.partners_ids:
                raise ValidationError("The following person should not be among the attendees because he/she is the instructor.")
    
    # Seats number must not be negative or less than the number of attendees
    # Attendees must not exceed the seats number    
    @api.onchange('seats', 'partners_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats must not be negative",
                },
            }
        if self.seats < len(self.partners_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

