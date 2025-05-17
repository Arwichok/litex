vite:
	npx vite

css:
	npx @tailwindcss/cli -i ./static/styles.css -o ./static/dist/output.css --watch

dev:
	uv run litestar run --host 0.0.0.0 --reload

serve:
	uv run litestar run --host 0.0.0.0


build:
	npx vite build
	npx @tailwindcss/cli -i ./static/styles.css -o ./static/dist/output.css --minify

