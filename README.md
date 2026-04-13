# LaunchKit Landing Page

A modern static landing page built with plain HTML, CSS, and a small amount of JavaScript. The source files are already GitHub Pages-friendly, so you can host the site for free directly from your repository.

## Files you will edit most often

- `index.html` — page content and section structure
- `css/style.css` — colors, layout, spacing, and responsive styling
- `js/app.js` — mobile menu toggle and footer year

## Local development

```bash
npm install
npm start
```

## Production build

```bash
npm run build
```

The production output is generated in `dist/`.

## GitHub Pages deployment

### Option 1: Publish the source files directly
This project works as a plain static site from the repository root.

1. Push this project to GitHub.
2. If you want a user site, name the repository `<your-username>.github.io`.
3. In GitHub, open **Settings → Pages**.
4. Choose **Deploy from a branch**.
5. Select your branch and choose the **`/ (root)`** folder.
6. Save and wait for GitHub Pages to publish.

### Option 2: Publish the built `dist` output
If you prefer deploying the generated build, publish the contents of `dist/` using a Pages workflow or a dedicated branch.

## Customization ideas

- Replace the placeholder brand name `LaunchKit`
- Update the CTA email link in `index.html`
- Swap the testimonials and stats with your own content
- Adjust the color variables in `css/style.css`
- Add your own Open Graph preview image

## Notes

- All asset paths are relative for easier GitHub Pages hosting.
- No framework is required to edit the page.
- The page is responsive and works well as a portfolio, startup, or agency landing page.

