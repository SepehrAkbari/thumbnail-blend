# YouTube Thumbnail Blend

A Python script to download all thumbnails from a YouTube channel and blend them into a single image.

## Demo

Here is an example of all thumbnails blended from the *amazing* [Normal Knowledge](https://www.youtube.com/@NormalKnowledgeAG) YouTube channel:

![Blended Thumbnail](output/@NormalKnowledgeAG_average_thumbnail.jpg)

## Usage

Run the following commands in your terminal to run the script:

```bash
git clone https://github.com/SepehrAkbari/thumbnail-blend.git
cd thumbnail-blend

pip install -r requirements.txt

cd src

python load.py
python blend.py
```

The resulting blended image will be saved in the `output` directory.

## Contributing

To contribute to this project, you can fork this repository and create pull requests. You can also open an issue if you find a bug or wish to make a suggestion.

## License

This project is licensed under the [GNU General Public License (GPL)](LICENSE).

