import os
import requests
import concurrent.futures

def download_image(xx, yy):
    """Download an image given its xx and yy parameters and save it to the specified path."""
    base_url = "https://labs.m4ke.org/offsets/zeke/{}_{}.jpg"
    output_folder = "downloaded_images"
    
    image_url = base_url.format(xx, yy)
    image_filename = "{:03d}_{:03d}.jpg".format(xx, yy)
    save_path = os.path.join(output_folder, image_filename)

    response = requests.get(image_url, stream=True)
    response.raise_for_status()

    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(8192):
            file.write(chunk)
    print(f"Saved {image_filename}")

def main():
    output_folder = "downloaded_images"
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Use ThreadPoolExecutor to download in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        # Use executor.map to parallelize the download_image function
        list(executor.map(download_image, 
                          [xx for xx in range(80) for _ in range(100)],
                          [yy for _ in range(80) for yy in range(100)]
                         ))

if __name__ == "__main__":
    main()
