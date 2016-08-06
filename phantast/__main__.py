import argparse

import matplotlib.pyplot as plt
from PIL import Image

from phantast.phantast import phantast
from phantast.version import __version__


def main():
    parser = argparse.ArgumentParser(prog="phantast")
    parser.add_argument("--sigma", "-s", type=float, required=True)
    parser.add_argument("--epsilon", "-e", type=float, required=True)
    parser.add_argument("--halo", action="store_true")
    parser.add_argument("--view", action="store_true")
    parser.add_argument("--output", "-o")
    parser.add_argument("image")
    parser.add_argument("--version", "-v", action="version",
                        version="%(prog)s {}".format(__version__))
    args = parser.parse_args()

    im = Image.open(args.image)
    processed = phantast(im, args.sigma, args.epsilon, halo_correction=args.halo)

    if args.view:
        fig, axes = plt.subplots(nrows=1, ncols=2)
        axes[0].imshow(im)
        axes[1].imshow(processed, cmap=plt.get_cmap("gray"))
        plt.show()

    if args.output:
        Image.fromarray(processed).save(args.output)

if __name__ == "__main__":
    main()
