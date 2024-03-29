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
	account_currency_grand_total = 0
	company_currency_grand_total = 0
	for d in cs_data:
		row = frappe._dict({
			'name': d.name,
			'container_reference': d.container_reference,
			'conversion_rate': d.conversion_rate,
			'supplier' : d.supplier,
			'posting_date' : d.posting_date,
			'currency' : d.currency,
			'grand_total' : "%.3f" % round(d.grand_total, 3),
			'base_grand_total' : "%.3f" % round(d.base_grand_total, 3)
		})
		account_currency_grand_total += d.grand_total
		company_currency_grand_total += d.base_grand_total
		data.append(row)
		
	#total_grand_total += d.grand_total
	

	total_row = frappe._dict({
		'name': '',
		'container_reference': '',
		'supplier': '',
		'posting_date': '',
		'currency': '',
		'grand_total': '',
		'base_grand_total': '',
    })
	data.append(total_row)
	
	row2 = frappe._dict({
		'name': '',
		'container_reference': '',
		'supplier' : '',
		'posting_date' : "",
		'currency' : "Total",
		'grand_total' : "%.3f" % round(account_currency_grand_total, 3),
		'base_grand_total' :  "%.3f" % round(company_currency_grand_total, 3)
		
	},
	)
	data.append(total_row)
	row3 = frappe._dict({
		'name': '',
		'container_reference': 'Footer',
		'supplier' : " ",
		'posting_date' : "Account",
		'currency' : " ",
		'grand_total' : "Amount",
		'base_grand_total' : "Amount(CC)"
		
	},
	)
	data.append(row2)
	data.append(row3)
	landed_cost_list, total_grand_total, total_base_grand_total  = get_landed_cost(cs_data)
	if landed_cost_list:
		for landed_cost in landed_cost_list:
			row4 = frappe._dict(landed_cost)
			data.append(row4)
	grand_total_row = frappe._dict({
		'name': '',
		'container_reference': '',
		'supplier' : '',
		'posting_date' : "",
		'currency' : "Grand Total",
		'grand_total' : "%.3f" % round(account_currency_grand_total + total_grand_total, 3),
		'base_grand_total' : "%.3f" % round(company_currency_grand_total + total_base_grand_total, 3),	
	},
	)
	
	data.append(total_row)
	data.append(grand_total_row)

	
	
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
				"fieldtype": "Data",
				# "options": "Purchase Invoice",
				"width": 150,
				
			},
			{
				"label": _("Exchange Rate"),
				"fieldname": "conversion_rate",
				"fieldtype": "float",
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
	filters["docstatus"] = 1
	conditions = get_conditions(filters)
	data = frappe.get_all(
		doctype='Purchase Invoice',
		fields = ['name','container_reference','supplier','posting_date','conversion_rate','grand_total','base_grand_total','currency'],
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

def get_landed_cost(invoice_list):
	a = []
	total_grand_total = 0
	total_base_grand_total = 0
	for invoice in invoice_list:
		landed_cost_voucher = frappe.db.get_value("Landed Cost Purchase Receipt", {'receipt_document': invoice.name, 'docstatus': 1}, 'parent')
		landed_cost_accounts = frappe.db.sql("""select expense_account, amount, description from `tabLanded Cost Taxes and Charges` where parent = %s and docstatus = 1""", landed_cost_voucher, as_dict = 1)
		if landed_cost_accounts:
			for item in landed_cost_accounts:
				flag = False
				if len(a) > 0:
					for b in a:	
						if b["posting_date"] == item.expense_account:
							total_grand_total += item.amount
							total_base_grand_total += item.amount
							grand_total = float(b["grand_total"])
							grand_total += item.amount
							b["grand_total"] = "%.3f" % round(grand_total, 3)
							#b["grand_total"] += item.amount
							b["base_grand_total"] = b["grand_total"]
							flag = True
				if flag == False:
					total_grand_total += item.amount
					total_base_grand_total += item.amount
					a.append(
						{
							'name': '',
							'container_reference': item.description,
							'supplier' : "",
							'posting_date' : item.expense_account,
							'currency' : " ",
							'grand_total' : item.amount,
							'base_grand_total' : item.amount
						}
					)
	a.append(
		{
			'name': '',
			'container_reference': '',
			'supplier' : "",
			'posting_date' : '',
			'currency' : " ",
			'grand_total' : "%.3f" % round(total_grand_total, 3),
			'base_grand_total' : "%.3f" % round(total_base_grand_total, 3),
		}
	)
	return a, total_grand_total, total_base_grand_total