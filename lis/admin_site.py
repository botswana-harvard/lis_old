from django.contrib.admin import AdminSite


class LisAdminSite(AdminSite):
    site_header = 'Lis'
    site_title = 'Lis'
    index_title = 'Lis Administration'
    site_url = '/lis/'


lis_admin = LisAdminSite(name='lis_admin')
