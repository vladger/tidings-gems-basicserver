import requests
import os
import base64

def encrypt(string, key):
    result = ""
    if not key:
        key = "335e096de9a7f799573df689a6757f69"  # Using the key from the JS file
    
    for i in range(len(string)):
        fchar = string[i]
        keychar = key[(i % len(key)) - 1]
        ord_char = ord(fchar)
        ord_keychar = ord(keychar)
        sum_char = (ord_char + ord_keychar) % 256  # Ensure it stays within valid character range
        result += chr(sum_char)
    
    return base64.b64encode(result.encode("latin1")).decode()  # Match JavaScript behavior

def decrypt(string, key):
    result = ""
    string = base64.b64decode(string.encode()).decode("latin1")
    if not key:
        key = "335e096de9a7f799573df689a6757f69"  # Using the key from the JS file
    
    for i in range(len(string)):
        fchar = string[i]
        keychar = key[(i % len(key)) - 1]
        ord_char = ord(fchar)
        ord_keychar = ord(keychar)
        sum_char = (ord_char - ord_keychar) % 256  # Ensure correct decryption
        result += chr(sum_char)
    
    return result

def download_levels():
    url = "https://tidings.su/gems_ok/www/api.php"
    save_dir = "downloadedlevels"
    os.makedirs(save_dir, exist_ok=True)
    
    base_params = "auth%5Fkey=25ddc102dca37241a89c967d2b0b14e0&m=levelGet&network=ok&sid=null&viewer%5Fid=540635218937&l={}&notDecEn=2&user%5Fid=0&energy%5Fv=101&coins=105&session%5Fkey=%2Ds%2Db5Vu3dmZDX4t13eZG4Xr27gYC5Vqc2fdDU0r%2E4hbDV3R24DdG5yoZegYA7ZSY1ncB4zs0gD6Bbyyc1GYH3yt64lY%2DY3wY8haCWyQ0%2Dgd"
    
    for i in range(1001, 19900):  # Adjust as needed
        level = f"l{i:02d}"
        encrypted_param = encrypt(base_params.format(level), "335e096de9a7f799573df689a6757f69")
        print(f"Requesting {level}.js with k: {encrypted_param}")
        
        response = requests.get(url, params={"k": encrypted_param})
        if response.status_code == 200:
            decrypted_data = decrypt(response.text, "335e096de9a7f799573df689a6757f69")
            with open(os.path.join(save_dir, f"{level}.js"), "w", encoding="utf-8") as f:
                f.write(decrypted_data)
            print(f"Downloaded and saved {level}.js")
        else:
            print(f"Failed to download {level}.js, status code: {response.status_code}")

if __name__ == "__main__":
    download_levels()
