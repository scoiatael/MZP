from IPython.display import Image
from tempfile import NamedTemporaryFile
import matplotlib.pyplot as plt

def from_path(file_path):
    data = open(file_path, 'rb').read()
    return Image(data)


def from_anim(anim):
    plt.close(anim._fig)
    with NamedTemporaryFile(suffix='.gif') as f:
        anim.save(f.name, writer='imagemagick', fps=30);
        return from_path(f.name)
