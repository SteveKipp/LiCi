#exclude docs and tests
packages = find_packages(exclude=['docs', 'tests*']),

#other dependencies
#the equivalent of pip install
extras_require = {},

entry_points = {
    'console_scripts':[
       'lici=lici.cli.main',
    ],
},
