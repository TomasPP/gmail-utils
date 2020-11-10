from setuptools import setup


setup(
    name="gmail_utils",
    version="1.0.0",
    license="MIT",
    author="Tomas P",
    author_email="ttt@ttt.tt",
    url="...",
    py_modules=["gmail_utils"],
    install_requires=["yagmail>=0.14.245,<1",
                      # "requests>=2.23,<3",
                      # "pyyaml>=5.3.1,<=6",
                      ],
    # entry_points={"console_scripts": ["test=test:main"]},
)
