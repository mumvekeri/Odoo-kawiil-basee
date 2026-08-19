from odoo import models, fields


class LoanApplicationDocument(models.Model):
    _name = 'loan.application.document'
    _description = 'Loan Application Document'

    name = fields.Char(
        string='Name',
        required=True
    )

    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        string='State',
        default='new'
    )

    type_id = fields.Many2one(
        comodel_name='loan.application.document.type',
        string='Document Type',
        required=True
    )

    application_id = fields.Many2one(
        comodel_name='loan.application',
        string='Loan Application',
        required=True,
        ondelete='cascade'
    )

    attachment_id = fields.Many2one(
        comodel_name='ir.attachment',
        string='Attachment'
    )