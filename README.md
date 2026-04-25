# Portfolio Site

## Preview locally

From this directory, run:

```bash
python3 -m http.server 8000
```

Then open `http://127.0.0.1:8000/`.

`index.html` fetches `projects.json`, so preview it over HTTP instead of opening the file via `file://`.

## Deploy to GitHub Pages

1. Push the contents of this directory to the target Pages repository or to a `docs/` folder in that repository.
2. In GitHub, open **Settings > Pages**.
3. Select the branch and folder that contain `index.html`, `styles.css`, and `projects.json`.
4. Save, then wait for the Pages deployment to publish.

## Screenshots

If you add screenshots later, keep them under `assets/screenshots/` and reference them with relative paths.
