from setuptools import setup

setup(
    name='fanyi',
    py_modules=['fanyi'],
    install_requires=['requests', 'docopt'],
    entry_points={
        'console_scripts': ['fanyi=fanyi:translate_word']
    }
)
