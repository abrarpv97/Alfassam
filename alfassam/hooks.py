from . import __version__ as app_version
from alfassam.period_closing_voucher_custom import PeriodClosingVoucher

app_name = "alfassam"
app_title = "Alfassam"
app_publisher = "sastechnologies"
app_description = "CUstomized app for ERPNext"
app_email = "info@sastechnologies.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/alfassam/css/alfassam.css"
# app_include_js = "/assets/alfassam/js/alfassam.js"

# include js, css files in header of web template
# web_include_css = "/assets/alfassam/css/alfassam.css"
# web_include_js = "/assets/alfassam/js/alfassam.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "alfassam/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "alfassam.utils.jinja_methods",
#	"filters": "alfassam.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "alfassam.install.before_install"
# after_install = "alfassam.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "alfassam.uninstall.before_uninstall"
# after_uninstall = "alfassam.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "alfassam.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events


doc_events = {
	"Journal Entry": {
		"autoname": "alfassam.alfassam.hooks.journal_entry.autoname",
        "validate": "alfassam.alfassam.hooks.journal_entry.validate",
	},
    "Item Price":{
        "on_update": "alfassam.alfassam.hooks.item_price.on_update"
    },
    "Item":{
        "validate": "alfassam.alfassam.hooks.item.validate"
    }
}

fixtures = [
    {
        "doctype": "Custom Field",
		"filters": {
			"name": ("in", (
				"Journal Entry-cost_center",
                "Item-supplier",
                "Journal Entry-division",
                "Period Closing Voucher-cost_center",
                "Purchase Order Item-part_no",
                "Item-part_no",
                "Purchase Invoice-container_reference",
                "Purchase Invoice-finished_items",
                "Purchase Invoice-finished_goods",
                "Purchase Order-remarks",
                "Quotation-remarks"
            ))
        }
    },
    {
        "doctype": "Translation",
		"filters": {
			"source_text": ("in", (
				"Cost Center"
            ))
        }
    }
]

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"alfassam.tasks.all"
#	],
#	"daily": [
#		"alfassam.tasks.daily"
#	],
#	"hourly": [
#		"alfassam.tasks.hourly"
#	],
#	"weekly": [
#		"alfassam.tasks.weekly"
#	],
#	"monthly": [
#		"alfassam.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "alfassam.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "alfassam.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "alfassam.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"alfassam.auth.validate"
# ]
