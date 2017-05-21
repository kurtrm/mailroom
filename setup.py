from setuptools import setup


dependencies = ['ipython', 'pytest']
extra_packages = {
    'testing': ['pytest', 'pytest-watch', 'pytest-cov']
}

setup(
    name='mailroom',
    description="Sends automatic emails to donors.",
    version=0.1,
    author='Kurt', 'Lynn'
    author_email='',
    license='MIT',
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={
        'console_scripts':
            'mailroom = mailroom:main'
    }
)
