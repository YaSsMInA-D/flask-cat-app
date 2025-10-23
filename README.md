# Flask Cat App – Evaluable

## Build and Run Commands

```bash
# Build Docker image
docker build -t flask-cat-app:alumnoyassm .

# Run container
docker run -p 8888:5000 flask-cat-app:alumnoyassm

## Explanation of GIF Location

I analyzed the code in `app.py` and discovered that:

1. **In `app.py`**: The `images` list was empty and needed GIF URLs
2. **Solution**: Instead of using local files, I added direct URLs to cat GIFs from Giphy
3. **Reason**: The code uses `random.choice(images)` to select random URLs
4. **In `index.html`**: The `<img src="{{url}}">` tag displays the selected URL
5. **Result**: Each time the page refreshes, a different cat GIF is shown

I used 6 working cat GIF URLs instead of local files.