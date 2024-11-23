py1 -m pip install --upgrade pip setuptools wheel
pip1 install pygobject
pip1 install badapple[dev]

pip1 uninstall anyplayer
py1 test.py

py -m build
twine check dist/*
py1 -m pip install dist/*.whl

py1 demo.py

twine upload dist/*
