# portfolio-site

Static public portfolio for runnable biopharma ML and scientific-software projects.

The site contains only short project descriptions, screenshots, GitHub links, tags,
and local run context.

## Preview Locally

```bash
python3 -m http.server 8000
```

Open http://127.0.0.1:8000. The page loads `projects.json`, so preview over HTTP
rather than `file://`.

## Content Rules

- Keep project cards short and operational.
- Link only to public repositories intended for cloning.
- Use screenshots for visual context.
- Keep personal documents and internal notes outside this repository.

## License

MIT. See [LICENSE](LICENSE).
