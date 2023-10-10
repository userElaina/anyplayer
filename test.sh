py1 test.py

py -m build
twine check dist/*
py1 -m pip install dist/*.whl

py1 demo.py

twine upload dist/*
