from setuptools import setup, find_packages
with open('requirements.txt') as f:
    required_packages = f.readlines()

required_packages = [pkg.strip() for pkg in required_packages]
setup(
    name='xnoxscap',
    version='1.4',
    packages=find_packages(),
    install_requires=required_packages,
    author='Developerxnoxs',
    author_email='developerxnoxs@gmail.com',
    description='Paket python untuk menyelesaikan recaptchav2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/developerxnoxs/xnoxs',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
