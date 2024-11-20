from setuptools import setup, find_packages
setup(
    name = 'unity_catalog_example',
    version = '1.0',
    packages = find_packages(include = ('unity_catalog_example*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-spark-ai', 'prophecy-libs==1.9.24'],
    entry_points = {
'console_scripts' : [
'main = unity_catalog_example.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
