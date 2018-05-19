from setuptools import setup

setup(
    name='sismos',
    version='1',
    packages=['Lib.distutils', 'Lib.encodings', 'Lib.importlib', 'Lib.collections', 'Lib.site-packages.pip',
              'Lib.site-packages.pip._vendor', 'Lib.site-packages.pip._vendor.idna',
              'Lib.site-packages.pip._vendor.pytoml', 'Lib.site-packages.pip._vendor.certifi',
              'Lib.site-packages.pip._vendor.chardet', 'Lib.site-packages.pip._vendor.chardet.cli',
              'Lib.site-packages.pip._vendor.distlib', 'Lib.site-packages.pip._vendor.distlib._backport',
              'Lib.site-packages.pip._vendor.msgpack', 'Lib.site-packages.pip._vendor.urllib3',
              'Lib.site-packages.pip._vendor.urllib3.util', 'Lib.site-packages.pip._vendor.urllib3.contrib',
              'Lib.site-packages.pip._vendor.urllib3.contrib._securetransport',
              'Lib.site-packages.pip._vendor.urllib3.packages',
              'Lib.site-packages.pip._vendor.urllib3.packages.backports',
              'Lib.site-packages.pip._vendor.urllib3.packages.ssl_match_hostname',
              'Lib.site-packages.pip._vendor.colorama', 'Lib.site-packages.pip._vendor.html5lib',
              'Lib.site-packages.pip._vendor.html5lib._trie', 'Lib.site-packages.pip._vendor.html5lib.filters',
              'Lib.site-packages.pip._vendor.html5lib.treewalkers',
              'Lib.site-packages.pip._vendor.html5lib.treeadapters',
              'Lib.site-packages.pip._vendor.html5lib.treebuilders', 'Lib.site-packages.pip._vendor.lockfile',
              'Lib.site-packages.pip._vendor.progress', 'Lib.site-packages.pip._vendor.requests',
              'Lib.site-packages.pip._vendor.packaging', 'Lib.site-packages.pip._vendor.cachecontrol',
              'Lib.site-packages.pip._vendor.cachecontrol.caches', 'Lib.site-packages.pip._vendor.webencodings',
              'Lib.site-packages.pip._vendor.pkg_resources', 'Lib.site-packages.pip._internal',
              'Lib.site-packages.pip._internal.req', 'Lib.site-packages.pip._internal.vcs',
              'Lib.site-packages.pip._internal.utils', 'Lib.site-packages.pip._internal.models',
              'Lib.site-packages.pip._internal.commands', 'Lib.site-packages.pip._internal.operations',
              'Lib.site-packages.nose', 'Lib.site-packages.nose.ext', 'Lib.site-packages.nose.tools',
              'Lib.site-packages.nose.sphinx', 'Lib.site-packages.nose.plugins', 'Lib.site-packages.faker',
              'Lib.site-packages.faker.utils', 'Lib.site-packages.faker.providers',
              'Lib.site-packages.faker.providers.job', 'Lib.site-packages.faker.providers.job.ar_AA',
              'Lib.site-packages.faker.providers.job.en_US', 'Lib.site-packages.faker.providers.job.fa_IR',
              'Lib.site-packages.faker.providers.job.fi_FI', 'Lib.site-packages.faker.providers.job.fr_CH',
              'Lib.site-packages.faker.providers.job.fr_FR', 'Lib.site-packages.faker.providers.job.hr_HR',
              'Lib.site-packages.faker.providers.job.hu_HU', 'Lib.site-packages.faker.providers.job.ko_KR',
              'Lib.site-packages.faker.providers.job.pl_PL', 'Lib.site-packages.faker.providers.job.pt_BR',
              'Lib.site-packages.faker.providers.job.ru_RU', 'Lib.site-packages.faker.providers.job.uk_UA',
              'Lib.site-packages.faker.providers.job.zh_TW', 'Lib.site-packages.faker.providers.ssn',
              'Lib.site-packages.faker.providers.ssn.en_CA', 'Lib.site-packages.faker.providers.ssn.en_GB',
              'Lib.site-packages.faker.providers.ssn.en_US', 'Lib.site-packages.faker.providers.ssn.et_EE',
              'Lib.site-packages.faker.providers.ssn.fi_FI', 'Lib.site-packages.faker.providers.ssn.fr_CH',
              'Lib.site-packages.faker.providers.ssn.he_IL', 'Lib.site-packages.faker.providers.ssn.hr_HR',
              'Lib.site-packages.faker.providers.ssn.hu_HU', 'Lib.site-packages.faker.providers.ssn.it_IT',
              'Lib.site-packages.faker.providers.ssn.ko_KR', 'Lib.site-packages.faker.providers.ssn.nl_BE',
              'Lib.site-packages.faker.providers.ssn.nl_NL', 'Lib.site-packages.faker.providers.ssn.no_NO',
              'Lib.site-packages.faker.providers.ssn.pl_PL', 'Lib.site-packages.faker.providers.ssn.pt_BR',
              'Lib.site-packages.faker.providers.ssn.ru_RU', 'Lib.site-packages.faker.providers.ssn.sv_SE',
              'Lib.site-packages.faker.providers.ssn.uk_UA', 'Lib.site-packages.faker.providers.ssn.zh_CN',
              'Lib.site-packages.faker.providers.ssn.zh_TW', 'Lib.site-packages.faker.providers.bank',
              'Lib.site-packages.faker.providers.bank.de_AT', 'Lib.site-packages.faker.providers.bank.de_DE',
              'Lib.site-packages.faker.providers.bank.en_GB', 'Lib.site-packages.faker.providers.bank.fr_FR',
              'Lib.site-packages.faker.providers.bank.it_IT', 'Lib.site-packages.faker.providers.bank.nl_NL',
              'Lib.site-packages.faker.providers.bank.no_NO', 'Lib.site-packages.faker.providers.file',
              'Lib.site-packages.faker.providers.file.en_US', 'Lib.site-packages.faker.providers.isbn',
              'Lib.site-packages.faker.providers.isbn.en_US', 'Lib.site-packages.faker.providers.misc',
              'Lib.site-packages.faker.providers.misc.en_US', 'Lib.site-packages.faker.providers.color',
              'Lib.site-packages.faker.providers.color.ar_PS', 'Lib.site-packages.faker.providers.color.en_US',
              'Lib.site-packages.faker.providers.color.fr_FR', 'Lib.site-packages.faker.providers.color.hr_HR',
              'Lib.site-packages.faker.providers.color.hu_HU', 'Lib.site-packages.faker.providers.color.pt_BR',
              'Lib.site-packages.faker.providers.color.ru_RU', 'Lib.site-packages.faker.providers.color.uk_UA',
              'Lib.site-packages.faker.providers.lorem', 'Lib.site-packages.faker.providers.lorem.la',
              'Lib.site-packages.faker.providers.lorem.ar_AA', 'Lib.site-packages.faker.providers.lorem.el_GR',
              'Lib.site-packages.faker.providers.lorem.en_US', 'Lib.site-packages.faker.providers.lorem.he_IL',
              'Lib.site-packages.faker.providers.lorem.ja_JP', 'Lib.site-packages.faker.providers.lorem.ru_RU',
              'Lib.site-packages.faker.providers.lorem.zh_CN', 'Lib.site-packages.faker.providers.lorem.zh_TW',
              'Lib.site-packages.faker.providers.person', 'Lib.site-packages.faker.providers.person.en',
              'Lib.site-packages.faker.providers.person.ar_AA', 'Lib.site-packages.faker.providers.person.ar_PS',
              'Lib.site-packages.faker.providers.person.ar_SA', 'Lib.site-packages.faker.providers.person.bg_BG',
              'Lib.site-packages.faker.providers.person.cs_CZ', 'Lib.site-packages.faker.providers.person.de_AT',
              'Lib.site-packages.faker.providers.person.de_CH', 'Lib.site-packages.faker.providers.person.de_DE',
              'Lib.site-packages.faker.providers.person.dk_DK', 'Lib.site-packages.faker.providers.person.el_GR',
              'Lib.site-packages.faker.providers.person.en_GB', 'Lib.site-packages.faker.providers.person.en_TH',
              'Lib.site-packages.faker.providers.person.en_US', 'Lib.site-packages.faker.providers.person.es_ES',
              'Lib.site-packages.faker.providers.person.es_MX', 'Lib.site-packages.faker.providers.person.et_EE',
              'Lib.site-packages.faker.providers.person.fa_IR', 'Lib.site-packages.faker.providers.person.fi_FI',
              'Lib.site-packages.faker.providers.person.fr_CH', 'Lib.site-packages.faker.providers.person.fr_FR',
              'Lib.site-packages.faker.providers.person.he_IL', 'Lib.site-packages.faker.providers.person.hi_IN',
              'Lib.site-packages.faker.providers.person.hr_HR', 'Lib.site-packages.faker.providers.person.hu_HU',
              'Lib.site-packages.faker.providers.person.id_ID', 'Lib.site-packages.faker.providers.person.it_IT',
              'Lib.site-packages.faker.providers.person.ja_JP', 'Lib.site-packages.faker.providers.person.ka_GE',
              'Lib.site-packages.faker.providers.person.ko_KR', 'Lib.site-packages.faker.providers.person.lt_LT',
              'Lib.site-packages.faker.providers.person.lv_LV', 'Lib.site-packages.faker.providers.person.ne_NP',
              'Lib.site-packages.faker.providers.person.nl_NL', 'Lib.site-packages.faker.providers.person.no_NO',
              'Lib.site-packages.faker.providers.person.pl_PL', 'Lib.site-packages.faker.providers.person.pt_BR',
              'Lib.site-packages.faker.providers.person.pt_PT', 'Lib.site-packages.faker.providers.person.ro_RO',
              'Lib.site-packages.faker.providers.person.ru_RU', 'Lib.site-packages.faker.providers.person.sl_SI',
              'Lib.site-packages.faker.providers.person.sv_SE', 'Lib.site-packages.faker.providers.person.th_TH',
              'Lib.site-packages.faker.providers.person.tr_TR', 'Lib.site-packages.faker.providers.person.tw_GH',
              'Lib.site-packages.faker.providers.person.uk_UA', 'Lib.site-packages.faker.providers.person.zh_CN',
              'Lib.site-packages.faker.providers.person.zh_TW', 'Lib.site-packages.faker.providers.python',
              'Lib.site-packages.faker.providers.python.en_US', 'Lib.site-packages.faker.providers.address',
              'Lib.site-packages.faker.providers.address.en', 'Lib.site-packages.faker.providers.address.es',
              'Lib.site-packages.faker.providers.address.cs_CZ', 'Lib.site-packages.faker.providers.address.de_AT',
              'Lib.site-packages.faker.providers.address.de_DE', 'Lib.site-packages.faker.providers.address.el_GR',
              'Lib.site-packages.faker.providers.address.en_AU', 'Lib.site-packages.faker.providers.address.en_CA',
              'Lib.site-packages.faker.providers.address.en_GB', 'Lib.site-packages.faker.providers.address.en_US',
              'Lib.site-packages.faker.providers.address.es_ES', 'Lib.site-packages.faker.providers.address.es_MX',
              'Lib.site-packages.faker.providers.address.fa_IR', 'Lib.site-packages.faker.providers.address.fi_FI',
              'Lib.site-packages.faker.providers.address.fr_CH', 'Lib.site-packages.faker.providers.address.fr_FR',
              'Lib.site-packages.faker.providers.address.he_IL', 'Lib.site-packages.faker.providers.address.hi_IN',
              'Lib.site-packages.faker.providers.address.hr_HR', 'Lib.site-packages.faker.providers.address.hu_HU',
              'Lib.site-packages.faker.providers.address.id_ID', 'Lib.site-packages.faker.providers.address.it_IT',
              'Lib.site-packages.faker.providers.address.ja_JP', 'Lib.site-packages.faker.providers.address.ka_GE',
              'Lib.site-packages.faker.providers.address.ko_KR', 'Lib.site-packages.faker.providers.address.ne_NP',
              'Lib.site-packages.faker.providers.address.nl_BE', 'Lib.site-packages.faker.providers.address.nl_NL',
              'Lib.site-packages.faker.providers.address.no_NO', 'Lib.site-packages.faker.providers.address.pl_PL',
              'Lib.site-packages.faker.providers.address.pt_BR', 'Lib.site-packages.faker.providers.address.pt_PT',
              'Lib.site-packages.faker.providers.address.ru_RU', 'Lib.site-packages.faker.providers.address.sk_SK',
              'Lib.site-packages.faker.providers.address.sl_SI', 'Lib.site-packages.faker.providers.address.sv_SE',
              'Lib.site-packages.faker.providers.address.uk_UA', 'Lib.site-packages.faker.providers.address.zh_CN',
              'Lib.site-packages.faker.providers.address.zh_TW', 'Lib.site-packages.faker.providers.barcode',
              'Lib.site-packages.faker.providers.barcode.en_US', 'Lib.site-packages.faker.providers.company',
              'Lib.site-packages.faker.providers.company.bg_BG', 'Lib.site-packages.faker.providers.company.cs_CZ',
              'Lib.site-packages.faker.providers.company.de_DE', 'Lib.site-packages.faker.providers.company.en_US',
              'Lib.site-packages.faker.providers.company.es_MX', 'Lib.site-packages.faker.providers.company.fa_IR',
              'Lib.site-packages.faker.providers.company.fi_FI', 'Lib.site-packages.faker.providers.company.fr_CH',
              'Lib.site-packages.faker.providers.company.fr_FR', 'Lib.site-packages.faker.providers.company.hr_HR',
              'Lib.site-packages.faker.providers.company.hu_HU', 'Lib.site-packages.faker.providers.company.id_ID',
              'Lib.site-packages.faker.providers.company.it_IT', 'Lib.site-packages.faker.providers.company.ja_JP',
              'Lib.site-packages.faker.providers.company.ko_KR', 'Lib.site-packages.faker.providers.company.no_NO',
              'Lib.site-packages.faker.providers.company.pl_PL', 'Lib.site-packages.faker.providers.company.pt_BR',
              'Lib.site-packages.faker.providers.company.pt_PT', 'Lib.site-packages.faker.providers.company.ru_RU',
              'Lib.site-packages.faker.providers.company.sk_SK', 'Lib.site-packages.faker.providers.company.sl_SI',
              'Lib.site-packages.faker.providers.company.sv_SE', 'Lib.site-packages.faker.providers.company.zh_CN',
              'Lib.site-packages.faker.providers.company.zh_TW', 'Lib.site-packages.faker.providers.profile',
              'Lib.site-packages.faker.providers.profile.en_US', 'Lib.site-packages.faker.providers.currency',
              'Lib.site-packages.faker.providers.currency.en_US', 'Lib.site-packages.faker.providers.internet',
              'Lib.site-packages.faker.providers.internet.ar_AA', 'Lib.site-packages.faker.providers.internet.bg_BG',
              'Lib.site-packages.faker.providers.internet.bs_BA', 'Lib.site-packages.faker.providers.internet.cs_CZ',
              'Lib.site-packages.faker.providers.internet.de_AT', 'Lib.site-packages.faker.providers.internet.de_DE',
              'Lib.site-packages.faker.providers.internet.el_GR', 'Lib.site-packages.faker.providers.internet.en_AU',
              'Lib.site-packages.faker.providers.internet.en_US', 'Lib.site-packages.faker.providers.internet.fa_IR',
              'Lib.site-packages.faker.providers.internet.fi_FI', 'Lib.site-packages.faker.providers.internet.fr_CH',
              'Lib.site-packages.faker.providers.internet.fr_FR', 'Lib.site-packages.faker.providers.internet.hr_HR',
              'Lib.site-packages.faker.providers.internet.hu_HU', 'Lib.site-packages.faker.providers.internet.id_ID',
              'Lib.site-packages.faker.providers.internet.it_IT', 'Lib.site-packages.faker.providers.internet.ja_JP',
              'Lib.site-packages.faker.providers.internet.ko_KR', 'Lib.site-packages.faker.providers.internet.no_NO',
              'Lib.site-packages.faker.providers.internet.pl_PL', 'Lib.site-packages.faker.providers.internet.pt_BR',
              'Lib.site-packages.faker.providers.internet.pt_PT', 'Lib.site-packages.faker.providers.internet.ru_RU',
              'Lib.site-packages.faker.providers.internet.sk_SK', 'Lib.site-packages.faker.providers.internet.sl_SI',
              'Lib.site-packages.faker.providers.internet.sv_SE', 'Lib.site-packages.faker.providers.internet.uk_UA',
              'Lib.site-packages.faker.providers.internet.zh_CN', 'Lib.site-packages.faker.providers.internet.zh_TW',
              'Lib.site-packages.faker.providers.date_time', 'Lib.site-packages.faker.providers.date_time.ar_AA',
              'Lib.site-packages.faker.providers.date_time.ar_EG', 'Lib.site-packages.faker.providers.date_time.en_US',
              'Lib.site-packages.faker.providers.date_time.fr_FR', 'Lib.site-packages.faker.providers.date_time.hr_HR',
              'Lib.site-packages.faker.providers.date_time.hu_HU', 'Lib.site-packages.faker.providers.date_time.id_ID',
              'Lib.site-packages.faker.providers.date_time.ko_KR', 'Lib.site-packages.faker.providers.date_time.pl_PL',
              'Lib.site-packages.faker.providers.date_time.ru_RU', 'Lib.site-packages.faker.providers.date_time.sl_SI',
              'Lib.site-packages.faker.providers.automotive', 'Lib.site-packages.faker.providers.automotive.ar_JO',
              'Lib.site-packages.faker.providers.automotive.ar_PS',
              'Lib.site-packages.faker.providers.automotive.ar_SA',
              'Lib.site-packages.faker.providers.automotive.de_DE',
              'Lib.site-packages.faker.providers.automotive.en_CA',
              'Lib.site-packages.faker.providers.automotive.en_GB',
              'Lib.site-packages.faker.providers.automotive.en_US',
              'Lib.site-packages.faker.providers.automotive.hu_HU',
              'Lib.site-packages.faker.providers.automotive.id_ID',
              'Lib.site-packages.faker.providers.automotive.pt_BR', 'Lib.site-packages.faker.providers.user_agent',
              'Lib.site-packages.faker.providers.user_agent.en_US', 'Lib.site-packages.faker.providers.credit_card',
              'Lib.site-packages.faker.providers.credit_card.en_US', 'Lib.site-packages.faker.providers.phone_number',
              'Lib.site-packages.faker.providers.phone_number.ar_JO',
              'Lib.site-packages.faker.providers.phone_number.ar_PS',
              'Lib.site-packages.faker.providers.phone_number.bg_BG',
              'Lib.site-packages.faker.providers.phone_number.bs_BA',
              'Lib.site-packages.faker.providers.phone_number.cs_CZ',
              'Lib.site-packages.faker.providers.phone_number.de_DE',
              'Lib.site-packages.faker.providers.phone_number.dk_DK',
              'Lib.site-packages.faker.providers.phone_number.el_GR',
              'Lib.site-packages.faker.providers.phone_number.en_AU',
              'Lib.site-packages.faker.providers.phone_number.en_CA',
              'Lib.site-packages.faker.providers.phone_number.en_GB',
              'Lib.site-packages.faker.providers.phone_number.en_US',
              'Lib.site-packages.faker.providers.phone_number.es_ES',
              'Lib.site-packages.faker.providers.phone_number.es_MX',
              'Lib.site-packages.faker.providers.phone_number.fa_IR',
              'Lib.site-packages.faker.providers.phone_number.fi_FI',
              'Lib.site-packages.faker.providers.phone_number.fr_CH',
              'Lib.site-packages.faker.providers.phone_number.fr_FR',
              'Lib.site-packages.faker.providers.phone_number.he_IL',
              'Lib.site-packages.faker.providers.phone_number.hi_IN',
              'Lib.site-packages.faker.providers.phone_number.hr_HR',
              'Lib.site-packages.faker.providers.phone_number.hu_HU',
              'Lib.site-packages.faker.providers.phone_number.id_ID',
              'Lib.site-packages.faker.providers.phone_number.it_IT',
              'Lib.site-packages.faker.providers.phone_number.ja_JP',
              'Lib.site-packages.faker.providers.phone_number.ko_KR',
              'Lib.site-packages.faker.providers.phone_number.lt_LT',
              'Lib.site-packages.faker.providers.phone_number.lv_LV',
              'Lib.site-packages.faker.providers.phone_number.ne_NP',
              'Lib.site-packages.faker.providers.phone_number.nl_BE',
              'Lib.site-packages.faker.providers.phone_number.nl_NL',
              'Lib.site-packages.faker.providers.phone_number.no_NO',
              'Lib.site-packages.faker.providers.phone_number.pl_PL',
              'Lib.site-packages.faker.providers.phone_number.pt_BR',
              'Lib.site-packages.faker.providers.phone_number.pt_PT',
              'Lib.site-packages.faker.providers.phone_number.ru_RU',
              'Lib.site-packages.faker.providers.phone_number.sk_SK',
              'Lib.site-packages.faker.providers.phone_number.sl_SI',
              'Lib.site-packages.faker.providers.phone_number.sv_SE',
              'Lib.site-packages.faker.providers.phone_number.tr_TR',
              'Lib.site-packages.faker.providers.phone_number.tw_GH',
              'Lib.site-packages.faker.providers.phone_number.uk_UA',
              'Lib.site-packages.faker.providers.phone_number.zh_CN',
              'Lib.site-packages.faker.providers.phone_number.zh_TW', 'Lib.site-packages.wheel',
              'Lib.site-packages.wheel.tool', 'Lib.site-packages.wheel.signatures', 'Lib.site-packages.colorama',
              'Lib.site-packages.dateutil', 'Lib.site-packages.dateutil.tz', 'Lib.site-packages.dateutil.parser',
              'Lib.site-packages.dateutil.zoneinfo', 'Lib.site-packages.setuptools',
              'Lib.site-packages.setuptools.extern', 'Lib.site-packages.setuptools._vendor',
              'Lib.site-packages.setuptools._vendor.packaging', 'Lib.site-packages.setuptools.command',
              'Lib.site-packages.test_files', 'Lib.site-packages.pkg_resources',
              'Lib.site-packages.pkg_resources.extern', 'Lib.site-packages.pkg_resources._vendor',
              'Lib.site-packages.pkg_resources._vendor.packaging', 'Lib.site-packages.text_unidecode'],
    url='',
    license='',
    author='Diego',
    author_email='',
    description=''
)
