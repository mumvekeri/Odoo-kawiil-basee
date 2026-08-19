    from odoo import models, fields


class LoanApplicationDocumentType(models.Model):
    _name = 'loan.application.document.type'
    _description = 'Loan Application Document Type'

    name = fields.Char(
        string='Name',
        required=True
    )

    is_required = fields.Boolean(
        string='Required'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )