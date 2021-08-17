from setuptools import setup

package_name = 'ipc_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
 	(os.path.join('share', package_name, 'launch'),
         glob.glob('launch/*launch.py')),
        (os.path.join('share', package_name, 'config'), glob.glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='acharya',
    maintainer_email='srikrishna3118@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller = ipc_controller.controller:main'
        ],
    },
)
