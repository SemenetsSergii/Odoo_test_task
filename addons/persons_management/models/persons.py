from odoo import models, fields, api
from datetime import date


class Person(models.Model):
    _name = "persons.person"
    _description = "Person"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(
        string="Full Name", compute="_compute_full_name", store=True
    )
    birthday = fields.Date(string="Birthday")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    sex = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("non_binary", "Non-binary")],
        string="Sex",
        required=True,
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for person in self:
            person.full_name = (
                f"{person.first_name or ''}" f" {person.last_name or ''}"
            ).strip()

    @api.depends("birthday")
    def _compute_age(self):
        for person in self:
            if person.birthday:
                today = date.today()
                birth_date = person.birthday
                person.age = (
                    today.year
                    - birth_date.year
                    - (
                            (today.month, today.day)
                            <
                            (birth_date.month, birth_date.day))
                )
            else:
                person.age = 0
