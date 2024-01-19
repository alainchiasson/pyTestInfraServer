from setuptools import setup, find_packages

setup(
    name='dnscheck',
    version='1.0.0',
    description='A DNS checking tool',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/dnscheck',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        # Add your dependencies here
        blinker==1.7.0,
        click==8.1.7,
        Flask==3.0.1,
        itsdangerous==2.1.2,
        Jinja2==3.1.3,
        MarkupSafe==2.1.3,
        prometheus-client==0.19.0,
        uWSGI==2.0.23,
        Werkzeug==3.0.1,
    ],
    entry_points={
        'console_scripts': [
            'dnscheck=dnscheck.cli:main',
        ],
    },
)
