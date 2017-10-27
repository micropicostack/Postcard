import setuptools

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setuptools.setup(
    name="postcard",
    version=__import__('postcard').__version__,
    description="<some description>",
    long_description="<long_description>",
    classifiers=[],
    keywords='email html templates',
    author='Andre Leppik',
    author_email='leppika@hotmail.com',
    url='',
    license='TBD',
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
