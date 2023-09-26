py1 test.py

cd ../
py -m build
py1 -m pip install dist/*.whl

py1 demo.py
