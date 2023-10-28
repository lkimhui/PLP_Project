### How to clone the dataset in Huggingface via Github

# Make sure you have git-lfs installed (https://git-lfs.com)
```shell
git lfs install
git clone https://huggingface.co/datasets/ShashiVish/cover-letter-dataset
```

# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1