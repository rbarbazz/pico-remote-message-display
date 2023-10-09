# Prepare the code to be copied onto Pico
rsync -av --delete --exclude='styles/global.css' src/ dist/
cp -R .venv/lib/python3.11/site-packages/phew dist
npm run build