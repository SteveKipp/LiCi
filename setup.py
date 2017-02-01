from setuptools import Command, find_packages, setup

#setup information
setup(
        name = 'LiCi',
        url = 'https://github.com/SteveKipp/LiCi',
        author = 'Steve Kipp',
        author_email = 'sakqm2@mst.edu', 
        packages = find_packages(exclude=['docs', 'tests*']),
        install_requires = ['docopt'],
        extras_require = {},

        entry_points = {
            'console_scripts':[
                'lici=LiCi.app:main',
            ],
        },
)
