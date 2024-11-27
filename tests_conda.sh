# conda
conda create -y -n py311 python=3.11

conda activate py311
conda install --update-all pip setuptools wheel
conda install pyaudio portaudio opencv numpy pycairo
pip install pygobject
pip install "badapple[dev]"

pip uninstall anyplayer
py test_src.py

conda deactivate
py -m build
twine check dist/*
twine upload --repository testpypi dist/*

conda activate py311
pip install -i https://test.pypi.org/simple/ anyplayer
py test_example.py

conda deactivate
twine upload dist/*
