[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linter: flake8](https://img.shields.io/badge/linter-flake8-white)](https://github.com/PyCQA/flake8)
  
・PythonでAmazonからASINもしくはISBNを使って画像をダウンロードする  
・`amazon_image.py <ASIN>or<ISBN>`で画像を取得できる  
  
##### プログラムを実行する
`$ python3 amazon_image.py 4873115655`  
  `> DL完了 image/4873115655.jpg`  
  
##### DLしたimageの保存先  
```
.  
├── image  
│   └── 4873115655.jpg  
└── amazon_image.py  
```
