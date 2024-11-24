# venv
py -m venv ~/.local/my_py_venv/py1

py1 -m pip install --upgrade pip setuptools wheel
pip1 install pygobject pycairo
pip1 install "badapple[dev]"

pip1 uninstall anyplayer
py1 test_src.py

py -m build
twine check dist/*

py1 -m pip install dist/*.whl
py1 test_example.py

twine upload dist/*
