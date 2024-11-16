from setuptools import setup
from glob import glob
import os

package_name = 'mapeamento_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/description', glob('description/*.xacro')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='SEU_NOME',
    maintainer_email='SEU_EMAIL',
    description='Descrição do pacote',
    license='Licença do pacote',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odom_node = mapeamento_package.odom:main',
        ],
    },
)
