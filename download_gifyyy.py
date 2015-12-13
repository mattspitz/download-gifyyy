import argparse
import os.path
import subprocess


def fetch_gifyyy(gallery, idx, dest_dir):
    filename = os.path.join(dest_dir, "{:03d}.gif".format(idx))
    if os.path.exists(filename):
        return

    url = "http://gifyyy.com/gallery/{}/img{:d}".format(gallery, idx)
    scrape_cmd = ["phantomjs", "fetch_page.js", url]

    try:
        output = subprocess.check_output(scrape_cmd)
    except subprocess.CalledProcessError as e:
        raise Exception("Failed to scrape " + url + ": " + str(e))

    if not output.startswith("url="):
        raise Exception("Expected format 'url=<URL>'; got " + output)

    image_url = output[4:]

    pull_cmd = ["wget", "-O", filename, image_url]
    subprocess.check_call(pull_cmd)


def main():
    parser = argparse.ArgumentParser(description="Fetch GIFs from gifyyy")
    parser.add_argument("--index", type=int, required=True, help="Gifyyy index to fetch (e.g. 123 -> img123)")
    parser.add_argument("--dest", required=True, help="Destination directory")
    parser.add_argument("gallery", help="Gifyyy gallery (e.g. gifyyy.com/gallery/MySpookyParty")

    args = parser.parse_args()

    fetch_gifyyy(args.gallery, args.index, args.dest)


if __name__ == "__main__":
    main()
