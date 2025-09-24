import os
import re
import json
import hashlib
import tarfile
import subprocess
import urllib.request
from pathlib import Path


def latest_release(repo):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    headers = {}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)

    ver = data["tag_name"]
    return ver[1:], f"https://github.com/{repo}/releases/download/{ver}"


def remote_md5(url: str):
    txt = urllib.request.urlopen(f"{url}/md5-linux-musl-arm.txt").read().decode()
    return re.search(
        r"^([a-f0-9]{32})\s+./openlist-linux-musl-arm64\.tar\.gz$",
        txt,
        re.M,
    ).group(1)


def local_md5(fpath: str):
    h = hashlib.md5()
    with Path(fpath).open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)

    return h.hexdigest()


def verify(dld_path: str, dld_md5: str):
    print("\n校验 MD5 ...")
    if local_md5(dld_path) != dld_md5:
        raise RuntimeError("MD5 校验失败，文件可能被篡改")

    print("MD5 校验通过")


def download(url: str, dld_to: str, dld_md5: str):
    dld_file = Path(dld_to)
    if dld_file.exists() and local_md5(dld_file) == dld_md5:
        print("本地文件已存在且校验通过，跳过下载")
        return dld_to

    print("正在下载 ...")
    urllib.request.urlretrieve(
        f"{url}/openlist-linux-musl-arm64.tar.gz",
        dld_file,
        reporthook=lambda b, bsize, tsize: print(
            f"\r{b * bsize / 1024 / 1024:.1f} MB / {tsize / 1024 / 1024:.1f} MB",
            end="",
            flush=True,
        ),
    )
    verify(dld_to, dld_md5)
    return dld_to


def extract(fpath: str, extracto: str):
    extract_dir = Path(extracto)
    extract_dir.mkdir(exist_ok=True)
    with tarfile.open(Path(fpath), "r:gz") as tar:
        tar.extractall(extract_dir)

    print(f"解压完成，文件位于 {extract_dir.absolute()}")


def rm_cr():
    print("CRLF 转 LF")
    subprocess.run(
        [
            "bash",
            "-c",
            "find './' -type f -name '*.sh' -exec sed -i 's/\r$//' {} \;",
        ],
        check=True,
    )


def pack(module_name: str):
    print("打包中...")
    output = f"{module_name}.tar.gz"
    intermediate = f"{module_name}.tar"
    subprocess.run(["7z", "a", "-ttar", intermediate, module_name], check=True)
    subprocess.run(["7z", "a", "-tgzip", output, intermediate], check=True)
    if os.path.exists(intermediate):
        os.remove(intermediate)
    else:
        raise FileNotFoundError(f"生成中间产物 {intermediate} 出错!")

    print(f"打包完成, 输出 {output}")
    return f"./{output}"


def release(proj_name="openlist"):
    try:
        ver, url = latest_release("Yxiguan/OpenList_123")
        md5 = remote_md5(url)
        tar = download(url, f"./__pycache__/{md5}.tar.gz", md5)
        extract(tar, f"./{proj_name}/bin")
        with open(f"./{proj_name}/version", "w", encoding="utf-8") as f:
            f.write(ver)

        rm_cr()
        pack(proj_name)

    except Exception as e:
        print(f"打包出错: {e}")


if __name__ == "__main__":
    release()
