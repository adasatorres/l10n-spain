import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-l10n-spain",
    description="Meta package for oca-l10n-spain Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-l10n_es_account_asset>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_account_banking_sepa_fsdd>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_account_statement_import_n43>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod111>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod115>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod123>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod216>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod303>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod303_oss>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod347>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod349>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_mod390>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_partner_check>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_sii_oca>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_aeat_sii_oss>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_dua>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_dua_sii>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_facturae>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_igic>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_irnr>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_mis_report>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_partner>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_partner_mercantil>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_payment_order_confirming_aef>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_pos>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_ticketbai>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_ticketbai_api>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_ticketbai_api_batuz>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_ticketbai_batuz>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_toponyms>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_vat_book>=16.0dev,<16.1dev',
        'odoo-addon-l10n_es_vat_prorate>=16.0dev,<16.1dev',
        'odoo-addon-payment_redsys>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
