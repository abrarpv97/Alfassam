# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint



def execute(filters=None):
	if not filters: filters = {}

	data, columns = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		msgprint(_('No records found'))
		return columns, cs_data

	data = []
	for d in cs_data:
		row = frappe._dict({
				'name': d.name,
				'container_reference': d.container_reference,
				'supplier' : d.supplier,
				'posting_date' : d.posting_date,
				'grand_total' : d.grand_total,
				'base_grand_total' : d.base_grand_total,
				'currency' : d.currency,
			})
		
	# 	total_grand_total += d.grand_total
		data.append(row)

	# total_row = frappe._dict({
	# 			'name': '',
	# 			'container_reference': '',
	# 			'supplier': '',
	# 			'posting_date': '',
	# 			'grand_total': total_grand_total,
	# 			'base_grand_total': '',
	# 			'currency': '',
    # })
	# data.append(total_row)
	
	# row2 = frappe._dict({
	# 				'name': '',
	# 				'container_reference': '',
	# 				'supplier' : '',
	# 				'posting_date' : "",
	# 				'grand_total' : "",
	# 				'base_grand_total' : '',
	# 				'currency' : '',
	# 			})
	# data.append(row2)

	# row3 = frappe._dict({
	# 				'name': '',
	# 				'container_reference': '',
	# 				'supplier' : '',
	# 				'posting_date' : "total",
	# 				'grand_total' : 1000,
	# 				'base_grand_total' : '',
	# 				'currency' : '',
	# 			})
	# data.append(row3)
	
	return columns, data, None

def get_columns():
	return [
			{
				"label": _("ID"),
				"fieldname": "name",
				"fieldtype": "Link",
				"options": "Purchase Invoice",
				"width": 200,
				
			},
			{
				"label": _("Supplier"),
				"fieldname": "supplier",
				"fieldtype": "Link",
				"options": "Purchase Invoice",
				"width": 150,
				
			},
			{
				"label": _("Date"),
				"fieldname": "posting_date",
				"fieldtype": "date",
				"options": "Purchase Invoice",
				"width": 150,
				
			},
			{
				'fieldname': 'container_reference',
				'label': _('Container Reference'),
				'fieldtype': 'Data',
				'width': '120'
			},
			{
			"label": _("Currency"),
				"fieldname": "currency",
				"fieldtype": "date",
				"options": "Purchase Invoice",
				"width": 150,
			},
			{
				"label": _("Grand Total"),
				"fieldname": "grand_total",
				"fieldtype": "date",
				"options": "Purchase Invoice",
				"width": 150,
				
			},
			{
			"label": _("Grand Total (Company Currency)"),
				"fieldname": "base_grand_total",
				"fieldtype": "date",
				"options": "Purchase Invoice",
				"width": 150,
			},
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype='Purchase Invoice',
		fields = ['name','container_reference','supplier','posting_date','grand_total','base_grand_total','currency'],
		filters=conditions,
		# order_by='name desc'
	)
	return data
	
def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value

	return conditions