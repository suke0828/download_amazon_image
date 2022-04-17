import sys
import requests
import os


def download_amazon_image(asin):
    url = f"http://images-jp.amazon.com/images/P/{asin}.09.LZZZZZZZ.jpg"
    # image_cacheディレクトリにxxxxxxxxxx.jpg形式で保存される
    local_filename = f"image_cache/{asin}.jpg"
    if os.path.isfile(local_filename):
        print(f"> {local_filename}はすでに存在するため処理を終了しました")
        return
    # stream=Trueを設定するとイテレータ形式で取得することが可能になり、応答が完全に完了する前からデータの読み取りを開始できる
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            # iter_contentメソッドで反復処理
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    print(f"> DL完了 {local_filename}")


if __name__ == "__main__":
    args = sys.argv
if len(args) == 2:
    asin = args[1]
    download_amazon_image(asin)
else:
    print("$ amazon_image.py <asin> 形式でasinを指定してください")
