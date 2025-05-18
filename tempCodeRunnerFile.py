     
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait for new data to load
        time.sleep(2)  # Adjust based on your site's load speed

        # Calculate new scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        # If height hasn’t changed, assume no more data
        if new_height == last_height:
            break
        last_height = new_height

    print("All data loaded.")