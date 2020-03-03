from __future__ import unicode_literals
from frappe import _
import frappe

def get_data():
	return [
		{
			"label": _("Inbob Reports"),
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Inbob General Ledger",
					"doctype": "GL Entry"
				},
								{
					"type": "report",
					"is_query_report": True,
					"name": "Inbob Sales Person Commission Summary",
					"doctype": "Sales Order"
				}
			]
		}
	
	]